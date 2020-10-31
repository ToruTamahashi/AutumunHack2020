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
import axios from "axios";

export default {
  components: {
    DatePicker,
    TimePicker,
  },
  data: function () {
    return {
      valid: true,
      task: this.editTask.name,
      taskRules: [
        (v) => !!v || "タスクは必須です",
        (v) =>
          (v && v.length <= 100) || "タスクは100文字以内である必要があります",
      ],
      email: this.editTask.mail,
      emailRules: [
        (v) => !!v || "メールアドレスは必須です",
        (v) => /.+@.+\..+/.test(v) || "有効なメールアドレスを入力してください",
      ],
      checkbox: false,
      date: null,
      time: "",
      responseTaskList: [],
      editFormBoolean: this.editForm
    };
  },
  computed: {
    fullDate() {
      return new Date(`${this.date}/${this.time}:00`);
    },
    fullDateString() {
      return `${this.date}/${this.time}:00`;
    },
  },
  props: {
    editTask: {
      type: Object,
    },
    editForm: {
      type: Boolean
    }
  },
  watch: {
    editTask(newTask) {
      this.task = newTask.name;
      this.email = newTask.mail;
    },
    editForm(newEditForm) {
      this.editFormBoolean = newEditForm
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
      if (!this.editForm) {
        // axiosで送信処理をする
      axios
        .post("http://localhost:5000/create/task", {
          title: this.task,
          mail: this.email,
          deadline_at: this.fullDateString,
          tweet: this.booleanToNumber(), // タスク追加時にツイートするか
          // tweetedExpiredTask: 0, // 既に期限切れタスクとしてツイートしたか/
        })
        .then(() => {
          this.addedTask();
        });
      } else {
        this.updateTask()
      }
      this.task = "";
      this.email = "";
      this.$refs.form.resetValidation();
    },
    updateTask() {
      axios
        .put("http://localhost:5000/update/task", {
          id: this.editTask.id,
          title: this.task,
          mail: this.email,
          tweet: this.booleanToNumber(),
          deadline_at: this.fullDateString,
        })
        .then((res) => {
          console.log(res)
          this.addedTask();
          this.$emit("updated")
        })
        .catch((e) => {
          console.log(e.message);
        });
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
      this.$emit("passTaskListAfterAddTask", data);
    },
    addedTask() {
      this.$emit("addedTask");
    },
    booleanToNumber() {
      if (this.checkbox) {
        return 1;
      } else {
        return 0;
      }
    },
  },
};
</script>