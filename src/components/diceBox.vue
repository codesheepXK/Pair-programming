<template>
  <div class="diceBox">
    <ul>
        <li v-for="(item,index) in diceData" :key="index" 
            @click="confirmChoice(index)">
            <!-- <span v-show="item!=0">{{item}}</span> -->
            <img v-show="item==1" src="../assets/dice/dice1.png">
            <img v-show="item==2" src="../assets/dice/dice2.png">
            <img v-show="item==3" src="../assets/dice/dice3.png">
            <img v-show="item==4" src="../assets/dice/dice4.png">
            <img v-show="item==5" src="../assets/dice/dice5.png">
            <img v-show="item==6" src="../assets/dice/dice6.png">
        </li>
    </ul>
  </div>
</template>

<script>
import { MessageBox } from 'mint-ui';
import {mapMutations,mapGetters,mapActions} from 'vuex';
// import Vue from 'vue'
export default {
    props:{
        isTurn:Boolean,
        pos:String,
        BoardData:Array
    },
    data(){
        return{
            diceData:[0,0,0,0,0,0,0,0,0],
            timer: null,
        }
    },
    watch: {
        "diceData":{
            deep: true,
            immediate: true,
            handler(){
                this.diceData = this.BoardData
            }
        }
    },
    computed:{
        ...mapGetters('dice',['number','isReady','isAI',"isOver","otherSum",'ownSum']),
    },
    methods:{
        ...mapActions('dice',['checkOver',"updateDataAI"]),
        ...mapMutations('dice',[
        "getNum",
        'updateData',
        'updateTurn',
        "updateReady",
        'getData',
        "retAll"]),
        confirmChoice(index){
            if(this.isReady==false||this.isTurn==false||this.diceData[index]!=0){
                return;
            }
            MessageBox.confirm('确定放在这里吗?').then(()=>{
                this.updateData({pos:this.pos,index:index,data:this.number});

                if(!this.isAI){
                    this.$nextTick(()=>{
                        this.checkOver({pos:this.pos})
                        if(this.isOver){
                            MessageBox.alert(this.otherSum + ":" + this.ownSum, "游戏结束").then(() => {
                                this.$router.replace('/index')
                            })
                        }
                        else{
                            this.updateTurn()
                            this.getNum()
                        }  
                    })
                }
                else{
                    this.$nextTick(()=>{
                        this.checkOver({pos:this.pos})
                        if(this.isOver){
                            MessageBox.alert(this.otherSum + ":" + this.ownSum, "游戏结束").then(() => {
                                this.$router.replace('/index')
                            })
                        }
                        else{
                            this.getNum()
                            this.updateTurn()
                            clearTimeout(this.timer);
                            this.timer = setTimeout(()=>{
                                this.updateDataAI()
                                this.checkOver({pos:this.pos})
                                if(this.isOver){
                                    MessageBox.alert(this.otherSum + ":" + this.ownSum, "游戏结束").then(() => {
                                        this.$router.replace('/index')
                                    })
                                }else{
                                    this.getNum()
                                    this.updateTurn()
                                }
                            },1000);
                        }
                        
                    })
                }
            })
        }
    }

}
</script>

<style lang="less" scoped>
.diceBox{
    width: 80%;
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    ul{
        width: 80%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        li{
            width: 65px;
            height: 65px;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #999;
            // font-size: 25px;
            // font-weight: bold;
            border-radius: 10px;
            background-color: rgba(255,255,255,1);
            img{
                width: 50px;
                height: 50px;
            }
            margin:5px;
            &:hover{
                box-shadow: 0 0 5px gray inset;
                transform: scale(1.1)
            }
        }
    }
}
</style>
