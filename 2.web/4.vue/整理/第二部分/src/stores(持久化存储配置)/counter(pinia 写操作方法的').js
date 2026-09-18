import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)  // 全局共享数据

  // 操作共享数据的方法
  function increment() {
    count.value++
  }

  return { count, increment }
},{
  persist:true,
})