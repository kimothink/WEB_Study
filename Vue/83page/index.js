new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js',
  },
  methods: {
    handleInput: function (event) {
      // 할당 전에 어떤 처리하기
      this.message = event.target.value
    }
  }
})