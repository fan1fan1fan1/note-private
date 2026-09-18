<!-- vue -->
    <!-- vue用于构建用户界面的渐进式js框架   
        构建用户界面: 把得到的数据变成人话给客户
        vue特点:  1.组件化模式 提高复用 便于修改
                    把js中每一块定义为一个.vue文件 其中写html、css、js交互
                2.使用声明式编码
                    声明式编码: 技术细节黑盒 不直接接触dom、事件
                    命令式编码: 技术细节手写 手搓
                    类似面向对象和面向过程
                3.虚拟DOM + Diff算法
                    通过diff只判断修改后与原来的变化 不会重构页面 提高页面的制作效率 防止出现页面崩塌
    -->



<!-- 想完成数据赋值 -->
    <!-- 命令式编码 
    <ul id="list"></ul>
    <script>
        const persons = [   // 数据
            { id: 1001, name: "zhan", age: 18 },
            { id: 1002, name: "li", age: 19 },
            { id: 1003, name: "wang", age: 20 }
        ]

        // 1.定义html字符串
        let htmlStr = ''

        // 2.遍历数据拼接html字符串
        presons.forEach(p => {
            htmlStr += <li>${p.id} - ${p.name} - ${p.age}</li>
        });

        // 3.获取list元素
        let list = document.getElementById('list')

        // 4.修改内容
        list.innerHTML = htmlStr


        // 或者
        // 创建数组，用来保存学生数据
        var stuArray = [
            {id:1001, name:'张三', age: 12},
            {id:1002, name:'李四', age: 13},
            {id:1003, name:'王五', age: 14}
        ]
        var stu = document.getElementById('stuList');
        
        // 根据数据动态创建Li：一条数据对应一个Li
        for(var stu of stuArray){
            var newLi = document.createElement('li');
            newLi.innerText = stu.id +"-" stu.name + "-" + stu.age;
            stuList.appendChild(newLi);
        }
    </script>
    -->

    <!-- 声明式编码 
    <ul id="list">
        <li v-for="p in persons">
            {{p.id}} - {{p.name}} - {{p.age}}
        </li>
    </ul>
    -->



<!-- MVC和MVVM架构 -->
    <!-- MVC: mode + view + controller  
            类似命令式编码

            html + css = view
            js => mode  或  js => controller

            当我们点击搜索按钮，把输入框里面输入的数据发送给服务器，查询数据
            1、搜索按钮的鼠标单击事件，执行某个行为 ->【Controller】
            2、通过Ajax和服务器进行数据交互 -> 【Model】

            用户通过model交互发出数据 view展示数据结果(视图页面) 更新页面 发出指令  
                            model -> view -> controller -> model
                            
        MVVM:  通过MVC演变来 MVC的升级版
            C->VM  mode + view + viewmodel 实现model和view的自动更新   
            类似声明式编码
            双向数据绑定  view -> viewmodel <-> model
            双向数据绑定依据Listeners和Data Bindings实现
    -->



<!-- 安装Node.js 
    Node.js可以使js脱离浏览器运行 -> javaScript运行环境

    nvm off                 //禁用node.js版本管理（不卸载任何东西）
    nvm on                  //启用node.js版本管理
    nvm install <version>   //安装node.js的命名 version是版本号 例如：nvm install 8.12.0
    nvm uninstall <version> //卸载node.js是的命令，卸载指定版本的nodejs，当安装失败时卸载使用
    nvm ls                  //显示所有安装的node.js版本
    nvm list available      //显示可以安装的所有node.js的版本
    nvm use <version>       //切换到使用指定的nodejs版本
    nvm v                   //显示nvm版本
    nvm install stable      //安装最新稳定版
    nvm install latest      //安装最新版本
-->



<!-- vue使用 
    方式一 多页面应用 多个.html 引入vue.js
    方式二 单页面应用 单个.html 多个组件
-->



