public class User2 {
    // 属性
    private String id;
    private String username;
    private String password;

    // 空参
    public User2() {

    }

    // 全参
    public User2(String id, String username, String password) {
        this.id = id;
        this.username = username;
        this.password = password;
    }

    // get set
    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }

}
