__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import PropTypes from 'prop-types'
const { div, p } = require('hyperscript-helpers')(e)
''')

def modalRender(self):
    # Render nothing if the "show" prop is false
    if not self.props.show:
        return None

    # The gray background
    backdropStyle = {
        'position': "fixed",
        'top': 0,
        'bottom': 0,
        'left': 0,
        'right': 0,
        'backgroundColor': "rgba(0,0,0,0.3)",
        'padding': 50
        }

    # the modal "window"
    modalStyle = {
        'backgroundColor': '#fff',
        'borderRadius': 5,
        'maxWidth': 500,
        'minHeight': 200,
        'margin': "0 auto",
        'padding': 30
        }

    return div({ 'style': backdropStyle },
        div({ 'style': modalStyle },
            div({ 'align': "center" },
                p({ 'className': "h1" }, "Welcome to Coolcats!")),
            div(None, self.props.children)))

Modal = createReactClass({
    'render': lambda: modalRender(this)
    })

Modal.propTypes = {
    'show': PropTypes.bool,
    'children': PropTypes.node
    }

__pragma__('js', 'export default Modal')
