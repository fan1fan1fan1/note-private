public class arrayObject2 {
    // 属性
    private String id;
    private String name;
    private double price;
    private int count;

    // 空参
    public arrayObject2(){

    }

    // 全部参数
    public arrayObject2(String id, String name, double price, int count){
        this.id = id;
        this.name = name;
        this.price = price;
        this.count = count;
    }

    // get set
    public String getID(){
        return id;
    }
    public String getName(){
        return name;
    }
    public double getPrice(){
        return price;
    }
    public int getCount(){
        return count;
    }

    public void setID(String id){
        this.id = id;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setPrice(double price){
        this.price = price;
    }
    public void setCount(int count){
        this.count = count;
    }

    // 方法


}
