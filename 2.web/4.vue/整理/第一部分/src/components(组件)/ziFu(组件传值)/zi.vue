<template>
    <!-- 子组件向父组件传值：[APP.vue父组件、SonComponent子组件]

        子组件传值：在子组件内部，通过自定义事件的方式，传递数据给父组件
            //1、通过defineEmits函数定义自定义事件
            const emits = defineEmits(['coustomEvent'])；// coustomEvent自定义事件名
            【类似于click】

            //2、点击按钮的时候，触发自定义事件
            const sendDataToParent = () =>{
            // 触发自定义事件 emits('自定义事件名'，传递的数据)
            emits('coustomEvent',childData.value)}


        父组件接值：在父组件中，通过函数接收子组件传递进来的值
            <template>
                <SonComponent@coustomEvent="handler"></SonComponent>
            </template>
            <script setup>
                import SonComponent from "./components/SonComponent.vue"
                //父组件接值：在父组件中，通过函数接收子组件传递进来的值
                const handler = (data)=>{
                console.log('子组件传递过来的数据是'，data)； }
            </script>
    -->



    <h3>我是子组件的标题 <button type="button"@click="zi">点击发送数据给父组件</button></h3>
</template>

<script setup>
    import { ref, defineEmits } from 'vue';
    // 子组件的数据
    const childData = ref('小黑子');

    // 子组件传值：在子组件内部，通过自定义事件的方式，传递数据给父组件
    // 1、通过defineEmits函数定义自定义事件
    const emits = defineEmits(['coustomEvent']); // coustomEvent自定义事件名 【类似于click】

    //2、点击按钮的时候，触发自定义事件
    const sendDataToParent=()=>{
        // 触发自定义事件 emits('自定义事件名'，传递的数据)
        emits('coustomEvent', childData.value)
    }
</script>

<style scoped>
</style>