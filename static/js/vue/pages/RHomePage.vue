<template>
    <v-container tag="section">
        <v-row align="center" align-content="stretch" justify="space-around">
            <v-col v-for="dev in devices" :key="dev.title" sm="6" md="4">
                <v-card class="ma-0 ma-sm-2 ma-md-4">
                    <v-list-item two-line>
                        <v-list-item-content>
                            <v-list-item-title class="text-h5 mb-1">
                                {{ dev.title.toUpperCase() }}
                            </v-list-item-title>

                            <v-list-item-subtitle>
                                {{ dev.remark }}
                            </v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-avatar size="72" color="grey">
                            <v-icon size="48" dark>
                                {{ dev.state ? "mdi-led-on" : "mdi-led-off" }}
                            </v-icon>
                        </v-list-item-avatar>
                    </v-list-item>

                    <v-card-actions>
                        <v-btn text @click="turnOnLed(dev)"> Turn On </v-btn>
                        <v-btn text @click="turnOffLed(dev)"> Turn Off </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
module.exports = {
    data: function () {
        return {
            title: "Home",
            devices: [
                { title: "living", state: false, remark: "" },
                { title: "kitchen", state: false, remark: "" },
                { title: "tv", state: false, remark: "" },
            ],
        };
    },
    methods: {
        turnOnLed(device) {
            fetch(`/on/${device.title}`);
            device.state = true;
        },
        turnOffLed(device) {
            fetch(`/off/${device.title}`);
            device.state = false;
        },
    },
};
</script>

<style scoped>
h2 {
    color: red;
}
</style>
