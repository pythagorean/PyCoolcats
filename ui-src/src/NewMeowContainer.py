__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import NewMeow from './NewMeow'
import { post, postImageAttachment } from './actions'
''')

mapStateToProps = lambda: {}

mapDispatchToProps = lambda dispatch: {
    'post': lambda message, then: dispatch(
        post(message, then)),
    'postImageAttachment': lambda postHash, thumbnail, then: dispatch(
        postImageAttachment(postHash, thumbnail, then))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(NewMeow)')
