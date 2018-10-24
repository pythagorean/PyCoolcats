js_import = ('''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import { Link } from 'react-router-dom'
const { div, span, button, input, li, i, h3, ul } = require('hyperscript-helpers')(e)
''')

def followRender(self):
    filteredNotFollowing = self.props.notFollowing.filter(
        lambda unfollowed: unfollowed.handle.toLowerCase().startsWith(
            self.state.newFollowText.toLowerCase()))
    return div({ 'className': "panel panel-default" },
        div({ 'className': "close"},
            e(Link, { 'to': "/" },
                "x"
                )),
        div({ 'className': "panel-body" },
            div({ 'className': "row" },
                h3(None, 'Following'),
                ul({ 'id': "following" },
                    len(self.props.following) is 0 and li(None,
                        "You currently aren't following anyone."),
                    len(self.props.following) > 0 and div({
                            'class': "panel-body",
                            'style': {
                                'overflow-y': 'scroll',
                                'height': '100px'
                                }},
                        div({
                                'class': "mid-width wrapItems",
                                'style': {
                                    'padding-top': '10px',
                                    'background-color': '#eeeeee',
                                    'height': '100px'
                                    }},
                            self.props.following.map(
                                lambda user: li({
                                        'className': 'following-handle',
                                        'key': user.handle
                                        },
                                    div({ 'className': 'col-xs-9' },
                                        span({ 'className': 'handle' },
                                            user.handle
                                            )),
                                    div({
                                            'className': 'col-xs-3',
                                            'style': {
                                                'padding-bottom': '10px'
                                                }},
                                        button({
                                                'type': 'button',
                                                'className': 'btn btn-default',
                                                'onClick':
                                                    lambda: self.props.unfollow(user.handle)
                                                },
                                            'Unfollow'
                                            )))))))),
            div({ 'className': "row" },
                h3({ 'id': "myModalLabel" }, 'Follow someone'),
                div({ 'className': "col-xs-12" },
                    div({ 'className': "form-group input-icon" },
                        i(None, '@'),
                        input({
                            'value': self.state.newFollowText,
                            'onChange': self.updateFollowText,
                            'type': "text",
                            'className': "form-control",
                            'id': "followHandle",
                            'placeholder': "handle"
                            }))),
                ul({ 'id': "not-following" },
                    len(filteredNotFollowing) is 0 and li(None,
                        "There are no users that you aren't already following."),
                    len(filteredNotFollowing) > 0 and div({
                            'class': "panel-body",
                            'style': {
                                'overflow-y': 'scroll',
                                'height': '200px'
                                }},
                        div({
                                'class': 'mid-width wrapItems',
                                'style': {
                                    'padding-top': '10px',
                                    'background-color': '#eeeeee',
                                    'height': '200px'
                                    }},
                            filteredNotFollowing.map(
                                lambda user: li({
                                    'className': 'following-handle',
                                    'key': user.handle
                                    },
                                    div({ 'className': 'col-xs-9' },
                                        span({ 'className': 'handle' },
                                            user.handle
                                            )),
                                    div({
                                            'className': 'col-xs-3',
                                            'style': {
                                                'padding-bottom': '10px'
                                                }},
                                        button({
                                                'type': 'button',
                                                'className': 'btn btn-default',
                                                'onClick':
                                                    lambda: self.props.follow(user.handle)
                                                },
                                            'Follow'
                                            ))))))),
                div({ 'className': "row" },
                    div({ 'className': "col-sm-1" }),
                    div({ 'className': "col-sm-4" }),
                    div({ 'className': "col-sm-6" },
                        button({
                                'type': "button",
                                'id': "close",
                                'className': "btn btn-primary pull-right",
                                'onClick':
                                    lambda: self.props.history.push('/')
                                },
                            'Close'
                            ))))))

Follow = createReactClass({
    'getInitialState': lambda: { 'newFollowText': '' },

    'updateFollowText': lambda follow: this.setState(
        { 'newFollowText': follow.target.value }),

    'render': lambda: followRender(this)
    })

__pragma__('js', 'export default Follow')
