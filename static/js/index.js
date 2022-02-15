Vue.use(httpVueLoader);

new Vue({
    vuetify: new Vuetify(),
    router: new VueRouter({
        mode: "history",
        routes: [],
    }),
}).$mount("#app");
