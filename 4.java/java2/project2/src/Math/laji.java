package Math;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class laji {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");

        Iterator<String> it = list.iterator(); // 创建迭代器 默认指向0索引

        while(it.hasNext()){ // 判断当前指向位置是否有元素 有true执行循环 没有false跳出循环
            String str1 = it.next(); // 获取当前指针元素 移动指针
            System.out.println(str1);

            // 迭代器遍历过程中不能用集合对象修改元素
            // list.remove(str1); 会报错 ConcurrentModificationException

            // 迭代器遍历过程中如果要删除元素 只能用迭代器的删除方法
            if (str1.equals("b")){
                it.remove();
            }

            System.out.println(list);
        }

    }

}
