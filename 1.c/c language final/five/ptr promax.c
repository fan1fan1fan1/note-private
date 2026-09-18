#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>   // 不知到第多少个头文件 用于写字符串型
#include <errno.h>    // 同 用于处理c引入文件时对错误的处理

// void 只通过指针改变数据内容 不返回东西

// 使用指针修改数据值 并传递修改后的函数值
void add_ten_by_value(int32_t* value);


// 使用指针修改函数值后返回指针案例
// 员工薪资管理系统
	// define 定义方法 #define 函数名 数据个数
#define EMPLOYEES_COUNT 5

// 函数名中包含形参变量 EMLOYEES_COUNT为常量 不能写在函数名里 -> size
// 函数中形参不能只写变量名 要标明数据类型
// 1.批量涨工资
void update_salary(uint32_t* salaries, size_t size, uint32_t increment);   // 此处size_t size = 5 员工数量

// 输出函数
void print_emp(uint32_t* salaries);

// 2.计算并返回年终奖
uint32_t calc_bonus(uint32_t salary);

// 3.查询最高工资员工 并返回其地址
uint32_t* find_highest_salary(const uint32_t* salaries);


// 玩家获取经验等级提升
void increment_exp(int32_t* palyer_exp, int32_t amount);  // amount 为玩家每次增加经验值

// 检查玩家等级提升
bool check_level_up(int32_t* exp, int32_t* level);

#define EXP_PER_LEVEL 100   // 设置当经验值为100时提升一个等级
#define MAX_LEVEL 10        // 设置最高等级为10	
#define HINTS_COUNT 10      // 宝藏提示的数量 

const char* get_treasure_hint(int32_t player_level);   // 当玩家升级时获得宝藏 宝藏数量固定 const


// 更新分数
void update_score(int32_t* score, int32_t points);   // point为每次更新的改变量

// 比较玩家分数 输出最高得分者 
int32_t* compare_score(int32_t* score1, int32_t* score2);

// 分数倍增
void double_score(int32_t* score);


int main(void) {

	// 指针访问多维数组
	int matrix[2][3] = {    // 定义一个二维数组
		{1,2,3},
		{4,5,6}
	};

	int(*ptr)[3] = matrix;   // 长度为3的一个一维指针数组

	// (*ptr)[3] : ptr是一个指针，它指向一个包含3个int元素的一维数组中的指针 -> {1，2，3}的地址
	// 一维数组->首数据地址   二维数组->第一行地址(指向一个一维数组)  第一行数据有三个 因此 (*ptr)[3]

	// 若不加括号 int*ptr[3] -> 声明了三个指针 一个指针的一维数组

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			{
				printf("%d ", ptr[i][j]);
			}
		}
		printf("\n");
	}



	// 指针数组
	int32_t department1[] = { 1001,1002,1003 };   // 第一个部门的员工id
	int32_t department2[] = { 2001,2002 };
	int32_t department3[] = { 3001,3002,3003,3004 };

	/*
	 int32_t* p1 = &department1;
	 int32_t* p2 = &department2;
	 int32_t* p3 = &department3;
	*/
	int32_t* department_ptrs[3] = { department1, department2, department3 };

	size_t department_size[3] = { sizeof(department1) / sizeof(int),
		sizeof(department2) / sizeof(int),
		sizeof(department3) / sizeof(int),
	};



	// 打印所有员工
	for (size_t i = 0; i < 3; i++) {
		printf("Department %zu: ", i + 1);

		for (size_t j = 0; j < department_size[i]; j++) {
			printf("%" PRId32 " ", department_ptrs[i][j]);
		}
		printf("\n");
	}



	// 函数值的传递(Pass by value)
	// 地址传递(Pass by Reference)
	int32_t my_value = 5;

	printf("原本的值: %" PRId32 "\n", my_value);

	// 修改函数值
	// 引用函数
	add_ten_by_value(&my_value);   // 直接在地址上作用 进行修改

	printf("已经调用add: %" PRId32 "\n", my_value);
	// 直接调用函数并不能修改my_value的值 在函数执行完毕后 数据生命周期结束 不能进行输出 此时使用指针地址传递
	// 在函数中对my_value的地址进行修改 再返回给my_value 

	// 通过函数中的指针进行外部服务 主体中调用时使用& 函数中调用(函数名)使用*



	// 调用了地址后需要返回地址 
	// 案例一
	/*
		员工薪资管理系统

		1.批量涨工资
		2.计算并返回员工的年终奖
		3.查找最高薪资员工
	*/
	uint32_t salaries[EMPLOYEES_COUNT] = { 3000,3500,4000,5000,5500 };

	uint32_t increment = 10000;  // 1.所有员工涨工资

	// update   函数
	// 想要改变员工工资 在函数中 使用指针 修改数组中参数地址 此时变量应为数组的地址
	update_salary(&salaries[0], EMPLOYEES_COUNT, increment);

	// 若不加设&salaries[0]  只使用salaries -> 只传递了数组首地址 不能大范围批量更改数组值
	// int* p = salaries;  ===  int* p = &salaries[0];

	print_emp(salaries);

	uint32_t* highest_salary = find_highest_salary(salaries);
	// 2.计算并返回员工的年终奖
	printf("最高薪资的年终奖是: %" PRIu32 "\n", calc_bonus(*highest_salary));

	// 3. 查找最高薪资员工
	printf("最高薪资是: %" PRIu32 "\n", *highest_salary);



	// 案例二 
	/*
		游戏概念
		1.玩家属性: exp level

		2.解密:

		3.等级提升:

		4.游戏目标:
	*/

	int32_t player_exp = 0;            // 玩家经验值
	int32_t player_level = 1;          //  玩家等级

	// 指针函数 玩家获取经验后提升等级 
	increment_exp(&player_exp, 50);
	increment_exp(&player_exp, 75);    // 假设解密后增加经验值75+25=100 

	// 检查增加经验后是否能增加等级
	if (check_level_up(&player_exp, &player_level)) {

		// 返回值为是否玩家等级提升 使用bool
		// 若玩家成功升级 则获得宝藏
		printf("%s\n", get_treasure_hint(player_level));
	}
	else {
		printf("还需要更多的经验才能升级!\n");
	}



	// 案例三
	// 更新分数
	int32_t player1_score = 100;
	int32_t player2_score = 150;

	// 改变player1的分数
	update_score(&player1_score, 50);

	// 将两个玩家的分数进行比较
	int32_t* higher_score = compare_score(&player1_score, &player2_score);
	printf("较高的分数是:%" PRId32 "\n", *higher_score);

	// 分数倍增 设置将玩家2的分数翻倍
	double_score(&player2_score);

	return 0;
}

