<template>
    <zi @coustomEvent="handler"></zi>
</template>
<script setup>
    import zi from"./components/ziFu/zi.vue"
    // 父组件接值：在父组件中通过函数接收子组件传递进来的值
    const handler = (data) => {
        console.log('子组件传递过来的数据是',data);
    }
</script>

<style scoped>
</style>