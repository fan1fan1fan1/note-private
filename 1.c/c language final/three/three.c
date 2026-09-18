#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdbool.h>
#include <math.h>
#include <windows.h>
#include <time.h>

#include <ctype.h>
#include <wchar.h>
#include <locale.h>
// 下一个是第16个



// 局部常量 局部宏定义 全局宏定义
#define SIZE
#define STUDENT_COUNT 5 
#define DAYS_IN_WEEKS 7
#define ACCOUNT_COUNT 3
#define CANDIDATE_COUNT 4
#define LETTER_COUNT 26
#define MAX_SIZE     10
#define board_size   15

#define N 10


// 函数

// 先声明 后定义
void loop_i();
void print_line();
// 按住ctrl不放 点击函数名称 可跳转到函数位置

void greet(int age, bool gender);
// 函数的参数

// void 没有类型返回 不用写return
// int 需要返回值

// 函数的返回值
void add(int num1, int num2);

// 若需要函数的返回值 需定义int. 
int add1(int num1, int num2);

#define PI 3.14
// 函数声明
double square_area(double side);
double rectangle_area(double length, double width);
double circle_area(double redius);

// 判断闰年还是平年
int is_leap_year(int year);


// 石头剪刀布 游戏选项
#define ROCK 1
#define PAPER 2
#define SCISSORS 3

void print_instructions();
uint32_t get_player_choice();
uint32_t get_computer_choice();

void print_choice(uint32_t choice);

void determine_winner(uint32_t player_choice, uint32_t computer_choice);


// 表驱动法
#define MONTH_COUNT 12
int get_days_in_month(int month, int year);
// 函数将传递一个月份，返回一个月份有多少天的结果

// 判断闰年还是平年 此处直接引用上方输入过的


// 成绩评分系统
#define GRADE_COUNT 11
char get_grade(int score);




int main(void)
{



	// wchar.h 宽字符
	// locale.h 本地化函数
	// ⭕ ● 引用空心圆和实心圆
	// 中文使用的编码 GBK 

	// Unicode 万国码 可以表示任何语言


	// 案例 绘制五子棋棋盘
	// 引用第十四 十五个头文件 #include <wchar.h> #include <locale.h>
	// c two




	// 函数 functions 功能块

	// 提取重复的代码 节省内容和效率
	// main是所有函数的入口点 
	// 模块化 功能抽离 达到复用性


	// 在int main 前使用void loop_i() --内容
	// 直接输入 loop_i();
	loop_i();
	loop_i();

	// 调用函数
	print_line();


	// 传递函数 函数的参数  

	// 实际参数 调用使
	greet(18, 1);
	greet(20, 0);

	// 形式参数和实际参数   假设 void momney()
	// 形式参数为画饼 实际参数为实际金钱 

	// 调用函数时 函数首先把输入的实际参数 放到形式参数中输出结果 再将结果返回到原函数 进行下一步操作

	// 函数的返回值
	add(7, 8);        // 15
	add1(7, 8);      // 15
	int num1 = add1(7, 8);

	printf("num1 = %d\n", num1);



	// 案例 求面积函数
	double side = 5.0;                     // 正方形边长

	double length = 10.0, width = 7.8;     // 长方形的长宽

	double redius = 3.5;                   // 圆的半径 

	square_area(6.0); // 36

	printf("%lf\n", square_area(6.0));
	printf("%lf\n", rectangle_area(15.0, 10.0));
	printf("%lf\n", circle_area(3.0));



	/*
		函数编写要领

		1.明确函数目的 明确它的功能将帮助你决定哪些输入是必须的 (形式参数模板)， 以及如何报告它的工作结果

		2.识别所需要的输入

		3.确定函数的输出

		4.使用适当的数据类型

		5.函数的命名清晰，并且先声明后定义
	*/


	// 判断是否为闰年
	int year = 2023;
	printf("%d年%s\n", year, is_leap_year(year) ? "是闰年" : "不是闰年");

	// 建议每个函数只做一件事情



	 /*
		全局变量

		局部变量

		作用域

	 */

	int year1 = 2024;
	// 此处int只能在main中使用 属于局部变量 作用域为main

	// 若该int写在main的平级 和函数声明放在一起 写在main外 属于全局变量
	// #define 全局宏定义 全局常量

	for (int i = 0; i < 10; i++) {
		// 此处的int为作用域  作用域为for
	}



	// 案例 石头剪刀布  与软件工程的规则映射设计技巧

	// 方法一 旧方法
	// 初始化随机数生成器
	srand(time(NULL));  // 随机数

	// 打印游戏说明
	puts("石头、剪刀、布游戏开始！");
	puts("规则: 输入数字，确定猜拳。 1是石头，2是布，3是剪刀:\n");
	puts("=============================================================");

	// 获取玩家和计算机选择
	/*
		uint32_t player_choice;
		uint32_t computer_choice;

		uint32_t choice;
		printf("请选择1石头，2布，3剪刀: \n");
		scanf_s("%d", &choice);

		while (choice < ROCK || choice > SCISSORS) {
			printf("无效选择! 请重新选择: 1石头， 2布，3剪刀:\n");
			scanf_s("%d", &choice);
		}
	*/

	// 方法二 使用函数

	// 初始化随机数生成器
	srand(time(NULL));  // 随机数

	// 打印游戏说明
	print_instructions();

	// 获取玩家和计算机的选择
	uint32_t player_choice = get_player_choice();
	uint32_t computer_choice = get_computer_choice();

	// 展示玩家和计算机的选择
	puts("你选择了");
	print_choice(player_choice);
	puts("计算机选择了");
	print_choice(computer_choice);

	// 判断确定赢家 并展示
	determine_winner(player_choice, computer_choice);



	// 表驱动法
	// 定义一个月份 根据月份输出相应的结果
	int res_day = get_days_in_month(12, 2023);
	printf("%d\n", res_day); // 输出结果为天数

	printf("grade: %c\n", get_grade(100));


	return 0;
}



