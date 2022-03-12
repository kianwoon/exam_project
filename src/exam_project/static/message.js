// var app = new Vue({
//     el: '#app',
//     delimiters: ['[[', ']]'],
//     data: {
//       results: 'Welcome to K2Lab '
//     },
//     mounted() {
//       axios.get("http://192.168.1.154:8080/Announcement/")
//       .then(response => {this.results = response.data.results[0].msg_body})
//     }
// })


const apiURL = '/Announcement/';
//    const apiURL = 'https://jsonplaceholder.typicode.com/todos';
var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        results: 'welcome to k2lab',
    },
    methods: {
        greet: function () {
            alert()
        },
        fetchData: function () {
            // Messenger();
            this.load = true;
            axios.get(apiURL)
                .then(function (response) {
                    this.results = (response.data.results[0].msg_body);
                    
                }.bind(this))
                .catch(function (error) {
                    console.log(error);
                });

        },
    },
    mounted: function () {
        this.fetchData();

        this.interval = setInterval(function () {
            this.fetchData();
        }.bind(this), 300000);
    },
})