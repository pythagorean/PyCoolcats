__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import App from './App'
import { appProperty, getHandle, getHandles, getFollow, getPostsBy } from './actions'
''')

mapStateToProps = lambda state: __pragma__('js', '{}', '{ ...state }')

mapDispatchToProps = lambda dispatch: {
    'getMyHandle': lambda: dispatch(
        appProperty('Agent_Handle')),

    'getHandle': lambda userHash, isMe, then: dispatch(
        getHandle(userHash, isMe, then)),

    'getHandles': lambda then: dispatch(
        getHandles(then)),

    'getFollow': lambda handle, type, then: dispatch(
        getFollow(handle, type, then)),

    'getPostsBy': lambda handles, then: dispatch(
        getPostsBy(handles, then))
    }

__pragma__('js', 'export default connect(mapStateToProps, mapDispatchToProps)(App)')
