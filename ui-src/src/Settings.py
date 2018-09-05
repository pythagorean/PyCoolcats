__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { div, p, i, form, input, button } = require('hyperscript-helpers')(e)
''')

MAX_HANDLE_LENGTH = 20

def settingsOnHandleSubmit(self, handle):
    getFirstName = self.props.getFirstName
    handles = self.props.handles
    newHandle = self.props.newHandle
    setFirstName = self.props.setFirstName
    toggleModal = self.props.toggleModal
    newHandleText = self.state.newHandleText

    handle.preventDefault()

    # empty string given as input
    if not newHandleText: return

    # max characters exceeded
    if len(newHandleText) > MAX_HANDLE_LENGTH:
        self.setState({ 'newHandleText': '' })
        return

    newHandle(newHandleText)

    handleExists = handles.find(
        lambda handleObj: handleObj.handle is newHandleText)
    if handleExists:
        newHandle('')
        return

    # check if a name has been set, and if not default to handle
    if not (getFirstName() and len(getFirstName()) > 1):
        setFirstName(newHandleText)

    toggleModal()

Settings = createReactClass({
    'getInitialState': lambda: { 'newHandleText': '' },

    'updateHandleText': lambda handle: this.setState(
        { 'newHandleText': handle.target.value }),

    'onHandleSubmit': lambda handle: settingsOnHandleSubmit(this, handle),

    'render': lambda: div({ 'className': "panel panel-default" },
        div({ 'className': "panel-body" },
            div({ 'style': { 'paddingLeft': 30, 'paddingBottom': 10 } },
                p({
                        'className': "text-info",
                        'style': {
                            'display': (len(this.state.newHandleText) is 0 and this.props.handleTaken is False) and 'inline' or 'none'
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
                            'value': this.state.newHandleText,
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
