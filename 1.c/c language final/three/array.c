#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

#define SIZE
#define STUDENT_COUNT 5 
#define DAYS_IN_WEEKS 7
#define ACCOUNT_COUNT 3
#define CANDIDATE_COUNT 4
#define LETTER_COUNT 26
#define MAX_SIZE     10
#define board_size   15

#define N 10

int main(void) {
	// 计算机系统/编程语言要考虑的三大因素：1.数据组织 2.资源优化 3.性能管理

// 数组
// 最基础的数据管理，资源优化，性能管理的方式



// 初始化
	uint32_t numbers[10] = { 1,2,3,4,5,6,7,8,9,10 };
	// 数组中元素编号从0开始   0 1 2 3 4 5 6 7 8 9



	// 或者不定义元素
	uint32_t numbers_2[10];



	// 下标 index 即每个数组元素的索引号

	numbers[0];  // 将数组中中'0'取出

	printf("%" PRIu32 "\n", numbers[0]);   // 输出结果为1



	// 输出整个数组
	for (uint8_t index = 0; index < 10; index++) {

		// index = 0从0开始输入第一个数组; 一共10个数 ; 输出后进行下一位

		printf("%" PRIu32 "\n", numbers[index]);
	}
	// 输出结果为1，2，3，4，5，6，7，8，9，10



	// 查看数组值
	numbers[2] = 3;



	// 案例 植物大战僵尸

	// 定义不同僵尸
	uint32_t regular_zombie = 1;        // 最普通的僵尸
	uint32_t conehead_zombie = 2;       // 路障僵尸   
	uint32_t bucket_head_zombie = 3;    // 木桶僵尸
	uint32_t flag_zombie = 4;           // 旗子僵尸
	uint32_t newspaper_zombie = 5;      // 报纸僵尸

	// 定义一个包含不同类型僵尸数组
	uint32_t zombies[5] = { regular_zombie, conehead_zombie, bucket_head_zombie, flag_zombie, newspaper_zombie };

	// 定义上场战斗植物
	uint32_t battle_plants[5] = { 6,7,8,9,10 };  // 假如6-10也是特定的植物，此处不一一描述 uint32_t sun_flower =6..

	// 定义可选择植物有10个
	uint32_t available_plants[10] = { 6,7,8,9,10,11,12,13,14,15 };


	printf("Zombies in the game (Type ids):\n");
	for (int i = 0; i < 5; i++) {
		printf("%" PRIu32 "\n", zombies[i]);
	}

	printf("\n Plants selected for battle in the game (Type ids):\n");
	for (int i = 0; i < 5; i++) {
		printf("%" PRIu32 "\n", battle_plants[i]);
	}

	printf("\nAvailable plants for selection (Type ids):\n");
	for (int i = 0; i < 10; i++) {
		printf("%" PRIu32 "\n", available_plants[i]);
	}



	// 数组定义时下标注意常量 数组长度问题 size

	uint32_t numbers_1[10];
	// 数组的长度 -> 10    

	// c语言中数组的长度为固定值 不是变量 不可变 只能为右值 不能为右值赋值后的左值
	// 也不能使用const定义 const编译的时候是变量，不以常量定义，定义后的值在局部函数中会固定下来 


	// 定义常量的方法 宏定义: 头文件 #define SIZE
	uint32_t numbers_3[SIZE] = { 1,2,3,4,5 };
	// 数组里面的1 2 3 4 5称为元素


	// numbers[0] 下标为0的数组 index 
	// 定义，初始化数组时长度都不能为变量 编译时数组长度固定且已知
	// index 索引号



	// 数组注意事项 (易发生错误类型)
	// 1. 越界访问  当size为5时 索引号0-4 输出时不能出现5 超出长度范围 number[0-4]

	// 2. 未初始化数组  数组必须初始化
	uint32_t uninit_array[5];                   // 此处错误 未初始化 应写 _array[5] = {balabala};

	// 3. 数组大小错误
	// uint32_t wrong_size_arr[-1];                此处错误 所有数组元素 size>0

	// 警告1. 部分初始化
	uint32_t part_init_arr[SIZE] = { 1,2 };     // 1,2,000000000

	// 提示: 总是初始化数组
	uint32_t number[SIZE] = { 0 };              // 00000000



	// 数组插入
	int i_Num[N + 1] = { 23, 45, 60, 67, 88 }, i_Insert;
	int i, j;
	printf("\n 请输入一个要插入的数: ");
	scanf_s("%d", &i_Insert);

	for (i = 0; i < N; i++) {        // 寻找要插入的位置
		if (i_Num[i] > i_Insert) {
			break;
		}
	}
	for (j = N; j > i; j--) {        // 从后向前移动元素
		i_Num[j] = i_Num[j + 1];
	}
	i_Num[i] = i_Insert;             // 插入

	printf("\n 插入后的数组元素: \n");
	for (i = 0; i < N + 1; i++) {
		printf("%d", i_Num[i]);
	}



	// 案例(一) 分数
	// 假如五个学生的成绩，我们需要计算平均成绩，找出最高分和最低分，排序

	uint32_t grades[STUDENT_COUNT] = { 85,92,88,96,79 };


	uint32_t sum = 0;
	uint32_t max_grade = grades[0];
	uint32_t min_grade = grades[0];


	puts("所有人的成绩单如下:");


	for (uint32_t index = 0; index < STUDENT_COUNT; index++)
	{
		printf("学生 %" PRIu32 "的成绩: %" PRIu32 "\n", index + 1, grades[index]);

		sum += grades[index];

		if (grades[index] > max_grade) {
			max_grade = grades[index];
		}
		if (grades[index] < min_grade) {
			min_grade = grades[index];
		}
	}

	double average = (double)sum / STUDENT_COUNT;

	printf("五个学生加在一起的总成绩为: %d\n", sum);
	printf("平均成绩: %.2f\n", average);
	printf("最高成绩: %d\n", max_grade);
	printf("最低成绩: %d\n", min_grade);



	// 案例(二) 天气
	// 要求: 计算一周七天气温 最高气温 最低气温 平均值
	uint32_t daily_temperatures[DAYS_IN_WEEKS] = { 22,22,19,16,21,20,18 };


	uint32_t sum1 = 0;
	uint32_t max_temp = daily_temperatures[0];
	uint32_t min_temp = daily_temperatures[0];


	puts("一周内每天的最高温度:");


	for (uint32_t index = 0; index < DAYS_IN_WEEKS; index++) {

		printf("第 %" PRIu32 "天: %" PRIu32 "°C\n", index + 1, daily_temperatures[index]);

		sum1 += daily_temperatures[index];

		if (daily_temperatures[index] > max_temp) {
			max_temp = daily_temperatures[index];
		}

		if (daily_temperatures[index] < min_temp) {
			min_temp = daily_temperatures[index];
		}
	}

	double average1 = (double)sum1 / DAYS_IN_WEEKS;
	printf("平均气温为: %.2f°C\n", average1);
	printf("最高气温为: %d°C\n", max_temp);
	printf("最低气温为: %d°C\n", min_temp);



	// 案例(三) 账户存款取款
	int32_t account_balances[ACCOUNT_COUNT] = { 1000,1500,2000 };

	int32_t total_assets = 0;


	puts("初始账户金额:");


	for (uint8_t index = 0; index < ACCOUNT_COUNT; index++) {
		printf("账户 %d: %" PRId32 "元\n", index + 1, account_balances[index]);
	}


	account_balances[0] += 5000;
	account_balances[1] -= 2500;


	puts("\n进行存款和取款操作后的账户金额:");


	for (uint8_t index = 0; index < ACCOUNT_COUNT; index++) {
		printf("账户 %d: %" PRId32 "元\n", index + 1, account_balances[index]);

		total_assets += account_balances[index];
	}

	printf("\n总资产: %" PRId32 "元\n", total_assets);



	// 案例(五) 候选班长投票
	uint32_t votes[CANDIDATE_COUNT] = { 0 };

	uint32_t total_votes = 0;

	uint32_t max_votes = 0;

	uint32_t winner = 0;           // 候选人的index下标索引

	votes[0] += 152;
	votes[1] += 200;
	votes[2] += 149;
	votes[3] += 201;

	for (uint32_t index = 0; index < CANDIDATE_COUNT; index++) {
		total_votes += votes[index];

		if (votes[index] > max_votes) {
			max_votes = votes[index];

			winner = index;       // 更新获胜候选人的索引
		}
	}

	puts("各个候选人的票数: ");
	for (uint32_t index = 0; index < CANDIDATE_COUNT; index++) {
		printf("候选人 %d: %" PRIu32 "票\n", index + 1, votes[index]);
	}

	printf("\n总票数: %d\n", total_votes);
	printf("获胜候选人: 候选人 %d, 得票数: %d\n", winner + 1, max_votes);



	// 案例(六) 字母次数统计
	uint32_t frequency[LETTER_COUNT] = { 0 };

	char text[] = "Example text for frequently analysis.";   // 用于显示字母出现频率的例子

	// 统计每个字母出现的次数
	for (uint32_t i = 0; text[i] != '\0'; i++)
	{
		// 从索引0开始，只要当前字符text[i]不等于'0'就一直执行循环体

		char ch = tolower(text[i]);
		// tolower为c c++标准库中的函数 将大写字母转换为小写字母
		// 将text[i]转换为小写 句子首字母E计算在频率内

		if (ch >= 'a' && ch <= 'z')
		{
			// 判断ch是小写字母

			frequency[ch - 'a']++;   // 更新对应字母的频率 
			// 其中ch - 'a'的作用是将字母转换为对应在数组中的索引
		}
	}

	// 第十三个头文件 #include <ctype.h> 用于使用函数tolower() 将字母转化为小写



	// 隐式确定数组大小初始化

	// 当数组内元素清晰 且不发生变化使 可以不初始化 即隐式初始化   前提是每一个元素都可以被初始化
	uint32_t arr_1[] = { 1,2,3,4 };  // []内为4可不写

	// 如果访问索引号超出最大数组索引值 显示越界访问



	puts("字母频率:");
	for (uint32_t i = 0; i < LETTER_COUNT; i++) {
		if (frequency[i] > 0) {
			printf("%c: %d\n", 'a' + i, frequency[i]);
		}
	}




	// 数组知识汇总


	// 1.数组 Array
	uint32_t numbers_arr[MAX_SIZE] = { 0 };
	// 定义   数组名      头文件中     数组长度 初始化

	// 2.元素 Element 每一个格子里的数据

	// 3.下表 Index索引值 从0开始

	// 4.长度 Length 

	// 5.数组的内存分布 Memory Layout  所占内存

	// 6.遍历 将数组中每个值从第一个到最后一个都访问一遍 不一定输出 可能有其他操作 增删改查




	// 二维数组 有长宽 定义一个箱子
	uint32_t box_arr[5][5] = {
		{1,2,3,4,5},
		{2,3,4,5,6},
		{4,4,5,6,2},
		{3,5,6,2,2},
		{6,5,4,2,1}
	};

	box_arr[0][0];   // 1
	printf("%" PRIu32 "\n", box_arr[3][1]);  // 4

	// 遍历全部元素
	for (uint32_t i = 0; i < 5; i++) {

		// 定义了一个5*5的二维数组 行数为5 则i<5

		for (uint32_t j = 0; j < 5; j++) {

			// 列数为5 j<5

			printf("%" PRIu32 "\n", box_arr[i][j]);
		}

		printf("\n");
	}


	int a[][3] = { {1},{4, 5} };
	// 可以看出数组有两行 a[2][3]


	// 二维数组的插入
	int i, j, num[4][2];
	for (i = 0; i < 4; i++) {    // 控制行 小于行数
		for (j = 0; j < 2; j++) {   // 控制列数 小于列数
			scanf_s("%d", &num[i][j]);
		}
	}
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 2; j++) {
			printf("%d", num[i][j]);
		}
		printf("\n");
	}


	// 转置
	int a[2][3] = { {1, 2, 3}, {4, 5, 6} };
	int b[3][2], i, j;    // 定义一个转置的数组
	for (i = 0; i < 2; i++) {
		for (j = 0; j < 3; j++) {
			printf("%5d", a[i][j]);   // 输入原数组
			b[j][i] = a[i][j];        // 将行列换位置 赋值给b
		}
		printf("\n");
	}
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 2; j++) {     // 输出数组b
			printf("%5d", b[i][j]);
		}
		printf("\n");
	}


	// 两个数组相加
	int a[2][2] = { {1, 2}, {4, 5} };
	int b[2][2] = { {4, 5}, {4, 5} };
	int i, j;
	int c[2][2];

	for (i = 0; i < 2; i++) {
		for (j = 0; j < 2; j++) {
			c[i][j] = b[i][j] + a[i][j];
		}
	}
	for (i = 0; i < 2; i++) {
		for (j = 0; j < 2; j++) {
			printf("%2d", c[i][j]);
		}
		printf("\n");
	}



	return 0;
}