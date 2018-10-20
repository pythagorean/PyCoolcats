__pragma__('js', '{}', '''
import createReactClass from 'create-react-class'
''')

def attachmentComponentDidMount(self):
    if 'imagedata' in self.props.post: return
    if 'attachment' not in self.props.post: return
    getImageSmall = self.props.getImageSmall
    attachment = self.props.post.attachment
    if 'image_small' in attachment: getImageSmall()

def attachmentRender(self):
    return 'imagedata' in self.props.post and self.props.post.imagedata[:40] or ''

Attachment = createReactClass({
    'componentDidMount': lambda: attachmentComponentDidMount(this),
    'render':            lambda: attachmentRender(this)
    })

__pragma__('js', 'export default Attachment')
