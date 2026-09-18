package practice;

public class test4 {
    public static void main(String[] args){
        /* 可爱的小明特别喜欢爬楼梯，他有的时候一次爬一个台阶，有的时候一次爬两个台阶。
            如果这个楼梯有20个台阶，小明一共有多少种爬法呢?
            运算结果：
            1层台阶 1种爬法
            2层台阶 2种爬法
            7层台阶 21种爬法

            假设在19阶 上20只有一种爬法
            假设在18阶 上20只有一种爬法 因为从18到19到20 已经算在19阶的方法里了
            上17阶的台阶 不需要再考虑 因为上1步->18  上2步->19 都考虑过1了

            因此 上20台阶方法 = 上19阶台阶 + 上18阶台阶
            fn(20) = fn(19) + fn(18)

            斐波那契
         */

        System.out.println(fn(20));


    }
    public static int fn(int step){
        if(step == 1){
            return 1;
        }

        if(step == 2){
            return 2;
        }

        return fn(step-1) + fn(step-2);
    }

}
