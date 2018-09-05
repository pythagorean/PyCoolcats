__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import { Route, Link } from 'react-router-dom'
import createReactClass from 'create-react-class'
import EditProfileContainer from './EditProfileContainer'
import FollowContainer from './FollowContainer'
import FollowingFeedContainer from './FollowingFeedContainer'
import MeowContainer from './MeowContainer'
import Modal from './components/Modal'
import NewMeowContainer from './NewMeowContainer'
import SettingsContainer from './SettingsContainer'
import UserFeedContainer from './UserFeedContainer'
import HashtagFeedContainer from './HashtagFeedContainer'
const { div, img, h2, p, a, em, strong } = require('hyperscript-helpers')(e)
''')

DEFAULT_PROFILE_PIC = '/cat-eating-bird-circle.png'

def appComponentWillMount(self):
    # this fetches the hash which represents the active users userHash
    self.props.getMyHandle()
    self.props.getHandles()
    self.props.getProfilePic()
    self.props.getFirstName()
    self.interval = setInterval(self.props.getHandles, 2000)

def appComponentDidUpdate(self, prevProps):
    # console.log(prevProps.handle, self.props.handle)
    if not prevProps.handle and self.props.handle:
        self.props.getFollow(self.props.handle, 'following')

def appComponentWillUnmount(self):
    if self.interval: clearInterval(self.interval)

def appRender(self):
    appProperties = self.props.appProperties
    firstName = self.props.firstName
    handle = self.props.handle
    modalIsOpen = self.props.modalIsOpen
    profilePic = self.props.profilePic
    # if an agent handle already exists, there is no need to query for a handle
    if modalIsOpen and not appProperties.Agent_Handle:
        return div(None, e(Modal, { 'show': modalIsOpen },
            e(SettingsContainer, None)))
    return div({ 'className': "container" },
        div({ 'className': "spinner transition500" }),
        div({ 'className': "error transition500" }),
        div({ 'className': "row first" },
            div({ 'className': "fixed-area" },
                div({ 'className': "col-sm-2 contentcontainer" },
                    div({ 'className': "logo" },
                        img({
                            'src': profilePic and profilePic or DEFAULT_PROFILE_PIC,
                            'alt': "user-profile"
                            }),
                        div({ 'id': "displayName" },
                            firstName
                            ),
                        e(Link,
                            { 'to': "/editProfile", 'id': "handle" },
                            "@",
                            handle
                            ))),
                div({ 'className': "col-sm-7" },
                    div({ 'className': "contentcontainer" },
                        e(Link, {
                                'to': "/follow",
                                'id': "followButton",
                                'className': "btn btn-default"
                                },
                            "Follow People"
                            ),
                        div({ 'id': "banner" },
                            e(Link,
                                { 'to': "/" },
                                "Coolcats (Clutter)"
                                ),
                            div({ 'className': "subtitle" },
                                "can haz herd cats?"
                                )),
                        div({ 'id': "content" },
                            e(Route, { 'path': "/", 'exact': True, 'component': NewMeowContainer }),
                            e(Route, { 'path': "/editProfile", 'component': EditProfileContainer }),
                            e(Route, { 'path': "/follow", 'component': FollowContainer }),
                            e(Route, { 'path': "/meow/:meowHash", 'component': MeowContainer }),
                            e(Route, {
                                    'path': "/tag/:hashtag",
                                    'component': HashtagFeedContainer
                                    })))),
                div({ 'className': "col-sm-3" },
                    div({ 'className': "alphabox" },
                        div({ 'id': "about" },
                            h2(None,
                                "What is Clutter?"
                                ),
                            p(None,
                                a({
                                        'href': "https://en.wiktionary.org/wiki/clutter",
                                        'target': "blank"
                                        },
                                    em(None,
                                        "clutter"
                                        )),
                                ' ',
                                "is a flock of cats."
                                ),
                            p(None,
                                strong(None,
                                    "Clutter"
                                    ),
                                " is a fully decentralized alternative to Twitter."
                                ),
                            p(None,
                                "Impossible to censor or control."
                                ),
                            p(None,
                                "Join the mewvolution on",
                                ' ',
                                a({ 'href': "http://holochain.org", 'target': "blank" },
                                    "holochain.org"
                                    ),
                                "."
                                ))))),
            div({ 'className': "row" },
                div({ 'className': "contentcontainer", 'id': "feedContent" },
                    div(None,
                        e(Route, { 'path': "/", 'exact': True, 'component': FollowingFeedContainer }),
                        e(Route, { 'path': "/u/:handle", 'component': UserFeedContainer })
                        )))))

App = createReactClass({
    'componentWillMount': lambda: appComponentWillMount(this),

    'componentDidUpdate': lambda prevProps: appComponentDidUpdate(this, prevProps),

    'componentWillUnmount': lambda: appComponentWillUnmount(this),

    'render': lambda: appRender(this)
    })

__pragma__('js', 'export default App')
