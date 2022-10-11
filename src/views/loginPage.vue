<template>
  <div class="loginBox">
    <el-form label-position="top" label-width="80px" class="loginForm">
        <h1>Welcome</h1>
        <el-form-item label="账号">
            <el-input v-model="account" clearable></el-input>
        </el-form-item>
        <el-form-item label="密码">
            <el-input v-model="password" show-password></el-input>
        </el-form-item>
        <mt-button @click="loginSubmit">登录</mt-button>
    </el-form>
    <img src="../assets/login.svg">
  </div>
</template>

<script>

export default {
    data(){
        return{
            account:"",
            password:""
        }
    },
    methods:{
        loginSubmit(){
            this.$router.replace("/intro")
        }
    }
}
</script>

<style lang="less" scoped>
.loginBox{
    position: relative;
    width: 100%;
    height: 100vh; 
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(to right bottom,rgb(181, 225, 239),rgb(237, 237, 218));
    img{
        position:absolute;
        top:30px;
        left: 10px;
        width:150px;
        height:150px;
    }
}
.loginForm{
    width: 75%;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: rgba( 255, 255, 255, 0.7 );
    border: 1px solid rgba( 255, 255, 255, 0.18 );
    border-radius: 20px;
    h1{
        align-self: flex-start;
        font-size: 30px;
        font-weight: bold;
        color: #999;
        margin: 0px 0px 20px 30px;
    }
    .el-form-item{
        box-sizing: border-box;
        font-size: 15px;
        font-weight: bold;
        margin-bottom:10px;
        :deep(.el-form-item__label){
            color: #999;
            padding:0px 0px;
        }

    }
    
        .mint-button{   
        width: 80%;
        height: 40px;
        color: #aaa;
        font-weight: 600;
        background-color: #fff;
        border: 2px solid #eee;
        border-radius: 20px;
        margin: 20px 0;
            &:hover{
                transform: scale(.95)
            }
        }
    
}

</style>
