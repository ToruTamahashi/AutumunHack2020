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
    },
    defaultItem: {
      name: "",
      limit: 0,
    },
    now: new Date(),
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },

    tasks() {
      return [
        {
          name: "課題",
          limit: `${this.getLimitDay(new Date("2020/10/31/06:22:18"))}日
                  ${this.getLimitHours(new Date("2020/10/31/06:22:18"))}時
                  ${this.getLimitMinutes(new Date("2020/10/31/06:22:18"))}分
                  ${this.getLimitSeconds(new Date("2020/10/31/06:22:18"))}秒
                  `,
        },
        {
          name: "プログラミングする",
          limit: `${this.getLimitDay(new Date("2020/10/22/12:30:22"))}日
                  ${this.getLimitHours(new Date("2020/10/22/12:30:22"))}時
                  ${this.getLimitMinutes(new Date("2020/10/22/12:30:22"))}分
                  ${this.getLimitSeconds(new Date("2020/10/22/12:30:22"))}秒
                  `,
        },
        {
          name: "ES提出",
          limit: `${this.getLimitDay(new Date("2020/10/24/17:12:58"))}日
                  ${this.getLimitHours(new Date("2020/10/24/17:12:58"))}時
                  ${this.getLimitMinutes(new Date("2020/10/24/17:12:58"))}分
                  ${this.getLimitSeconds(new Date("2020/10/24/17:12:58"))}秒
                  `,
        },
        {
          name: "英単語100個",
          limit: `${this.getLimitDay(new Date("2020/10/26/22:00:00"))}日
                  ${this.getLimitHours(new Date("2020/10/26/22:00:00"))}時
                  ${this.getLimitMinutes(new Date("2020/10/26/22:00:00"))}分
                  ${this.getLimitSeconds(new Date("2020/10/26/22:00:00"))}秒
                  `,
        },
        {
          name: "書類提出",
          limit: `${this.getLimitDay(new Date("2020/11/3/07:00:30"))}日
                  ${this.getLimitHours(new Date("2020/11/3/07:00:30"))}時
                  ${this.getLimitMinutes(new Date("2020/11/3/07:00:30"))}分
                  ${this.getLimitSeconds(new Date("2020/11/3/07:00:30"))}秒
                  `,
        },
        {
          name: "ランニング10km",
          limit: `${this.getLimitDay(new Date("2020/10/23/03:15:40"))}日
                  ${this.getLimitHours(new Date("2020/10/23/03:15:40"))}時
                  ${this.getLimitMinutes(new Date("2020/10/23/03:15:40"))}分
                  ${this.getLimitSeconds(new Date("2020/10/23/03:15:40"))}秒
                  `,
        },
        {
          name: "友達と遊ぶ",
          limit: `${this.getLimitDay(new Date("2020/10/30/09:48:13"))}日
                  ${this.getLimitHours(new Date("2020/10/30/09:48:13"))}時
                  ${this.getLimitMinutes(new Date("2020/10/30/09:48:13"))}分
                  ${this.getLimitSeconds(new Date("2020/10/30/09:48:13"))}秒
                  `,
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
          }, 1000);
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
      this.checkbox = false
      this.editedIndex = this.tasks.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.tasks.splice(this.editedIndex, 1);
      if (this.checkbox) {
        console.log("Tweet task complete!")
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

    getLimitDay(date) {
      const limitDateMilliseconds = date.getTime() - this.now.getTime();
      return Math.floor(limitDateMilliseconds / dayfullMilliseconds);
    },

    getLimitHours(date) {
      const limitDateMilliseconds = date.getTime() - this.now.getTime();
      const day = Math.floor(limitDateMilliseconds / dayfullMilliseconds);
      return Math.floor(
        (limitDateMilliseconds - day * dayfullMilliseconds) / hourMilliseconds
      );
    },

    getLimitMinutes(date) {
      const limitDateMilliseconds = date.getTime() - this.now.getTime();
      const day = Math.floor(limitDateMilliseconds / dayfullMilliseconds);
      const hours = Math.floor(
        (limitDateMilliseconds - day * dayfullMilliseconds) / hourMilliseconds
      );
      return Math.floor(
        (limitDateMilliseconds -
          day * dayfullMilliseconds -
          hours * hourMilliseconds) /
          minuteMilliseconds
      );
    },

    getLimitSeconds(date) {
      const limitDateMilliseconds = date.getTime() - this.now.getTime();
      const day = Math.floor(limitDateMilliseconds / dayfullMilliseconds);
      const hours = Math.floor(
        (limitDateMilliseconds - day * dayfullMilliseconds) / hourMilliseconds
      );
      const minutes = Math.floor(
        (limitDateMilliseconds -
          day * dayfullMilliseconds -
          hours * hourMilliseconds) /
          minuteMilliseconds
      );
      return Math.floor(
        (limitDateMilliseconds -
          day * dayfullMilliseconds -
          hours * hourMilliseconds -
          minutes * minuteMilliseconds) /
          1000
      );
    },
  },
};
</script>

<style scoped>
.v-card.v-sheet.theme--light {
  padding: 2rem;
}
</style>
