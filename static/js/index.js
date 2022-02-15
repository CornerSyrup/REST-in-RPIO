Vue.use(httpVueLoader);

new Vue({
    vuetify: new Vuetify({
        theme: {
            primary: "#3f51b5",
            secondary: "#607d8b",
            accent: "#2196f3",
            error: "#ff5722",
            warning: "#e91e63",
            info: "#ffc107",
            success: "#8bc34a",
        },
    }),
    router: new VueRouter({
        mode: "history",
        routes: [],
    }),
    data: function () {
        return {
            message: null,
        };
    },
}).$mount("#vue");
