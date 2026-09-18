package com.puzzleGame.ui;

import javax.swing.*;

public class gameLogin extends JFrame {
    // 2.创建登录界面 规定gameLogin这个界面表示的就是登录界面 与登录界面相关的代码都写在这个类里面

    /*  获取用户输入的用户名
        获取用户输入的密码
        生成一个验证码
        获取用户输入的验证码
         */

    public gameLogin() {
        this.setTitle("拼图登录界面, v1.0");  // 设置标题
        this.setAlwaysOnTop(true); // 设置界面置顶
        this.setLocationRelativeTo(null); // 设置界面居中
        this.setDefaultCloseOperation(3); // 设置关闭方式

        this.setSize(488, 430);
        this.setVisible(true);

    }


}
