public class girlfriendObiect5 {
    // 属性
    private String name;
    private int age;
    private String gender;
    private String hobby;

    // 空参
    public girlfriendObiect5(){}

    // 全参
    public girlfriendObiect5(String name, int age, String gender, String hobby){
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.hobby = hobby;
    }

    // get set
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public String getGender(){
        return gender;
    }
    public String getHobby(){
        return hobby;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public void setHobby(String hobby){
        this.hobby = hobby;
    }

    // 方法
}
