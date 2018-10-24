js_import = ('''
import { connect } from 'react-redux'
import Faves from './components/Faves'
import { addFavourite, removeFavourite } from './actions'
''')

def mapStateToProps(state):
    return { 'favourites': state.favourites }

def mapDispatchToProps(dispatch, ownProps):
    return {
        'addFavourite': lambda favouriteHash: dispatch(
            addFavourite(favouriteHash)),
        'removeFavourite': lambda favouriteHash: dispatch(
            removeFavourite(favouriteHash))
        }

__pragma__('js',
    'export default connect(mapStateToProps, mapDispatchToProps)(Faves)')
