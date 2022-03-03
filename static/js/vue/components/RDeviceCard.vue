<template>
  <v-card class="ma-0 ma-sm-2 ma-md-4">
    <v-list-item two-line>
      <v-list-item-content>
        <v-list-item-title class="text-h5 mb-1">
          {{ title.toUpperCase() }}
        </v-list-item-title>

        <v-list-item-subtitle>
          {{ remark }}
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar size="72" color="grey">
        <v-icon size="48" dark>
          {{ state ? "mdi-led-on" : "mdi-led-off" }}
        </v-icon>
      </v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text @click="(ev) => $emit('switch', true)"> Turn On </v-btn>
      <v-btn text @click="(ev) => $emit('switch', false)"> Turn Off </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
module.exports = {
  model: {
    prop: "state",
  },
  emits: ["switch"],
  props: {
    state: { type: Boolean, default: false },
    title: { type: String, default: "device" },
    remark: { type: String, default: "" },
  },
};
</script>
