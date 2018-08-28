__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import { Link } from 'react-router-dom'
const { div, p, form, label, input, button } = require('hyperscript-helpers')(e)
''')

MAX_PIC_SIZE = 2000000

def editProfileComponentWillMount(self):
    firstName = self.props.firstName
    getFirstName = self.props.getFirstName
    profilePic = self.props.profilePic
    getFirstName()
    self.setState({
        'newNameText': firstName,
        'newProfilePic': profilePic
        })

def editProfileComponentDidUpdate(self, prevProps):
    firstName = self.props.firstName
    if not prevProps.firstName and firstName:
        self.setState({ 'newNameText': firstName })

def editProfileOnHandleSubmit(self, handle):
    newNameText = self.state.newNameText
    newProfilePic = self.state.newProfilePic
    history = self.props.history
    firstName = self.props.firstName
    profilePic = self.props.profilePic
    setFirstName = self.props.setFirstName
    setProfilePic = self.props.setProfilePic

    handle.preventDefault()

    if newProfilePic and newProfilePic is not profilePic:
        setProfilePic(newProfilePic)

    if not newNameText: return
    if newNameText is not firstName: setFirstName(newNameText)
    else: self.setState({ 'newNameText': firstName })
    # Redirect user to main page
    history.push('/')

def editProfileReadBlob(self, file):
    input = file.target

    if input.size > MAX_PIC_SIZE:
        alert('File is too big!')
        return
    self.upload(input.files[0]).then(
        lambda dataURL: self.setState({
            'newProfilePic': dataURL
            })
        )

def editProfileUpload(self, file, resolve):
    reader = __new__(FileReader())
    reader.onload = lambda read: resolve(read.target.result)
    reader.readAsDataURL(file)

def editProfileRender(self):
    handle = self.props.handle
    newNameText = self.state.newNameText

    return div({ 'className': "panel panel-default" },
        div({ 'className': "close" },
            e(Link,
                { 'to': "/" },
                "x"
                )),
        div({ 'className': "panel-body" },
            p(None,
                "Profile"
                ),
            form({
                    'id': "editProfileForm",
                    'onSubmit': self.onHandleSubmit,
                    'className': "form-group"
                    },
                div({ 'className': "form-row" },
                    div({ 'className': "form-group col-xs-6" },
                        label(None,
                            "Handle"
                            ),
                        p({ 'id': "handle" },
                            "@",
                            handle
                            )),
                    div({ 'className': "form-group col-xs-6" },
                        label(None,
                            "Name"
                            ),
                        input({
                            'type': "text",
                            'onChange': self.updateNameText,
                            'className': "form-control",
                            'id': "inputName",
                            'placeholder': "name",
                            'value': newNameText
                            })),
                    div({ 'className': "form-group" },
                        div({ 'className': "form-group col-xs-10" },
                            label(None,
                                "Profile Picture"
                                ),
                            input({
                                'type': "file",
                                'accept': "image/*",
                                'onChange': self.readBlob,
                                'hidden': True,
                                'id': "image"
                                })))),
                div({ 'className': "form-group col-xs-6" },
                    button({
                            'id': "saveChanges",
                            'type': "submit",
                            'className': "btn btn-primary"
                            },
                        "Save Changes"
                        )))))

EditProfile = createReactClass({
    'getInitialState':
        lambda: {
            'newNameText': '',
            'newProfilePic': ''
            },

    'componentWillMount':
        lambda: editProfileComponentWillMount(this),

    'componentDidUpdate':
        lambda prevProps: editProfileComponentDidUpdate(this, prevProps),

    'updateNameText':
        lambda update: this.setState({
            'newNameText': update.target.value
            }),

    'onHandleSubmit':
        lambda handle: editProfileOnHandleSubmit(this, handle),

    'readBlob':
        lambda file: editProfileReadBlob(this, file),

    'upload':
        lambda file: __new__(Promise(
            lambda resolve, reject: editProfileUpload(this, file, resolve)
            )),

    'render': lambda: editProfileRender(this)
    })

__pragma__('js', 'export default EditProfile')
