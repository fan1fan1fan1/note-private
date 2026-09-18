#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h> 
#include <time.h>
#include <stdlib.h>


// 爱心代码
#include<string.h> 
#include<float.h>
#include<windows.h>


#include <stdbool.h>
// 函数 模拟组件的健康检查
bool check_component_health(uint32_t component_id);


// 五子棋
#define board_size   15
#include <math.h>
#include <ctype.h>
#include <wchar.h>
#include <locale.h>



int main(void)
{
	// 爱心代码
	system("color 0c");

	Sleep(200);

	float x, y, z;
	for (y = 1.5f; y > -1; y -= 0.1f)
	{
		for (x = -1.5f; x < 1.5f; x += .05)
		{
			z = x * x + y * y - 1;
			putchar(z * z * z - x * x * y * y * y < 0.0f ? 'x' : ' ');
		}
		Sleep(200);
		putchar('\n');
	}




	// 输入输出
	// 输入 scanf_s()

	printf("Please input a number:\n");

	int number;

	scanf_s("%d", &number);

	printf("%d", number);


	// 在scanf中 &意为取地址 用于读取变量的地址 以便scanf函数能正确地将输入的值存储到对应的变量中



	int number1, number2, number3;

	scanf_s("%d %d %d", &number1, &number2, &number3);

	printf("Your number is = %d %d %d", number1, number2, number3);

	printf("Your number is = %d + %d + %d", number1, number2, number3);

	// 进入输出窗口后 可根据格式输入 然后回车



	char name[50];

	scanf_s("%s", name, 50);

	printf("Your name is %s\n", name); // 弹出窗口后输入名字



	// scanf 不安全 企业不建议 使用下方头文件
	// 第九个头文件 #define _CRT_SECURE_NO_WARNINGS  写在#include <stdio.h>前面  crt_secure_no_warnings
	int age;

	printf("请输入你的年龄：\n");

	scanf_s("%d", &age);

	printf("age = %d\n", age);



	printf("hello world");
	// 引用了scanf_s()后代码不能输出 只能输入




	// 案例 检查组件障碍 选修
	const uint32_t total_components = 5;  // 系统有5个组件

	srand(time(NULL));                    // 假设该组件损坏

	puts("开始健康检查...");

	for (uint32_t i = 0; i < total_components; i++) {
		printf("检查组件 %" PRIu32 "...", i + 1);

		if (check_component_health(i + 1)) {
			printf("组件 %" PRIu32 "状态良好.\n", i + 1);
		}
		else {
			printf("组件 %" PRIu32 "出现故障.\n", i + 1);

			// 在实际应用中，这里会处理错误，比如警告或是尝试修复方案或者是列举修复方案进行选择
		}
	}

	puts("健康检查已完成！");
	// 结果随机生成

	// 调试输出
	// 跟踪循环的执行情况，监测每一个循环变量的变化

	// 下方return 0 后的函数 跟着这部分







	// 案例 绘制五子棋棋盘
	// 引用第十四 十五个头文件 #include <wchar.h> #include <locale.h>


	// 要求
	// 设置控制台代码页为 UTF-8 (选修）
	SetConsoleOutputCP(65001);

	// 设置区域为系统默认
	setlocale(LC_ALL, "");



	// 用 wchar_t 代替 char
	// 棋盘大小
	wchar_t board[board_size][board_size];

	// 五子棋坐标
	uint32_t x1, y1;


	// 状态 定义一个玩家使用⚪ 

	// 使用 ⚪ 的方式  十六进制 0x25CF
	// 使用  ●  的方式  十六进制 0x00B7

	wchar_t current_player = 0x25CF;


	// 使用for循环画出一个正方形棋盘
	// 初始化 此时棋盘上没有棋子
	// 在后面的使用中每一次进行下棋操作都需要 清屏+打印棋盘 但不能输入board[i][j] = 0x00B7
	for (uint32_t i = 0; i < board_size; i++) {

		for (uint32_t j = 0; j < board_size; j++) {
			board[i][j] = 0x00B7;
		}
	}


	wchar_t control = L'y';   // L用于表示wchar类型 所有的wchar都以L开头 格式固定

	while (control == L'y' || control == L'Y') {
		// 控制面板 进行变化
		// 当按下y时继续下 当按下n使停止 游戏结束

		system("cls");        // 清屏效果

		// 制作一个棋盘并打印
		for (uint32_t i = 0; i < board_size; i++) {

			for (uint32_t j = 0; j < board_size; j++) {
				board[i][j] = 0x00B7;

				// 打印方式
				wprintf(L"%lc ", board[i][j]);
			}

			wprintf(L"\n");
		}

		wprintf(L"玩家 %lc 请输入坐标(0 - %d) , 中间用空格隔开:\n", current_player, board_size - 1);

		// 若输入值大于棋盘大小 则:
		if (scanf_s("%" PRIu32 "%" PRIu32, &x1, &y1) != 2) {

			while (getchar() != '\n');

			wprintf(L"输入无效请重新输入。\n");

			system("pause");

			continue;
		}

		// 若有位置（1.无坐标，2.且在范围内），即无棋子，该位置可下棋子 :
		if (x1 < board_size && y1 < board_size && board[x1][y1] == 0x00B7) {
			board[x1][y1] = current_player;

			// 切换玩家
			current_player = (current_player == 0x25CF) ? 0x25CB : 0x25CF;
			//   如果目前玩家是⚪   为真    则切换为●  若为假则切换为⚪
		}
		else {
			// 若判断结果为else说明要么该位置已经有棋子 或是该位置不在范围内
			wprintf(L"无效的移动请重试");
			system("pause");
			continue;
		}

		// 再次清屏
		system("cls");

		// 再次打印棋盘
		for (uint32_t i = 0; i < board_size; i++) {

			for (uint32_t j = 0; j < board_size; j++) {
				wprintf(L"%lc ", board[i][j]);
			}
			wprintf(L"\n");
		}

		wprintf(L"是否继续？(y / n");
		while (getchar() != '\n');    // 清空输入缓冲
		wscanf_s(L"%lc", &control, 1);
	}
	wprintf(L"游戏结束！\n");



	srand((unsigned int)time(NULL));    // 时间作为随机因子
	// 随机餐谱
	int choise = (rand() % 10 + 1);     // 以时间作为随机数字
	switch (choise)
	{
	case 1:printf("今天吃茶香鸡\n"); break;
	case 2:printf("今天吃二楼汉堡\n"); break;
	case 3:printf("今天吃花甲粉\n"); break;
	case 4:printf("今天吃木桶饭\n"); break;
	case 5:printf("今天吃麻辣烫\n"); break;
	case 6:printf("今天吃面条\n"); break;
	case 7:printf("今天吃煎饼\n"); break;
	case 8:printf("今天吃烤盘饭\n"); break;
	case 9:printf("今天吃小笼包\n"); break;
	case 10:printf("今天吃滑蛋饭\n"); break;
	}



	// 库函数
	// 怎么编写头文件 （难）
	// 初步制作一个简易游戏

	/*
		我们需要创建头文件使用结构体包含游戏的角色    game_types.h
		我们需要在资源文件中使用联合包含不同角色的能力和属性
			 使用联合可以将不同数据类型定义在同一个内存地址上，节省内存空间    创建一个头文件   game_abilities.h
		我们需要创建一个头文件，包含一个结构体，将以上内容嵌套到一起   game_struct.h
	*/












	// (二）
	// 随机数猜数游戏规则
	// 第十 十一个头文件 #include <time.h>    #include <stdlib.h>

	uint32_t secret_num, guess;

	// 生成随机数 库函数
	srand(time(NULL));

	// 生成1-100的随机数
	secret_num = rand() % 100 + 1;

	puts("猜猜我想的是哪一个数？（1-100）？");

	do {
		puts("请输入你的猜测：");

		scanf_s("%d", &guess);

		if (guess < secret_num) {
			puts("大傻逼！太小了，再试试看！");
		}
		else if ("guess > secret_num") {
			puts("大傻逼！太大了，再试试看！");
		}
	} while (guess != secret_num);

	printf("恭喜大傻逼！猜对啦！答案是%" PRIu32 "\n", secret_num);

	return 0;
}


// 引用函数 
bool check_component_health(uint32_t component_id) {

	// 在实际应用中，这里真的可能会发送网络请求或者是执行检查的复杂操作
	// 我们这里就简单模拟一下 假设所有的组件偶尔都会有故障

	if (rand() % 10 < 2) {     // 20%
		return false;
	}

	return true;
}