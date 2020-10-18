<template>
  <v-form>
    <v-container fluid fill-height align="center">
      <v-row align="center">
        <v-col cols="12" sm="6">
          <v-text-field
            class="mb-10"
            v-model="secret_mess"
            :rules="rules"
            counter="50"
            hint="絶対誰にも言わないから"
            label="とっておきの秘密を教えて！"
          ></v-text-field>

          <v-btn depressed color="primary">これに決定！</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data: function () {
    return {
      secret_mess: "",
      rules: [v => v.length <= 50 || 'Max 50 characters'],
    }
  },
};
</script>
