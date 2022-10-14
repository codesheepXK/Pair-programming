<template>
  <div class="avatarBox">
    <span>次子</span>
    <img src="../assets/avatar2.jpg">
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.avatarBox{
    width: 120px;
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
        margin-right: 20px;
    }
}
</style>
