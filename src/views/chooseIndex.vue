<template>
  <div class="indexBox">
    <mt-button icon="back"  @click='$router.replace("/intro")' class="backBtn"></mt-button>
    <img src="../assets/choose.png">
    <div class="chooseBox">
        <mt-button 
            v-for="(item,index) in buttons" :key="index" 
            @click='goBoard(index)'
            plain
        >
            {{item.title}}
        </mt-button>
    </div>
    <div class="toPoint" @click='$router.replace("/list")'>
        <span>点击查看排行榜</span>
        
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
export default {
    data(){
        return{
            buttons:[{title:"人机对战"},{title:"本地对战"},{title:"匹配对战"}]
        }
    },
    computed:{
        ...mapGetters('dice',['isAI'])
    },
    methods:{
        ...mapMutations('dice',["setAI"]),
        goBoard(index){
            if(index==0&&this.isAI==false){
                this.setAI()
            }
            else if(index!=0&&this.isAI==true){
                this.setAI()
            }
            this.$router.replace('/main')
        }
    }
}
</script>

<style lang="less" scoped>
.indexBox{
    position: relative;
    width: 100%;
    height: 100vh; 
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(to right bottom,rgb(181, 225, 239),rgb(237, 237, 218));
    .backBtn{
        position: absolute;
        top:0px;
        left: 0px;
        color: #fff;
        background-color: inherit;
        border: 0px;
         box-shadow: none;
    }
    img{
        position: absolute;
        top: 68px;
        width: 80%;
    }
    .toPoint{
        position: absolute;
        bottom: 40px;
        right: 0px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 150px;
        height: 40px;
        color: #999;
        font-weight: bold;
        background-color: #fff;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
    }
}
.chooseBox{
    width: 75%;
    height: 50%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    background: rgba( 255, 255, 255, 0.5 );
    border: 1px solid rgba( 255, 255, 255, 0.18 );
    border-radius: 20px;
    margin-top: 80px;
    .mint-button{   
        width: 60%;
        height: 45px;
        color: #aaa;
        font-weight: 600;
        background-color: #fff;
        border: 2px solid #eee;
        border-radius: 10px;
        margin: 20px 0;
        &:hover{
            box-shadow: 0 0 5px gray inset;
            transform: scale(.95)
        }
    }
    .mint-button:nth-child(1){
        margin-top: 60px;
    }
}

</style>
