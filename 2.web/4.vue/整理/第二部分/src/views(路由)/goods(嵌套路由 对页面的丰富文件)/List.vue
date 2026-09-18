<template>
    <div>
        <p>这里是商品列表页(goods/List.vue)</p>
        <ul>
            <li v-for="good in goods" :key="good.id">
            商品名：{{good.name}}、价格：{{good.price}}
            </li>
        </ul>
    </div>
</template>

<script setup>
    import { reactive } from "vue"
    const goods = [
        {id: 1, name: '火龙果', price: 3.98},
        {id: 4, name: '海南千禧', price: 5.88},
        {id: 5, name: '牛奶小吊瓜', price:1.98},
    ]
</script>

<style scoped>
</style>