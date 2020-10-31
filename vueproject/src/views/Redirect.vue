<template>
    <p>redirecting...</p>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Redirect",
        created() {
            console.log( this.$route.query.oauth_token)
            console.log( this.$route.query.oauth_verifier)
            let param = {'oauth_token':this.$route.query.oauth_token,'oauth_verifier':this.$route.query.oauth_verifier}
            axios.post('http://localhost:5000/token_cookie',param, { withCredentials: true })
            .then(response => {
              console.log(response.data) ;
              if (response.data.result == 'success') {
                  location.href = 'http://localhost:8888/top'
              }
            })
            .catch(response => {
              console.log(response);
              alert("データの取得に失敗しました。");
            })
        }
    }
</script>

<style scoped>

</style>