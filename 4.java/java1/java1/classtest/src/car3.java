import java.util.Scanner;

public class car3 {
    public static void main(String[] args){
        /*
            定义数组存储3部汽车对象
            属性: 汽车的品牌 价格 颜色
            创建三个汽车对象 数据通过键盘录入 并把数据存入数组中
         */

        // 1.创建数组  此处创建对象不能写在循环里面
        carObject3[] arr = new carObject3[3];

        // 2.创建三个对象 键盘录入
        Scanner sc = new Scanner(System.in);
        for(int i=0; i < arr.length; i++){
            carObject3 c = new carObject3();  // 定义对象

            System.out.println("请输入汽车品牌");
            String brand = sc.next();  // 录入
            c.setBrand(brand);  // 赋值

            System.out.println("请输入汽车价格");
            int price = sc.nextInt();
            c.setPrice(price);

            System.out.println("请输入汽车颜色");
            String color = sc.next();
            c.setColor(color);

            // 3.将对象赋给数组
            arr[i] = c;
        }

        // 4.遍历
        for(int i=0; i<arr.length; i++){
            carObject3 car = arr[i];
            System.out.println(car.getBrand() + "," + car.getPrice() + "," + car.getColor());
        }
    }
}