<!-- 执行vue -->
<!--1.创建项目命令
        npm create vue@latest
        Ok to proceed? (y) : 是否继续 输入y
        输入项目名称
        选择包含的功能  Router(单页面)   Prettier(代码格式化)

    2.cd 项目名
        
    3.安装依赖的命令   -> 产生node-modules
        npm install
        
    4.启动项目命令
        npm run dev

    5.可访问成功页面
         http://localhost:5173

    5.项目清理  删除不需要的代码
        1.删除 src/assets下的 base.css  main.css

        2.删除 src/components 目录下：所有文件

        3.删除 src/router/index.js 中部分代码：routes数组中的配置、导入HomeView.vue的代码
            剩下:
            import { createRouter, createwebHistory } from 'vue-router'
            const router = createRouter({
                history: createwebHistory(import.meta.env.BASE_URL), 
                routes: [
                ],
            })
            export default router

        4.删除 src/views 目录下：AboutView.vue、HomeView.vue

        5.格式化(全删) src/App.vue 文件的代码，只保留script、template、style标签
        <template>
            <div>

            </div>
        </template>
        <script>
            export default {

            }
        </script>

        <style scoped>

        </style>

        6.删除src/main.js中，用来引入main.css的代码
-->



<!-- Vue里面组件的分类：
    公共组件：多个页面可以重复使用的组件。比如一个按钮组件。，【定义在components目录】
    页面组件：一个组件代表一个页面。比如登录组件、注册主键。【定义在views目录】 
-->


<!-- 现在产生了vue文件
    1.public 
        favicon.ico 快捷图标 可替换

    2.src 存放自带生成的静态资源 ~重要
        (1) assert 
                logo.svg 图片 可替换
        (2) components 公共组件(多个页面可以重复使用)
        (3) router 存放路由配置文件
                index.js 路由规则
        (4) views 页面组件
        (5) App.vue 根组件 整个应用的入口组件 打开页面显示的组件
        (6) main.js 应用的入口文件 负责创建vue实例并挂载到dom上 

    3.index.html 页面

    4.package.json 项目的依赖、脚本、其他元数据

    5.vite.config.js 配置 vite 的各种选项，包括开发服务器、构建设置、插件等
-->



<!-- vue各部分文件介绍
    1.main.js       
    2.App.vue    一个页面三部分构成: 结构、表现、行为 
-->



<!-- 模板语法 -->
<!--1.data函数
    定义组件的数据 会被vue进行响应式处理
        响应式处理: 数据改变会影响网页
        数据: (任何js类型) Number、String、Boolean、Null、Unidefined、Object(数组、自定义对象、内置对象)
    


    2.数据绑定
    插值表示法{{}}、v-html、v-text -> 都属于单向绑定
    单向绑定: 数据对象上的值改变时，对应渲染的内容变化 反过来不变

    v-text会直接输出输入的全部内容  v-html会进行前端格式解析
    


    3.属性绑定
    把data的数据插入到标签的属性中
    v-bind:  简写:

    

    4.事件绑定
    v-on    简写@
    v-on:事件名="方法名"
    方法要写在vue配置的methods属性中

    js事件类型和事件对象:
        鼠标事件: click、mouseover、mouseout、mousedown、mouseup
        表单事件: change、focus、blue、input、submit、reset
        事件对象: 事件发生时 浏览器创建的对象 会传递给事件函数
        


    5.事件增强
    $event对象   表示当前触发者对象
    如果调用事件函数的时候，没有传递参数，那么形参就代表事件对象。
    如果调用事件函数的时候，传递了参数，那么形参就代表传递进来的值。
    如果调用事件函数的时候，传递了参数，那么额外传递一个$event，就表示事件对象
    


    6.事件修饰符
    在事件处理程序中调用 event.preventDefault()或event.stoppropaaation()是非常常见的需求。尽管我们可以在方法中轻松实现这点，但更好的方式是；
    方法只有纯粹的数据逻辑，而不是去处理DOM事件细节。

    事件流：事件冒泡和事件捕获
    e.stopPropagation()阻止事件的传播行为
    e.preventDefault() 阻止浏览器的默认行为

    为了解决这个问题，Vue.is为v-on 提供了事件修饰符。
    .stop
    ·prevent
    .capture
    .self

    <a v-on:click.stop="doThis"></a>                阻止单击事件继续传播
    <form v-on:submit.prevent="onSubmit"></form>    提交事件不再重载页面
    <a v-on:click.stop.prevent="doThat"></a>        修饰符可以串联
    <form v-on:submit.prevent></form>               只有修饰符
    <div v-on:click.capture="doThis">...</div>      添加事件监听器时使用事件捕获模式
            即内部元素触发的事件先在此处理，然后才交由内部元素进行处理
    <div v-on:click.self="doThat">...</div>         只当在 event.target 是当前元素自身时触发处理函数
            即事件不是从内部元素触发的
    


    7.表单输入绑定
    【重点】你可以用v-mode1 指令在表单<input>、<textarea>及<select>元素上创建双问数据绑定。
    单行文本：v-model绑定是字符串类型的数据
    单行文本：文本输入框(text)、密码框(password)、邮箱输入框(email)、数值框(number)、电话号码框(tel)、搜索框(search)
    多行文本：v-mode1绑定是字符串类型的数据

    需求：实现双向数据绑定
    当用户修改model数据时，贡面dom发生变化；
    当用户修改页面dom时，model数据发生变化；
    你可以用v-model 指令在表单<input>、<textarea>、<select>元素上创建双向数据绑定。
        <input>  单行文本 复选框 单选按钮   
        <textarea>  多行文本
        <select> 选择框       
            
    双向数据绑定: 赋了同样值，一起改变，本质上是同一个地址，本质上是同一个东西