void add_ten_by_value(int32_t* value) {
	// 要保存地址 使用 * 保存地址

	// 要拿到数据本身 * + 变量名
	*value += 10;

	// value += 10 将数据往前往后挪十位
	// *value += 10 将数据内部数字加十
}



void update_salary(uint32_t* salaries, size_t size, uint32_t increment) {

	for (size_t i = 0; i < EMPLOYEES_COUNT; ++i) {
		salaries[i] += increment;  // 数据内部更改 salaries = 原salaries + increment
	}
}

void print_emp(uint32_t* salaries) {
	// 只输出员工工资修改后的工资 则函数名后只有salaries

	for (size_t i = 0; i < EMPLOYEES_COUNT; ++i) {
		printf("%d ", salaries[i]);
	}
	printf("\n");
}


uint32_t calc_bonus(uint32_t salary) {
	return salary / 10;
}

uint32_t* find_highest_salary(const uint32_t* salaries) {

	const uint32_t* highest = salaries;

	for (size_t i = 1; i < EMPLOYEES_COUNT; ++i) {
		// 先假设第一个数据值为最大 依次将每个值与第一个值比较 若小则不变 若大则取代该值

		if (salaries[i] > *highest) {
			highest = &salaries[i]; // 取代该值
		}
	}

	return (uint32_t*)highest;
	// 返回指针时 对数据类型加括号() 否则有语法错误 报错 能够确保优先级正确 不会被误视为乘号*
}



// 玩家获取经验提升等级
void increment_exp(int32_t* exp, int32_t amount) {
	*exp += amount;
}

// 检查玩家等级是否提升
bool check_level_up(int32_t* exp, int32_t* level) {

	while (*exp >= EXP_PER_LEVEL && *level < MAX_LEVEL)
	{
		*exp -= EXP_PER_LEVEL;   // 计算提升的等级
		(*level)++;
		printf("恭喜你升级到了%" PRId32 "级!\n", *level);
		return true;
	}
	return false;  // 没有提升等级
}

// 获得宝藏 
// 输出固定的宝藏数量 及宝藏提示
const char* get_treasure_hint(int32_t player_level) {

	static const char* hints[HINTS_COUNT] = { "宝藏二的提示", "宝藏三的提示..." };

	if (player_level > 0 && (size_t)player_level <= HINTS_COUNT) {
		// size_t 加括号 (size_t)

		return hints[(size_t)player_level - 1];
	}
	return "未知提示: 请确保你在等级的有效范围内才能解锁宝藏提示!";
}



// 更新分数
void update_score(int32_t* score, int32_t points) {
	*score += points;

	printf("当前分数: %" PRId32 "\n", *score);
}

// 比较两个玩家分数 输出最高得分者
int32_t* compare_score(int32_t* score1, int32_t* score2) {

	return(*score1 > *score2) ? score1 : score2;
	// 条件加括号()
}

// 分数倍增
void double_score(int32_t* score) {
	*score *= 2; // score = score原来 * 2
	printf("翻倍后分数: %" PRId32 "\n", *score);
}

