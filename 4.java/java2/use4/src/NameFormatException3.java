public class NameFormatException3 extends RuntimeException{
    // Student2中name不合法的异常
    // 继承 RuntimeException

    /* 命名规则
        NameFormat 当前异常名字 表示姓名格式化有问题
        Exception 表示当前类是一个异常类

        运行时 RuntimeException 核心 由于参数错误而导致的问题
        编译时 Exception 核心 提醒程序员检查基本信息

        alt insert 构造函数 选前两个
     */

    public NameFormatException3() {
    }

    public NameFormatException3(String message) {
        super(message);
    }

    /* 那么
        原Student2中name的setter异常方法可以改写为
        public void setName(String name) throws RuntimeException{
            int len = name.length();
            if(len < 3 || len > 10){ // 判断年龄长度是否超出
                throw new NameFormatException3("姓名范围超出，当前姓名为"+name);
            }
            this.name = name;
        }
     */
}
