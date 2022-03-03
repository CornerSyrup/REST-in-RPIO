<template>
  <v-container tag="section">
    <v-row align="center" align-content="stretch" justify="space-around">
      <v-col v-for="dev in devices" :key="dev.title" sm="6" md="4">
        <r-device-card
          v-model="dev.state"
          :title="dev.name"
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
      devices: [],
    };
  },
  methods: {
    turnOnLed(device) {
      fetch(`/pins/dev/${device.name}`, {
        method: "PUT",
        body: JSON.stringify({ state: true }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      device.state = true;
    },
    turnOffLed(device) {
      fetch(`/pins/dev/${device.name}`, {
        method: "PUT",
        body: JSON.stringify({ state: false }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      device.state = false;
    },
    registerNewDev(device) {
      console.log("");
      if (!device.isValid()) {
        return;
      }

      fetch(`/devices/`, {
        method: "post",
        body: JSON.stringify(device),
        headers: { "Content-Type": "application/json" },
      }).then((res) => {
        if (res.status >= 200 && res.status < 300) {
          this.devices.push(device);
        }
      });
    },
  },
  mounted: function () {
    fetch("/devices/")
      .then((res) => res.json())
      .then((data) => (this.devices = data.devices));
  },
};
</script>
