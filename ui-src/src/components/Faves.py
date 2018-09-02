__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import PropTypes from 'prop-types'
const { div, button } = require('hyperscript-helpers')(e)
''')

def Faves(ref):
    addFavourite = ref.addFavourite
    favourites = ref.favourites
    hash = ref.hash
    removeFavourite = ref.removeFavourite

    return div(None,
        (favourites and favourites.includes(hash)) and button({
            'onClick': lambda: removeFavourite(hash),
            'className': "glyphicon glyphicon-heart",
            'style': { 'color': "red" }
            }
        ) or button({
            'onClick': lambda: addFavourite(hash),
            'className': "glyphicon glyphicon-heart-empty",
            'style': { 'color': "red" }
            }
        ))

Faves.defaultProps = {
    'hash': '',
    'favourites': []
    }

Faves.propTypes = {
    'addFavourite': PropTypes.func.isRequired,
    'removeFavourite': PropTypes.func.isRequired
    }

__pragma__('js', 'export default Faves')
