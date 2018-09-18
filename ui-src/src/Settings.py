__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { div, p, i, form, input, button } = require('hyperscript-helpers')(e)
''')

MAX_HANDLE_LENGTH = 20

def settingsOnHandleSubmit(self, handle):
    getFirstName = self.props.getFirstName
    useHandle = self.props.useHandle
    setFirstName = self.props.setFirstName
    toggleModal = self.props.toggleModal
    useHandleText = self.state.useHandleText

    handle.preventDefault()

    # empty string given as input
    if not useHandleText: return

    # max characters exceeded
    if len(useHandleText) > MAX_HANDLE_LENGTH:
        self.setState({ 'useHandleText': '' })
        return

    useHandle(useHandleText)

    # check if a name has been set, and if not default to handle
    if not (getFirstName() and len(getFirstName()) > 1):
        setFirstName(useHandleText)

    toggleModal()

Settings = createReactClass({
    'getInitialState': lambda: { 'useHandleText': '' },

    'updateHandleText': lambda handle: this.setState(
        { 'useHandleText': handle.target.value }),

    'onHandleSubmit': lambda handle: settingsOnHandleSubmit(this, handle),

    'render': lambda: div({ 'className': "panel panel-default" },
        div({ 'className': "panel-body" },
            div({ 'style': { 'paddingLeft': 30, 'paddingBottom': 10 } },
                p({
                        'className': "text-info",
                        'style': {
                            'display': (len(this.state.useHandleText) is 0 and this.props.handleTaken is False) and 'inline' or 'none'
                            }
                        },
                    "Set your handle to get meowing"
                    )),
            div({ 'style': { 'paddingLeft': 30, 'paddingBottom': 10 } },
                p({
                        'className': "text-danger",
                        'style': {
                            'display': this.props.handleTaken is True and 'inline' or 'none'
                            }
                        },
                    "This handle already has a home, try something else!"
                    )),
            form({
                    'id': "handleForm",
                    'onSubmit': this.onHandleSubmit,
                    'className': "form-group"
                    },
                div({ 'className': "col-xs-8" },
                    div({ 'className': "form-group input-icon" },
                        i(None,
                            "@"
                            ),
                        input({
                            'value': this.state.useHandleText,
                            'onChange': this.updateHandleText,
                            'type': "text",
                            'className': "form-control",
                            'id': "myHandle",
                            'placeholder': "handle"
                            }))),
                div({ 'className': "col-xs-2" },
                    button({
                            'id': "setHandleButton",
                            'type': "submit",
                            'className': "btn btn-primary"
                            },
                        "Set Handle"
                        )))))
        })

__pragma__('js', 'export default Settings')
