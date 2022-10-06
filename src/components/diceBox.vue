<template>
  <div class="diceBox">
    <ul>
        <li v-for="(item,index) in diceData" :key="index" 
            @click="confirmChoice(index)">
            <span v-show="item!=0">{{item}}</span>
        </li>
    </ul>
  </div>
</template>

<script>
import { MessageBox } from 'mint-ui';
import {mapMutations,mapGetters,mapActions} from 'vuex';
import Vue from 'vue'
export default {
    props:{
        isTurn:Boolean,
        pos:String,
        BoardData:Array
    },
    data(){
        return{
            diceData:[0,0,0,0,0,0,0,0,0]
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
        ...mapGetters('dice',['number','isReady']),
    },
    methods:{
        ...mapActions('dice',['checkOver']),
        ...mapMutations('dice',[
        "getNum",
        'updateData',
        'updateTurn',
        "updateReady",
        'getData']),
        confirmChoice(index){
            if(this.isReady==false||this.isTurn==false||this.diceData[index]!=0){
                return;
            }
            MessageBox.confirm('确定放在这里吗?').then(()=>{
                Vue.set(this.diceData,index,this.number);
                this.updateData({pos:this.pos,index:index,data:this.number});
                this.$nextTick(()=>{
                    this.checkOver({pos:this.pos})
                    this.updateTurn()
                    this.getNum()  
                })

            })
        }
    }

}
</script>

<style lang="less" scoped>
.diceBox{
    width: 100%;
    height: 280px;
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
            width: 80px;
            height: 80px;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #999;
            font-size: 30px;
            font-weight: bold;
            border-radius: 10px;
            background-color: rgba(255,255,255,1);
            margin:5px;
            &:hover{
                box-shadow: 0 0 5px gray inset;
                transform: scale(1.1)
            }
        }
    }
}
</style>