<template>
  <div class="listBox">
    <mt-button icon="back"  @click='$router.replace("/index")' class="backBtn"></mt-button>
    <div class="list">
        <ul>
            <div class="header">
                <span>用户</span>
                <span>积分</span>
            </div>
            <li v-for="(item,index) in userData" :key="index">
                <img src="../assets/logo.jpg">
                <span class="title">{{item.title}}</span>
                <span class="point">{{item.point}}</span>
            </li>
        </ul>
        <div class="tip">仅展示前8名</div>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            userData:[
                {title:"FZUer1",point:"999"},
                {title:"FZUer2",point:"888"},
                {title:"FZUer3",point:"777"},
                {title:"FZUer4",point:"666"},
                {title:"FZUer5",point:"555"},
                {title:"FZUer6",point:"444"},
                {title:"FZUer7",point:"333"},
                {title:"FZUer8",point:"222"},
            ]
        }
    }
}
</script>

<style lang="less" scoepd>
.listBox{
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
    .list{
        position: relative;
        box-sizing: border-box;
        width: 75%;
        height: 85%;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba( 255, 255, 255, 0.7 );
        border: 1px solid rgba( 255, 255, 255, 0.18 );
        padding: 0px 20px;
        border-radius: 20px;
        ul{
            width:90%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            .header{
                width: 100%;
                font-size: 20px;
                color: #999;
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 20px 0pc 10px 0px;
            }
            li{
                width: 100%;
                display: flex;
                flex-direction: row;
                justify-content: space-around;
                align-items: center;
                color: #999;
                border-bottom: 1px solid #999;
                padding-bottom: 5px;
                margin: 5px 0px;

                img{
                    width: 40px;
                    height:  40px;
                    border-radius: 50%;
                    background-color: #fff;
                    margin-right:10px ;
                }
                .title{
                    flex: 1;
                }
                .point{
                    margin-right: 5px;
                }
            }
        }
        .tip{
            position: absolute;
                bottom: 10px; 
                color: #999;
                font-size: 5px;
               
        }
    }
}
</style>