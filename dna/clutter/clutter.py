def getProperty(name):
    return hc_property(name)

def appProperty(name):
    if name == 'Agent_Handle':
        hc_debug('Agent_Handle')
        hc_debug(getHandle(App.Key.Hash))
        return getHandle(App.Key.Hash)
    if name == 'App_Agent_String': return App.Agent.String
    if name == 'App_Key_Hash':     return App.Key.Hash
    if name == 'App_DNA_Hash':     return App.DNA.Hash
    return 'Error: No App Property with name: ' + name

def newHandle(handle):
    hc_debug('<mermaid>' + App.Agent.String + '-->>DHT:Check to see if ' + App.Agent.String + ' has any existing handles</mermaid')
    handles = hc_getLinks(App.Key.Hash, 'handle')
    hc_debug('<mermaid>DHT->>' + App.Agent.String + ':returned ' + len(handles) + ' existing handles for ' + App.Agent.String + '</mermaid>')
    if len(handles) > 0:
        if anchorExists('handle', handle) == 'false':
            oldKey = handles[0].Hash
            key = hc_update('handle', anchor('handle', handle), oldKey)
            hc_debug('<mermaid>' + App.Agent.String + '->>' + App.Agent.String + ':' + App.Agent.String + ' has a handle so update it</mermaid>')
            hc_commit('handle_links',
                {'Links': [
                    {'Base': App.Key.Hash, 'Link': oldKey, 'Tag': 'handle', 'LinkAction': HC.LinkAction.Del},
                    {'Base': App.Key.Hash, 'Link': key, 'Tag': 'handle'}
                ]})
            hc_debug('<mermaid' + App.Agent.String + '->>DHT:Update link to ' + handle + ' in "handle_links"</mermaid')
            hc_commit('directory_links',
                {'Links': [
                    {'Base': App.DNA.Hash, 'Link': oldKey, 'Tag': 'handle', 'LinkAction': HC.LinkAction.Del},
                    {'Base': App.DNA.Hash, 'Link': key, 'Tag': 'handle'}
                ]})
            hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Update link to ' + handle + ' in "directory_links"</mermaid>')
            return key
        else:
            # hc_debug('HandleInUse')
            return 'HandleInUse'
    if anchorExists('handle', handle) == 'false':
        newHandleKey = hc_commit('handle', anchor('handle', handle))
        hc_debug('<mermaid>' + App.Agent.String + '->>', App.Agent.String + ':commit new handle' + handle + '</mermaid>')
        hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Publish ' + handle + '</mermaid>')
        hc_commit('handle_links', {'Links': [{'Base': App.Key.Hash, 'Link': newHandleKey, 'Tag': 'handle'}]})
        hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link ' + newHandleKey + ' to "handle_links"</mermaid>')
        hc_commit('directory_links', {'Links': [{'Base': App.DNA.Hash, 'Link': newHandleKey, 'Tag': 'directory'}]})
        hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link ' + handle + ' to "directory_links"</mermaid>')
        return newHandleKey
    else:
        # hc_debug('HandleInUse')
        return 'HandleInUse'

def getHandle(agentKey):
    links = hc_getLinks(agentKey, 'handle', {'Load': True});
    # hc_debug(links)
    if len(links) > 0:
        anchorHash = links[0].Entry.replace('"', '')
        return hc_get(anchorHash).anchorText
    else:
        return ''

def getAgent(handle):
    if anchorExists('handle', handle) == 'false':
        return ''
    else:
        return hc_get(anchor('handle', handle), {'GetMask': HC.GetMask.Sources})[0]

def getHandles():
    # hc_debug('get the handles')
    if hc_property('enableDirectoryAccess') != 'true':
        return None
    links = hc_getLinks(App.DNA.Hash, 'directory', {'Load': True})
    # hc_debug(links)
    handles = []
    for i in range(len(links)):
        handleHash = links[i].Source
        handle = hc_get(links[i].Entry).anchorText
        hc_debug(handle + 'handle')
        handles.append({'handleHash': handleHash, 'handle': handle})
    return handles

