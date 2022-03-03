<template>
  <v-container tag="section">
    <v-row align="center" align-content="stretch" justify="space-around">
      <v-col v-for="dev in devices" :key="dev.title" sm="6" md="4">
        <r-device-card
          v-model="dev.state"
          :title="dev.title"
          :remark="dev.remark"
          @switch="(ev) => (ev ? turnOnLed(dev) : turnOffLed(dev))"
        />
      </v-col>
    </v-row>

    <r-device-form @input="(ev) => registerNewDev(ev)" />
  </v-container>
</template>

<script>
Vue.component(
  "r-device-card",
  httpVueLoader("static/js/vue/components/RDeviceCard.vue")
);
Vue.component(
  "r-device-form",
  httpVueLoader("static/js/vue/components/RDeviceForm.vue")
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
    registerNewDev(device) {
      console.log("");
      if (!device.isValid()) {
        return;
      }

      fetch(`/devices/`, { method: "post", body: JSON.stringify(device) }).then(
        (res) => {
          if (res.status >= 200 && res.status < 300) {
            this.devices.push(device);
          }
        }
      );
    },
  },
};
</script>