// 函数

// 函数的定义
void loop_i() {

	// 函数体
	for (int i = 0; i < 5; i++) {
		printf("iiii\n");
	}
}

/*
	void     无参数   void X()
	int ...  有参数   int X(int x)

	return 有返回值
	printf 无返回值
*/


void print_line() {
	printf("hello!\n");
}



void greet(int age, bool gender) {
	// 参数列表 形式参数 定义声明使
	printf("您的年龄为:%d, 您的性别是: %s\n", age, gender ? "男" : "女");
}



void add(int num1, int num2) {
	printf("sum = %d\n", num1 + num2);
}

int add1(int num1, int num2) {

	// printf("sum = %d\n", num1 + num2);

	return num1 + num2;
	// 返回值是数字时 使用return

	// 返回值是字符使 使用char    char 'c'

}



double square_area(double side) {
	return side * side;
}
double rectangle_area(double length, double width) {
	return length * width;
}
double circle_area(double redius) {
	return redius * redius * PI;
}



// 判断闰年还是平年
int is_leap_year(int year) {
	// return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);

	if (year % 400 == 0) {
		return 1;  // 对400取余等于1
	}
	else if (year % 100 == 0) {
		return 0;  // 对100取余等于0
	}
	else if (year % 4 == 0) {
		return 1;  // 对4取余等于1
	}
	else {
		return 0;
	}
}



void print_instructions() {
	// 打印游戏说明
	puts("石头、剪刀、布游戏开始！");
	puts("规则: 输入数字，确定猜拳。 1是石头，2是布，3是剪刀:\n");
	puts("=============================================================");
}

uint32_t get_player_choice() {

	uint32_t choice;
	printf("请选择1石头，2布，3剪刀: \n");
	scanf_s("%d", &choice);

	while (choice < ROCK || choice > SCISSORS) {
		// 只能选择 1 2 3 中一种 不能出现一种既小于石头 又大于剪刀的选项

		printf("无效选择! 请重新选择: 1石头， 2布，3剪刀:\n");
		scanf_s("%d", &choice);
	}
	return choice;
}

uint32_t get_computer_choice() {

	return (rand() % (SCISSORS - ROCK + 1)) + ROCK;
	// 定义电脑输出一种随机数 这个数是 1 2 3中其中一种
}

void print_choice(uint32_t choice) {

	// 定义了一种使用switch else的循环判断结果
	switch (choice) {
	case ROCK: puts("石头"); break;
	case PAPER: puts("布"); break;
	case SCISSORS: puts("剪刀"); break;

	default:
		break;
	}
}

