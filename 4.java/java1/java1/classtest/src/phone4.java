public class phone4 {
    public static void main(String[] args){
        /*
            定义数组存储3部手机对象
            属性: 品牌 价格 颜色
            要求计算三部手机价格平均值
         */

        // 1.创建数组
        phoneAverage4[] arr = new phoneAverage4[3];

        // 2.创建对象
        phoneAverage4 p1 = new phoneAverage4("小米", 1999, "白色");
        phoneAverage4 p2 = new phoneAverage4("华为", 3999, "黑色");
        phoneAverage4 p3 = new phoneAverage4("苹果", 4999, "蓝色");

        // 3.对象赋给数组
        arr[0] = p1;
        arr[1] = p2;
        arr[2] = p3;

        // 4.遍历
        for(int i=0; i< arr.length; i++){
            phoneAverage4 phone = arr[i];
            System.out.println(phone);
        }

        // 5.计算平均值
        double sum = 0;
        for(int i=0; i< arr.length; i++){
            phoneAverage4 phone = arr[i];
            sum = sum + phone.getPrice();   // 获取price的数据 并求和
        }

        double average = sum / arr.length;  // 数据能不写死 就不写死
        System.out.println("手机价格平均值为: " + average);
    }
}
