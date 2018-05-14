__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { div, h3, p, i, form, input, button } = require('hyperscript-helpers')(e)
''')

def settingsOnHandleSubmit(self, handle):
    handle.preventDefault()
    self.setState({ 'newHandleText': '' })
    if not self.state['newHandleText']: return
    self.props.newHandle(self.state['newHandleText'])
    self.setState({ 'newHandleText': '' })

Settings = createReactClass({
    'getInitialState': lambda: { 'newHandleText': '' },

    'updateHandleText': lambda handle: this.setState(
        { 'newHandleText': handle.target.value }),

    'onHandleSubmit': lambda handle: settingsOnHandleSubmit(this, handle),

    'render': lambda: div({ 'className': 'panel panel-default' },
        div({ 'className': 'panel-body' },
            h3({ 'id': 'setHandleModalLabel' }, 'Set your handle'),
            p({ 'style': { 'display':
                    'inline' if this.props.handleTaken is True else 'none'
                }},
                'Handle already taken try another one'
                ),
            form({
                    'id': 'handleForm',
                    'onSubmit': this.onHandleSubmit,
                    'className': 'form-group'
                    },
                div({ 'className': 'col-xs-8' },
                    div({ 'className': 'form-group input-icon' },
                        i(None, '@'),
                        input({
                            'value': this.state.newHandleText,
                            'onChange': this.updateHandleText,
                            'type': 'text',
                            'className': 'form-control',
                            'id': 'myHandle',
                            'placeholder': 'handle'
                            })
                        )),
                div({ 'className': 'col-xs-2' },
                    button({
                            'id': 'setHandleButton',
                            'type': 'submit',
                            'className': 'btn btn-primary'
                            },
                        'Set Handle'
                        )))))
    })

__pragma__('js', 'export default Settings')
