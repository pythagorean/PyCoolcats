__pragma__('js', '{}', '''
import createReactClass from 'create-react-class'
''')

def attachmentComponentDidMount(self):
    if 'attachment' not in self.props.post: return
    attachment = self.props.post.attachment
    if 'image_small' in attachment:
        self.setState({ 'data': attachment.image_small })

def attachmentRender(self):
    return self.state.data

Attachment = createReactClass({
    'getInitialState': lambda: { 'data': '' },

    'componentDidMount': lambda: attachmentComponentDidMount(this),

    'render': lambda: attachmentRender(this)
    })

__pragma__('js', 'export default Attachment')
