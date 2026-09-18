#include <stdio.h>
#include <stdint.h>      // int16_t ，运算符
#include <inttypes.h>    // int类型最大值 , 运算符
#include <stdbool.h>     // bool类型

int main(void) {
	// while

	const uint32_t	TOTAL_LAPS = 10;    // 常量 一共要跑十圈

	uint32_t current_lap = 0;           // 当前跑的圈数

	puts("开始罚跑");

	if (true) {                         // 当if内的东西为true时 可执行大括号内内容

	}

	while (current_lap < TOTAL_LAPS) {  // 只要当前跑的圈数小于总圈数就一直跑

		// 跑步的人在跑步 假设跑完了一圈: 告诉老师，我跑完了一圈，你看!

		current_lap++;    // 计次 （迭代点）， current_lap += 2 每次跑两圈

		printf("跑步的人完成第 %"PRIu32" 圈.\n", current_lap);
	}

	// 当current_lap >= TOTAL_LAPS 为真时停止执行 即current_lap = 10
	// 当current_lap < TOTAL_LAPS 为真时一直跑下去




	// 当循环条件为true时执行循环 （1 < 10)
	// 为false时停止循环 （ 10 < 10) 此时跳出循环
	// 若无计次 即无current lap++; 则执行死循环，持续执行第0圈

	// 循环五大条件：初始化 判断 循环体 迭代 终止

	// 迭代: 当执行到某一程序时 停止执行下方程序 重新回到第一行 称为迭代



	// (一）
	// 自动贩卖机
	// 要求：这个机器只支持1，2，5元硬币
	// 假设只卖一种饮料，每瓶$5元，用户只需要一直投币，直到金额足够，这样机器才可以提供饮料

	// 1.初始化
	const uint32_t PRICE = 5;  // price 饮料的价格 常数

	uint32_t balance = 0;  // 用户当前投入的总金额 计次迭代

	uint32_t coin; // 每次投入的硬币

	// 提示语
	puts("欢迎使用自动贩卖机！本机只提供一种饮料，价格是$5");

	puts("请投币（只接受1，2，5元三种硬币）:");

	// 2.处理循环的条件
	// 什么情况下会一直投币 只要钱不够就要一直投
	// balance < PRICE (PRICE为5）

	while (balance < PRICE) {
		puts("钱不够，请投币：");

		// 模拟投币。用户输入，假设投币成功，假设用户输入金额就是投币
		// 输入端
		scanf_s("%" PRIu32, &coin);

		// 每次检查投币是否有效 （1，2，5元硬币）
		if (coin == 1 || coin == 2 || coin == 5) {
			balance += coin;  // balance = balance + coin
			printf("您已经投入了$%" PRIu32 "\n", balance);
		}
		else {
			printf("对不起，我们不接受$%" PRIu32 "\n", coin);
		}

		// 当 balance < PRICE 为 false时 即投入硬币达到了$5，停止循环 
	}

	// 找零 （在循环体外面）
	// eg. 假设第一次投入2元 第二次投入5元 共7元 > 5元 但多投了2元

	if (balance > PRICE) {
		printf("请收好找零 $%" PRIu32 "\n", balance - PRICE);  // =2
	}

	puts("谢谢用户，请取走您的饮料！");

	// 在输入端进行投币




	// 当遇到不好排查，有逻辑有意义，有检查，有循环的地方->使用printf->清晰知道已经写到了这步 若输入错误则可找到错误位置

	// 该循环为输入端循环，即调试后printf将被输出在输入端可见

	// printf("---测试");


	// 循环体内尽可能少计算，循环尽可能展开写




	// (二)
	// 协议供货计算求整数和的案例
	// 用户从终端输入一系列数字，用回车隔开，直到用户输入一个单个0作为结束，然后把所有的数字相加，计算结果

	uint32_t suum = 0;        // 初始时 总数和为0

	uint32_t numBer = 1;     // 初始数字1 不能为0 为0则不执行循环直接结束循环

	puts("请输入一系列数字，用回车隔开，我们将计算他们的和，输入0结束");

	while (numBer != 0) {
		// != 不等于 当输入为0时判断为false 不执行循环

		printf("请输入一个数字：\n");

		scanf_s("%" PRIu32, &numBer);
		// scanf会把numBer重新赋值 从输入的地方重新给numBer赋值 当在输入端输入时 numBer被初始化为输入的值 
		// 此时uint32_t 就浪费掉了

		suum += numBer;       // sum = sum + numBer


		printf("所求的和为suum是 %" PRIu32 "\n", suum);
	}

	// 在输入端输入Q也可以退出




	// 如何利用死循环
	uint32_t summ = 0;

	uint32_t numBber;    // numBer不赋值

	puts("请输入一系列数字，用回车隔开，我们将计算他们的和，输入0结束");

	while (true) {      // 设置为一直判断为true 则循环一直进行

		printf("请输入一个数字：\n");

		scanf_s("%" PRIu32, &numBber);

		// 该处加入
		if (numBber == 0) {
			break;
			// break 为提前打破，打断循环，跳出  break权限大
		}

		summ += numBber;

		printf("所求的和为summ是 %" PRIu32 "\n", summ);
		// 当输入数字0时，停止循环
	}



	// do while和while区别
	// while：先进行判断条件，检查条件是否为true再执行，如果不满足则不执行
	// do while：先不检查，执行一遍，再检查条件，条件满足则继续跑，不满足则不跑
	// do while：无论条件真假，至少执行一次




	// do while
	// (一)
	// 游戏菜单案例

	uint32_t choice;

	do
	{
		// 显示菜单
		puts("****主菜单****");
		puts("1. 新游戏");
		puts("2. 载入游戏");
		puts("3. 退出");
		puts("4. 请选择一个选项：");
		scanf_s("%" PRIu32, &choice);

		// 处理用户的选择
		switch (choice)
		{
		case 1:
			puts("新游戏已经启动...");
			// 新游戏逻辑...TODO
			// 此处省略一万字
			puts("游戏已经玩完，返回菜单重新选择");
			break;
		case 2:
			puts("载入存档中...");
			puts("存档已经载入...");
			// 载入存档后的游戏逻辑...TODO
			// 此处省略一万字
			puts("游戏已经玩完，返回主菜单重新选择...");
			break;
		case 3:
			puts("感谢游玩，再见！");
			puts("游戏已经玩完，返回主菜单重新选择...");
			break;

		defaule:
			puts("无效选择，请重新选择！");
		}
	} while (choice != 3);         // 只要用户不输入3，就一直循环




	// (二）
	// 随机数猜数游戏规则
	// 第十 十一个头文件 #include <time.h>    #include <stdlib.h>

	// 具体内容放在了 c two



	// continue 
	// 跳过本次循环中的剩余部分
	// 进行数据筛选

	uint32_t ssum = 0;
	int32_t number_11;

	puts("请输入一系列正整数来计算他们的和");
	puts("可以输入负数,但它们不会被加入到总和之中");
	puts("输入0以结束输入并显示出总和");

	while (1) {
		puts("请输入一个数字：");
		scanf_s("%d", &number_11);

		if (number_11 == 0) {
			break;                // 循环终止
		}
		if (number_11 < 0) {
			continue;             // 跳过本次循环中的剩余部分
			// 当输入数字小于0时 不再执行该行后的循环，重新返回puts("请输入一个数字：");
		}

		ssum += number_11;
	}



	// 案例
	/*
		加入要处理一系列数字，忽略负数和大于100的数，只能处理0-100的数
		对于每一个有效数字，如果是偶数，打印一条消息并且告知它是偶数
		若是奇数，打印一条语并且告知它是奇数
		用户输入-1则结束程序
	*/
	int32_t number_12;

	puts("请输入数字(0-100),输入-1后结束程序");

	while (1) {
		puts("请输入一个数字：");
		scanf_s("%d", &number_12);

		// 检查退出条件
		if (number_12 == -1) {
			break;
		}

		// 判断跳过所有的负数和大于100的数
		if (number_12 < 0 || number_12 > 100) {
			continue;    // 跳过本次循环的剩余部分
		}

		// 处理有效数字
		if (number_12 % 2 == 0) {
			// 偶数
			printf("%" PRId32 "是偶数.\n", number_12);
		}
		else {
			// 奇数
			printf("%" PRId32 "是奇数.\n", number_12);
		}
	}

	puts("程序结束！");
	return 0;
}