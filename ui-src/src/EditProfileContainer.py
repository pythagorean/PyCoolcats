js_import = ('''
import { connect } from 'react-redux'
import EditProfile from './EditProfile'
import { getFirstName, setFirstName, setProfilePic } from './actions'
''')

def mapStateToProps(state):
    return {
        'handle': state.handle,
        'firstName': state.firstName,
        'profilePic': state.profilePic
        }

def mapDispatchToProps(dispatch):
    return {
        'setFirstName': lambda data: dispatch(
            setFirstName(data)),
        'setProfilePic': lambda data: dispatch(
            setProfilePic(data)),
        'getFirstName': lambda: dispatch(
            getFirstName())
        }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(EditProfile)')
