package Math;

public class fenKuai2 {
    public static void main(String[] args) {
        /* 分块查找
            1.前一块中的最大数据 小于后一块中的所有数据 (块内无序 块间有序)
            2.块数数量一般等于数字的个数开根号 (比如16个数字一般分成四块)
            3.先确定要查找的元素在哪一块 然后在块内查找

            1.先定义一个块类
            2.创建对象 数组->索引表
         */
        int[] arrR = {16,5,9,12,21,18,26,23,37,32,45,34,50,48,61,52};

        // 1.类
        class Block{
            private int max;   // 块中的最大值
            private int startIndex;   // 起始索引
            private int endIndex;     // 结束索引

            public Block() {
            }

            public Block(int max, int startIndex, int endIndex) {
                this.max = max;
                this.startIndex = startIndex;
                this.endIndex = endIndex;
            }

            public int getMax() {
                return max;
            }

            public void setMax(int max) {
                this.max = max;
            }

            public int getStartIndex() {
                return startIndex;
            }

            public void setStartIndex(int startIndex) {
                this.startIndex = startIndex;
            }

            public int getEndIndex() {
                return endIndex;
            }

            public void setEndIndex(int endIndex) {
                this.endIndex = endIndex;
            }
        }


        // 2.创建对象

        /* 分块查找并创建对象
        int blockSize = (int) Math.sqrt(arrR.length);   // 块数
        Block[] blocks = new Block[blockSize];   // 创建对象数组

        // 3.分块
        for (int i = 0; i < blockSize; i++) {
            blocks[i] = new Block();   // 每个对象都要创建
        }
         */

        fenKuai2.Block B1 = new fenKuai2.Block(26, 0, 3);
        fenKuai2.Block B2 = new fenKuai2.Block(45, 4, 7);
        fenKuai2.Block B3 = new fenKuai2.Block(61, 8, 11);
        fenKuai2.Block B4 = new fenKuai2.Block(52, 12, 15);

        // 4.定义数组 索引表
        fenKuai2.Block[] blocks = {B1, B2, B3, B4};

        // 5.查找的数字
        int number = 50;

        // 6.调用方法
        int index = getIndex(blocks, arrR, number);



        // 扩展的分块查找 无规律的数据


    }

    static class Block{
        private int max;   // 块中的最大值
        private int startIndex;   // 起始索引
        private int endIndex;     // 结束索引

        public Block() {
        }

        public Block(int max, int startIndex, int endIndex) {
            this.max = max;
            this.startIndex = startIndex;
            this.endIndex = endIndex;
        }

        public int getMax() {
            return max;
        }

        public void setMax(int max) {
            this.max = max;
        }

        public int getStartIndex() {
            return startIndex;
        }

        public void setStartIndex(int startIndex) {
            this.startIndex = startIndex;
        }

        public int getEndIndex() {
            return endIndex;
        }

        public void setEndIndex(int endIndex) {
            this.endIndex = endIndex;
        }
    }


    // 3.分块查找 查找number索引
    private static int getIndex(Block[] blocks, int[] arr, int number) {
        // 1.确定number在哪一块
        int indexBlock = findIndexBlock(blocks, number);

        // 2.不在
        if(indexBlock == -1){
            return -1;
        }

        // 3.在
        // 获取起始索引和结束索引 遍历
        int startIndex = blocks[indexBlock].getStartIndex();
        int endIndex = blocks[indexBlock].getEndIndex();

        for (int i = startIndex; i <= endIndex; i++) {
            if(arr[i] == number){
                return i;
            }
        }

        return -1;
    }

    // 3.分块查找 确定number在哪个块里
    public static int findIndexBlock(Block[] blocks, int number){
        // 从0索引开始遍历数组 如果number小于max 那么就表示number是在这一块中
        for (int i = 0; i < blocks.length; i++) {
            if (number <= blocks[i].getMax()) {
                return i;
            }
        }
        return -1;
    }

}
