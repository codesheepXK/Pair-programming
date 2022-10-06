<template>
  <div class="mainBox">
    <div class="header">
       <mt-button icon="back"  @click='$router.replace("/index")'></mt-button>
       <span class="numStyle">当前数字：{{number}}</span>
       <mt-button icon="more" ></mt-button>
    </div>
    <diceBox :isTurn="!isTurn" pos="top" :BoardData="otherBoard"></diceBox>
    <diceBox :isTurn="isTurn" pos="bottom" :BoardData="ownBoard"></diceBox>
    <pageBottom></pageBottom>
  </div>
</template>

<script>
import diceBox from "../components/diceBox.vue"
import pageBottom from "../components/pageBottom.vue"
import {mapActions,mapGetters} from 'vuex';
export default {
  data(){
    return{
    }
  },
  computed:{
    ...mapGetters('dice',["number","isTurn","ownBoard","otherBoard"])
  },
  components:{
    diceBox,
    pageBottom
  },
  methods:{
     ...mapActions('dice',[
     'updiceData',
     'updateTurn',
     'calSum',
     'checkOver']),
  }
}
</script>

<style lang="less" scoped>
.mainBox{
  position: relative;
  width: 100%;
  height: 100vh;
  background: linear-gradient(to right bottom,rgb(181, 225, 239),rgb(237, 237, 218));
  // &::before{
  //   content: '';
  //   position: absolute;
  //   top: 0;
  //   left: 0;
  //   width: 100%;
  //   height: 100%;
  //   filter: blur(12px);
  //   background: url("../assets/logo.jpg") no-repeat;
  //   background-size: 100% 100%;
  //    z-index: -1;
  // };
  .header{
    width: 100%;
    height: 40px;
    position:relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    .numStyle{
      text-align: center;
      font-size: 18px;
      font-weight: 600;
      color: #fff;
    }
    .mint-button {
      background-color:inherit;
      font-size: 12px;
      color: #fff;
      border: 0px;
      box-shadow: none;
    }
  }
}

</style>