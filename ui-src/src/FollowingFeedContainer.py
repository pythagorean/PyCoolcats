js_import = ('''
import { connect } from 'react-redux'
import FollowingFeed from './FollowingFeed'
import { getPostsBy, getFollow } from './actions'
''')

__pragma__('noalias', 'keys') # use js_keys
__pragma__('noalias', 'sort') # use js_sort

def mapStateToProps(state):
    listOfFollowingPlusSelf = Object.keys(state.follows).concat([state.handle])
    # is the post by someone active user is following (or themselves)?
    byFollowing = lambda pId: listOfFollowingPlusSelf.indexOf(state.posts[pId].author) > -1
    return {
        'postList': Object.keys(state.posts).filter(byFollowing).sort().reverse().map(
            lambda pId: Object.assign({}, state.posts[pId], {
                'userHandle': state.handles[state.posts[pId].author] or state.posts[pId].author
                })),
        'handle': state.handle,
        'follows': Object.keys(state.follows)
        }

mapDispatchToProps = lambda dispatch: {
    'getPostsBy': lambda handles, then: dispatch(
        getPostsBy(handles, then)),

    'getFollow': lambda handle, type, then: dispatch(
        getFollow(handle, type, then))
    }

def mergeProps(stateProps, dispatchProps, ownProps):
    props = __pragma__('js', '{}', '{ ...stateProps, ...dispatchProps }')
    # my feed is a list of posts that are either by me or people I follow
    props['getMyFeed'] = lambda postsBy: dispatchProps.getPostsBy(postsBy)
    return props

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps, mergeProps)(FollowingFeed)')
