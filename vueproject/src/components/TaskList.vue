<template>
  <v-data-table
    :headers="headers"
    :items="tasks"
    sort-by="limit"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="800px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <TaskForm
              ref="taskform"
              @submitFromTaskForm="save"
              @closeFromTaskForm="close"
              @addedTask="fetchTasks"
              @updated="updated"
              :editTask="editTask"
              :editForm="editForm"
            />
          </v-card>
        </v-dialog>

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline"
              >このタスクを削除しますか？</v-card-title
            >

            <v-form ref="form" v-model="valid" lazy-validation>
              <v-checkbox
                v-model="checkbox"
                label="タスク完了ツイートをする"
              ></v-checkbox>
            </v-form>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >キャンセル</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import TaskForm from "./TaskForm.vue";
import axios from "axios";

const dayfullMilliseconds = 1000 * 60 * 60 * 24;
const hourMilliseconds = 1000 * 60 * 60;
const minuteMilliseconds = 1000 * 60;

export default {
  components: {
    TaskForm,
  },
  data: () => ({
    valid: true,
    checkbox: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "ID",
        value: "id",
      },
      {
        text: "タスク",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "期限", value: "limit", sortable: false },
      { text: "操作", value: "actions", sortable: false },
    ],
    editedIndex: -1,
    editedItem: {
      name: "",
      limit: 0,
      id: "",
    },
    defaultItem: {
      name: "",
      limit: 0,
    },
    now: new Date(),
    taskData: [],
    tasks: [],
    editTask: {},
    editForm: false
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },

    // tasks() {
    //   return [
    //     {
    //       name: "課題",
    //       limit: this.msToTime(new Date("2020/10/16/12:30:00")),
    //       id: 1,
    //     },
    //   ];
    // },
  },
  created() {
    axios.get("http://localhost:5000/read/tasks")
    .then((res) => {
      res.data.forEach((task) => {
        this.tasks.push({
          id: task.id,
          user_id: task.user_id,
          name: task.title,
          mail: task.mail,
          limit: this.msToTime(new Date(task.deadline_at)),
          tweet: task.tweet
        });
      });
    })
    .catch(e => {
      console.log(e.message)
    })
    // this.sendOauthVerifier(this.$route.query.oauth_verifier);

    this.findExpiredTask();
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
    now: {
      handler(value) {
        if (value > 0) {
          setTimeout(() => {
            this.now = new Date();
          }, 1000 * 60);
        }
      },
      immediate: true,
    },
  },

  methods: {
    editItem(item) {
      this.editedIndex = this.tasks.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.editTask = this.tasks[this.editedIndex]
      this.editForm = true
      this.dialog = true;
    },

    deleteItem(item) {
      this.checkbox = false;
      this.editedIndex = this.tasks.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      const deleteTaskId = this.tasks[this.editedIndex].id;
      console.log(deleteTaskId);
      axios
        .post("http://localhost:5000/destroy/task", { id: deleteTaskId })
        .then(() => {
          this.tasks = [];
          this.fetchTasks();
        })
        .catch((e) => {
          console.log(e.message);
        });
      if (this.checkbox) {
        console.log("Tweeted task done!");
      }
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      this.$refs.taskform.submit();
      this.close(); // formを閉じる
    },

    updated() {
      this.editForm = false
    },

    msToTime(date) {
      const duration = date.getTime() - this.now.getTime();
      if (duration < 0) {
        return "期限切れ";
      }

      const day = Math.floor(duration / dayfullMilliseconds);
      const hour = Math.floor(
        (duration - dayfullMilliseconds * day) / hourMilliseconds
      );
      const minute = Math.floor(
        (duration - dayfullMilliseconds * day - hourMilliseconds * hour) /
          minuteMilliseconds
      );

      const hh = ("00" + hour).slice(-2);
      const mm = ("00" + minute).slice(-2);
      // const ms = ("00000" + (duration % 60000)).slice(-5);

      const time = `${String(day).padStart(2, "0")}日${hh}時${mm}分`;

      return time;
    },

    findExpiredTask() {
      this.tasks.forEach((task) => {
        if (task.limit === "期限切れ") {
          const tweetTaskId = task.id;
          console.log(tweetTaskId);
          // バックエンドにid渡してツイート要請
          axios.get(`/task/${tweetTaskId}`).then((res) => {
            const tweetedExpiredTask = res.data.tweetedExpiredTask;
            if (tweetedExpiredTask === 0) {
              // まだツイートしていない
              // id添えてツイートするようpostリクエスト送る
              axios.put(`/task/update/${tweetTaskId}`, {
                tweetedExpiredTask: 1,
              });
            }
          });
        }
      });
    },

    // sendOauthVerifier(query) {
    //   axios
    //     .post("link", {
    //       token: query,
    //     })
    //     .then((res) => {
    //       this.taskData = res;
    //     });
    // },

    updateTaskListAfterAddTask(data) {
      // 送信後のres.data
      this.tasks = [];
      data.forEach((task) => {
        this.tasks.push({
          id: task.id,
          user_id: task.user_id,
          name: task.title,
          mail: task.mail,
          limit: this.msToTime(new Date(task.deadline_at)),
          tweet: task.tweet
        });
      });
    },

    fetchTasks() {
      this.tasks = [];
      axios.get("http://localhost:5000/read/tasks").then((res) => {
        res.data.forEach((task) => {
          this.tasks.push({
          id: task.id,
          user_id: task.user_id,
          name: task.title,
          mail: task.mail,
          limit: this.msToTime(new Date(task.deadline_at)),
          tweet: task.tweet
        });
        });
      });
    },
  },
};
</script>

<style scoped>
.v-card.v-sheet.theme--light {
  padding: 2rem;
}
</style>
