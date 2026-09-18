window.addEventListener('load', function () {
    this.alert(1);

    // 1.获取元素
    var arrow_l = this.document.querySelector('.arrow-l');   // 左按钮
    var arrow_r = this.document.querySelector('.arrow-r');   // 右按钮
    var focus = this.document.querySelector('.focus');       // 主轮播图

    // 2.鼠标经过focus 就显示被隐藏的左右按钮
    focus.addEventListener('mouseenter', function () {
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
        clearInterval(timer);
        timer = null;  // 清除定时器变量
    })
    focus.addEventListener('monseleave', function () {
        arrow_l.style.display = 'none';
        arrow_r.style.display = 'none';
        timer = setInterval(function () { // 定时器
            // 手动调用点击事件
            arrow_r.click();
        }, 2000);
    })

    // 3.动态生成小圆圈
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('.circle');
    for (var i = 0; i < ul.children.length; i++) {
        // 创建一个小li
        var li = this.document.createElement('li');

        // 记录当前小圆圈的索引号 通过自定义属性来做
        li.setAttribute('index', i);

        // 把小li插入到ol里面
        ol.appendChild(li);
    }

    // 4.小圆圈的排他思想
    // 我们可以直接在生成小圆圈的同时直接绑定点击事件
    li.addEventListener('click', function () {
        // 干掉所有人 把所有的小li 清除 current 类名
        for (var i = 0; i < ol.children.length; i++) {
            ol.children[i].className = '';
        }
        // 留下自己 当前的小li 设置为 current 类名
        this.className = 'current';

        // 5.点击小圆圈 移动图片 移动ul
        // ul的移动距离 小圆圈的索引号 乘以 图片的宽度 注意是负值
        // 当我们点击了某个小li 就拿到当前小li 的索引号
        var index = this.getAttribute('index');
        var focusWidth = focus.offsetWidth;
        console.log(focusWidth);
        console.log(index);


        // animate(obj, target, callback);    animate(ul, -index * focusWidth, callback);
        animate(ul, -index * focusWidth, callback);
    })


    // 把ol里面的第一个小li设置为类名 current
    ol.children[0].className = 'current';

    // 克隆第一张照片 放在最后
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);

    // 7.点击右侧按钮 图片滚动一张
    var num = 0;
    // circle 控制小圆圈的播放
    var circle = 0;
    // 节流阀
    var flag = true;

    arrow_r.addEventListener('click', function () {
        if (flag) {
            flag = false;  // 关闭节流阀

            // 如果走到了最后复制的一张图片 此时 我们的ul 要快速复原 left 改为0
            if (num == ul.children.length - 1) {
                ul.style.left = 0;
                num = 0;
            }

            num++;
            // animate(ul, -num * focusWidth, callback);
            animate(ul, -num * focusWidth, function () {
                flag = true;  // 打开节流阀
            });

            // 8.点击右侧按钮 图片滚动一张 小圆圈随之变化
            circle++;
            /* 如果circle==4 说明走到最后我们克隆的这张图片了 我们就复原
            if (circle == 4) {
                circle = 0;
            }*/
            if (circle == ol.children.length) {
                circle = 0;
            }

            // 调用函数
            circleChange();

            // 先清除其余小圆圈的current类名
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';
            }
            // 留下当前的小圆圈的current类名
            ol.children[circle].className = 'current';
        }
    });
})