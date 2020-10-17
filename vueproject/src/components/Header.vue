<template>
  <!-- <div>
    <router-link to="/">Landing</router-link>
    <router-link to="/top">Top</router-link>
    <router-link to="/user">User</router-link>
  </div> -->
  <v-card
  color="grey lighten-4"
  flat
  tile
  >
  <v-toolbar dense>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>時間の達人</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text>
         <router-link to="/">トップ</router-link>
      </v-btn>

      <v-btn text>
        <router-link to="/top">タスクの追加</router-link>
      </v-btn>

      <v-btn text>
        <router-link to="/user">秘密の設定</router-link>
      </v-btn>
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  
}
</script>

<style scoped>
  a {
    margin-right: 1rem;
  }
</style>