js_import = ('''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { img } = require('hyperscript-helpers')(e)
''')

def attachmentComponentDidMount(self):
    if 'imagedata' not in self.props and 'attachment' in self.props.post:
        getImageSmall = self.props.getImageSmall
        post = self.props.post
        if 'image_small' in post.attachment:
            getImageSmall(post.stamp, post.attachment.image_small)

def attachmentRender(self):
    if 'imagedata' not in self.props: return ''
    return img({ 'src': self.props.imagedata })

Attachment = createReactClass({
    'componentDidMount': lambda: attachmentComponentDidMount(this),
    'render':            lambda: attachmentRender(this)
    })

__pragma__('js', 'export default Attachment')
