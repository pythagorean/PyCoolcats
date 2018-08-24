def anchor(anchor):
    anchorType = {'anchorType': anchor.anchorType, 'anchorText': ''}
    rootAnchortype = {'anchorType': 'anchorTypes', 'anchorText': ''}
    anchorHash = hc_makeHash('anchor', anchor)
    anchorGet = hc_get(anchorHash)
    hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Check to see if ' + anchor.anchorText + ' exists</mermaid>')
    # hc_debug('anchorGet ' + JSON.stringify(anchorGet))
    if anchorGet is None:
        anchorType = {'anchorType': anchor.anchorType, 'anchorText': ''}
        rootAnchortype = {'anchorType': 'anchorTypes', 'anchorText': ''}
        anchorTypeGet = hc_get(hc_makeHash('anchor', anchorType))
        hc_debug('anchorTypeGet ' + JSON.stringify(anchorTypeGet))
        hc_debug('<mermaid>' + App.Agent.String + '-->>DHT:Check to see if ' + anchor.anchorType + ' has been setup</mermaid>')
        if anchorTypeGet is None:
            rootAnchorTypeHash = hc_makeHash('anchor', rootAnchortype)
            hc_debug('<mermaid>' + App.Agent.String + '-->>DHT:Check to see if the Root of all anchors has been setup</mermaid>')
            if hc_get(rootAnchorTypeHash) is None:
                rootAnchorTypeHash = hc_commit('anchor', rootAnchortype)
                hc_debug('<mermaid>' + App.Agent.String + '->>' + App.Agent.String + ':commit Root of all anchors to local chains</mermaid>')
                hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Publish Root of all anchors</mermaid>')
                # hc_debug('Root Anchor Type Created: ' + rootAnchorTypeHash)
            hc_debug('<mermaid>DHT-->>' + App.Agent.String + ':Return the Root Anchor Type</mermaid>')
            anchorTypeHash = hc_commit('anchor', anchorType)
            hc_debug('<mermaid>' + App.Agent.String + '->>' + App.Agent.String + ':commit ' + anchor.anchorType + ' to local chain</mermaid')
            hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Publish ' + anchor.anchorType + '</mermaid>')
            # hc_debug('Anchor Type Created: ' + anchorTypeHash)
            hc_commit('anchor_link', {'Links': [{'Base': rootAnchorTypeHash, 'Link': anchorTypeHash, 'Tag': anchorType.anchorType}]})
            hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link ' + anchor.anchorType + ' to Root of all anchors</mermaid>')
        else:
            anchorTypeHash = hc_makeHash('anchor', anchorType)
            hc_debug('<mermaid>' + App.Agent.String + ':Return the anchorType ' + anchor.anchorType + '</mermaid>')
        anchorHash = hc_commit('anchor', anchor)
        hc_debug('<mermaid>' + App.Agent.String + '->>' + App.Agent.String + ':commit ' + anchor.anchorText + ' has been setup</mermaid>')
        hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Publish ' + anchor.anchorText + '</mermaid>')
        # hc_debug('Anchor Created ' + anchorHash)
        hc_commit('anchor_link', {'Links': [{'Base': anchorTypeHash, 'Link': anchorHash, 'Tag': anchor.anchorText}]})
        hc_debug('<mermaid>' + App.Agent.String + '->>DHT:Link ' + anchor.anchorText + ' to ' + anchorType.anchorType + '</mermaid>')
    hc_debug('<mermaid>' + App.Agent.String + ':Return the anchor ' + anchor.anchorType + ' = ' + anchor.anchorText + '</mermaid>')
    return anchorHash

def exists(anchor):
    hc_debug('<mermaid>' + App.Agent.String + '-->>DHT:Check to see if ' + anchor.anchorText + ' exists</mermaid>')
    # hc_debug('does it exist?')
    # hc_debug(hc_get(hc_makeHash('anchor', anchor)))
    key = hc_get(hc_makeHash('anchor', anchor))
    # hc_debug(key)
    if key is not None:
        hc_debug('<mermaid>DHT-->>' + App.Agent.String + ':' + anchor.anchorText + ' exists</mermaid>')
        return True
    hc_debug('<mermaid>DHT-->>' + App.Agent.String + ':' + anchor.anchorText + ' does not exist</mermaid>')
    return False

def anchors(js_type):
    links = hc_getLinks(hc_makeHash('anchor', {'anchorType': js_type, 'anchorText': ''}), '')
    # hc_debug(links)
    return links

def genesis():
    return True

def validatePut(entry_type, entry, header, pkg, sources):
    # hc_debug('Anchors validatePut:' + sources)
    return validateCommit(entry_type, entry, header, pkg, sources)

def validateCommit(entry_type, entry, header, pkg, sources):
    # hc_debug('Anchors validatePut:' + sources)
    if entry_type == 'anchor':
        return True
    if entry_type == 'anchor_link':
        return True
    return False

def validateLink(linkingEntryType, baseHash, linkHash, pkg, sources):
    # hc_debug('Anchors validateLink:' + sources)
    return True

def validateMod(entry_type, hash, newHash, pkg, sources):
    # hc_debug('Anchors validateMod:' + sources)
    return True

def validateDel(entry_type, hash, pkg, sources):
    # hc_debug('Anchors validateDel:' + sources)
    return True

def validatePutPkg(entry_type):
    # hc_debug('Anchors validatePutPkg')
    return None

def validateModPkg(entry_type):
    # hc_debug('Anchors validateModPkg')
    return None

def validateDelPkg(entry_type):
    # hc_debug('Anchors validateDelPkg')
    return None

def validateLinkPkg(entry_type):
    # hc_debug('Anchors validateLinkPkg')
    return None
