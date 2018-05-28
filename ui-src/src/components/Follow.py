__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { div, span, button, input, li, i, h3, ul } = require('hyperscript-helpers')(e)
''')

def followRender(self):
    # console.log(self.props.following)
    filteredNotFollowing = self.props.notFollowing.filter(
        lambda unfollowed: unfollowed.handle.toLowerCase().startsWith(
            self.state.newFollowText.toLowerCase()))
    return div({ 'className': 'panel panel-default' },
        div({ 'className': 'panel-body' },
            div({ 'className': 'row' },
                h3(None, 'Following'),
                ul({ 'id': 'following' },
                    len(self.props.following) is 0 and li(None,
                        "You currently aren't following anyone."),
                    self.props.following.map(
                        lambda user: li({
                                'className': 'following-handle',
                                'key': user.handle
                                },
                            div({ 'className': 'col-xs-9' },
                                span({ 'className': 'handle' },
                                    user.handle
                                    )),
                            div({ 'className': 'col-xs-3' },
                                button({
                                        'type': 'button',
                                        'className': 'btn btn-default',
                                        'onClick':
                                            lambda: (self.props.unfollow(user.handle)).bind(self)
                                        },
                                    'Unfollow'
                                    )))))),
            div({ 'className': 'row' },
                h3({ 'id': 'myModalLabel' }, 'Follow someone'),
                div({ 'className': 'col-xs-12' },
                    div({ 'className': 'form-group input-icon' },
                        i(None, '@'),
                        input({
                            'value': self.state.newFollowText,
                            'onChange': self.updateFollowText,
                            'type': 'text',
                            'className': 'form-control',
                            'id': 'followHandle',
                            'placeholder': 'handle'
                            }))),
                ul({ 'id': 'not-following' },
                    len(filteredNotFollowing) is 0 and li(None,
                        "There are no users that you aren't already following."),
                    filteredNotFollowing.map(
                        lambda user: li({
                            'className': 'following-handle',
                            'key': user.handle
                            },
                            div({ 'className': 'col-xs-9' },
                                span({ 'className': 'handle' },
                                    user.handle
                                    )),
                            div({ 'className': 'col-xs-3' },
                                button({
                                        'type': 'button',
                                        'className': 'btn btn-default',
                                        'onClick':
                                            lambda: (self.props.follow(user.handle)).bind(self)
                                        },
                                    'Follow'
                                    ))))))))

Follow = createReactClass({
    'getInitialState': lambda: { 'newFollowText': '' },

    'updateFollowText': lambda follow: this.setState(
        { 'newFollowText': follow.target.value }),

    'render': lambda: followRender(this)
    })

__pragma__('js', 'export default Follow')
