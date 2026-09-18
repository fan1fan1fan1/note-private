public class test {
    public static void main(String[] args) {
        int count = 1;
        for (int i = 100; i <= 999; i++) {
            int g = i % 10; // 个位
            int s = i / 10 % 10; // 十位
            int b = i / 100; // 百位
            if (g*g*g+s*s*s+b*b*b == i) {
                System.out.println("第" + count + "个水仙花数：" + i);
                count++;
                if (count > 3) {
                    break;
                }
            }
        }
    }
}