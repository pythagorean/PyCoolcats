__pragma__('js', '{}', '''
import { createRef, createElement as e } from 'react'
import createReactClass from 'create-react-class'
import Jimp from 'jimp/es'
const { form, div, textarea, label, input, button } = require('hyperscript-helpers')(e)
''')

def newMeowOnSubmit(self, meow):
    meow.preventDefault()
    newMeowText = self.state['newMeowText']
    newMeowImage = self.state['newMeowImage']
    if not newMeowText: return
    postImageSmall = self.props.postImageSmall
    post = self.props.post
    if newMeowImage:
        Jimp.read(newMeowImage).then(
            lambda image: (image
                .scaleToFit(200, 150, Jimp.RESIZE_BICUBIC)
                .quality(100)
                .getBase64(Jimp.MIME_JPEG,
                    lambda _err, thumbnail: postImageSmall(thumbnail,
                        lambda attach: post(newMeowText, { 'image_small': attach })
                        ))))
        self.setState({ 'newMeowImage': "" })
        self.inputImage.current.value = ""
    else: post(newMeowText)
    self.setState({ 'newMeowText': "" })

def newMeowUpdateImage(self, file):
    input = file.target
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
