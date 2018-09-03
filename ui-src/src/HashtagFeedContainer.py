__pragma__('js', '{}', '''
import { connect } from 'react-redux'
import HashtagFeed from './HashtagFeed'
import { getPostsWithHashtag } from './actions'
''')

__pragma__('noalias', 'keys') # use js_keys
__pragma__('noalias', 'sort') # use js_sort

def mapStateToProps(state, ownProps):
    containsTag = lambda pId: state.posts[pId].message.includes('#' + ownProps.match.params.hashtag)
    return {
        'postList': Object.keys(state.posts).filter(containsTag).sort().reverse().map(
            lambda pId: Object.assign({}, state.posts[pId], {
                'userHandle': state.handles[state.posts[pId].author] or state.posts[pId].author
                })),
        'hashtag': ownProps.match.params.hashtag
        }

def mapDispatchToProps(dispatch, ownProps):
    return {
        'getPosts':
            lambda hashtag: dispatch(
                getPostsWithHashtag([hashtag]))
        }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(HashtagFeed)')
