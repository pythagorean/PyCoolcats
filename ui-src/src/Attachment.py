__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { img } = require('hyperscript-helpers')(e)
''')

def attachmentComponentDidMount(self):
    if 'imagedata' in self.props.post: return
    if 'attachment' not in self.props.post: return
    getImageSmall = self.props.getImageSmall
    attachment = self.props.post.attachment
    if 'image_small' in attachment: getImageSmall()

def attachmentRender(self):
    if 'imagedata' not in self.props.post: return ''
    imagedata = self.props.post.imagedata
    return img({ 'src': imagedata })

Attachment = createReactClass({
    'componentDidMount': lambda: attachmentComponentDidMount(this),
    'render':            lambda: attachmentRender(this)
    })

__pragma__('js', 'export default Attachment')
