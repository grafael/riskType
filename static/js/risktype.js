var app = new Vue({
    el: '#app_risktype',
    delimiters: ['[[', ']]'],
    data: {
      headers: [{text: 'Name', value:'name', align:'left'}],
      dialog: false,
      selected: {},
      riskTypes: [],
    },
    mounted: function() {
        this.fetchRiskTypes();
    },
    methods: {
      fetchRiskTypes: function(){
          axios.get('risktype')
          .then(function(response){
            app.riskTypes = response.data;
          }); 
      },
      showForm: function(item){
        this.selected = item;
        this.dialog = true;
      },
      hideForm: function(){
        this.selected = {};
        this.dialog = false;
      },
    }

  })
