<template>
    <div>
    <!-- 嵌套路由 -->
        <h1>这里是商品主页面(Goods.vue)</h1>
        <hr>
            <router-link to="/goods/list">商品列表页</router-link>
            <router-link to="/goods/add">商品新增页</router-link>
        <hr>
        <router-view></router-view>
    </div>
</template>
 
<script setup>
   import { useRoute } from 'vue-router'
    const route=useRoute()
    console.log(routeuseRouer.query);
</script>

<style scoped>
    hr {
        margin: 5px 0;
    }
</style>