-->



<!-- 计算和监听属性 -->
<!-- 计算属性
    计算属性：计算得出来一个属性，这个属性会成为data的数据。
    计算属性定义computed中
    快捷键：vcomputed

    模板template部分可以写计算 单过多计算会导致模板过重 我们可以使用计算属性
        插值表达式: 用于插值和简单运算
        复杂逻辑使用计算属性 计算属性可以缓存


    侦听器 用于监听
    侦听器主要用来侦听data中的数据的变化的，一旦侦听到数据的变化，就会触发侦听器中所定义的同名的方法，
    一般用在当数据变化的时候需要执行异步或者比较消耗资源的操作的时候。
    侦听器函数要写到watch中
-->



<!-- 条件渲染 -->
<!-- v-if 
     v-else-if
     v-else
    
     v-show 只有两个选项 适合多次修改
-->



<!-- 列表渲染 -->
<!-- v-for 遍历
    需要 item in items

    key
    在遍历的过程中，给每项元素设置一个唯一的key值，有助于提高vue的性能，对我们开发以及显示不会有任何影响。
    当然如果不设置key值也可以，但是性能会略慢，所以推荐设置key值。
    v-for="item in items" v-bind:key="item.id">

    建议尽可能在使用 v-for 时提供 key attribute，除非遍历输出的 DOM 内容非常简单，或者是刻意依赖默认行为
    以获取性能上的提升。
    因为它是Vue 识别节点的一个通用机制，key 并不仅与 v-for 特别关联。后面我们将在指南中看到，它还具有其它用途。
    不要使用对象或数组之类的非基本类型值作为 v-for的key。请用字符串或数值类型的值。
 -->



<!-- api风格 -->
<!-- Vue 的组件可以按两种不同的风格书写：选项式 API 和 组合式 API。
    Vue2：选项式API
    Vue3：组合式API
    无论是那种API，影响的只是script标签里面的写法；template和style里面不变。 

    选项式API 我们可以用包含多个选项的对象来描述组件的逻辑，
              例如 data、methods 和 mounted。选项所定义的属性都会暴露在函数内部,它会指向当前的组件实例。
        data函数：组件需要的数据
        methods：组件需要的函数
        computed：计算属性
        watch: 监听器
        mounted：生命周期函数，页面挂载完毕执行      
    
    组合式API 我们可以使用导入的API函数来描述组件逻辑。在单文件组件中，<script setup>使用。
        这个 setup attribute是一个标识，告诉Vue需要在编译时进行一些处理，让我们可以更简洁地使用组合式API。
        比如，<script setup> 中的导入和顶层变量/函数都能够在模板中直接使用。

        1、组合式 API 通常会与‘<script setup> 搭配使用。
        2、通过组合式 API，我们可以使用导入的API函数来描述组件逻辑。
        定义组件需要的数据：引入ref函数
        定义组件需要的函数：直接定义函数即可
        定义计算属性：引入computed函数
        定义监听器：引入watch函数
        定义生命周期函数：引入对应的生命周期函数
-->



