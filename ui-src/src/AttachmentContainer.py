__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import Attachment from './Attachment'
''')

def mapStateToProps(state):
    return {}

def mapDispatchToProps(dispatch, ownProps):
    return {}

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Attachment)')
