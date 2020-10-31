<template>
  <v-app>
    <v-container fluid fill-height class="purple darken-4">
      <v-row
        class="purple darken-4"
        style="height: 450px"
        justify="center"
        align-content="center"
      >
        <v-img
          contain
          max-height="600"
          max-width="600"
          src="../assets/top-image.png"
        ></v-img>
        <v-col>
          <h1 class="mb-10 font-weight-black white--text">
            自分を追い込むたった一つの方法
          </h1>
          <p class="mb-10 font-weight-black white--text">
            当サービスは、秘密を書き込み決められた時間にタスクが終わらなかった場合、強制的にTwitterに書き込まれるクレイジーでストイックなサービスです。
          </p>
          <v-btn
            @click="getCreateUrl()"
            class="cyan accent-3 black--text font-weight-regular"
            depressed
            elevation="15"
            raised
            rounded
            x-large
            >時間の達人になる</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  import axios from 'axios'
export default {
  methods: {
    getCreateUrl() {
      axios.get('http://localhost:5000/session',{ withCredentials: true })
            .then(response => {
              console.log(response.data.url);
              if (response.data.cookie == 'none') {
                location.href = response.data.url
              }else{
                location.href = 'http://localhost:8888/top'
              }
            })
            .catch(response => {
              console.log(response);
              alert("データの取得に失敗しました。");
            })
    }
  }
};
</script>
