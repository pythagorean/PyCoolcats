js_import = ('''
import { connect } from 'react-redux'
import Attachment from './Attachment'
import { getImageSmall } from './actions'
''')

def mapStateToProps(state, ownProps):
    postStamp = ownProps.post.stamp
    if 'imagedata' not in state.posts[postStamp]: return ownProps
    props = dict(ownProps)
    props.post['imagedata'] = state.posts[postStamp].imagedata
    return props

mapDispatchToProps = lambda dispatch, ownProps: {
    'getImageSmall': lambda: dispatch(
        getImageSmall(ownProps.post.stamp, ownProps.post.attachment.image_small))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Attachment)')
