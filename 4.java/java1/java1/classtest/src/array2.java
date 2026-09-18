public class array2 {
    public static void main(String[] args){
        /*
            定义数组存储三个商品对象
            商品的属性: id 名字 价格 库存
            创建三个商品对象 并能吧商品对象存入数组当中
         */

        // 1.创建一个数组
        arrayObject2[] arr = new arrayObject2[3];

        // 2.创建三个商品对象(给属性赋值)
        arrayObject2 a1 = new arrayObject2("001", "华为", 5999.0, 100);
        arrayObject2 a2 = new arrayObject2("002", "苹果", 6999.0, 100);
        arrayObject2 a3 = new arrayObject2("003", "小米", 3999.0, 100);

        // 3.商品添加到数组索引里
        arr[0] = a1;
        arr[1] = a2;
        arr[2] = a3;

        // 4.遍历
        for(int i=0; i< arr.length; i++){
            arrayObject2 array = arr[i];
            System.out.println((array.getID() + "," + array.getName() + "," + array.getPrice() + "," + array.getCount()));
        }

        //

    }
}
