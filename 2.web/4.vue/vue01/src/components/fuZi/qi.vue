<template>
    <!-- 父组件向子组件传值![APP.vue父组件、ChildComponent子组件]
        父组件传值：在子组件开始标签中，通过自定义属性绑定的方式，将父组件的数据传递给子组件
        子组件接值：在子组件内部，通过defineProps函数接收
        import ( defineProps } from 'vue'; // 导入defineProps函数 
    -->


    <!--父组件传值：在子组件开始标签中，通过自定义属性绑定的方式，将父组件的数据传递给子组件 -->
    <zhi :name="name" :age="age":student="student":goods="goods"></zhi>
</template>

<script setup>
    import { reactive, ref } from "vue";
    import zhi from "./components/fuZi/zhi.vue";
    //qi.vue父组件的基本类型数据
    const name = ref('张三')
    const age = ref(18)
    // qi.vue父组件的引用类型数据
    const student = reactive({
        id: 1001, 
        name:'小黑',
        age: 13, 
        classes:'初一1班'
    })
    const goods = reactive(['香蕉','苹果','西红柿','火龙果'])
</script>

<style scoped>
</style>