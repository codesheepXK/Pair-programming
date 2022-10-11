<template>
  <div class="introBox">
    <mt-button icon="back"  @click='$router.replace("/login")' class="backBtn"></mt-button>
    <div class="introText">
        <h1>游戏规则介绍</h1>
        <p>1.玩家AB轮流掷骰,选择己方九宫格一线摆放骰子</p>
        <p>2.在己方某线置放骰后,对方该线同点数骰将被消除</p>
        <p>3.当某一方的九宫格满时,游戏结束,进入结算</p>
        <p>4.线得分=Σ (各点数×此点数在此线出现次数的平方)</p>
        <p>5.玩家总得分=Σ(己区各线得分),总得分高者获胜</p>
    </div>
    <mt-button @click='$router.replace("/index")' class="btn">选取游戏模式</mt-button>
    
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.introBox{
    position: relative;
    width: 100%;
    height: 100vh; 
    display: flex;
    justify-content: center;
    align-items: flex-start;
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
    .introText{
        box-sizing: border-box;
        width: 75%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: rgba( 255, 255, 255, 0.7 );
        border: 1px solid rgba( 255, 255, 255, 0.18 );
        padding: 0px 20px;
        border-radius: 20px;
        margin-top:80px;
        h1{
            color: #666;
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        p{
            color: #999;
            font-size: 20px;
            margin: 5px 0px;
        }
    }
    .btn{
        position: absolute;
        bottom: 100px;
        width: 200px;
        color: #aaa;
        font-weight: 600;
        background-color: #fff;
        border: 2px solid #eee;
        border-radius: 20px;
    }
}
</style>