<!-- 响应式基础 
    <script setup>中的顶层的导入、声明的变量和函数可在同一组件的模板(template)中直接使用。
    顶层的导入：import { computed, onMounted, ref, watch } from "vue";
    声明的变量：const count = ref(0)；
    声明的函数：const increment = ()=> {count.value++}
    setup是组合API表演的舞台

    ref()：用来声明响应式状态[数据发生改变，view随之改变]
    语法：const 变量名=ref(initValue)
    接收的数据可以是：基本类型、也可以是引用类型。[ref一般用来接收基本类型]
    基本类型数据：Number、String、Boolean、Null、Unidefined
    对象类型：Object、数组
    JS获取值：变量名.value
    模板中获取值：{{变量名}}

    除了ref  响应式还可使用reactive()
    作用：定义一个对象类型的响应式数据（基本类型不要用它，要用ref 函数）
    语法：const 代理对象= reactive（源对象）接收一个对象（或数组），
         返回一个代理对象(Proxy的实例对象，简称proxy对象)
    reactive定义的响应式数据是“深层次的”。
    内部基于 ES6 的Proxy实现，通过代理对象操作源对象内部数据进行操作。

    ref() reactiv()使用区别:  基本数据类型用ref  引用数据类型用reactive
-->



<!-- 组件 -->
<!-- 基础组件(公共组件) + 页面组件(容器组件)
    基础组件/公共组件：多个页面可以复用的组件，一般定义在`src/components`
    页面组件/容器组件：用于构建某个页面或页面的某个部分，一般定义在`src/views`

    自定义组件
        步骤一：定义
            components中新建.vue文件，填充三部分代码：template、script、style。
            组件名：采用驼峰原则，首字母大写，之后的每个单词首字母都大写。
        步骤二：导入组件
            import 组件名 from组件的地址'；
            个人建议：import后面的组件名和组件文件的名字保持一致。
        步骤三：使用组件
            把组件当成自定义标签使用即可

    组件通信
        1.父->子
        2.子->父

    组件插槽
        组件应用：
            1、定义一个Mybutton组件，在组件内部定义结构和样式；
                组件结构：<button type="button">按钮</button>
                组件样式：button {
                            padding: 8px 15px;
                            border: none;
                            background: linear-gradient(to right, red, yellow);
                            color:#fff；
                        }
            2、导入组件
            3、使用组件

            需求：在使用组件的时候，自定义按钮的文本内容。
            1、在button标签中定义slot标签，slot就是插槽，表示占位符。
            2、在使用组件的时候，传入文本内容
    
    具名插槽
        插槽太多了 起名字
        1、给slot标签添加name属性
        2、每份内容都需要定义一个template标签，并且给标签添加#插槽名
-->



<!-- 第三方UI组件库 -->
<!-- Element UI 
    • vue2：ElementUI，官网地址：https://element.eleme.cn/#/zh-CN
    • vue3：Element-plus，官网地址：https://cn.element-plus.org/zh-CN/

    安装 npm install element-plus --save

    在main.js中配置
        import { createApp } from 'vue'
        import ElementPlus from 'element-plus'   √
        import 'element-plus/dist/index.css'     √
        import App from './App.vue'
        const app = createApp(App)
        app.use(ElementPlus)                     √
        app.mount('#app')

    1、从官网找到对应的组件，Ctrl+c，粘贴到我们项目的组件中
    2、对于复杂的组件，需要查看文档

-->



<!-- ui网站中 表单Form -->



<!-- 生命周期函数 mount -->

<!-- ------------------------------------------------------------------------------------------- -->


