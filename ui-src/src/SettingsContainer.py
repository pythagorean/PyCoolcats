__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import Settings from './Settings'
import { appProperty, getFirstName, newHandle, setFirstName, toggleModal } from './actions'
''')

mapStateToProps = lambda state: {
    'handleTaken': state.handleTaken,
    'isOpen': state.isOpen,
    'handles': state.handles,
    'appProperties': state.appProperties
    }

mapDispatchToProps = lambda dispatch: {
    'getFirstName': lambda: dispatch(
        getFirstName()),

    'getMyHandle': lambda: dispatch(
        appProperty('Agent_Handle')),

    'newHandle': lambda handle, then: dispatch(
        newHandle(handle)),

    'setFirstName': lambda firstName: dispatch(
        setFirstName(firstName)),

    'toggleModal': lambda: dispatch(
        toggleModal())
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Settings)')
