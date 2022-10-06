<template>
  <div class="bottomBox">
    <mt-button type="default" @click="gameHost">
        {{hostText}}
    </mt-button>
    <span v-show="isHost">托管中...</span>
    <mt-button type="default" @click="gameStart">开始游戏</mt-button>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'
export default {
    data(){
        return{
            isHost:false,
            hostText:"托管"
        }
    },
    methods:{
        ...mapMutations('dice',["getNum","updateTurn","updateReady"]),
        gameHost(){
            this.isHost=!this.isHost;
            if(this.isHost){
                this.hostText="取消托管"
            }else{
                this.hostText="托管"
            }
        },
        gameStart(){
            this.getNum();
            this.updateReady();
        }
    }
}
</script>

<style lang="less" scoped>
.bottomBox{
    position:absolute;
    bottom: 0px;
    width: 100%;
    height: 60px;
    display: flex;
    justify-content:space-around;
    align-items: center;
    background-color: #fff;
    span{
        font-weight: bold;
        color: #999;
    }
    .mint-button{
        color: #999;
    }
}
</style>