def follow(handle):
    # Expects a handle of the person you want to follow
    #  Commits a new follow entry to my source chain
    #  On the DHT, puts a link on their hash to my hash as a "follower"
    #  On the DHT, puts a link on my hash to their hash as a "following"
    hc_debug('Follow ' + handle)
    anchorHash = anchor('handle', handle)
    hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link ' + handleHash() + ' to follow ' + anchorHash + '</mermaid>')
    return hc_commit('follow',
        {'Links': [
            {'Base': anchorHash, 'Link': handleHash(), 'Tag': 'followers'},
            {'Base': handleHash(), 'Link': anchorHash, 'Tag': 'following'}
        ]})

# get a list of all the people from the DHT a user is following or follows
def getFollow(params):
    js_type = params.js_type
    base = anchor('handle', params.js_from)
    # base = hc_makeHash('handle', params.js_from)
    hc_debug('params.from ' + params.js_from + ' hash=' + JSON.stringify(base))
    handles = []
    if js_type == 'followers' or js_type == 'following':
        handleLinks = hc_getLinks(base, js_type)
        for i in range(len(handleLinks)):
            handles.append(hc_get(handleLinks[i].Hash).anchorText)
    return handles

def post(post):
    key = hc_commit('post', post) # Commits the post block to my source chain, assigns resulting hash to 'key'
    hc_debug('<mermaid>' + App.Agent.String + '->>' + App.Agent.String + ':commit new meow</mermaid>')
    hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Publish new meow</mermaid>')

    # On the DHT, puts a link on my anchor to the new post
    hc_commit('post_links', {'Links': [{'Base': handleHash(), 'Link': key, 'Tag': 'post'}]})
    hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link meow to "post links"</mermaid>')

    # hc_debug(key)
    return key # Returns the hash key of the new post to the calling function

def postMod(params):
    # hc_debug(params.post);
    key = hc_update('post', params.post, params.hash)
    # hc_commit('post_links',
    #     {'Links': [
    #         {'Base': App.Key.Hash, 'Link': oldKey, 'Tag': 'handle', 'LinkAction': HC.LinkAction.Del},
    #         {'Base': App.Key.Hash, 'Link': key, 'Tag': 'handle'}
    #     ]}
    return key

# TODO add "last 10" or "since timestamp" when query info is supported
def getPostsBy(handles):
    # From the DHT, gets all "post" metadata entries linked from this userAddress
    posts = []
    for i in range(len(handles)):
        author = anchor('handle', handles[i])
        authorPosts = doGetLinkLoad(author, 'post')
        # add in the author
        for j in range(len(authorPosts)):
            post = authorPosts[j]
            post.author = handles[i]
            posts.append(post)
    return posts

def getPost(params):
    rawPost = hc_get(params.postHash, {'GetMask': HC.GetMask.All})
    if rawPost == None: return None
    post = {
        'post': rawPost.Entry,
        'author': getHandle(rawPost.Sources[0]),
        'H': params.postHash
    }
    return post

# helper function to do hc_getLinks call, handle the no-link error case, and copy the returned entry values into a nicer array
def doGetLinkLoad(base, tag):
    # get the tag from the base in the DHT
    links = hc_getLinks(base, tag, {'Load': True})
    links_filled = []
    for i in range(len(links)):
        link = {'H': links[i].Hash}
        link[tag] = links[i].Entry
        links_filled.append(link)
    return links_filled

# helper function to call hc_getLinks, handle the no links entry error, and build a simpler links array.
def doGetLink(base, tag):
    # get the tag from the base in the DHT
    links = hc_getLinks(base, tag, {'Load': False})
    # hc_debug('Links:' + JSON.stringify(links))
    links_filled = []
    for i in range(len(links)):
        links_filled.append(links[i].Hash)
    return links_filled

def anchor(anchorType, anchorText):
    return hc_call('anchors', 'anchor', {'anchorType': anchorType, 'anchorText': anchorText}).replace('"', '')

def handleHash(appKeyHash):
    # hc_debug('appKeyHash ' + appKeyHash)
    if appKeyHash == None:
        appKeyHash = App.Key.Hash
    return hc_getLinks(appKeyHash, 'handle', {'Load': True})[0].Entry.replace('"', '')

