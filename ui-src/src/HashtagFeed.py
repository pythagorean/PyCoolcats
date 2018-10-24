js_import = ('''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import Meow from './components/Meow'
const { div, h2 } = require('hyperscript-helpers')(e)
''')

def hashtagFeedSetupForNewUser(self):
    self.props.getPosts(self.props.hashtag)
    if self.interval: clearInterval(self.interval)
    self.interval = setInterval(
        lambda: self.props.getPosts(self.props.hashtag),
        1000)

HashtagFeed = createReactClass({
    'componentDidMount':
        lambda: this.setupForNewUser(),

    'componentDidUpdate':
        lambda prevProps: (
            prevProps.hashtag is this.props.hashtag and
                this.setupForNewUser()),

    'setupForNewUser':
        lambda: hashtagFeedSetupForNewUser(this),

    'componentWillUnmount':
        lambda: this.interval and clearInterval(this.interval),

    'render':
        lambda: div({ 'id': "meows" },
            h2({ 'id': "user-header" }, "#" + this.props.hashtag),
            this.props.postList.map(
                lambda post: e(Meow({ 'post': post, 'key': post.stamp }))))
    })

__pragma__('js', 'export default HashtagFeed')
