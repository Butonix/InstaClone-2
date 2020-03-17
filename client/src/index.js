import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import './utils/axiosSetup'

import store from './state/store'
import App from './App'
import FetchUser from './components/FetchUser'
import GlobalStyle from './components/styles/GlobalStyle'

ReactDOM.render(
  <>
    <GlobalStyle />
    <Provider store={store}>
      <FetchUser>
        <App />
      </FetchUser>
    </Provider>
  </>,
  document.getElementById('root')
)
