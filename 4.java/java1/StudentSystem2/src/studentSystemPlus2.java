import java.util.Scanner;

public class studentSystemPlus2 {
    public static void main(String[] args) {
        // 相较于1 多了用户登录界面
        /*
           1.输入账号 进行登录 登录成功后才可以进行操作
           2.如果没有账号 进行注册
           3.如果已有帐号 但忘记密码 根据身份证和手机号的匹配 进行修改密码
         */

        System.out.println("-------欢迎来到学生管理系统-------");

        Scanner sc = new Scanner(System.in);
        String choice = sc.next();

        switch (choice) {
             case "1":
                 System.out.println("登录");
                 break;
             case "2":
                 /* 注册步骤
                    1.用户名验证要求：
                        用户名唯一
                        用户名长度必须在3~15位之间
                        只能是字母加数字的组合，但是不能是纯数字
                    2，密码键盘输入两次，两次一致才可以进行注册。
                    3，身份证号码需要验证 验证要求：
                        长度为18位
                        不能以0为开头
                        前17位，必须都是数字
                        最为一位可以是数字，也可以是大写X或小写x
                    4，手机号验证。 验证要求：
                        长度为11位
                        不能以0为开头
                        必须都是数字
                  */
                 System.out.println("注册");
                 break;
             case "3":
                 System.out.println("忘记密码");
                 break;
             default:
                 System.out.println("输入有误，请重新输入");
                 break;
        }


    }
}
