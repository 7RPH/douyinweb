var Main = {
    data() {
      return {
        dynamicTags: [],
        inputVisible: false,
        inputValue: ''
      };
    },
    methods: {
      handleClose(tag) {
        this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
      },

      showInput() {
        this.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },

      handleInputConfirm() {
        let inputValue = this.inputValue;
        if (inputValue) {
          this.dynamicTags.push(inputValue);
        }
        this.inputVisible = false;
        this.inputValue = '';
      }
    }
  }
var Ctor = Vue.extend(Main)
new Ctor().$mount('#app')

$("#crawl").click(function(){
  let dom_tag=$(".el-tag")
  let keys=[]
  for(let i=0;i<dom_tag.length;i++){
    keys.push($.trim($(dom_tag[i]).text()))
  }
  $.post('/reloading_tag',JSON.stringify({
        key:keys
      }),
      function(data,status){

      })
})