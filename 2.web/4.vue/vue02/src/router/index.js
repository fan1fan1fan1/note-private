import { createRouter, createWebHistory } from 'vue-router'
/* createRouter      用来创建路由器实例
   createWebHistory  路由模式  提供HTML5的History模式,使用真实的URL路径
*/
import HomeView from '../views/HomeView.vue'

// 路由器实例对象
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [ // 路由集合 内一个{}为一个路由 由集合表示
        {
            path:'/',  // 路径
            name:'home',  // 唯一标识
            component:HomeView,  // 组件 导入组件方式一 直接加载
        },{
            path:'/about',
            name:'about',
            component: ()=> import('../view/AboutView.vue'),  //  导入组件方式二 异步加载/懒加载
        },{
            // 嵌套路由配置
            path:'/goods', 
            name:'goods', 
            component: ()=> import('../views/Goods.vue'), 
            children: [
                {
                path:'add', // 子路由路径不推荐加/·->·最终路径：/goods/li
                name: 'add', 
                component:() => import('../views/goods/Add.vue' ), 
                },{
                path:'list', 
                name:'list', 
                component: () => import('../views/goods/List.vue'), 
                }
            ]
        }
    ],
})

export default router
