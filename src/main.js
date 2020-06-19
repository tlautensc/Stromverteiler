import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import "./assets/materialKit.scss"
import VueFriendlyIframe from 'vue-friendly-iframe'

Vue.use(VueMaterial)
Vue.use(VueFriendlyIframe)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