void determine_winner(uint32_t player_choice, uint32_t computer_choice) {

	if (player_choice == computer_choice) {
		puts("平局!");
	}
	else if ((player_choice == ROCK && computer_choice == SCISSORS) || (player_choice == PAPER && computer_choice == ROCK) || (player_choice == SCISSORS && computer_choice == PAPER)) {
		// 石头赢剪刀 或 布赢石头 或 剪刀赢布
		puts("获胜!");

	}
	else {
		puts("失败!");
	}
	// 使用了较为复杂的逻辑判断 	



	// 优化方式  软件工程规则映射设计技巧
	// 规则映射
	// 创建一个规则映射 减少复杂条件
	if (player_choice == computer_choice) {

		// 卫语句
		puts("平局!");
		return;
	}

	// 定义一个胜利的规则而映射，其中键是玩家的移动，值是玩家可以打败计算机的移动

	uint32_t               s[4] = { 0, ROCK, SCISSORS, PAPER };  // 玩家输入的获胜规则
	uint32_t winning_choices[4] = { 0, SCISSORS, PAPER, ROCK };  // 电脑输入的获胜规则

	// 数组妙用             剪刀索引值1 当索引为1时 输出结果为ROCK石头 即获胜
	// 其中0是占位符

	// winning_choices[1] SCISSORS
	// ROCK == 1    即石头赢剪刀

	if (computer_choice = winning_choices[player_choice]) {
		// ⬆索引为1时输出为SCISSORS剪刀    此时⬆输出结果为1即ROCK石头 石头赢剪刀
		puts("你赢了!");
	}
	else {
		puts("你输了!");
	}
}



int get_days_in_month_ifelse(int month, int year) {

	// 此处也可以使用 switch else
	if (month < 1 || month > 12) {
		return -1;   // 无效输入
	}
	else if (month == 1) {
		return 31;
	}
	else if (month == 2) {

		if (is_leap_year(year)) {
			return 29;
		}
		else {
			return 28;
		}
		// 此处需要判断闰年还是平年 引用一个函数进行判断
	}
	else if (month == 3) {
		return 31;
	}
	else if (month == 4) {
		return 30;
	}
	else if (month == 5) {
		return 31;
	}
	else if (month == 6) {
		return 30;
	}
	else if (month == 7) {
		return 31;
	}
	else if (month == 8) {
		return 30;
	}
	else if (month == 9) {
		return 31;
	}
	else if (month == 10) {
		return 30;
	}
	else if (month == 11) {
		return 31;
	}
	else if (month == 12) {
		return 30;
	}



	// 优化方法
	return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

// 上一个函数的优化方法 表驱动法
int get_days_in_month(int month, int year) {
	const int days_in_month[MONTH_COUNT] = {
		31,
		is_leap_year(year) ? 29 : 28,
		31,30,31,30,31,30,31,30,31,30

		// 此处对二月的函数进行逻辑运算符判断 如果是真 返回29天 如果是假 返回28天 
	};

	// 增加一个范围 条件 无效月份
	if (month < 1 || month > MONTH_COUNT) {
		return -1;
	}

	return days_in_month[month - 1];
	// 一到十二月 索引值为0-11 此处索引值为 月份 - 1
}



// 表驱动法 
// 使用数据结构(array, hash)
// 使用数组 数组就是一种表
// 来替代复杂的逻辑语句

// 核心思想: 许多程序可以通过查表来确定，而不是通过复杂的条件语句

// 1. 识别：确定程序中可以用查表代替的逻辑部分
// 2. 设计：创建包含所有可能输入和对应输出的表(数组或Hash)
// 3. 实现：编写代码，使用输入作为索引或键来查找表中的对应输出
// 4. 优化：根据需要，调整表的结构以提高效率或者可读性



char get_grade(int score) {
	// 90 A
	// 80 B
	// ...
	// 60 F

	// 1.识别 分数和等级 
	// 2.设计 等级内容对应
	const char grades[GRADE_COUNT] = { 'F','F','F','F','F','F','D','C','B','A','A' };
	// 0-9 10-19 20-29 30-39 40-49 50-59 -> F    最后一个A为99 若输入成绩为100 则输出A 即需要增加一个A 数组中两个A

	// 增加一个条件 范围 要求分数必须大于0
	if (score < 0 || score > 100) {
		return 'X';
	}

	// 3.编写 
	return grades[score / 10];
	// 当输入值为90时 score/10 -> 9 'A'
	// 当输入值为91时 score/10 -> 9 'A'  int类型为整数 省略小数位 
}
