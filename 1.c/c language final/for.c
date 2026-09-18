#include <stdio.h>
#include <stdint.h>      // int16_t ，运算符
#include <inttypes.h>    // int类型最大值 , 运算符
#include <stdbool.h>     // bool类型

int main(void) {
	// for 循环


	/*
	  i++与++i的区别:
	  i++ 先计算再赋值
	  ++i 先执行再计算
	 */



	 // 九九乘法表
	int i;
	int j;
	for (i = 1; i <= 9; i++) {
		for (j = 1; j <= i; j++) {
			printf("%d*%d=%d ", j, i, i * j);
		}
		printf("\n");
	}



	// 打印一个菱形
	int i;  // 对行处理
	int j;  // 打印空格
	int k;  // 打印*
	for (i = 1; i <= 9; i++) {
		for (j = 0; j < 9 - i; j++) {
			printf(" ");
		}
		for (k = 0; k < (2 * i - 1); k++) {
			printf("*");
		}
		printf("\n");
	}

	for (i = 1; i <= 9; i++) {
		for (j = 0; j < i; j++) {
			printf(" ");
		}
		for (k = 0; k < (2 * (9 - i) - 1); k++) {
			printf("*");
		}
		printf("\n");
	}



	// 跑圈 
	const uint32_t total_lapss = 10;  // 目标圈数

	uint32_t current_lapp = 0;        // 初始化当前圈数

	puts("跑步者开始跑步");

	for (uint32_t current_lapp = 1; current_lapp < total_lapss; current_lapp++) {

		// 对for循环判断条件：()里可以写三个; ; ;    

		// 第一个; 循环当中的自动变量的初始化current_lap 当此条件判断为true时 才执行for循环语句    
		// for()里的内容在此案例中为 uint32_t current_lap = 0; 即可省略上方条件 

		// 第二个; 案例执行的条件

		// 第三个; i++

		printf("跑步者完成第 %" PRIu32 " 圈\n", current_lapp);
	}




	// (一) 求平方和
	// 计算从1到n(n时用户输入的)所有整数的平方和 假设n = 3 -> 1²+2²+3²

	uint32_t number_13;            // 用户要输入的整数

	uint32_t sum_of_squares = 0;   // 平方求和的初始化

	puts("请输入一个整数N，我们将计算从1到N的所有整数的平方和！");

	scanf_s("%u", &number_13);

	// 用来计次的变量，我们这个程序后续不会用到，因此可以直接在for中的第一条语句定义初始化


	// Index 从初始化开始的自增值 计次
	for (uint32_t index = 1; index <= number_13; index++) {
		sum_of_squares += index * index;   // index的平方 + 总数
	}

	printf("从1到%" PRIu32 "的所有整数平方和时:%" PRIu32 "\n", number_13, sum_of_squares);




	// (二) 
	// “倒数五个数！”
	// 输入一个正整数，我们将从这个数开始倒数1

	uint32_t start_number;    // 初始化：从哪一个数开始倒数

	puts("请输入一个正整数，我们将从这个数开始倒数到1");

	// scanf_s 专用输出符号 SCNu32
	scanf_s("%" SCNu32, &start_number);

	puts("倒数开始！");

	for (uint32_t index = start_number; index > 0; index--) {

		// 条件： index > 0，假设3 2 1 0 ，当至0时，index > 0为false，循环结束

		printf("%" PRIu32 "\n", index);

		// Linux中可以引用sleep()完成该循环

	}

	puts("倒数开始！");




	// (三)
	// 阶乘
	// 输入一个正整数，计算阶乘，默认从1开始

	uint32_t number_14;          // input 

	uint32_t factorial = 1;      // 阶乘初始化为1

	puts("请输入一个正整数，我们将计算它的阶乘:");
	scanf_s("%" PRIu32, &number_14);    // & 里是：最初给出的要进行改变的数

	for (uint32_t index = 1; index <= number_14; index++) {

		// uint32_t index = 的是开始计数时的第一个数

		factorial *= index;
	}

	// puts("%" PRIu32 "! = %" PRIu32 "\n", number_14, factorial);




	// sqrt开跟与素数
	double number_15 = 4.00;       // input

	printf("%lf\n", sqrt(number_15));
	// number_15 换成任意数

	printf("%lf\n", sqrt(22));



	// 选修
	// 素数 7: 一个人七块（7） 七个人每人一块（1,1,1,1,1,1）
	// 非   4：一个人四块（4） 四个人每人一块（1，1，1，1） 两个人每人两块（2，2）          



	// 训练（一） 判断素数（选修）
	// 假设有28块饼干 1个人->28  2个人->14  4个人->7  7个人->4 14个人->2 28个人->1
	// 从该数平方根处发生改变 根号28=5.3   4<5.3  7>5.3  总是满足这个条件 （一个因数大于5.3 另一个因数小于5.3）

	// 循环从2开始 保证 ÷？中 ？< 根号28   -> index = 2; index < sqrt(n); index++

	uint32_t number_16;

	bool is_prime = true;    // 素数

	puts("请输入一个正整数，除了1之外，我们将检查它是否为素数：");

	scanf_s("%" PRIu32, &number_16);

	if (number_16 <= 1) {
		is_prime = false;    // 素数 
	}
	else {
		// for,检查除了1和它本身以外的因数
		for (uint32_t i = 2; i <= sqrt(number_16); i++) {
			// 从2开始 到 小于根号下这个数
			if (number_16 % i == 0) {
				// 这个数除以2余0 -> 不是素数 返回值0 false
				is_prime = 0;
				break;
			}
		}
	}



	// 训练（二） 简单的乘法表

	uint32_t number_17;

	puts("请输入一个正整数，我们将为您生成乘法表。");

	scanf_s("%" PRIu32, &number_17);

	printf("乘法表 %"PRIu32":\n", number_17);

	for (uint32_t index = 1; index <= 10; index++) {
		printf("%" PRIu32 " * %" PRIu32 " = %" PRIu32 "\n", number_17, index, number_17 * index);
	}




	// 训练（三） 简单绘制正方形
	uint32_t size;

	puts("请输入图案的大小:");

	scanf_s("%" PRIu32, &size);

	// 长宽相同
	puts("打印正方形图案");

	for (uint32_t i = 0; i < size; i++) {

		// 当i < size时 （假设size为5 5为长度 即打印一个5个单位的*****）
		// 执行下方循环 即打印出一个* 当 i < size为false即打印到第五个*时 停止循环

		for (uint32_t j = 0; j < size; j++) {

			// j为宽度即行数 即另起行的次数
			printf("* ");
		}
		printf("\n");
		// 此时另起一行 重复该循环 直到打出5 * 5 个*
		// for循环嵌套

	}




	// 训练（四） 简单绘制三角形
	uint32_t size_1;

	puts("请输入图案的大小");

	scanf_s("%" PRIu32, &size_1);

	puts("打印三角形图案");

	// i为行 j为列

	for (uint32_t i = 0; i < size_1; i++) {
		for (uint32_t j = 0; j <= i; j++) {

			// 第一遍时 i=0 j<=i 即j=0 j++ -> 输出一个*
			// 第二遍时 i++=1 j<=i 即j=1 j++ -> 输出两个**
			printf("* ");
		}
		printf("\n");
	}




	// 训练（五） 金字塔数字 杨辉三角

	uint32_t levels;    // 定义总行数

	puts("请输入金字塔的层数");
	scanf_s("%" PRIu32, &levels);

	puts("数字金字塔图案如下：");

	// i为行 j为金字塔中每一行的数

	for (uint32_t i = 1; i <= levels; i++) {

		// 空格数量 = level - i
		// 输入数值 - 1 假设输入levels=5 在第二行时 数字前空格有5-2=3个

		// 假设level=5:   第一行 level=5 空格个数=level-1=5-1=4  
		//                第二行 level=5 空格个数=level-2=5-2=3     

		uint32_t spaces = levels - i;  // 计算并提前存储每层空间


		// 输出空格

		for (uint32_t j = 0; j < levels - i; j++) {
			printf("  ");
		}

		// 输出左边半边金字塔
		for (uint32_t j = 1; j <= i; j++) {

			// j=1与上一个for中j=0无关

			// 从第一个开始输出 一直到第i个 递增

			printf("%" PRIu32 " ", j);

			// 当前输入2 -> 1 2  输入3 -> 1 2 3   
		}

		// 输出右边半边金字塔
		for (uint32_t j = i - 1; j >= 1; j--) {

			// 从第i个右边继续输出 此时j>=1 直到j=1 递减 停止输出

			printf("%" PRIu32 " ", j);
		}
		printf("\n");
	}


	// 每一次输出 每一次printf 都是一次损耗 在性能上不高效




	// 循环中实际应用 进度条
	// 0。。。。。。——100%

	const uint32_t total_steps = 50;         // 总步长数，进度条长度

	puts("处理中，请稍后：");

	for (uint32_t i = 0; i <= total_steps; i++) {

		// 打印进度条的完整部分
		for (uint32_t j = 0; j < i; j++) {

			printf("#");

			// 打印了50个#
		}

		for (uint32_t j = i; j < total_steps; j++) {
			printf(" ");
		}
		printf("] %" PRIu32 "%%", (i * 100) / total_steps);
		// (已经传输的数据量 / 文件总大小) * 100%


		// 控制秒数 引用一个模拟时间
		// 第十二个头文件 在windows中使用#include <windows.h>
		//               在linux中适用#include <unisted.h> 

		fflush(stdout);        // 确保进度条及时显示
		//sleep(10);             // 模拟时使用 可不写 用于耗时
	}

	puts("处理完成！");



	// 案例 检查组件障碍 选修 
	// c two 



	// 案例 分配餐厅中的桌子和椅子
	const int NUM_TABLES = 3;        // 有三张桌子

	const int SEATS_PER_TABLE = 4;   // 有四个座位

	// 外层循环遍历（桌子）
	for (int table_num = 1; table_num <= NUM_TABLES; table_num++) {

		// 依次遍历每个桌子 首先第一个桌子，当前桌子的每一个座位

		printf("桌子编号：%d\n", table_num);

		// 内层循环遍历
		for (int seat_num = 1; seat_num <= SEATS_PER_TABLE; seat_num++) {

			printf("\t座位编号: %d\n", seat_num);

			// 在这里执行具体的座位分配操作
			// 此处省略一万字

			printf("\t\t处理中: 桌子%d, 座位%d\n", table_num, seat_num);
		}
	}

	// 点击行号 生成红点 可在F5 执行且调试中在此标记位置停顿

	return 0;
}