import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// Storeを生成
const store = new Vuex.Store({
  state: {
    task: "",
    email: "",
    date: "",
    time: "",
    checkbox: ""
  },
  getters: {},
  mutations: {
    changeTask(state, content) {
      state.task = content
    }
  },
  actions: {}
});
export default store;