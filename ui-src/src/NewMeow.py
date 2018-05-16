__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
const { form, input, button } = require('hyperscript-helpers')(e)
''')

def newMeowOnSubmit(self, meow):
    meow.preventDefault()
    if not self.state['newMeowText']: return
    self.props.post(self.state['newMeowText'])
    self.setState({ 'newMeowText': '' })

NewMeow = createReactClass({
    'getInitialState': lambda: { 'newMeowText': '' },

    'updateMeowText': lambda meow: this.setState(
        { 'newMeowText': meow.target.value }),

    'onMeowSubmit': lambda meow: newMeowOnSubmit(this, meow),

    'render': lambda: form({
            'onSubmit': this.onMeowSubmit,
            'id': 'meow-form',
            'action': ''
            },
        input({
                'value': this.state.newMeowText,
                'onChange': this.updateMeowText,
                'className': 'form-control',
                'id': 'meow',
                'name': 'meow',
                'type': 'text',
                'size': '64'
                }),
        button({
                'type': 'submit',
                'id': 'postMeow',
                'className': 'btn btn-primary'
                },
            'Meow'
            ))
    })

__pragma__('js', 'export default NewMeow')
