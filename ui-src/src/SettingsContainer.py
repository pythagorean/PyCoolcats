__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import Settings from './Settings'
import { newHandle } from './actions'
''')

mapStateToProps = lambda state: { 'handleTaken': state.handleTaken }

mapDispatchToProps = lambda dispatch: {
    'newHandle': lambda handle, then: dispatch(
        newHandle(handle))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Settings)')
