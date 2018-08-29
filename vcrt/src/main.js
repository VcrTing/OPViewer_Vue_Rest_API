// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './base.css'
import Axios from 'axios'
import QS from 'qs'
import PubSub from 'pubsub-js'
import SQL from './utils/storage_util.js'

// Axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencode'
Vue.config.productionTip = false
Vue.prototype.$axios = Axios
Vue.prototype.$qs = QS
Vue.prototype.$pubsub = PubSub
Vue.prototype.$sql = SQL
Vue.prototype.$web_conf = {
  'WEB_URL': 'http://127.0.0.1:8000',
  'MEDIA_URL': 'http://127.0.0.1:8000/media/',
  'USER_URL': 'http://127.0.0.1:8000/api/user',
  'KUUKANN_URL': 'http://127.0.0.1:8000/api/kuukann'
}
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
