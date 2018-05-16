__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import NewMeow from './NewMeow'
import { post } from './actions'
''')

mapStateToProps = lambda: {}

mapDispatchToProps = lambda dispatch: {
    'post': lambda message, then: dispatch(
        post(message, then)
        )}

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(NewMeow)')
