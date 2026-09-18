package com.puzzleGame.ui;

import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class gameStart extends JFrame {
    // 首先extends JFrame 继承父类的方法

    int[][] arr2 = new int[4][4]; // 管理数据 加载图片的时候根据二维数组中的数据加载

    // 1.创建游戏主界面 规定gameStart这个界面表示的就是游戏主界面 与游戏主界面相关的代码都写在这个类里面
    public gameStart() {
        // 初始化内容代码多 ctrl+alt+m 抽取方法 设置名称 成为一个函数在下方
        // 创建游戏主界面
        initJFrame();

        // 创建菜单栏
        initJMenuBar();

        // 打乱图片 要放在添加图片的前面
        initShuffle();

        // 添加图片 JLabel 图片+文字
        initImage();  // alt+回车 创建方法

        this.setVisible(true); // 显示
    }



    // 4.打乱图片 长度确定的用数组 不确定的用集合
    private void initShuffle() {
        int[] arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            int index = random.nextInt(arr.length);
            int temp = arr[i];
            arr[i] = arr[index];
            arr[index] = temp;
        }

        for (int i = 0; i < arr.length; i++) {
            arr2[i/4][i%4] = arr[i];
        }
    }



    // 3.添加图片 JLabel 图片+文字
    private void initImage() {
        /*  创建ImageIcon对象
            ImageIcon icon = new ImageIcon("D:\\22820\\Desktop\\code\\java\\java2\\animal\\1.jpg");

            创建JLabel对象 管理标签、图片
            JLabel jLabel = new JLabel(icon);

            指定图片位置
            jLabel.setBounds(105*j, 105*i, 105, 105);
            this.getContentPane().add(jLabel); 第一张图片(0,0) 长105 宽105 那么第二张图片就是(105,0) 以此类推
        */

        // 优化添加图片代码
        // int num = 1;
        // 根据二维数组中管理的数据添加图片

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                // 优化添加图片代码
                // int num = 1;
                // 根据二维数组中管理的数据添加图片
                int num = arr2[i][j];
                JLabel jLabel = new JLabel((new ImageIcon("D:\\22820\\Desktop\\code\\java\\java2\\animal\\"+ num +".jpg")));
                // 上边是添加图片路径 一共16张图片 因此设定一个变量表示图片序号并循环遍历
                // num++;

                jLabel.setBounds(105*j, 105*i, 105, 105);
                this.getContentPane().add(jLabel);
            }
        }

        this.setLayout(null); // 取消默认的流式布局

        // this.add(jLabel);
        // this.getContentPane().add(jLabel);
    }



    // 2.创建游戏菜单栏 JMenuBar
    private void initJMenuBar() {
        // 创建菜单栏JMenuBar
        JMenuBar menuBar = new JMenuBar();

        // 创建菜单JMenu
        JMenu menu = new JMenu("菜单");
        JMenu aboutJMenu = new JMenu("关于我们");

        // 创建菜单项JMenuItem
        JMenuItem replayItem = new JMenuItem("重新游戏");
        JMenuItem reLoginItem = new JMenuItem("重新登录");
        JMenuItem accountItem = new JMenuItem("公众号");
        JMenuItem exitItem = new JMenuItem("退出游戏");

        JMenuItem startItem = new JMenuItem("开始游戏");
        JMenuItem registerItem = new JMenuItem("注册账号");
        JMenuItem loginItem = new JMenuItem("登录账号");

        // 把菜单项添加到菜单中 菜单名.add(菜单项名)
        menu.add(replayItem);
        menu.add(reLoginItem);
        menu.add(accountItem);
        menu.add(exitItem);
        aboutJMenu.add(startItem);
        aboutJMenu.add(registerItem);

        // 把菜单添加到菜单栏中 菜单栏名.add(菜单名)
        menuBar.add(menu);
        menuBar.add(aboutJMenu);

        // 把菜单栏添加到游戏主界面中 游戏主界面名.setJMenuBar(菜单栏名)
        this.setJMenuBar(menuBar);
    }



    // 1.创建游戏主界面
    private void initJFrame() {
        this.setTitle("拼图游戏单机版, v1.0");  // 设置标题
        this.setAlwaysOnTop(true); // 设置界面置顶
        this.setLocationRelativeTo(null); // 设置界面居中
        this.setDefaultCloseOperation(3); // 设置关闭方式

        this.setSize(603, 680); // 设置界面宽高
    }


}









