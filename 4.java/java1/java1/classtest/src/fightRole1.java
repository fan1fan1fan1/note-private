import java.util.Random;

public class fightRole1 {
    // 属性
    private String name;
    private int blood;
    private char gender;
    private String face;
    String[] boyfaces= {"风流俊雅","气宇轩昂","相貌英俊","五官端正","相貌平平","一塌糊涂","面目狰狞"};
    String[] girlfaces ={"美奂绝伦","沉鱼落雁","婷婷玉立","身材娇好","相貌平平","相貌简陋","惨不忍睹"};

    // 攻击描述
    String[] attacks_desc={
            "%s使出了一招【背心钉】，转到对方的身后，一掌向%s背心的灵台穴拍去。",
            "%s使出了一招【游空探爪】，飞起身形自半空中变掌为抓锁向%s。",
            "%s大喝一声，身形下伏，一招【劈雷坠地】，捶向%s双腿。",
            "%s运气于掌，一瞬间掌心变得血红，一式【掌心雷】，推向%s。",
            "%s阴手翻起阳手跟进，一招【没遮拦】，结结实实的捶向%s",
            "%s上步抢身，招中套招，一招【劈挂连环】，连环攻向%s。"
    };

    // 受击描述
    String[] injureds_desc={
            "结果%s退了半步，毫发无损",
            "结果给%s造成一处瘀伤",
            "结果一击命中，%s痛得弯下腰",
            "结果%s痛苦地闷哼了一声，显然受了点内伤",
            "结果%s摇摇晃晃，一跤摔倒在地",
            "结果%s脸色一下变得惨白，连退了好几步",
            "结果『轰』的一声，%s口中鲜血狂喷而出",
            "结果%s一声惨叫，像滩软泥般塌了下去"
    };


    // 空参
    public fightRole1(){
    }

    // 有参
    public fightRole1(String name, int blood, char gender){
        this.name = name;
        this.blood = blood;
        this.gender = gender;

        // 随机长相
        setFace(gender);
    }


    // get
    public String getName(){return name;}
    // set
    public void setName(String name){this.name = name;}


    public int getBlood(){return blood;}
    public void setBlood(int blood){
        this.blood = blood;
    }

    public char getGender(){return gender;}
    public void setGender(char gender){
        this.gender = gender;
    }

    public String getFace(){
        return face;
    }
    public void setFace(char gender){
        Random r = new Random();

        if(gender == '男'){
            int index = r.nextInt(boyfaces.length);
            this.face = boyfaces[index];   // 如果定义的类的类型是int 或者char 此处可以直接return
        }
        else if(gender == '女'){
            int index = r.nextInt(boyfaces.length);
            this.face = girlfaces[index];
        }
        else{
            this.face = "性别未知";
        }
    }

        // 方法 攻击
        public void attack(fightRole1 role){
            // 1.随机进行技能招式攻击
            Random r = new Random();
            int index = r.nextInt(attacks_desc.length);
            String gongji = attacks_desc[index];


            // 2.造成伤害
            System.out.printf(gongji, this.getName(), role.getName());
            System.out.println();
            int hurt = r.nextInt(20) + 1;  // 设定伤害是1-20中随机数 范围[0, 20)  加一后[1, 20]

            // 3.判断角色是否死亡 若死亡就结束 没死亡就进行攻击
            int remainBlood = role.getBlood() - hurt;
            remainBlood = remainBlood < 0 ? 0 : remainBlood;  // 如果剩余血量小于0 就输出0 大于0就输出这个剩余血量
            role.setBlood(remainBlood);

            // 4.受击描述 不是随机的
            /*
                血量 > 90 0索引的描述
                80 - 90 1索引的描述
                70 - 80 2索引的描述
                60 - 70 3索引的描述
                40 - 60 4索引的描述
                20 - 40 5索引的描述
                10 - 20 6索引的描述
                血量 < 10 7索引的描述
             */
            if(remainBlood > 90){
                System.out.printf(injureds_desc[0], role.getName());
            }
            else if(remainBlood > 80){
                System.out.printf(injureds_desc[1], role.getName());
            }
            else if(remainBlood > 70){
                System.out.printf(injureds_desc[2], role.getName());
            }
            else if(remainBlood > 60){
                System.out.printf(injureds_desc[3], role.getName());
            }
            else if(remainBlood > 40){
                System.out.printf(injureds_desc[4], role.getName());
            }
            else if(remainBlood > 20){
                System.out.printf(injureds_desc[5], role.getName());
            }
            else if(remainBlood > 10){
                System.out.printf(injureds_desc[6], role.getName());
            }
            else{
                System.out.printf(injureds_desc[7], role.getName());
            }
            System.out.println();



            // 5.this表示方法的调用者
            System.out.println(this.getName() + "举起拳头，打了" + role.getName() + "一下，"
                    + "造成了" + hurt + "点伤害，" + role.getName() + "还剩下了" + remainBlood + "点血");
        }

        public void show(){
            System.out.println("姓名：" + getName() + " 血量：" + getBlood() +" 性别：" + getGender() + " 长相：" + getFace());
        }

}
