__pragma__('js', '{}', '''
import { createRef, createElement as e } from 'react'
import createReactClass from 'create-react-class'
import Jimp from 'jimp/es'
const { form, div, textarea, label, input, button } = require('hyperscript-helpers')(e)
''')

def newMeowAttach(self, posted):
    if not self.state['newMeowImage']: return
    Jimp.read(self.state['newMeowImage']).then(
        lambda image: image.scaleToFit(200, 150).getBase64(Jimp.MIME_PNG,
            lambda err, thumbnail: not err and alert(
                "Attach thumbnail to " + posted + ":\n\n" + thumbnail)
            ))
    self.setState({ 'newMeowImage': "" })
    self.inputImage.current.value = ""

def newMeowOnSubmit(self, meow):
    meow.preventDefault()
    if not self.state['newMeowText']: return
    self.props.post(self.state['newMeowText'],
        lambda posted: newMeowAttach(self, posted))
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

    'inputImage': createRef(),

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
                'ref': this.inputImage,
                'onChange': this.updateImage,
                'hidden': True,
                'id': "image",
                }
            ))
    })

__pragma__('js', 'export default NewMeow')
