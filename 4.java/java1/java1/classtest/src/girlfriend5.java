public class girlfriend5 {
    public static void main(String[] args) {
        /*
            定义数组存储4个女朋友的对象
            属性: 姓名 年龄 性别 爱好
            要求1 计算出四个女朋友的平均年龄
            要求2 统计年龄比平均值低的女朋友有几个 并把她们的信息打印出来
         */

        // 1.定义数组
        girlfriendObiect5[] arr = new girlfriendObiect5[3];

        // 2.创建对象 并把对象赋值给数组
        arr[0] = new girlfriendObiect5("小A", 18, "女", "看电影");
        arr[1] = new girlfriendObiect5("小B", 20, "女", "看电视剧");
        arr[2] = new girlfriendObiect5("小C", 22, "女", "看小说");

        // 3.计算平均值
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i].getAge();
        }
        int avg = sum / arr.length;
        System.out.println("平均值为: " + avg);

        // 4.统计年龄比平均值低的女朋友有几个 并把她们的信息打印出来
        int count = 0;  // 用于记录个数
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].getAge() < avg) {   // 判断小于平均值的女朋友
                count++;
                System.out.println(arr[i].getName() + " " + arr[i].getAge() + " " + arr[i].getGender() + " " + arr[i].getHobby());
            }
        }
        System.out.println("年龄比平均值低的女朋友有: " + count + " 个");
    }
}
