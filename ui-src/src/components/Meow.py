js_import = ('''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import { Link } from 'react-router-dom'
import AttachmentContainer from '../AttachmentContainer'
import FavesContainer from '../FavesContainer'
const { div, a, br } = require('hyperscript-helpers')(e)
''')

__pragma__('noalias', 'split') # use js_split

def meowComponentDidMount(self):
    if not self.props.post: self.props.getPost()

# replace 'https' URLs with links
def meowUrlify(self, text):
    re = __new__(RegExp('(https?://[^\\s]+)', 'g'))
    urlRegexSplit = text.split(re)
    return urlRegexSplit.map(lambda str, i: (
        (str.startsWith('https') and
            a({ 'key': i, 'target': '_blank', 'href': str }, str)) or
        (str.includes('#') and
            self.hashify(str)) or
        str))

# identify all hashtags and replace with links
def meowHashify(self, text):
    message = text
    re = __new__(RegExp('(\\B#\\w*[a-zA-Z]+\\w*)', 'g'))
    splitMessage = message.split(re)
    return splitMessage.map(lambda str, i: (
        (str.startsWith('#') and
            e(Link, {
                'key': i,
                'to': '/tag/' + str.replace('#', ''),
                'className': 'hashtag'
                },
            str)) or
        str))

def meowRender(self):
    post = self.props.post
    if not post: return None
    stamp = post['stamp']
    message = post['message']
    author = post['author']
    hash = post['hash']
    userHandle = post['userHandle']
    return div({ 'className': "meow", 'id': stamp },
        a({ 'className': "meow-edit", 'onClick': lambda: "openEditPost('+id+')" },
            'edit'),
        e(Link, { 'to': "/u/" + author, 'className': "user" },
            "@",
            userHandle),
        ' ', '|', ' ',
        e(Link, { 'to': "/meow/" + hash, 'className': "stamp" },
            __new__(Date(stamp)).toString()),
        div({ 'className': "message" },
            self.urlify(message), br(),
            e(AttachmentContainer, { 'post': post })),
        e(FavesContainer, { 'hash': hash }))

Meow = createReactClass({
    'componentDidMount': lambda: meowComponentDidMount(this),

    'urlify': lambda text: meowUrlify(this, text),

    'hashify': lambda text: meowHashify(this, text),

    'render': lambda: meowRender(this)
    })

__pragma__('js', 'export default Meow')
