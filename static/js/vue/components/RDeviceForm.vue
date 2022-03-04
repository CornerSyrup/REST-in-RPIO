<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" max-width="600px">
      <template #activator="{ on }">
        <v-btn color="primary" fixed bottom right fab v-on="on">
          <v-icon> mdi-plus </v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Add New Device</span>
        </v-card-title>
        <v-card-text>
          <v-container tag="form" ref="form">
            <v-row>
              <v-col>
                <v-text-field
                  label="Name"
                  v-model="value.name"
                  :rules="[rules.required]"
                />
              </v-col>
              <v-col>
                <v-text-field
                  label="Pin"
                  type="number"
                  v-model="value.pin"
                  :rules="[rules.pin]"
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea label="Remarks" v-model="value.remarks" />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="(ev) => cancelForm()">
            Cancel
          </v-btn>
          <v-btn color="primary" text @click="(ev) => saveForm()"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
module.exports = {
  data: function () {
    return {
      dialog: false,
      value: new Device(),
      rules: {
        required: (value) => !!value,
        pin: (pin) => pin > 0 && pin <= 27,
      },
    };
  },
  methods: {
    closeForm() {
      this.dialog = false;
      this.value = new Device();
    },
    cancelForm() {
      this.$emit("input", null);
      this.closeForm();
    },
    saveForm() {
      this.$emit("input", this.value);
      this.closeForm();
    },
  },
};
</script>
