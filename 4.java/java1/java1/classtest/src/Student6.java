public class Student6 {
    public static void main(String[] args){
        /*
            定义一个长度为3的数组，数组存储1~3名学生对象作为初始数据，学生对象的学号，姓名各不相同。
            学生的属性：学号，姓名，年龄。
            要求1：再次添加一个学生对象，并在添加的时候进行学号的唯一性判断。
            要求2：添加完毕之后，遍历所有学生信息。
            要求3：通过id删除学生信息
                  如果存在，则删除，如果不存在，则提示删除失败。
            要求4：删除完毕之后，遍历所有学生信息。
            要求5：查询数组id为“heima002”的学生，如果存在，则将他的年龄+1岁
         */

        //1.定义数组
        StudentObject6[] arr = new StudentObject6[3];

        //2.创建学生对象
        StudentObject6 s1 = new StudentObject6(001,"zhangsan",23);
        StudentObject6 s2 = new StudentObject6(002,"lisi",24);
        StudentObject6 s3 = new StudentObject6(003,"wangwu",25);

        //3.将学生对象添加到数组中
        arr[0] = s1;
        arr[1] = s2;
        arr[2] = s3;



        //4.再次添加一个学生对象，并在添加的时候进行学号的唯一性判断。
        StudentObject6 s4 = new StudentObject6(004,"zhaoliu",26);
        boolean flag = contains(arr,s4.getId());

        if(flag){
            // (1).已经存在
            System.out.println("学号重复");
        }
        else{
            // (2).不存在 将新的数据赋值给数组

            // 此处需要判断数组是否已经存满 存满了就不能在添加
            int count = getCount(arr);
            if (count == arr.length) {
                // (1).数组已经存满 不能再添加
                System.out.println("数组已经存满");

                /* 如果数组已经存满
                    创建一个新数组 长度 = 老数组长度 + 1
                    然后把老数组的元素 拷贝到新数组
                 */
                StudentObject6[] newArr = createNewArr(arr);
                // 将新的数据赋值给新数组  添加在数组最后一个位置 也就是数组个数count
                newArr[count] = s4;



                //5.添加完毕之后，遍历所有学生信息。
                /* 此处有两种可能
                    根据4. 最后得到的数组可能是arr 也可能是newArr
                    假设最后newArr有数据 就说明if语句走了数据为满情况 我们就直接打印newArr
                    如果newArr没有数据 就说明没有创建并拷贝newArr 我们就直接打印arr
                */
                // 5.调用遍历
                printArr(newArr);
            }
            else{
                // (2).数组没有存满 可以添加
                arr[count] = s4;

                // 5.调用遍历
                printArr(arr);
            }
        }


        // 6. 通过id删除学生信息
        int index = getIndex(arr,002);
        // System.out.println(index);   找到了索引位置

        if (index >= 0) {
            // (1).找到了
            arr[index] = null;  // 将找到的索引位置赋值为null


            // 7.删除完毕之后，遍历所有学生信息。
            printArr(arr);
        }
        else{
            // (2).没有找到
            System.out.println("删除失败");
        }


        // 8.查询数组id为“heima002”的学生，如果存在，则将他的年龄+1岁
        int index2 = getIndex(arr,003);
        if (index2 >= 0) {
            // (1).找到了
            arr[index2].setAge(arr[index2].getAge() + 1);   // 获取这个数据的年龄属性 + 1
            System.out.println("年龄+1岁");


            // 9.查询完毕之后，遍历所有学生信息。
            printArr(arr);
        }
        else{
            // (2).没有找到
            System.out.println("查询失败");
        }

    }

    // 用于判断数组中是否存在指定id的学生 即是否会有重复的id
    /*
        1.我要干嘛  进行唯一性判断
        2.我干这件事情需要什么才能完成  数组  学生id
        3.我干完了，要不要把结果返回给调用者  要返回一个boolean类型的值
     */
    public static boolean contains(StudentObject6[] arr, int id) {
        for (int i = 0; i < arr.length; i++) {   // 依次获取数组中学生对象
            if (arr[i] != null && arr[i].getId() == id) {  // 判断数组中是否已经有指定id的学生
                return true;   // 已经存在
            }
        }
        return false;   // 当循环结束 即依次比较后仍没找到一样的return false
    }


    // 用于判断数组中已经存了多少数据
    public static int getCount(StudentObject6[] arr){
        int count = 0;  // 用于记录数组中有多少个数据

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != null) {  // 说明当前位置有数据 判断下一个数据
                count++;
            }
        }
        return count;
    }


    // 如果数组已经存满 就创建一个新数组
    public static StudentObject6[] createNewArr(StudentObject6[] arr){
        // 创建一个新数组 长度 = 老数组长度 + 1
        StudentObject6[] newArr = new StudentObject6[arr.length + 1];
        // 把老数组的元素 拷贝到新数组
        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i];
        }
        // 把新数组赋值给老数组
        arr = newArr;

        return newArr;
    }


    // 遍历数组
    public static void printArr(StudentObject6[] arr){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]!= null) {
                System.out.println(arr[i].getId() + "," + arr[i].getName() + "," + arr[i].getAge());
            }
        }
    }


    // 查找准备删除的学生的索引
    public static int getIndex(StudentObject6[] arr, int id){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]!= null && arr[i].getId() == id) {
                return i;
            }
        }
        // 如果循环结束 即依次比较后仍没找到一样的return -1
        return -1;
    }
}
