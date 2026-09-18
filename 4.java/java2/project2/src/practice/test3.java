package practice;

public class test3 {
    public static void main(String[] args) {
        /* 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，
            又多吃了一个，第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后
            每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩
            下一个桃子了。求第一天共摘了多少个桃子？

            反向递归
         */

        System.out.println(getCount(1));


    }
    public static int getCount(int day){
        if(day <= 0 || day >= 11){
            System.out.println("错误");
            return -1;
        }

        if(day == 10){
            return 1;
        }

        return (getCount(day + 1) + 1) * 2;
    }
}
