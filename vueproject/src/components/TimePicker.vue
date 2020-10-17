<template>
  <v-row>
    <v-col cols="11" sm="5">
      <v-menu
        ref="menu"
        v-model="menu2"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="time"
        transition="scale-transition"
        offset-y
        max-width="290px"
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="time"
            label="Picker in menu"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="menu2"
          v-model="time"
          full-width
          @click:minute="$refs.menu.save(time)"
          @input="changeTime"
        ></v-time-picker>
      </v-menu>
      <!-- <p>
        Time in ISO format: <strong>{{ time }}</strong>
      </p> -->
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      time: null,
      menu2: false,
      modal2: false,
    };
  },
  created() {
    const date = new Date();
    const initHours = date.getHours() + 1
    const initMinutes = date.getMinutes()
    this.time = `${String(initHours).padStart(2, '0')}:${String(initMinutes).padStart(2, '0')}`
  },
  methods: {
    changeTime() {
      this.$emit("passTimeToParent", this.time);
    },
  },
};
</script>