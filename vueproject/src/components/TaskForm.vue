<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field
      v-model="task"
      :counter="100"
      :rules="taskRules"
      label="Task"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <DatePicker @passDateToParent="updateDate" />
    <TimePicker @passTimeToParent="updateTime" />

    <v-checkbox
      v-model="checkbox"
      label="タスク着手のツイートをする"
    ></v-checkbox>

    <v-btn :disabled="!valid" color="success" class="mr-4" @click="callSubmit">
      Submit
    </v-btn>

    <v-btn color="warning" @click="callClose">Close</v-btn>
  </v-form>
</template>

<script>
import DatePicker from "./DatePicker.vue";
import TimePicker from "./TimePicker.vue";
import axios from "axios"

export default {
  components: {
    DatePicker,
    TimePicker,
  },
  data: () => ({
    valid: true,
    task: "",
    taskRules: [
      (v) => !!v || "タスクは必須です",
      (v) =>
        (v && v.length <= 100) || "タスクは100文字以内である必要があります",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "メールアドレスは必須です",
      (v) => /.+@.+\..+/.test(v) || "有効なメールアドレスを入力してください",
    ],
    checkbox: false,
    date: null,
    time: "",
    responseTaskList: []
  }),
  computed: {
    fullDate() {
      return new Date(`${this.date}/${this.time}:00`);
    },
    fullDateString() {
      return `${this.date}/${this.time}:00`
    }
  },
  created() {
    const date = new Date();
    const initHours = date.getHours() + 1;
    const initMinutes = date.getMinutes();
    this.time = `${String(initHours).padStart(2, "0")}:${String(
      initMinutes
    ).padStart(2, "0")}`;
    this.date = this.formatDate(new Date(), "YYYY/MM/DD");
  },
  methods: {
    callSubmit() {
      if (this.$refs.form.validate()) {
        this.$emit("submitFromTaskForm");
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    callClose() {
      this.task = "";
      this.email = "";
      this.$refs.form.resetValidation();
      this.$emit("closeFromTaskForm");
    },
    submit() {
      // axiosで送信処理をする
      axios.post("/task/create/add", {
        task: this.task,
        email: this.email,
        deadLine: this.fullDateString,
        tweet: this.checkbox,
        tweetedExpiredTask: 0
      }).then(res => {
        this.responseTaskList = res.data
        this.passTaskListAfterAddTask(res.data)
      })
      this.task = "";
      this.email = "";
      this.$refs.form.resetValidation();
    },
    updateDate(date) {
      this.date = date;
    },
    updateTime(time) {
      this.time = time;
    },
    formatDate(date, format) {
      format = format.replace(/YYYY/, date.getFullYear());
      format = format.replace(/MM/, date.getMonth() + 1);
      format = format.replace(/DD/, date.getDate());

      return format;
    },
    passTaskListAfterAddTask(data) {
      this.$emit("passTaskListAfterAddTask", data)
    }
  },
};
</script>