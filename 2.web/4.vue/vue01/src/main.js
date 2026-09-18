import { createApp } from 'vue'   // 从vue依赖中导入crateApp函数
import App from './App.vue'  //导入App.vue组件
import router from './router'  //导入路由规则 router/index.js

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'



const app = createApp(App)  // 创建vue项目的应用实例对象，将App.vue组件作为根组件

app.use(router)  //将Vue Router实例挂载到Vue应用上，以便处理路由相关的请求。

app.use(ElementPlus)

app.mount('#app')  //应用实例必须在调用了.mount()方法后才会渲染出来。该方法接收一个“容器”参数，可以是一个实际的 DOM 元素或是一个 CSS 选择器字符串


