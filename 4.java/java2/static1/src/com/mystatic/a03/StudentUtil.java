package com.mystatic.a03;

import java.util.ArrayList;

public class StudentUtil {
    // 定义工具类
    private StudentUtil(){

    }

    // 定义方法
    public static int getMaxAge(ArrayList<Student> list){
        int max = list.get(0).getAge();
        for(int i = 1; i < list.size(); i++){
            int age = list.get(i).getAge();
            if(age > max){
                max = list.get(i).getAge();
            }
        }
        return max;
    }

}
