public class carObject3 {
    // 属性
    private String brand;
    private int price;
    private String color;

    // 空参
    public carObject3(){

    }

    // 全参
    public carObject3(String brand, int price, String color){
        this.brand = brand;
        this.price = price;
        this.color = color;
    }

    // get和set
    public String getBrand(){
        return brand;
    }
    public int getPrice(){
        return price;
    }
    public String getColor(){
        return color;
    }

    public void setBrand(String brand){
        this.brand = brand;
    }
    public void setPrice(int price){
        this.price = price;
    }
    public void setColor(String color){
        this.color = color;
    }

    // 方法

}
