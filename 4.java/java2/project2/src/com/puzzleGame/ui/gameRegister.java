package com.puzzleGame.ui;

import javax.swing.*;

public class gameRegister extends JFrame {
    // 3.创建注册界面 规定gameRegister这个界面表示的就是注册界面 与注册界面相关的代码都写在这个类里面

    /*  获取用户输入的用户码
        获取用户输入的密码 两次
        比较两次的密码是否一致
        判断当前用户是否已经注册
         */

    public gameRegister() {
        this.setTitle("拼图注册界面, v1.0");  // 设置标题
        this.setAlwaysOnTop(true); // 设置界面置顶
        this.setLocationRelativeTo(null); // 设置界面居中
        this.setDefaultCloseOperation(3); // 设置关闭方式

        this.setSize(488, 500);
        this.setVisible(true);
    }
}