<!-- 进入第二部分 -->
<!-- Axios -->
<!-- 网络请求库 向服务器发送请求
    1.安装
            npm install axios
    2.导入
            import axios from 'axios'
    3.cv
            axios-http.cn/


    (一) GET请求 key-value形式发送数据
            axios.get('')
            <form action="地址" method="get/post">   

            方式一 URL拼接参数
            axios.get ('/user?id=12345')
                .then(function (response)
                    // 处理成功情况
                    console. log(response)；
                }）
                .catch(function (error)
                    // 处理错误情况
                    console.log(error)；
                }）
                .finally(function () {
                    // 总是会执行
                )；

            解释：
            /user       服务器处理请求的地址
            id=1001     Get请求携带的数据
            then()      请求成功的处理函数
            catch()     请求失败的处理函数 
            finally()   总会执行   
            response    服务器响应对象 数据载体

            方式二 通过params配置定义参数
            axios.get('/user',{
                params:{
                    ID：1001
                }
            }).then(function(response){
                console.log(response);
            }).catch(function (error) {
                console.log(error);
            }).finally(function (){ 
                //总是会执行
            })

    (二) POST请求
            方式一 data携带参数 发送的json格式数据
                axios.post('/user', 
                    firstName: 'Fred', 
                    lastName: 'Flintstone'
                }).then(function (response) {
                    console.log(response);
                ).catch(function (error) 
                    console.log(error);
                })；

            方式二 URLSearchParams传递参数 发送key-value      (不怎么使用)
                let params = new URLearchParams();
                params.append("firstName", 'Fred');
                params .append("lastName", 'Flintstone');
                axios.post('/user', params).then(function (response) {
                    console.log(response) ;
                })

    (三)axois其他请求
            delete请求 和get请求用法相同
            put请求 和post请求用法相同
-->



<!-- 应用案例：
    1、引入Element-plus: npm install element-plus --save
    2、在main.js 中配置：
        import ElementPlus from 'element-plus!
        import 'element-plus/dist/index.css'
        import zhCn from 'element-plus/es/locale/lang/zh-cn'// 引入中文语言包
        app.use(ElementPlus,
        ( locale: zhCn })//使用中文语言包
    3、获取列表数据
        查询小区数据，接口地址：http://43.143.190.87:8091/panchudaojiaBackend/community/communityIist
        服务器响应的数据：
            list：当前页的数据
            pageNum：页码
            pageSize:每页显示的条目数
            total：总数据量
    4、数据渲染
        想要在tamplate动态渲染的数据，必须成为组件的数据。
        ref/reactive就是用来定义组件的数据。 
-->



<!-- Pinia状态管理 -->
<!-- 状态管理库
    作用: 集中管理跨组件共享的数据（如用户登录状态、主题配置）。
          解耦组件与数据逻辑，避免"prop drilling”（深层传递props）。

    使用场景： 用户认证状态    登录用户信息、权限令牌
              全局UI状态      主题、语言、侧边栏折叠状态
              跨组件数据共享  购物车商品、表单多步骤数据
              服务端数据缓存  API返回的数据避免重复请求


    1.安装
            npm install pinia

    2.在Vue中注册
        在main.js中:
            import { createApp } from 'vue';
            import { createPinia } from 'pinia';
            import App from './App.vue';
            const app = createApp(App);
            const pinia = createPinia();
            app.use(pinia);
            app.mount('#app');

    3.导入
            import axios from 'axios'

    4.cv
            pinia.vuejs.org/zh/

        创建Store   
        Store（如 Pinia）是一个保存状态和业务逻辑的实体，它并不与你的组件树绑定。换句话说，它承载着全局状态。
            在stores/counter. js中:
                import { ref } from 'vue'
                import { defineStore } from 'pinia'
                export const useCounterStore = defineStore('counter',()=> {
                    const count = ref(0)
                    function increment() {
                        count.value++
                    }
                    return { count, increment }
                })
-->



