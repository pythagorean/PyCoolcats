__pragma__('js', '{}', '''
import { createElement as e } from 'react'
import ReactDOM from 'react-dom'
import Root from './Root'
import './index.css'
import registerServiceWorker from './registerServiceWorker'
import CreateStore from './store'
''')

ReactDOM.render(e(Root, CreateStore()),
    document.getElementById('root'));

registerServiceWorker()
