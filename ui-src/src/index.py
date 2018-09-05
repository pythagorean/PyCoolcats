__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import ReactDOM from 'react-dom'
import Root from './Root'
import './index.css'
import registerServiceWorker from './registerServiceWorker'
import CreateStore from './store'
''')

store = CreateStore()

ReactDOM.render(e(Root, {
        'store': store['store'],
        'persistor': store['persistor']
        }),
    document.getElementById('root'));

registerServiceWorker()
