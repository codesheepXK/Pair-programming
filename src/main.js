import Vue from 'vue'
import App from './App.vue'
import Mint from 'mint-ui';
import router from './router'
import store from './store/index.js'
import 'mint-ui/lib/style.css'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Mint);
Vue.use(ElementUI);
Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App),

}).$mount('#app')