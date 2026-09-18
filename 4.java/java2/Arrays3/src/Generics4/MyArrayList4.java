package Generics4;

public class MyArrayList4<N,I> {
    private N name;
    private I age;
    // 如果属性，姓名、年龄的数据类型不确定 就可以使用泛型 N代表姓名 I代表年龄

    /* 在定义吃东西方法时 由于不同生物吃东西语句不同 我们使用抽象类定义抽象方法
         public abstract void eat();
         同时右键取消报错 选择第二个 Make Animal abstract 将Animal类变成抽象类
     */

    /* 此处定义一个大类 然后会定义四种不同动物的具体子类
        此时对于父类 我们有两种继承方式
        1.继承抽象类 重写里面的所有方法
        2.本身cat dog也是一个抽象类 让cat子类再重写方法

        由于各种子类 波斯猫 狸花猫的抽象方法输出不同 因此我们选择第二种方法进行重写

        public class cat1 extends Cat{
            在此之前 会建一个第二大类cat 用于继承MyArrayList4动物类

            @Override
            public void eat(){
                System.out.println("一只叫做" + getName() + "的，" + "getAge()" + "岁的波斯猫，正在吃小饼干");
            }
        }
     */
}
