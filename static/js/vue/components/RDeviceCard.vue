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
      <v-spacer></v-spacer>

      <v-menu offset-y bottom>
        <template #activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item>
            <v-list-item-title @click="(ev) => $emit('delete', this.title)">
              DELETE
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-card-actions>
  </v-card>
</template>

<script>
module.exports = {
  model: {
    prop: "state",
  },
  emits: ["switch", "delete"],
  props: {
    state: { type: Boolean, default: false },
    title: { type: String, default: "device" },
    remark: { type: String, default: "" },
  },
};
</script>
