public class phoneAverage4 {
    // 属性
    private String brand;
    private double price;
    private String color;

    // 空参
    public phoneAverage4(){}

    // 全参
    public phoneAverage4(String brand, double price, String color){
        this.brand = brand;
        this.price = price;
        this.color = color;
    }

    // get set
    public String getBrand(){
        return brand;
    }
    public double getPrice(){
        return price;
    }
    public String getColor(){
        return color;
    }

    public void setBrand(String brand){
        this.brand = brand;
    }
    public void setPrice(double price){
        this.price = price;
    }
    public void setColor(String color){
        this.color = color;
    }

    // 方法

}
