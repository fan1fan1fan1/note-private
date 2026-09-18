public class method6 {
    public static void main(String[] args) {
        // 由public static void main 框起来的叫main方法 主方法

        // 方法(method)是程序中最小的执行单元
        // 要么都执行 要么都不执行
        // 提高代码复用性 可维护性 提高效率

        /* 1.方法定义格式
            public static 返回值类型 方法名(参数){
                方法体;
                return 返回值;
            }
         */

        // 2.方法调用
        HelloWorld();


        int a = 1;
        int b = 2;
        ADD(a,b);

        // 调用方法1 直接调用
        SUM(a,b);

        // 调用方法2 赋值调用
        int c = SUM(a,b);

        // 调用方法3 输出调用
        System.out.println(SUM(a,b));



        /* 方法的重载
            同一class类当中 定义了多个method同名的方法 有相同的功能 但参数int a不同 就构成了重载关系
            参数不同: 个数不同 数据类型不同 顺序不同
         */
        sum(10, 20);
        sum(10,20,30);



        // 判断某数据是否在数组中存在
        int arr[] = {1,2,3,4,5};
        int num = 1;
        boolean flag = contains(arr, num);
        System.out.println(flag); // true



        // 赋值拷贝数组
        /* 需求
        定义一个方法
        将数组arr中从索引from开始(包含from)
        到索引to结束(不包含to)的元素复制到新数组中
        返回
         */
        int arr1[] = {1,2,3,4,5};
        int[] copyArr = copy(arr, 1, 3);
        for (int i = 0; i < copyArr.length; i++) {
            System.out.println(copyArr[i] + " ");  // 2 3
        }



    }
    // 无参数方法
    public static void HelloWorld(){
        System.out.println("HelloWorld");
    }


    // 有参数方法
    public static void ADD(int num1, int num2){
        int result = num1 + num2;
        System.out.println(result);
    }

    // 有返回值方法
    public static int SUM(int num1, int num2){
        int c = num1 + num2;
        return c;
    }

    // 构成重载关系的方法 在主函数main中 会根据个数或数据类型不同来区分使用哪个方法
    public static int sum(int a, int b){
        return a + b;
    }
    public static int sum(int a, int b, int c){
        return a + b + c;
    }

    /* 由于参数不同不构成重载关系
    public static void fn(int a){
        // 方法体
    }
    public static int fn(int a){
        // 方法体
    }
     */


    // 判断某数据是否在数组中存在
    public static boolean contains(int[] arr, int num){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == num){
                return true;
            }
        }
        return false;
    }


    // 赋值拷贝数组
    public static int[] copy(int[] arr, int from, int to){
        // 1.定义数组
        int newArr[] = new int[to - from];

        // 2.定义伪造索引
        int index = 0;

        // 3.把原始数组中的from到to上对应的元素拷贝下来 放到newarr中
        for(int i = from; i < to;i++){
            newArr[index] = arr[i];
            index++;
        }

        // 4.返回新数组
        return newArr;
    }


    public static void fn(int num){
        num = 100; // 形参的改变不会影响实际参数值 没改变指针的地址值
    }

    // 当传递类型是引用数据类型时 传递的是地址值 形参的改变会影响实际参数值
    public static void fn(int[] arr){
        arr[0] = 100; // 形参的改变会影响实际参数值 对数组操作时使用new关键字 使用了栈堆 会改变实际参数
    }

}
