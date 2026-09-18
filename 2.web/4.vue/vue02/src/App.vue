<template>
  <!-- 直接从 store 中访问 state -->
  <div >Current Count: {{ counter.count }}
    <button type="button" @click="counter.increment">点击+1</button>



    <!-- 编程式导航 router常用方法 -->
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <router-link to="/goods">商品主页面</router-link>
      <hr>
      <p>编程式导航 - push</p>
      <button type="button" @click="doRedirect('')">Home</button>
      <button type="button" @click="doRedirect('about')">About</button>
      <button type="button" @click="doRedirect('goods')">商品主页面</button>
      <p>编程式导航- replace</p>
      <button type="button" @click="doReplace('')">Home</button>
      <button type="button" @click="doReplace('about')">About</button>
      <button type="button"@click="doReplace('goods')">商品主页面</button>
      <p>编程式导航- go</p>
      <button type="button" @click="doBackward()">后退</button>
      <button type="button" @click="doForward()">前进</button>
    </nav>



    <!-- 路由传参 -->
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <!-- 方式一：params传递参数-->
      <RouterLink to="/about/1001/zhangsan">About</RouterLink>
      <!-- 方式二：query传递参数-->
      <router-link to="/goods?id=1002&username=lisi">商品主页面</router-link>
      <hr>
      <p>编程式导航- push</p>
      <button type="button" @click="doRedirect('')">Home</button>
      <button type="button" @click="doRedirect('about' ) ">About</button>
      <button type="button" @click="doRedirect('goods')">商品主页面</button>
      <p>编程式导航 - replace</p>
      <button type="button" @click="doReplace('')">Home</button>
      <button type="button"@click="doReplace('about')">About</button>
      <button type="button" @click="doReplace('goods')">商品主页面</button>
      <p>编程式导航- go</p>
      <button type="button" @click="doBackward()">后退</button>
      <button type="button"@click="doForward()">前进</button>
    </nav>
  </div>

  <hr>
  <MyCompontents></MyCompontents>
</template>



<script setup>
  // 有关store
  import{
    useCounterStore
  } from '@/stores/counter'

  import MyCompontents from "@/compontents/MyCompontents.vue"

  const counter = useCounterStore()


  // 有关route常用方法
  import {
    RouterLink, 
    RouterView, 
    useRouter
  }from 'vue-router'

  
  //导入useRouter函数：该函数的作用是为了获取得到当前路由器实例。
  const router = useRouter();

  const doRedirect = (url) => {
    router.push(`/${url}`)   // 模板字符串
  }
  const doReplace = (url) => {
    router.replace(`/${url}`)
  }

  const doBackward = () => {
    router.go(-1)
  }


  // 有关路由传参
  const doForward = () =>{
    router.go(1)
  }
</script>