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
              @passTaskListAfterAddTask="updateTaskListAfterAddTask"
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
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
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
  }),
  created() {
    axios.get("/json").then((res) => {
      res.data.forEach((task) => {
        this.tasks.push({
          name: task.name,
          limit: this.msToTime(new Date(task.deadLine)),
          id: task.id,
        });
      });
    });
    this.sendOauthVerifier(this.$route.query.oauth_verifier);

    this.findExpiredTask();
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },

    tasks() {
      return [
        {
          name: "課題",
          limit: this.msToTime(new Date("2020/10/16/12:30:00")),
          id: 1,
        },
        {
          name: "プログラミングする",
          limit: this.msToTime(new Date("2020/10/21/9:30:00")),
          id: 2,
        },
        {
          name: "ES提出",
          limit: this.msToTime(new Date("2020/10/21/11:22:00")),
          id: 3,
        },
        {
          name: "英単語100個",
          limit: this.msToTime(new Date("2020/10/21/17:00:00")),
          id: 4,
        },
        {
          name: "書類提出",
          limit: this.msToTime(new Date("2020/10/21/10:25:00")),
          id: 5,
        },
        {
          name: "ランニング10km",
          limit: this.msToTime(new Date("2020/10/21/9:40:00")),
          id: 6,
        },
        {
          name: "友達と遊ぶ",
          limit: this.msToTime(new Date("2020/10/21/22:00:30")),
          id: 7,
        },
      ];
    },
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
      this.dialog = true;
    },

    deleteItem(item) {
      this.checkbox = false;
      this.editedIndex = this.tasks.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
      axios
        .delete(`/task/delete/${item.id}`)
        .then((res) => {
          res.data.forEach((task) => {
            this.tasks = []
            this.tasks.push({
              name: task.name,
              limit: this.msToTime(new Date(task.deadLine)),
              id: task.id,
            });
          });
        });
    },

    deleteItemConfirm() {
      this.tasks.splice(this.editedIndex, 1);
      if (this.checkbox) {
        console.log("Tweet task complete!");
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
      if (this.editedIndex > -1) {
        // 編集
        Object.assign(this.tasks[this.editedIndex], this.editedItem);
      } else {
        // 新規投稿
        this.tasks.push(this.editedItem);
        this.$refs.taskform.submit();
      }
      this.close();
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

    sendOauthVerifier(query) {
      axios
        .post("link", {
          token: query,
        })
        .then((res) => {
          this.taskData = res;
        });
    },

    updateTaskListAfterAddTask(data) { // 送信後のres.data
    this.tasks = []
      data.forEach((task) => {
        this.tasks.push({
          name: task.name,
          limit: this.msToTime(new Date(task.deadLine)),
          id: task.id,
        });
      });
    }
  },
};
</script>

<style scoped>
.v-card.v-sheet.theme--light {
  padding: 2rem;
}
</style>
