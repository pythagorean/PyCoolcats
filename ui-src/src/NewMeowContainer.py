__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import NewMeow from './NewMeow'
import { post, postImageSmall } from './actions'
''')

mapStateToProps = lambda: {}

mapDispatchToProps = lambda dispatch: {
    'post': lambda message, attachment, then: dispatch(
        post(message, attachment, then)),
    'postImageSmall': lambda thumbnail, then: dispatch(
        postImageSmall(thumbnail, then))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(NewMeow)')
