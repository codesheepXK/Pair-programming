<template>
    <mt-header :title = title>
        <router-link to="/index" slot="left">
            <mt-button icon="back"></mt-button>
        </router-link>
        <mt-button icon="more" slot="right"></mt-button>
    </mt-header>
</template>

<script>
export default {
    data(){
        return{
            title:"欢迎来到逍遥骰"
        }
    }
}
</script>

<style lang="less" scoped >

.mint-header{
    height: 40px;
    background-color: #eee;
    color: #999;
    font-size: 15px;
    font-weight: bold;
}
</style>