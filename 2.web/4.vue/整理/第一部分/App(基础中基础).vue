<!-- vbase -->
<!-- 组件的模板结构 -->
<template>
    <div>
        <!-- 插值表示法的实现 -->
        {{ message }}
        <p>{{ message }}</p>



        <!-- v-html -->
        <div v-html="name"></div>



        <!-- v-bind -->
        <h1>属性绑定</h1>
        <a href="linkUrl" target="_blank">百度一下</a>
        <img v-bind:src="imgUrl" alt="这是一张图片">
        <img :src="imgUrl" alt="这是一张图片">



        <!-- v-on -->
        <h1 v-on:click="toUpper">{{ name }}</h1>
        <h1 @:click="addAge">{{ age }}</h1>



        <!-- 事件增强 -->
        <!-- 点击按钮获取标签内容并弹出 -->
        <!-- 1.没有参数 绑定的时候有没有()都可以 -->
        <button @click="test1">test1</button>
        <!-- 2.如果有参数 就需要() -->
        <button @click="test2('abc')">test2</button>
        <button @click="test3('a','b', $event)">test3</button>



        <!-- 事件流 -->
        <!-- 阻止 可以在函数内写e.stopPropagation() 或者在此处属性写stop prevent -->
        <div class="outer" @click="f1">
            <div class="middle" @click.prevent="f2">
                <div class="inner" @click.stop="f3"></div>
            </div>
        </div>



        <!-- 表单输入绑定 v-model -->
        <!-- 1.单行文本 -->
        <!-- 单行文本绑定字符串 -->
        用户名: <input type="text" v-model="username">

        <!-- v-bind是单向绑定：data数据发生改变,页面内容随之改变；但是页面内容改变，不会影响data数据-->
        <p>单向数据绑定：<input type="text" v-bind:value="username" /><br/></p>

        <!-- v-model是双向绑定：data数据发生改变，页面内容随之改变；页面内容改变，data数据也会改变-->
        <p>双向数据绑定：<input type="text"v-model="username" /></p>

        <p>username的值: {{username}}</p>


        <!-- 2.多行文本 -->
        <!-- 多行文本绑定字符串 -->
        <span>多行义本性的内容定：</span>
        <p> style="white-space: pre-line;">{{ multilineMsg }}</p>
        <br>
        <textarea v-mode1="multilineMsg" placeholder="请输入多行文本框内容"
            style="width: 300px; height:120px; resize:none;">
        </textarea>


        <!-- 3.复选框 -->
        <!-- 单个复选框 v-model要绑定布尔类型的值 -->
        <!-- 多个复选框 v-model要绑定数组类型数据 -->
        <input type="checkbox" id="checkbox" v-model="checked">
        <label for="checkbox">{{ checked }}</label>


        <!-- 4.单选按钮 -->
        <input type="radio" id="one" value="One" v-model="picked">
        <label for="one">0ne</label>
        <br>
        <input type="radio" id="two" value="Two" v-model="picked">
        <label for="two">Two</label>
        <br>
        <span>picked:{{ picked }}</span>


        <!-- 双向数据绑定 -->
        <p>
            单选框:
                <label>
                    <input type="radio" name="sex" value="男" v-model="sex">男
                </label>
                <label>
                    <input type="radio" name="sex" value="女" v-model="sex">女
                </label>
        </p>


        <!-- 5.选择框 下拉框 -->
        <!-- 只能选一个 v-model绑定字符串 -->
        <!-- 多个选择框 v-model绑定数组 -->
        <p>
            学历:
                <!-- 单 字符串 -->
                <select name="edu" v-model="edu">
                    <option value="" disabled>请选择</option>
                    <option value="高中">高中</option>
                    <option value="大专">大专</option>
                    <option value="本科">本科</option>
                </select>
        </p>

        <p>
            课程:
                <!-- 多 数组 -->
                <select name="course" v-model="course" multiple>
                    <option value="" disabled>请选择</option>
                    <option value="语文">语文</option>
                    <option value="数学">数学</option>
                    <option value="英语">英语</option>
                </select>
        </p>



        <!-- 计算属性 -->
        <!-- 想反转message join转为字符串 直接插值表达式 -->
        {{ message.split('').reverse().join('') }}
        <!-- 使用计算属性 -->
        {{ reverseMessage }}
        <!-- 在methods中写 -->
        {{ reverseMe() }}



        <!-- 侦听器 -->
        <p>
            姓氏: <input type="text" v-model="firstName">
        </p>
        <p>
            名字: <input type="text" v-model="lastName">
        </p>
        <p>
            姓名: {{ firstName }}{{ lastName }}
            {{ num }}
        </p>



        <!-- 条件渲染 v-if -->
        <p v-if=" lv == 'A' "> 您的会员等级为: A </p>
        <p v-else-if=" lv == 'B' "> 您的会员等级为: B </p>
        <p v-else-if=" lv == 'C' "> 您的会员等级为: C </p>
        <p v-else> 非会员 </p>

        <p v-show="flag">flag为true,显示; flag为false,隐藏</p>
        <p v-if="flag">flag为true,显示; flag为false,隐藏</p>



        <!-- 列表渲染 v-for -->
        <h3>遍历hobbys数组</h3>
        <ul>
            <li v-for="hobby in hobbys">{{ hobby }}</li>
        </ul>
        
        <h3>遍历girls数组</h3>
        <ul>
            <li v-for="girl in girls">姓名:{{girl.name}},年龄:{{ígirl.age}}</li>
        </ul>

        <h3>遍历boys数组</h3>
        <ul>
            <li v-for="boy in boys">姓名:{{boy[0]}}，年龄:{{boy[1]}}</li>
        </ul>

        <h3>遍历students数组</h3>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>姓名</th>
                    <th>性别</th>
                    <th>年龄</th>
                    <th>爱好</th>
                </tr>
            </thead>
        </table>
        <tbody>
            <tr v-for="student in students">
                <td>{{student.id}}</td>
                <td>{{student.name}}</td>
                <td>{{student.sex}}</td>
                <td>{{student.age}}</td>
                <td>{{fstudent.hobbys.join('、')}}</td>
                <td>
                    <a href="">编辑</a>
                    <a href="">删除</a>
                </td>
            </tr>
        </tbody>



        <!-- api风格1 选项式api -->
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
    </div>
