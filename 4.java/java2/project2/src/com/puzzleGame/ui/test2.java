package com.puzzleGame.ui;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class test2 {
    public static void main(String[] args) {
        // 已知一维数组 要求打乱一维数组中的数据 并按照4个一组的方式添加到二维数组中
        int[] arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

        // 遍历数组 得到每一个元素 用每一个元素跟随机索引上的数据进行交换
        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            // 生成随机索引
            int index = random.nextInt(arr.length);
            // 交换数据
            int temp = arr[i];
            arr[i] = arr[index];
            arr[index] = temp;
        }

        // 定义一个二维数组 用来存储打乱后的数组
        int[][] arr2 = new int[4][4];
        // 第一种解法: 遍历数组 把打乱后的数组 按照4个一组的方式添加到二维数组中
        for (int i = 0; i < arr.length; i++) {
            arr2[i/4][i%4] = arr[i];
        }

        // 第二种解法: 遍历二维数组 直接打印
        /*
        for (int i = 0; i < arr2.length; i++){
            for (int j = 0; j < arr2[i].length; j++){
                arr2[i][j] = arr[i*4+j];
            }

        }
        */

        /* 打印数组
        for (int i = 0; i < arr2.length; i++) {
            for (int j = 0; j < arr2[i].length; j++) {
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }
        */




        /* 事件
            包括: 事件、监听、响应

            事件案例: 1.创建按钮 2.添加按钮 3.添加事件

            事件: 可以被组件识别的操作 当你对组件干了某件事情之后 就会执行对应的代码

            1.事件源: 按钮、图片、窗体...
            2.事件: 某些操作例如鼠标单击、鼠标划入
            3.绑定监听: 当事件源触发了事件 就会执行绑定的监听代码
                KeyListener  监听键盘事件
                MouseListener  监听鼠标事件
                ActionListener  监听按钮事件
        */



        /* 具体操作方法
            1.创建一个按钮
            JButton btn = new JButton("我是按钮");


            2.设置按钮的位置 宽高
            btn.setLocation(0,0,100,100);


            3.动作监听: 鼠标单击+空格 触发后要执行的代码
            (一)第一种写法
            btn.addActionListener(new ActionListener() {
                在实际开发中 我们使用匿名内部类进行定义按钮

                @Override
                public void actionPerformed(ActionEvent e) {
                    System.out.println("按钮被点击了");
                }
            });

            (二)第二种写法 按钮很多用这种方法
            文件头extents 继承类ActionListener()

            btn.addActionListener(this);
            } 主函数后面 ⬇

            @Override
            public void actionPerformed(ActionEvent e) {
                // 如果按钮很多 先判断是哪个按钮 获取按钮
                if(e.getSource() == btn1){
                    System.out.println("按钮1被点击了");
                }
                else if(e.getSource() == btn2){
                    System.out.println("按钮2被点击了");
                }
            }


            4.添加按钮
            (一)第一种写法
            jFrame.getContentPane().add(btn);

            (二)第二种写法
            this.getContentPane().add(btn2);


            5.测试类
            new 书写按钮类的名();
         */



        /* 动作监听机制对鼠标类型(默认点击)

            鼠标监听机制
            1.划入动作
            2.按下动作 2 3为单击事件
            3.松开动作
            4.划出动作
         */


        // 阶段项目5



    }
}
