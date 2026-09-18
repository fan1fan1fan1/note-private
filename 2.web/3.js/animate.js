function animate(obj, target, callback) {
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        var step = (target - obj.offsetLeft) / 10;
        step > 0 ? Math.ceil(step) : Math.floor(step);
        if (obj.offsetLeft == target) {
            clearInterval(timer);

            // 回调函数写在此处 定时器结束时
            if (callback) {
                callback();
            }
        }
        obj.style.left = obj.offsetLeft + step + 'px';
    }, 30);
}
var div = document.querySelector('div');
animate(div, 300, function () {
    alert('hi');
    span.style.backgroundColor = 'red';
});
