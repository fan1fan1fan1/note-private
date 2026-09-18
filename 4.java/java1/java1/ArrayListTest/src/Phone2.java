public class Phone2 {
    // 属性
    private String brand;
    private int price;

    // 空参
    public Phone2() {

    }

    // 全参
    public Phone2(String brand, int price) {
        this.brand = brand;
        this.price = price;
    }

    // getter和setter
    public String getBrand() {
        return brand;
    }
    public void setBrand(String brand) {
        this.brand = brand;
    }
    public int getPrice() {
        return price;
    }
    public void setPrice(int price) {
        this.price = price;
    }



}
