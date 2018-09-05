__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import Meow from './components/Meow'
const { div, h2 } = require('hyperscript-helpers')(e)
''')

def userFeedComponentDidUpdate(self, prevProps):
    if prevProps.handle is not self.props.handle:
        self.setupForNewUser()

def userFeedSetupForNewUser(self):
    self.props.getPosts(self.props.handle)
    if self.interval: clearInterval(self.interval)
    self.interval = setInterval(
        (lambda: self.props.getPosts(self.props.handle)), 1000)

def userFeedComponentWillUnmount(self):
    if self.interval: clearInterval(self.interval)

UserFeed = createReactClass({
    'componentDidMount':
        lambda: this.setupForNewUser(),

    'componentDidUpdate':
        lambda prevProps: userFeedComponentDidUpdate(this, prevProps),

    'setupForNewUser':
        lambda: userFeedSetupForNewUser(this),

    'componentWillUnmount':
        lambda: userFeedComponentWillUnmount(this),

    'render':
        lambda: div({ 'id': 'meows' },
            h2({ 'id': 'user-header' }, this.props.handle),
            this.props.postList.map(
                lambda post: e(Meow, {
                    'post': post,
                    'key': post.stamp
                })))
    })

__pragma__('js', 'export default UserFeed')
