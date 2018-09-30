__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { form, div, textarea, label, input, button } = require('hyperscript-helpers')(e)
''')

def newMeowOnSubmit(self, meow):
    meow.preventDefault()
    if not self.state['newMeowText']: return
    if self.state['newMeowImage']:
        alert('Has attachment: ' + self.state['newMeowImage'])
        self.setState({ 'newMeowImage': "" })
    self.props.post(self.state['newMeowText'])
    self.setState({ 'newMeowText': "" })

def newMeowUpdateImage(self, file):
    input = file.target
    if input.size > 2000000:
        alert('File is too big!')
        return
    self.upload(input.files[0]).then(
        lambda dataURL: self.setState({
            'newMeowImage': dataURL
            }))

def newMeowUpload(self, file, resolve):
    reader = __new__(FileReader())
    reader.onload = lambda read: resolve(read.target.result)
    reader.readAsDataURL(file)

NewMeow = createReactClass({
    'getInitialState': lambda: {
        'newMeowText': "",
        'newMeowImage': ""
        },

    'updateMeowText': lambda meow: this.setState({
        'newMeowText': meow.target.value
        }),

    'updateImage': lambda file: newMeowUpdateImage(this, file),

    'upload':
        lambda file: __new__(Promise(
            lambda resolve, reject: newMeowUpload(this, file, resolve)
            )),

    'onMeowSubmit': lambda meow: newMeowOnSubmit(this, meow),

    'render': lambda: form({
            'onSubmit': this.onMeowSubmit,
            'id': "meow-form",
            'action': ""
            },
        div({ 'className': "form-group col-xs-12" },
            textarea({
                    'value': this.state.newMeowText,
                    'onChange': this.updateMeowText,
                    'className': "form-control",
                    'id': "meow",
                    'name': "meow",
                    'wrap': "soft"
                    }
                )),
        button({
                'type': "submit",
                'id': "postMeow",
                'className': "btn btn-primary"
                },
            'Meow'
            ),
        label(None, "Attach image"),
        input({
                'type': "file",
                'accept': "image/*",
                'ref': this.state.newMeowImage,
                'onChange': this.updateImage,
                'hidden': True,
                'id': "image",
                }
            ))
    })

__pragma__('js', 'export default NewMeow')
