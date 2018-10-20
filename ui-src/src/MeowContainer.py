__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import Meow from './components/Meow'
import { getPost } from './actions'
''')

__pragma__('noalias', 'keys') # use js_keys

def mapStateToProps(state, ownProps):
    meowHash = ownProps.match.params.meowHash
    arrayOfPosts = Object.keys(state.posts).map(
        lambda postStamp: state.posts[postStamp])
    meow = arrayOfPosts.find(
        lambda p: p.hash is meowHash)
    post = Object.assign({}, meow, {
            'userHandle': state.handles[meow.author]
        }) if meow else meow
    return { 'post': post }

mapDispatchToProps = lambda dispatch, ownProps: {
    'getPost': lambda: dispatch(
        getPost(ownProps.match.params.meowHash))
    }

__pragma__('js', 'export default connect(mapStateToProps, mapDispatchToProps)(Meow)')
