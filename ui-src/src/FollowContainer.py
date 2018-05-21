__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import Follow from './components/Follow'
import { follow, unfollow } from './actions'
''')

__pragma__('noalias', 'keys') # use js_keys

def mapStateToProps(state):
    # console.log('state.handles ' + JSON.stringify(state.handles))
    return {
        'following': Object.keys(state.follows).map(
            lambda handle: { 'handle': handle }),

        'notFollowing': Object.keys(state.handles).filter(
            lambda handleHash:
                not state.follows[state.handles[handleHash].handle] and
                    state.handles[handleHash].handle is not state.handle
                    ).map(
            lambda handleHash: {
                'handleHash': handleHash,
                'handle': state.handles[handleHash].handle
                })
        }

mapDispatchToProps = lambda dispatch: {
    'follow': lambda handle, then: dispatch(follow(handle, then)),
    'unfollow': lambda handle, then: dispatch(unfollow(handle, then))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Follow)')
