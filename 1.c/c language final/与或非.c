#include <stdio.h>
#include <stdint.h>      // int16_t ，运算符
#include <inttypes.h>    // int类型最大值 , 运算符
#include <stdbool.h>     // bool类型

int main(void) {
	// 按位运算符

/*
	按位"与" &    a & b 嵌入式 作用：将一个数的特定位置清零 检查某位置是否为1
	按位"异或" ^  a ^ b 作用：将两个数据的二进制位进行比较 将每个位置依次比较 大小不同输出1 大小相同输出0 再将输出结果转化为十进制
	按位"与或" |  a | b 作用：让特定地方打开 使多个选项合并成单一选项
*/



// 解释:  设 a = 12 → 1100 二进制
//          b = 25 → 11001

// 按位与:   1100
//          11001
//            ⬇ 
// 比较结果：01000→8 转十进制 0和1比较→0 0和0比较→0 1和1比较→1
// 即 12&25 结果 8

// 按位或：  1100
//          11001
//            ⬇
//          1101 0和1比较→1 0和0比较→0 1和1比较→1

// 按位异或：1100
//         11001
//            ⬇  
//          0101 一个为1一个为0→1 其他→0


// 按位与
// 数据类型与变量名毫无意义
	int aaa = 12;
	int bbb = 25;

	printf("%d\n", 12 & 25); // 8


	// 按位或
	// 数据类型与变量名毫无意义
	int aaaa = 2;
	int bbbb = 5;

	printf("%d\n", 2 | 5); // 7


	// 按位异或
	// 数据类型与变量名毫无意义
	int aaaaa = 2;
	int bbbbb = 10;

	printf("%d\n", 2 ^ 10); // 8

	// 逻辑异或 XOR操作：当有一个1时 另一个必为0 结果才为1
	// 检测不同 若检测灯泡 1开0关 需要01010 使用按位异或判断代码是否正确



	// 定义一个a = 1 b = 2 时a变为2 b变为1
	int a = 1;
	int b = 2;
	// 方法一
	int temp;

	temp = a;
	a = b;
	b = temp;

	// 方法二
	a = a + b;
	b = a - b;
	a = a - b;

	// 方法三 按位运算符
	a = a ^ b;
	b = a ^ b;
	a = a ^ b;



	// 按位取反 ~ 
	// 把所有的0变成1 把所有的1变成0
	// 掩码

	uint8_t status = 0b00001100;

	status = ~status;

	printf("FINAL: 0b");

	// print_binary(status);
	// void处输入 void print_binary(uint_8 num);

	printf("\t(Binary)\n");
	// 0b 指二进制开头



	// 逻辑运算符 
	// && 并且 两个同时满足为真才为真 两个统一
	// || 至少有一个满足为真就为真 

	int condition_a = 1;
	int condition_b = 0;

	int res = condition_a && condition_b;

	printf("res = %d\n", res); // 0

	res = condition_a || condition_b;
	printf("res = %d\n", res); // 1



	// 复合赋值运算符
	// expression1 += expression2
	// 理解为expression1 =expression1 + expression2
	// 赋值 必须为整型或浮点型
	// 复合情况:
	int base_number = 8;
	int add_number = 2;
	int sub_number = 3;
	int mul_number = 4;
	int div_number = 2;
	int mod_number = 5;
	int left_shift_number = 1;
	int right_shift_number = 2;
	int and_number = 0b1010;
	int or_number = 0b0101;
	int xor_number = 0b1111;

	base_number += add_number;
	base_number -= sub_number;
	base_number *= mul_number;
	base_number /= div_number;
	base_number %= mod_number;
	base_number <<= left_shift_number;
	base_number >>= right_shift_number;
	base_number &= and_number;
	base_number |= or_number;
	base_number ^= xor_number;

	printf("base_number = %d\n", base_number); // 有问题
	// 原地赋值 可以提高性能 在自己身上进行修改 再赋值给自己 变量值在原始的存储位置上被更新
	// 而不是在另一个位置上 简单创建一个新的值 做出计算然后赋值给原来的值
	// In-place Modification 原地修改



	// 逗号运算符
	// ， 复制最后一次表达式的计算 即最后一个，后的运算
	// 尽量不使用 使用时加注释 可读性差

	// 变量名毫无意义，仅供娱乐
	uint32_t a1 = 1, b1 = 1, c1 = 1;

	uint32_t result1 = (a1 += 1, b1 += 2, c1 += 3);

	printf("a1 = %d, b1 = %d, c1 = %d, result = %d\n", a1, b1, c1, result1); // 0复制了 c1 +=3




	// 计算的优先级和顺序 （加减乘除运算律）
	// a = a + b中 +优先于= 因此先算右边 并赋值给左边
	// 函数不使用计算优先级


	return 0;
}