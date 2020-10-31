import Vue from "vue"
import VueRouter from "vue-router"

import Landing from "./views/Landing.vue"
import Top from "./views/Top.vue"
import User from "./views/User.vue"
import Redirect from "./views/Redirect.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    component: Landing
  },
  {
    path: "/top",
    component: Top
  },
  {
    path: "/user",
    component: User
  },
  {
    path: "/redirect",
    component: Redirect
  }
]

const router = new VueRouter({
  mode: "history",
  routes
})

export default router