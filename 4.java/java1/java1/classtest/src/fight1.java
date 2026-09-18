public class fight1 {
    public static void main(String[] args) {
        // 案例 文字版格斗游戏
        /* 要求
            1.角色姓名 角色血量 长相
            2.操作 攻击对方 至一方死亡 武功
        */

        // 1.创建角色
        fightRole1 r1 = new fightRole1("小孙", 30, '女');
        fightRole1 r2 = new fightRole1("小樊", 30, '女');

        // 2.打印角色信息
        System.out.println(r1.getName() + " " + r1.getBlood() + " " + r1.getGender() +" " + r1.getFace());
        System.out.println(r2.getName() + " " + r2.getBlood() + " " + r2.getGender() +" " + r2.getFace());


        // 3.战斗
        while(true){
            r1.attack(r2);
            if(r2.getBlood() == 0){
                System.out.println(r2.getName() + "死了");
                break;
            }

            r2.attack(r1);
            if(r1.getBlood() == 0){
                System.out.println(r1.getName() + "死了");
                break;
            }
        }
    }
}

