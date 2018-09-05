__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import PropTypes from 'prop-types'
import { Provider } from 'react-redux'
import { PersistGate } from 'redux-persist/es/integration/react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import AppContainer from './AppContainer'
''')

Root = lambda stored: e(Provider, { 'store': stored['store'] },
    e(PersistGate, { 'loading': None, 'persistor': stored['persistor']},
        e(Router, None,
            e(Route, { 'path': '/', 'component': AppContainer }))))

Root.propTypes = { 'store': PropTypes.object.isRequired }

__pragma__('js', 'export default Root')
