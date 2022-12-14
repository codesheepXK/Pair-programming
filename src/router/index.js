import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)
export default new VueRouter({
    routes: [

        {
            path: "/main",
            name: "main",
            component: () =>
                import ("../views/mainPage.vue")
        },
        {
            path: "/intro",
            name: "intro",
            component: () =>
                import ("../views/introPage.vue")
        },
        {
            path: "/list",
            name: "list",
            component: () =>
                import ("../views/listPage.vue")
        },
        {
            path: "/index",
            name: "index",
            component: () =>
                import ("../views/chooseIndex.vue")
        },
        {
            path: "/login",
            name: "login",
            component: () =>
                import ("../views/loginPage.vue")
        },
    ]
})
