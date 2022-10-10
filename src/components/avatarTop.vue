<template>
  <div class="avatarBox">
    <img src="../assets/logo.jpg">
    <span>十亿少女的梦</span>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.avatarBox{
    width: 180px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    img{
        width: 45px;
        height: 45px;
        border-radius: 50%;
    }
    span{
        font-size: 18px;
        font-weight: bold;
        color: #fff;
        margin-left: 20px;
    }
}
</style>