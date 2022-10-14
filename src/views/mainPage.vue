<template>
  <div class="mainBox">
     <div class="btn song">
      <i class="iconfont icon-yinlemusic215"></i>
      <span>音乐</span>
    </div>
    <avatarTop class="avatarTop"></avatarTop>
    <diceBox :isTurn="!isTurn" pos="top" :BoardData="otherBoard" class="diceBoxTop"></diceBox>
    <div class="number">
      <mt-button v-if="!isBegin" type="default" @click="gameStart">开始游戏</mt-button>
      <img v-show="number==1" src="../assets/dice/dice1.png">
      <img v-show="number==2" src="../assets/dice/dice2.png">
      <img v-show="number==3" src="../assets/dice/dice3.png">
      <img v-show="number==4" src="../assets/dice/dice4.png">
      <img v-show="number==5" src="../assets/dice/dice5.png">
      <img v-show="number==6" src="../assets/dice/dice6.png">
    </div>
    <diceBox :isTurn="isTurn" pos="bottom" :BoardData="ownBoard" class="diceBoxBottom"></diceBox>
    <avatarBottom class="avatarBottom"></avatarBottom>
    <div class="btn return" @click='$router.replace("/index")'>
      <i class="iconfont icon-fanhui5"></i>
      <span>返回</span>
    </div>
    <div class="btn back" @click="retData()">
      <i class="iconfont icon-chexiao-tianchong"></i>
      <span>撤销</span>
    </div>
    <div class="btn out">
      <i class="iconfont icon-shibai"></i>
      <span>认输</span>
    </div>
  </div>
</template>

<script>
import avatarTop from "../components/avatarTop.vue"
import avatarBottom from "../components/avatarBottom.vue"
import diceBox from "../components/diceBox.vue"
import {mapMutations,mapGetters} from 'vuex';
export default {
  data(){
    return{
      isBegin:false,
      needSong:true
    }
  },
  computed:{
    ...mapGetters('dice',["number","isTurn","ownBoard","otherBoard","isOver","otherSum",'ownSum']),
  },
  components:{
    avatarTop,
    avatarBottom,
    diceBox,
  },
  mounted(){
    this.retAll()
  },
  methods:{
     ...mapMutations('dice',[
     'updiceData',
     'updateTurn',
     'calSum',
     'checkOver',
     'getNum',
     'updateReady',
     "retData",
     "retAll"]),
     gameStart(){
        this.isBegin=true;
        this.getNum();
        this.updateReady();
     }
  }
}
</script>

<style lang="less" scoped>
.mainBox{
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  background: linear-gradient(to right bottom,rgb(181, 225, 239),rgb(237, 237, 218));
  .btn{
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    span{
      font-weight: bold;
    }
    .iconfont{
      font-size: 35px;
    }
  }
  .song{
    position: absolute;
    top :20px;
    right: 20px;
  }
  .return{
    position: absolute;
    bottom  :5px;
    left: 10px;
  }
  .back{
    position: absolute;
    bottom  :5px;
    left: 60px;
  }
  .out{
    position: absolute;
    bottom  :5px;
    left: 110px;
  }
  .number{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80px;
    margin: 10px 0px;
    img{
      width: 60px;
      height: 60px;
    }
  }
  .avatarTop{
    align-self: flex-start;
    margin: 10px 0px 10px 20px
  }
  .avatarBottom{
    align-self: flex-end;
    margin-right: 20px;
    margin-top: 10px;
  }
}

</style>