<!-- 持久化存储
        1.安装
                npm install pinia-plugin-persistedstate

        2.main.js中注册
                import piniaPersist from 'pinia-plugin-persitedstate'
                pinia.use(piniaPersist);   // 持久化插件

        2.在Store 中配置持久化：然后，在创建store时，使用 persist 配置来启用持久化存储。
                import { ref } from 'vue'
                import { defineStore } from 'pinia'

                export const useCounterStore = defineStore('counter', ()=>{
                    const count = ref(0)
                    function increment() {
                        count.value++
                    }
                    return { count, increment } 
                },{
                    persist: true, 
                }   
-->



<!-- 路由 -->
<!-- 路由其实是一种映射关系，类似于key=>value的键值对的关系，其中key表示请求的路径path。
    • 路由是根据不同的url地址展示不同的内容或页面。
    • 路由分为前端路由和后端路由。
        前端路由：前端路由的value表示组件，一个path映射一个组件；
                /login -> Login.vue
                /home -> Home.vue
        后端路由：后端路由的value表示处理请求的回调函数，针对不同请求的path，处理不同的业务逻辑；
                地址 发送请求

    组件和路由
        组件是对特定功能代码(html、css、js)的封装，通过组件的名字可以重复利用该组件中的代码。
        路由就是url地址和对应的资源（组件）的映射，通过一个路径的url地址，可以唯一找到一个资源。
        区分路由组件和非路由组件的最大区别在于：组件有没有被注册为路由! 
-->



<!-- Vue Router 路由器
        Vue Router是Vue.js官方的路由管理器。它和Vue.is的核心深度集成，让构建单页面应用变得易如反掌。
        Vue Router的三个基本概念：
            route：首先它是个单数，译为路由，即我们可以理解为单个路由或者某一个路由,就是一个键值对映射.
            routes：它是个复数，表示多个的集合才能为复数；即我们可以理解为多个路由的集合,就是一堆键值对.
            router：译为路由器，上面都是路由，这个是路由器，我们可以理解为一个容器包含上述两个或者说它
                    是一个管理者，负责管理上述两个；

        举个常见的例子:  当用户在页面上点击按钮的时候，这个时候router就会去routes中去查找route，
                        就是说路由器会去路由集合中找对应的路由。
    
    在src router index.js中写路由内容

    路由链接
        <router-lirk> 是路由中提供的标签，默认会被渲染为a标签，to属性默认被渲染为href属性。
        请注意，我们没有使用常规的a标签，而是使用一个自定义组件 router-link 来创建链接。
        这使得 Vue Router 可以在不重新加载页面的情况下更改URL，处理URL的生成以及编码。
        <router-link to="/">Home</router-link> 
        <router-link to="/about">About</router-link> 

    路由出口
        <router-view>标签，渲染某个路由路径对应的组件，称为路由出口。
        router-view 将显示与url对应的组件。你可以把它放在任何地方，以适应你的布局。
        <!--将来通过路由规则匹配到的组件，将会被渲染到 router-view 所在的位置
        router-view 或者 RouterView
    
    路由的基本使用
        1、创建路由组件：在src/views目录下面创建vue文件即可：
            组件名：首字母大写，多个单词组成，则每个单词的首字母都大写。
        2、配置路由：在src/router/index.is中配置路由规则；
            path:''，//路由地址
            name：'，//路由的唯一标识
            component:()=> import('组件地址')//路由对应的组件
        3、添加路由链接
            <router-linkl to="/goods">
-->



<!-- 嵌套路由   嵌套组件的命名：
    方式一：
        都定义在src/views文件夹下面
        Goods.vue
        GoodsList.vue
        GoodsAdd.vue
    方式二：通过文件夹区分
        Goods.vue
        goods文件夹：
        List.vue
        Add.vue
    
    创建嵌套路由组件：采用方式二
    1.在 src/views/goods 下面创建路由组件(List.vue/Add.vue)。

    2.配置嵌套路由规则
        通过配置路由的children属性完成嵌套路由的配置。
        children: [
            {
                path:'list'，// 子路由路径不推荐加/ -> 最终路径：/goods/list
                name: 'list',
                component: ()=> import('../views/goods/List.vue')，
            },{
                path: 'add', 
                name: 'add', 
                component: () => import ('../views/goods/Add.vue'), 
            }
        ]
        
    3.添加路由链接和路由出口
-->



<!-- 编程式导航 -->
<!-- 类似a href   链接跳转

    Vue路由导航两种方式：  
    • 标签导航：标签导航 <router-1ink><router-link> 是通过转义为 <a></a> 标签进行跳转；
    • 编程式导航：我们可以通过 router对象 实现编程式导航，当然也可以实现参数传递。


    router路由去对象 控制路由跳转
        1.导入方式
        在需要的组件中，导入useRouter函数，通过该函数可以获取当前路由器实例：

            //导入useRouter函数：用于在组件中获取当前路由器实例
            import [ useRouter } from 'vue-router'
            const router = useRouter();


        2.常用方法
        (1)push方法
            router.push(path)：相当于点击路由链接；
            
            这个方法会向history 栈添加一个新的记录，所以，当用户点击浏览器后退按钮时，则回到之前的URL。
            当你点击 <router-1ink>时，这个方法会在内部调用，所以说，点击 <router-link:to="...">等同于调用router.push(...)。
            该方法的参数可以是一个字符串路径，或者一个描述地址的对象。例如：
            
                router.push('/home')                                     //字符串：跳转到指定路径

                router.push({ path: '/home' })                           //对象：跳转到指定路径

                router.push({ path:'/register', query:{ plan:'private'}) //对象：跳转到指定路径（查询参数），并传递参数
                //查询参数方式 ->/register?plan=private

                router.push({ name: 'user', params: { id: 123 } })       //对象：跳转到指定路径（命名路由），并传递参数 
                //命名路由方式-> /user/123

            注意：如果提供了 path，params 会被忽略，上述例子中的query并不属于这种情况。

        (2)replace方法
          $router.replace(path)：用新路由替换当前路由(不可以返回到当前路由界面)。
            跟router.push 很像，唯一的不同就是，它不会向 history 添加新记录，而是跟它的方法名一样——替换掉当前的 history记录。

        (3)go方法
            this.$router.go(n)：这个方法的参数是一个整数，意思是在history记录中向前或者后退多少步，类似window.history.go(n)。             
-->



<!-- 路由传参 -->
<!-- route对象 获取当前激活的路由信息(路径,参数,查询)
    1.导入 在需要的组件中华 导入useRouter函数
            import { useRoute } from "vue-router";
            const route = useRoute();


    2.常用api   
        1.params
            参数设置：通过路由路径传参。 传参成为了资源路径
            参数获取：route.params 一个key/value对象，包含了动态片段和全匹配片段，如果没有路由参数，就是一个空对象。
            对于路径/login/:username/:password >/1ogin/jerry/456，则有 route.params.username == jerry 和 route.params.password == 456
            
            完整语法：router.push(hame:'usep', params: ( id: 1001, username: zhangsan } })
            简洁语法：router.push('/user/1001/zhangsan')  
                        此处  /user为固定参数  /1001/zhangsan为动态参数
                            使用方法一       使用方法二
        2.query
            参数设置：通过?拼接路由路径中。
            参数获取：route.query 一个key/value对象，表示URL查询参数，如果没有查询参数，则是个空对象。
            对于路径/register?username=tom&password=123，则有route.query.username == tom 和 route.query.password == 123
            
            完整语法：router.push({ path:'/register'，query: ( plan: 'private' })
            简洁语法：router.push('/register?plan=private')

        协议://ip地址: 端口号/资源路径?查询字符串

    3.路由跳转并传递参数
        方式一：
            params传递参数
            完整语法：router.push(( name: 'user', params:id: 1001, username: zhangsan } })
            简洁语法：router.push('/user/1001/zhangsan') 【要求：定义的路由路径必须包含后面两部分】
            接收参数：通过route对象的params属性接收
        方式二：query传递参数
            完整语法：router.push(( path:'/user', query: ( id: 1001, username: zhangsan })
            简洁语法：router.push('/user?id=1001&username=zhangsan')
            接收参数：通过route对象的query属性接收
        
        route对象 表示单个路由对象,获取当前激活的路由信息(路径,参数,查询)
        导入方式：useRoute 函数：用于获取当前的路由信息。
                通过 useRoute，你可以在组件中获取当前路由的参数、查询字符串、路径等信息

        在Vue Router中，router和route 是两个核心但作用完全不同的对象，它们的区别可以用一句话概括：

    router 控制路由跳转 （如 push/go/replace） import { useRouter } from 'vue-router'
    route  获取当前路由信息（路径/参数/查询等）  import { useRoute } from 'vue-router'
-->



<!-- 重定向和别名 -->
<!-- 重定向
        访问路径A,重新定向到路径B
     别名
        重定向是指当用户访问/home时，URL会被替换，然后匹配成7。那么什么是别名呢?
        将/别名为/home，意味着当用户访问/home时，URL仍然是/home，但会被匹配为用户正在访问7。
        上面对应的路由配置为：
        const routes = [{ path:
        component: Homepage, alias: '/home'}]
        通过别名，你可以自由地将UI结构映射到一个任意的URL，而不受配置的嵌套结构的限制。
-->