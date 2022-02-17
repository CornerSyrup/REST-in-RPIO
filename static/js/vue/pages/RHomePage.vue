<template>
  <v-container tag="section">
    <v-row align="center" align-content="stretch" justify="space-around">
      <v-col v-for="dev in devices" :key="dev.title" sm="6" md="4">
        <r-device-card
          v-model="dev.state"
          :title="dev.title"
          :remark="dev.remark"
        />
      </v-col>
    </v-row>

    <v-btn color="primary" fixed bottom right fab style="z-index: 6">
      <v-icon> mdi-plus </v-icon>
    </v-btn>
  </v-container>
</template>

<script>
Vue.component(
  "r-device-card",
  httpVueLoader("static/js/vue/components/RDeviceCard.vue")
);

module.exports = {
  data: function () {
    return {
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
