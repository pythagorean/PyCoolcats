__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import NewMeow from './NewMeow'
import { post, postImageAttachment } from './actions'
''')

mapStateToProps = lambda: {}

mapDispatchToProps = lambda dispatch: {
    'post': lambda message, attachment, then: dispatch(
        post(message, attachment, then)),
    'postImageAttachment': lambda thumbnail, then: dispatch(
        postImageAttachment(thumbnail, then))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(NewMeow)')
