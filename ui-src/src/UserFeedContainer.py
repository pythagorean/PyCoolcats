js_import = ('''
import { connect } from 'react-redux'
import UserFeed from './UserFeed'
import { getPostsBy } from './actions'
''')

__pragma__('noalias', 'keys') # use js_keys
__pragma__('noalias', 'sort') # use js_sort

def mapStateToProps(state, ownProps):
    byUser = lambda pId: state.posts[pId].author is ownProps.match.params.handle
    return {
        'postList': Object.keys(state.posts).filter(byUser).sort().reverse().map(
            lambda pId: Object.assign({}, state.posts[pId], {
                'userHandle': (state.handles[state.posts[pId].author] or
                    state.posts[pId].author)
                })),
        'handle': ownProps.match.params.handle
        }

mapDispatchToProps = lambda dispatch, ownProps: {
    'getPosts': lambda handle: dispatch(getPostsBy([handle]))
    }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(UserFeed)')
