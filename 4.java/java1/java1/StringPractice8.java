import java.util.Scanner;

public class StringPractice8 {
    public static void main(String[] args) {
        // 案例一 用户登录
        // 需求: 已知用户名和密码 请用程序模拟用户登录 总共给三次机会 登录之后 给出相应的提示


        // 1.定义用户名和密码
        String username = "admin";
        String password = "123456";

        // 2.键盘输入用户名和密码
        for (int i = 0; i < 3; i++) {
            Scanner sc2 = new Scanner(System.in);
            System.out.println("请输入用户名");
            String inputUsername = sc2.next();

            System.out.println("请输入密码");
            String inputPassword = sc2.next();

            // 3.判断用户名和密码是否正确
            if (inputUsername.equals(username) && inputPassword.equals(password)) {
                System.out.println("登录成功");
                break;  // 登录成功 跳出循环
            }
            else {
                // 登录失败
                // 4.判断是否还有机会 已知机会一共有三次 直接进入下一次循环重新键盘录入
                if (i == 2) {
                    System.out.println("您的账号已被锁定，请联系管理员");
                    break;  // 账号被锁定 跳出循环
                }
                else {
                    System.out.println("登录失败，用户名或密码错误，您还有" + (2 - i) + "次机会");
                }
            }
        }



        // 案例二 遍历字符串
        /* 方法
            public char charAt(int index) 返回指定索引处的 char 值
            public int length() 返回此字符串的长度
         */

        // 1.键盘录入一个字符串
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个字符串");
        String str = sc.next();

        // 2.遍历字符串 str.length().fori
        for (int i = 0; i < str.length(); i++) {
            // str.charAt(i) ctrl+alt+v 自动生成左边
            char c = str.charAt(i);
            System.out.println(c);
        }



        // 案例三 统计字符个数
        // 需求: 键盘录入一个字符串 统计该字符串中大写字母字符, 小写字母字符, 数字字符出现的次数(不考虑其他字符)

        // 1.键盘录入一个字符串
        Scanner sc2 = new Scanner(System.in);
        System.out.println("请输入一个字符串");
        String str1 = sc2.next();

        // 2.定义三个变量 分别代表(1)大写字母, (2)小写字母, (3)数字字符   出现的次数
        int bigCount = 0;
        int smallCount = 0;
        int numberCount = 0;

        int otherCount = 0;

        // 3.遍历字符串 得到每一个字符
        for (int i = 0; i < str1.length(); i++) {
            char c = str1.charAt(i);
            // System.out.println(c);

            // 4.判断该字符属于哪种类型 然后对应类型的次数+1
            if (c >= 'A' && c <= 'Z') {
                bigCount++;
            }
            else if (c >= 'a' && c <= 'z') {
                smallCount++;
            }
            else if (c >= '0' && c <= '9') {
                numberCount++;
            }
            else {
                otherCount++;
            }
        }

        // 5.输出三种类型的字符出现的次数
        System.out.println("大写字母字符出现的次数为: " + bigCount);
        System.out.println("小写字母字符出现的次数为: " + smallCount);
        System.out.println("数字字符出现的次数为: " + numberCount);
        System.out.println("其他字符出现的次数为: " + otherCount);



        // 案例四 字符串拼接
        // 需求: 定义一个方法 把int数组按照指定格式拼接成一个字符串 格式参照如下: arr{1, 2, 3} -> [1, 2, 3]

        // 1.定义一个int数组
        int[] arr = {1, 2, 3};

        // 2.调用方法 把int数组按照指定格式拼接成一个字符串
        String result = arrayToString(arr);

        // 3.输出结果
        System.out.println(result);



        // 案例五 字符串反转
        // 需求: 定义一个方法 实现字符串反转 键盘录入一个字符串 调用该方法后  输出结果 例如 键盘录入 abc 输出结果 cba

        // 1.键盘录入一个字符串
        Scanner sc3 = new Scanner(System.in);
        System.out.println("请输入一个字符串");
        String str2 = sc.next();

        // 2.调用方法 实现字符串反转
        String result2 = reverse(str2);
        System.out.println(result2);



        // 案例六 指定词替换   金额转换
        // 123456789 -> 壹贰叁肆伍陆柒捌玖
        /* 需求:
            2135 -> 贰仟壹佰叁拾伍元
            方法: 贰仟壹佰叁拾伍元 -> 零零零贰壹参伍 -> 贰壹参伍 -> 2135

            1.创建一个数组 存储 0-9 对应的中文数字
            2.转换成壹贰叁肆伍陆柒捌玖 查表法
            3.前面补0
            4.插入单位
         */

        // 1.录入一个金额
        Scanner sc4 = new Scanner(System.in);
        int money;

        while (true) {
            System.out.println("请输入一个金额");
            money = sc4.nextInt();

            // 2.判断金额是否合法
            if (money >= 0 && money <= 9999999) {
                break;  // 结束循环
            }
            else {
                System.out.println("金额不合法");
            }
        }
        System.out.println(money);



        // 3.遍历 调用方法 将数字转换为中文数字

        // 定义一个字符串 用来存储转换后的中文数字
        String moneyStr = "";

        while(true){
            // 从右往左获取数据，因为右侧是数据的个位
            int ge = money % 10;

            // 已经得到了个位数 寻找对应的中文数字
            String number = getNumber(ge);

            // 已经得到了个位数对应的中文数字 将其再次转序拼接输出
            // 将number写在前面 每一次获取的新的中文数字就会被放在前面
            moneyStr = number + moneyStr;


            // 获取了最后一位数字后 将整个数字除以10 去掉最后一位  重复这个过程 再次拿出个位数
            money /= 10;

            // 判断money是否为0 结束循环
            if (money == 0) {
                break;
            }
        }


        // 4.在前面补0 补全7位
        int count = 7 - moneyStr.length();  // 假设2135  7-4=3  就需要补3个0
        for (int i = 0; i < count; i++) {
            moneyStr = "零" + moneyStr;
        }
        System.out.println(moneyStr);


        // 5.插入单位
        // 定义一个数组表示单位
        String[] units = {"佰", "拾", "万", "仟", "佰", "拾", "元"};
        // 已知得到的结果是   零    零    零    贰    壹    参    伍

        // 遍历moneyStr 得到每一个字符 将units的数据插入进去
        String result3 = "";

        for (int i = 0; i < moneyStr.length(); i++) {
            char c = moneyStr.charAt(i);

            /* 面向结果编程 直接输出数据方法
            System.out.print(c);
            System.out.print(units[i]);
             */

            // 把大写数字和单位拼接成一个字符串
            result3 = result3 + c + units[i];
        }

        System.out.println(result3);



        // 案例七 敏感词屏蔽 手机号屏蔽
        // 需求: 键盘录入一个手机号 屏蔽中间四位号码 最终效果为 156****1234

        /* 方法
            public String substring(int beginIndex, int endIndex)

            从旧数组中截取一部分 返回一个新字符串
            从指定的 beginIndex 处开始，直到索引 endIndex - 1 处的字符  (包头不包尾 包左不包右)
            子字符串的长度为 endIndex-beginIndex
            只有返回值是截取的字符串

            public String substring(int beginIndex)
            从指定的 beginIndex 处开始，直到该字符串末尾
         */

        // 1.键盘录入一个手机号
        String phoneNumber = "12345678910";

        // 2.截取字符串
        String newNumber = phoneNumber.substring(0, 3) + "****" + phoneNumber.substring(7);
        System.out.println(newNumber);



        // 案例八 身份证信息查看
        // 身份证信息: 2位省份 4位城市 6位区县 7-14位出生年月日 1516派出所 17性别 18随机

        // 需求: 键盘录入一个身份证号 将出生年月日和性别截取出来
        // 最终效果为 1990年12月12日 男

        // 1.定义一个字符串 存储身份证号
        String idCard = "110105199012121516";

        // 2.获取出生年月日
        String birth = idCard.substring(6, 14);
        System.out.println("出生日期为：" + birth);

        // 3.获取性别
        char gender = idCard.charAt(16);

        // 判断性别 已知字符ASCII表数值 '0'-'9' -> 48-57
        int num = gender - 48;

        if (num % 2 == 0) {
            System.out.println("性别为女");
        }
        else {
            System.out.println("性别为男");
        }



        // 案例九 敏感词替换
        // 需求: 键盘录入一个字符串 把指定数据变成***
        /* 方法
            public String replace(CharSequence target, CharSequence replacement)
            将target变成replacement
            字符串本身不发生变化 返回一个新的字符串
         */
        // 1.键盘录入一个字符串
        String talk = "你是一个大帅比";

        // 2.定义一个敏感词库 存储所有敏感词
        String[] sensitiveWords = {"大帅比", "TMD", "SB", "MLGB"};

        // 3.遍历敏感词库 替换敏感词
        for (int i = 0; i < sensitiveWords.length; i++) {
            talk = talk.replace(sensitiveWords[i], "***");
        }

        System.out.println(talk);
    }

    // 方法

    // 定义方法 把int数组按照指定格式拼接成一个字符串
    public static String arrayToString(int[] arr) {
        // 遍历数组 得到每一个元素 拼接成一个字符串

        if (arr == null) {
            return "null";
        }

        if (arr.length == 0) {
            return "[]";
        }

        String result = "[";
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                result += arr[i];  // 最后一个元素 不需要拼接逗号
                break;
            }
            else {
                result += arr[i] + ", ";
            }
        }

        result += "]";
        return result;
    }

    // 定义方法 实现字符串反转
    public static String reverse(String str) {
        // 将一个字符串反着遍历
        String result = "";  // 空字符串

        for (int i = str.length() - 1; i >= 0; i--) {
            char c = str.charAt(i);
            // System.out.println(c);

            // 将每一个字符拼接成一个字符串
            result += c;
        }
        return result;
    }

    // 定义方法 实现敏感词替换 将数字转换为中文数字
    public static String getNumber(int number) {
        // 1.创建一个数组 存储 0-9 对应的中文数字
        String[] arr = {"零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"};

        // 2.返回结果
        return arr[number];
    }


}
