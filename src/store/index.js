//引入Vue
import Vue from 'vue'

//引入Vuex
import Vuex from "vuex"

//使用Vuex插件
Vue.use(Vuex)

import dice from "./modules/dice.js"
import login from "./modules/login.js"
export default new Vuex.Store({
    modules: {
        login,
        dice
    }
})