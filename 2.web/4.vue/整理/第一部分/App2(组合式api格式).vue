<template>
    <div>
        <!-- api风格2 组合式api -->
        <h1>演示选项式API</h1>
        <button type="button" @click="increment">count的值:ffcount}}</button>
        <p>message的值:{{message}},反转之后:{{reserveMessage}}</p>
        <p>
            姓氏：<input type="text" v-model="firstName">
        </p>
        <p>
            名字：<input type="text" v-model="lastName">
        </p>
        <p>你的姓名是:{{firstName}}{{lastName}}</p>
        <p>姓名变化的次数：{{num}}</p> 



        <!-- 组件插槽 -->
        <MyButton>登录</MyButton>
        <MyButton>注册</MyButton>
        <MyButton>删除</MyButton>

        <BaseLayout>
            <template #header>
                <h1>我是header的内容</h1>
            </template>
            <template #default>
                <p>我是main的内容1</p>
                <p>我是main的内容 2</p>
            </template>
            <template #footer>
                <h3>我是footer的内容</h3>
            </template>
        </BaseLayout>

    </div>
</template>





<script setup>
    // 引入ref函数  不引入也会自动生成  
    import { ref } from 'vue'
    import { computed, onMounted, watch } from 'vue'

    import MyButton from "./components/MyButton.vue" 
    import BaseLayout from "./components/BaseLayout.vue"
    

    // 定义组件需要的数据
    const count = ref(0)
    const message = ref('hello')
    const firstName = ref('张')
    const lastName = ref('无忌')
    const num = ref(0)


    // 定义组件需要的函数
    function increment(){
        count.value++   // this.count++
    }
    // 简写
    const increment = function(){
        count.value++
    }
    // 简写
    const increment = ()=>{
        count.value++
    }


    // 计算属性
    const reserveMessage = computed(()=>{
        return this.message.split('').reverse().join('')
    })


    // 监听器
    watch([firstName, lastName], ()=>{
        num.value++   
    })


    // 生命周期函数
    onMounted(()=>{
        console.log('vue3组件加载完毕');
    })

</script>



<style scoped>

</style>