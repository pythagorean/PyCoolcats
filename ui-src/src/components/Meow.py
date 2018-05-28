__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import { Link } from 'react-router-dom'
const { div, a } = require('hyperscript-helpers')(e)
''')

def meowComponentDidMount(self):
    if not self.props.post: self.props.getPost()

def meowRender(self):
    post = self.props.post
    if not post: return None
    stamp = post['stamp']
    message = post['message']
    author = post['author']
    hash = post['hash']
    userHandle = post['userHandle']
    return div({ 'className': 'meow', 'id': stamp },
        a({ 'className': 'meow-edit', 'onClick': lambda: "openEditPost('+id+')" },
            'edit'),
        e(Link, { 'to': '/meow/' + hash, 'className': 'stamp' },
            __new__ (Date(stamp)).toString()
            ),
        ' |\xA0',
        e(Link, { 'to': '/u/' + author, 'className': 'user' },
            userHandle),
        div({ 'className': 'message' },
            message
            ))

Meow = createReactClass({
    'componentDidMount': lambda: meowComponentDidMount(this),

    'render': lambda: meowRender(this)
    })

__pragma__('js', 'export default Meow')