def anchorExists(anchorType, anchorText):
    return hc_call('anchors', 'exists', {'anchorType': anchorType, 'anchorText': anchorText})

# GENESIS - Called only when your source chain is generated:'hc gen chain <name>'
# ===============================================================================
def genesis(): # 'hc gen chain' calls the genesis function in every zome file for the app
    return True

# ===============================================================================
#   VALIDATION functions for *EVERY* change made to DHT entry -
#     Every DHT node uses their own copy of these functions to validate
#     any and all changes requested before accepting. put / mod / del & metas
# ===============================================================================

def validateCommit(entry_type, entry, header, pkg, sources):
    # hc_debug("Clutter validate commit: " + JSON.stringify(pkg));
    return validate(entry_type, entry, header, sources)

def validatePut(entry_type, entry, header, pkg, sources):
    # hc_debug("Clutter validate put: " + JSON.stringify(pkg));
    return validate(entry_type, entry, header, sources)

def validate(entry_type, entry, header, sources):
    if entry_type == 'post':
        l = len(entry.message)
        if l > 0 and l < 256: return True
        return False
    if entry_type == 'handle':
        return True
    if entry_type == 'follow':
        return True
    return True

# Are there types of tags that you need special permission to add links?
# Examples:
#   - Only Bob should be able to make Bob a "follower" of Alice
#   - Only Bob should be able to list Alice in his people he is "following"
def validateLink(linkEntryType, baseHash, links, pkg, sources):
    # hc_debug("Clutter validate link: " + sources)
    # if linkEntryType == 'handle_links':
    #     length = len(links)
    #     # a valid handle is when:
    #
    #     # there should just be one or two links only
    #     if length == 2:
    #         # if this is a modify it will have two links the first of which
    #         # will be the del and the second the new link.
    #         if links[0].LinkAction != HC.LinkAction.Del: return False
    #         if links[1].LinkAction != HC.LinkAction.Add: return False
    #     elif length == 1:
    #         # if this is a new handle, there will just be one Add link
    #         if links[0].LinkAction != HC.LinkAction.Add: return False
    #     else: return False
    #
    #     for i in range(length):
    #         link = links[i]
    #         # the base must be this base
    #         if link.Base != baseHash: return False
    #         # the base must be the source
    #         if link.Base != sources[0]: return False
    #         # The tag name should be "handle"
    #         if link.Tag != 'handle': return False
    #         #TODO check something about the link, i.e. get it and check it's type?
    #     return True
    return True

def validateMod(entry_type, entry, header, replaces, pkg, sources):
    # hc_debug("Clutter validate mod: " + entry_type + " header:" + JSON.stringify(header) + " replaces:" + JSON.stringify(replaces))
    if entry_type == 'handle':
        # check that the source is the same as the creator
        # TODO we could also check that the previous link in the type-chain is the replaces hash.
        orig_sources = hc_get(replaces, {'GetMask': HC.GetMask.Sources})
        if isErr(orig_sources) or orig_sources == None or len(orig_sources) != 1 or orig_sources[0] != sources[0]: return False
    elif entry_type == 'post':
        # there must actually be a message
        if entry.message == '': return False
        orig = hc_get(replaces, {'GetMask': HC.GetMask.Sources + HC.GetMask.Entry})
        # check that source is same as creator
        if len(orig.Sources) != 1 or orig.Sources[0] != sources[0]: return False
        orig_message = orig.Entry.message
        # message must actually be different
        return orig_message != entry.message
    return True

def validateDel(entry_type, hash, pkg, sources):
    # hc_debug('Clutter validateDel:' + sources)
    return True

def validatePutPkg(entry_type):
    hc_debug('Clutter validatePutPkg: ' + App.Agent.String)
    req = {}
    req[HC.PkgReq.Chain] = HC.PkgReq.ChainOpt.Full
    return req

def validateModPkg(entry_type):
    # hc_debug('Clutter validateModPkg')
    return None

def validateDelPkg(entry_type):
    # hc_debug('Clutter validateDelPkg')
    return None

def validateLinkPkg(entry_type):
    # hc_debug('Clutter validateLinkPkg')
    return None
