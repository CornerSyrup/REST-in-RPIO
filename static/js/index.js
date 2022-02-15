Vue.use(httpVueLoader);

new Vue({
    vuetify: new Vuetify(),
    router: new VueRouter({
        mode: "history",
        routes: [],
    }),
    data: function () {
        return {
            drawer: false,
            message: null,
        };
    },
}).$mount("#vue");