</template>



<!-- 组件的 JavaScript 行为 -->
<script>
    export default {
        // vdata
        data(){
            return{
                //key : value,

                // 插值表示法
                message : 'hello',

                // v-html
                name:'zhangsan',
                age: '<span style="color:red">18</span>',

                // v-bind
                linkUrl:"https://baidu.com",
                imgUrl:"D:\\22820\\Pictures\\动漫\\屏幕截图 2025-02-16 180655.png",

                // v-model
                username:'zhang',

                // 表单绑定多行文本
                multilineMsg:"",

                // 复选框 布尔类型
                checked: true,

                // 单选按钮
                picked:'',

                // 单选框
                sex:'',

                // 选择框 单选
                edu:'',

                // 选择框 多选
                course:[],

                // 侦听器
                firstName:'张',
                lastName:'三',
                num : 0,  // 修改次数

                // 条件渲染
                lv:'B',
                score:88,
                flag:true,

                // 列表渲染
                hobbys:['游泳','读书','爬山','绘画'],//字符串数组
                girls: [ //对象数组
                    {name:'小花',age:20},
                    {name:'小红',age:18},
                    {name:'马冬梅',age:30}
                ],
                boys:[//二维数组
                ['小黑',50],
                ['小绿',28],
                ['小黄',30]
                ],
                students:[
                {id:11,name:'李四',sex:'男',age:22},
                {id:12,name:'王五',sex:'男',age:23},
                {id:13,name:'赵六',sex:'女',age:24},
                {id:14,name:'田七',sex:'男',age:22}
                ]
            };
        },



        // 用来定义组件的函数
        // vmethods
        methods:{
            // v-on
            toUpper(){
                // 在事件函数中使用this表示当前组件的对象
                this.name = this.name.toUpperCase()   
                //重新赋值 = 取值 + 变大写
            },
            addAge(){
                this.age++
            },



            // 事件增强  $event
            // 如果没有传递参数, 形参e代表事件对象
            test1(e) {
                alert(e.target.innerHTML)
            },
            //绑定事件的时候，传递了参数，那么肯定代表的是传递进来的值
            test2(e) {
                alert(e)
            },
            //如果需要传递参数，并想要使用事件对象，那么额外传$event显式传入进来
            test3(x,y, e) {
                alert(x + y + '---' + e.target.innerHTML)
                // 也可以直接使用event关键词直接调用事件对象
                console.log(e)
            },
            f1(){
                console.log('outer的单击事件触发了...');
            },
            f2(){
                console.log('middle的单击事件触发了...');
            },
            f3(){
                console.log('inner的单击事件触发了...');
                e.stopPropagation();  //  阻止实现
            },


            
            // methods中也可以完成计算属性
            reverseMe(){
                return this.message.split('').reverse().join('')
            }            
        },



        // 计算属性
        // vcomputed
        computed:{
            reverseMessage(){
                // 计算属性得到的结果是data中数据 键值对   
                // 键:值   reverseMessage : this.message.split('').reverse().join('')
                return this.message.split('').reverse().join('')
            }
        },


        // 侦听器
        // vwatch
        watch:{
            firstName(newValue, oldValue){
                this.num++
            },
            lastName(newValue,oldValue){
                this.num++
            }
        },


        // 生命周期
        mounted(){
            console.log('页面挂载完毕');
            
        }
    }
</script>



<!-- 组件的样式: 添加scoped表示这里定义的样式只在此组件中有效 -->
<style scoped>

</style>