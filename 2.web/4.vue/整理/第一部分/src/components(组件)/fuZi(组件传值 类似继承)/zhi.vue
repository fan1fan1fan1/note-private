<template>
    <h3>子组件</h3>
    <p>父组件传递进来的name和age:{{name}}-{{age}}</p>
    <p>父组件传递进来的student:{{student.name}}-{{student.classes}}</p>
    <p>父组件传递进来的goods:
        <ul>
            <li v-for="good of goods">{{good}}</li>
        </ul>
    </p>
</template>

<script setup>
    // 子组件接值：在子组件内部，通过defineProps函数接收
    import { defineProps } from 'vue';
    // 导入defineProps函数
    // 调用defineProps函数接收
    const props = defineProps({
        name: String, 
        age: Number, 
        stu: Object, 
        goods: Array
    })
</script>

<style>
</style>