<template>
    <div>
        <button  type="button">
            <slot></slot>
        </button>
    </div>
</template>

<script setup>
    import MyButton from "./components/MyButton.vue" // 相对路径
    import MyButton from "@/components/MyButton.vue" // 绝对路径
</script>

<style scoped>
    button {
    padding: 8px 40px;
    border: none;
    background: linear-gradient(to right, red, yellow);
    color: #fff;
    cursor: pointer;
    }
</style>


