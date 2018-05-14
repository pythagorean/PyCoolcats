__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import { Route, Link } from 'react-router-dom'
import createReactClass from 'create-react-class'
import SettingsContainer from './SettingsContainer'
import FollowContainer from './FollowContainer'
import NewMeowContainer from './NewMeowContainer'
import FollowingFeedContainer from './FollowingFeedContainer'
import UserFeedContainer from './UserFeedContainer'
import MeowContainer from './MeowContainer'
const { div, img, h2, p, a, em, strong } = require('hyperscript-helpers')(e)
''')

def appComponentWillMount(self):
    # this fetches the hash which represents the active users userHash
    self.props.getMyHandle()
    self.props.getHandles()
    self.interval = setInterval(self.props.getHandles, 2000)

def appComponentDidUpdate(self, prevProps):
    # console.log(prevProps.handle, self.props.handle)
    if not prevProps.handle and self.props.handle:
        self.props.getFollow(self.props.handle, 'following')

def appComponentWillUnmount(self):
    if self.interval: clearInterval(self.interval)

App = createReactClass({
    'componentWillMount': lambda: appComponentWillMount(this),

    'componentDidUpdate': lambda prevProps: appComponentDidUpdate(this, prevProps),

    'componentWillUnmount': lambda: appComponentWillUnmount(this),

    'render': lambda: div({ 'className': 'container' },
        div({ 'className': 'spinner transition500' }),
        div({ 'className': 'error transition500' }),
        div({ 'className': 'row' },
            div({ 'className': 'col-sm-2' },
                div({ 'className': 'logo' },
                    img({ 'src': '/cat-eating-bird-circle.png', 'alt': 'cat eating bird' })
                    )),
            div({ 'className': 'col-sm-7' },
                div({ 'className': 'contentcontainer' },
                    div(None,
                        e(Link, { 'to': '/', 'id': 'handle' }, this.props.handle),
                        e(Link,
                            { 'to': '/settings', 'id': 'changeHandleButton', 'className': 'btn btn-default' },
                            'Settings'
                            )),
                    e(Link,
                        { 'to': '/follow', 'id': 'followButton', 'className': 'btn btn-default' },
                        'Follow People'
                        ),
                    div({ 'id': 'banner' },
                        'Clutter',
                        div({ 'className': 'subtitle' },
                            'can haz herd cats?'
                            )),
                    div({ 'id': 'content' },
                        e(Route, { 'path': '/', 'exact': True, 'component': NewMeowContainer }),
                        e(Route, { 'path': '/', 'exact': True, 'component': FollowingFeedContainer }),
                        e(Route, { 'path': '/u/:handle', 'component': UserFeedContainer }),
                        e(Route, { 'path': '/settings', 'component': SettingsContainer }),
                        e(Route, { 'path': '/follow', 'component': FollowContainer }),
                        e(Route, { 'path': '/meow/:meowHash', 'component': MeowContainer })
                        ))),
            div({ 'className': 'col-sm-3' },
                div({ 'className': 'alphabox' },
                    div({ 'id': 'about' },
                        h2(None, 'What is Clutter?'),
                        p(None,
                            'A ',
                            a({ 'href': 'https://en.wiktionary.org/wiki/clutter' },
                                em(None, 'clutter')),
                            ' is a flock of cats.'
                            ),
                        p(None,
                            strong(None, 'Clutter'),
                            ' is a fully decentralized alternative to Twitter.'
                            ),
                        p(None, 'Impossible to censor or control.'),
                        p(None,
                            'Join the mewvolution on ',
                            a({ 'href': 'http://holochain.org' }, 'holochain.org'),
                            '.'
                            ))))))
    })

__pragma__('js', 'export default App')
