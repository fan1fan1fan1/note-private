#include <stdio.h> 
#include <stdint.h>      // int16_t ，运算符
#include <inttypes.h>    // int类型最大值 , 运算符
#include <float.h>       // float类型最大值
#include <math.h>        // infinity 用于开根
#include <stdlib.h>      // 转义字符训练
#include <stdbool.h>     // bool类型
#define PI 3.14          // 定义变量 宏定义
#include <time.h>        // 第9 10行头文件用于do while循环
#include <windows.h>     // 控制秒数，引用一个模拟时间


// 双击stdint 可进入其文档查看类型


// void print_binary(uint8_t num);


int main(void)
{
	printf("hello world \n");

	// 打开vs 创建新项目 windows桌面向导 更改位置 下方打勾 控制台应用程序 空项目 新建源文件 改cpp为c

	// int -2的31幂-1到2的3幂-1 unsigned int 0到2的31幂-1 uint只能输出正数 输出负数则会整数溢出
	// ctrl+F5 开始调试

	// 输入变插入 键盘右上insert

	// ctrl+d 快速复制到下一行



	// int整数类型
	int number = 123;
	printf("number = %d\n0", number);
	// int类型占四个字节 short类型占两个字节 位数越大 数据处理范围越大



	// 初始化 
	// uint32_t number;   未初始化
	// uint32_t number = 1;  有初始化



	unsigned int positiveNum = 123;
	printf("Stored Value in Unsigned Int : %u\n", positiveNum);

	unsigned int sun_flower_max = 1000000;
	// 规定游戏阳光最大值为1000000



	// 800*600电脑屏幕分辨率
	unsigned short screenWidth = 800;
	unsigned short screenHeight = 600;
	// x,y
	unsigned short x = 400;
	unsigned short y = 300;

	printf("The screen resolution is : %u,%u\n", screenWidth, screenHeight);
	// 10进制无专用符号输出用u



	short myshort = 100;

	printf("myshort = %hd\n", myshort);

	printf("The screen resolution is : %hu,%hu\n", screenWidth, screenHeight);

	printf("Current position is : %hu,%hu\n", x, y);



	unsigned short color; // 16bit RGB

	color = 0b1111100000000000; //red

	printf("RED : %0xX\n", color);
	// short类型 嵌入式  
	// 处理像素 包含负数  unsigned short类型无负数



	// long类型 
	// 32位架构cpu下占四个字节 64位架构cpu下占八个字节 用%l输出 （L) 
	// long long 在32位cpu下占八个字节 64位cpu下占八个字节
	// 操作系统有32位和64为架构的区分 不同的cpu适用不同的架构    intel 8086 x86架构 32位CPU架构→64位 x86-64 x64
	// 64位架构可以向下兼容32位

	long number_1 = 123;
	long long number_2 = 456;

	printf("%ld", number_1);


	unsigned long number_3 = 123;

	printf("%lu", number);



	// sizeof 判断数据类型

	// size_t 数据类型 无符号整型 尺子 用来衡量信息块能装多少东西 用%z
	printf("Size of short : %zu byte(s)\n", sizeof(short));

	printf("Size of unsigned short : %zu byte(s)\n", sizeof(unsigned short));

	printf("Size of long : %zu byte(s)\n", sizeof(long));

	printf("Size of int : %zu byte(s)\n", sizeof(int));

	printf("Size of unsigned int : %zu byte(s)\n", sizeof(unsigned int));

	printf("Size of unsigned long : %zu byte(s)\n", sizeof(unsigned long));

	printf("Size of long long : %zu byte(s)\n", sizeof(long long));

	printf("Size of unsigned long long : %zu byte(s)\n", sizeof(unsigned long long));
	// %u为十进制无符号输出 




	// 第二个头文件<stdint.h> int_8 int_32 int_64
	// 第一个头文件<stdio.h> __int32 __int64 __int128
	__int32 sun_flower = 100;

	printf("int %d\n sun_flower", sun_flower);


	// 以下输出结果均为最大值 即int16_t输出结果最大值为32767
	int16_t myInt16 = 32767; // 用%hd输出
	uint16_t myUInt16 = 65535;

	int32_t myInt32 = 21474836; // 用%u输出
	uint32_t myUInt32 = 4294967295U;

	int64_t myInt64 = 9223372036854775807LL; // 用%lld输出
	uint64_t myUInt64 = 18446744073709551615ULL;

	printf("Size of int16_t : %zu byte(s)\n", sizeof(myInt16));

	printf("Size of uint16_t : %zu byte(s)\n", sizeof(myUInt16));

	printf("Size of int32_t : %zu byte(s)\n", sizeof(myInt32));

	printf("Size of uint32_t : %zu byte(s)\n", sizeof(myUInt32));

	printf("Size of int64_t : %zu byte(s)\n", sizeof(myInt64));

	printf("Size of uint64_t : %zu byte(s)\n", sizeof(myUInt64));
	// myint myuint为自拟       
	// 因数据过大 会在数据后加无符号标志U 避免溢出
	// int64 即long long 无符号标志为LL


	uint32_t uNum = UINT32_MAX;
	// 最大值快捷获取方式   按住ctrl 点击UINT32_MAX 右上角关闭
	// uNum；驼峰命名法
	// float_of_speed；下划线命名法 



	/*
	   int16_t →% hd\n
	   uint16_t → %hu\n
	   int32_t → %d\n
	   uint32_t → %u\n
	   int64_t → %lld\n
	   uint64_t → %llu\n
	 */


	 // uint8_t 常用于数字计算



	 // 类型转换 Type Conversion

	int16_t smallNum = 32767;
	int32_t bigNum;

	// 隐式转换
	bigNum = smallNum;


	int32_t bigNum_1 = 99999999;
	int16_t smallNum_1;

	// 显式转换 强制转换 尽可能用显式转换
	smallNum_1 = bigNum_1;

	printf("smallNum_1 = %d\n", smallNum_1);


	uint32_t uNum_1 = UINT32_MAX;
	int32_t sNum = uNum;

	printf("uint32_t:%u\n", uNum);
	printf("converted to int32_t:%d\n", sNum);
	// 无符号到有符号 强制转换 无法实现(超出转换类型最大值）
	// 显示类型转换→156行 int32_t sNum = (int32_t)uNum;


	// 大范围到小范围
	int64_t longNum = 50000;
	int16_t shortNum = (int16_t)longNum;

	printf("int64_t:%lld\n", longNum);
	printf("converted to int16_t:%hd\n", shortNum);
	// 超出转换类型最大值


	// 小范围到大范围(扩展负数）
	int16_t smallNum_4 = -1;
	uint32_t bigNum_4 = (uint32_t)smallNum_4; // uint32_t 无负数 最小值为0

	printf("int16_t:%hd\n", smallNum_4);
	printf("converted to uint32_t:%u\n", bigNum_4);
	// 超出转换类型最小值



	// 固定宽度整数类型 

	// 第三个头文件<inttypes.h>
	// 不使用printf输出 类型%过于复杂记不住
	int32_t myyInt32 = INT32_MAX;
	uint32_t myyUInt32 = UINT32_MAX;

	uint64_t myyUInt64 = UINT64_MAX;


	/*
	   printf("int32_t: %d\n", myyInt32);
	   printf("uint32_t: %u\n", myyUInt);
	   printf("uint64_t; %llu\n", myyUInt);
	*/

	printf("int32_t: %" PRId32 "\n", myyInt32);
	printf("uint32_t: %" PRIu32 "\n", myyUInt32);
	printf("uint64_t: %" PRIu64 "\n", myyUInt64);
	// 按住ctrl 点击PRI 解释其内容
	// int→PRId uint→PRIu



	int_least8_t number_5;
	// int_leastN_t number 至少有N位 可能更多 适用于需要保证最小存储容量的可移植代码
	// 定义的时候 保证至少有8（特定的位数）位 

	int_fast8_t;
	// 至少有N位 但是选择运算最快的类型 适用于需要性能敏感的场景
	// 保证最快至少有8位

	// 标准整数类型 → 固定宽度整数类型
	// 固定的位数 不可以越界 适用于需要精确数据大小的场景

	// 游戏玩家分数初始分
	int_least32_t playScore = 5000;

	// 初始化数据值
	int_fast32_t pixelValue = 128;



	// float类型
	// 32位浮点数类型 小数

	// 基数=尾数+指数
	// 数字 纯数 科学计数法小数点位置 指数大于0往右移 指数小于0往左移 
	// 例 3.14159 为314159 * 10^-5

	// 总32位 其中符号占1位1bit 基数占23位23bit（隐藏小数位1位 共24位） 指数占8位2bit

	/*
		在IEEE754标准电气功能标准中
		8bit共256个数据 0-255 中间值为127
		以127为标准 126为127-1即10^-1（左偏移） 130为10^3（右偏移）
		例 3.14159为    + 314159 122的二进制形式
	 */

	float temperture = 36.5f;

	float humidty = 48.3f;

	float speed_of_sound = 343.5e2f; // 科学计数法 343.5 * 10^2

	float length = 12.34f, width = 23.45f, height = 34.56f; // 多重变量在一行 多重定义 不建议

	printf("Temperture: %f\n", temperture);

	printf("Humidty: %f\n", humidty);
	printf("Humidty: %0.2f\n", humidty); // %0.2f保留两位小数

	printf("Speed_of_sound: %f\n", speed_of_sound);

	// 错误printf("Length: %f\n", length);
	printf("Dimensions (LxWxH): %f x %f x %f\n", length, width, height);

	// 丢失精度



	// printf 输出% 需要打两个 %%f
	float num = 123.456f;

	// %f
	printf("Using %%f: %f\n", num);

	// %e %E 科学计数法格式化
	printf("Using %%e: %e\n", num);

	printf("Using %%E: %E\n", num);

	// %a %A 十六进制浮点数 p计数法
	printf("Using %%a: %a\n", num);
	printf("Using %%A: %A\n", num);



	// 第四个头文件<float.h> 处理所有float单精度问题

	// float单精度 %f
	// double双精度 %lf 精度准确

	float max_float = FLT_MAX;
	// 按住ctrl不放 点击FLT_MAX 可查看float类型最大值

	float overflow = max_float * 1000.0f;
	// float类型浮点数 要保留小数位+f（单精度） 否则认为int类型 默认隐式转换

	float min_float = FLT_MIN;

	float underflow = min_float / 1000.0f;
	// 运算符号 *乘号 /除号

	printf("Maximum Float: %e\n", max_float);

	printf("Overflow: %e\n", overflow);
	// 溢出 OverFlow 上溢 浮点数用语 
	// 输出结果→inf infinity "∞"
	// printf("1/0 = %f\n", 1.0/0.0); →inf

	printf("Minimum Positive Float: %e\n", min_float);

	printf("Underflow: %e\n", underflow);
	// UnderFlow 下溢 数值过小无法用计算机测量



	// 第五个头文件 <math.h> 用于输出INFINITY 计算格式

	float positive_infinity = INFINITY;
	printf("Positive Infinity: %f\n", positive_infinity);
	// 正无穷大

	float negative_infinity = -INFINITY;
	printf("Negative Infinity: %f\n", negative_infinity);
	// 负无穷大

	float num_1 = 1.0f;
	float infinity = num_1 / 0.0f;

	printf("1.0 / 0.0 = %f\n", infinity);
	// 除以0产生的无穷大

	// 结果为Nan 表示一个不确定的值 Not a number
	float nan = 0.0f;
	printf("0.0 / 0.0 = %f\n", nan);

	// 开平方计算格式
	float number_6 = sqrt(4);
	printf("sqrt4 = %f\n", number_6);

	float negative_sqrt = sqrt(-1.0f);
	printf("sqrt(1.0f) = %f\n", negative_sqrt);


	// double类型

	// float瘦 丢失精度 速度快 eg.3D图形渲染
	// double 科研 准确 精度高 eg.银行利息

	// 小数 未定义的 默认为double
	printf("%f\n", 3.14);

	// 定义为float f
	printf("%f\n", 3.14f);


	double num1 = 123.456;
	double num2 = 76.543;

	double sum = num1 + num2;
	double difference = num1 - num2;
	double product = num1 * num2;
	double quotient = num1 / num2;

	printf("Sum: %f\n", sum);
	// 默认参数提升 float类型会提升为double 因此可用 %f 输出

	printf("Diffeerence: %f\n", difference);
	printf("Product: %f\n", product);
	printf("Quotient: %f\n", quotient);



	// long double类型 精度更高18位有效数字
	// double类型15位有效数字



	// float和double有效精度对比
	float float_num = 1.0 / 3.0;
	double double_num = 1.0 / 3.0;

	printf("Float precision: %.20f\n", float_num);
	printf("Double precision: %.20lf\n", double_num);

	printf("Defined max precision for float: %d\n", FLT_DIG);
	printf("Defined max precision for double: %d\n", DBL_DIG);
	// 表示浮点类型有效输出 按住ctrl 点击紫色区域可查看其有效精度



	// char类型 字符类型 存储字符 为了转换二进制
	// 字符类型整数 单个字母 单个符号 只一个 占1个字节 用%c
	// 字符值范围 -128到127
	// unsigned char 无符号类型 字符值范围0-255 用于字符处理

	char mych = 'A'; // char使用单引号‘’

	printf("mych: %c\n", mych);

	char mych1 = ','; // 44

	printf("mych1: %c\n", mych1);

	// 光标放到''区域 显示十进制数字 转化为二进制输出

	int mych2 = 44;

	printf("mych: %c\n", mych2); // ,

	// 美国信息交换标准代码ASCII编码 
	// 使用7个bit 128个字符 0-127
	// 控制字符 0-31和127 控制字符行为 eg.ASCII 13（CR） → 回车
	//                               eg.ASCII 10（LF） → 换行
	// 可打印字符 32-126 英文字母大小写 数字 标点 符号 A→65 a→97

	// Unicode 与 ASCII兼容 同为标准代码 包含地球上所有符号



	// 转义序列
	// 使用\反斜杠
	// \n 换行 字符间换行   \a 响铃 警报   \b Backspace   \f 换页   \r 回车
	// \t 制表符 字符间有间隙   \v 垂直制表符

	printf("123\t456\t789");

	printf("\\"); // \

	// 输出一个双引号

	// 错误 printf(" "" ");
	printf("\"");



	// 清除屏幕

	// printf("\033[2J");




	// 第六个头文件 <stdlib.h> 用于使用system

	// 移动光标

	// printf("\033[%d;%dH", 3, 3);

	// system("pause");



	// 生成警报
	printf("\a");



	// 练习
	printf("第一行文本\n\t第二行文本，带有缩进\n\t\t第三行文本，缩进更多\n\t\t\t");



	// 路径
	printf("C:\\Users\\22820");



	// bool类型

	// 布尔 占1位存储空间 不是1个字节
	// true 1
	// false 0
	// 第七个头文件<stdbool.h> 使用bool类型

	// 不使用bool
	int is_game_over = 0; // 输了false
	int is_game_won = 1; // 赢了true

	// 使用bool
	bool is_game_over1 = false;
	bool is_game_won1 = true;



	// 常量
	// int类型前面加const

	const int MAX_USERS = 100;
	// 用户量固定为100个 不可更改

	// 输出方式一 printf("MAX_USERS: %d\n", MAX_USERS);

	// 第八个头文件 #define PI 3.14 宏定义 
	// 输出PI结果 默认double类型 输出方式二
	printf("PI: %f\n", PI);



	// 运算符

	/*
		算术运算符 除号/ 取模%(算余数）
		关系运算符 赋值= 等于== 不等于!= 大于等于>=
		逻辑运算符 非! 并且&& 或者||
		赋值运算符 =
	*/


	// 需要用到第二个头文件<stdint.h>和第三个头文件<inttype.h>

	uint32_t apple_box = 5;
	uint32_t orange_box = 10;

	printf("橘子盒子里有 %"PRIu32"个橘子\n", orange_box);

	uint32_t total_fruit = apple_box + orange_box;

	printf("盒子里总共有 %"PRIu32"\n", total_fruit);

	// 数据对象      apple_box 
	// 左值(盒子名字) apple_box 
	// 右值Rvalue    5
	// 运算符


	// 多重赋值  
	// 在编程和研发中最高三层 一次性给多个变量赋相同的值
	// a,b,c仅仅是测试数据，并无实际意义

	uint32_t a, b, c;
	a = b = c = 10;

	printf("a: %"PRIu32"\n", a);
	printf("b: %"PRIu32"\n", b);
	printf("c: %"PRIu32"\n", c);

	// 第一步 z = 10
	// 第二步 y = z 
	// 第三步 x = y


	// 算术运算练习

	uint32_t apples = 10;
	uint32_t oranges = 5;

	uint32_t totalFruits = apples + oranges; // 加法
	uint32_t remainingApples = apples - 2; // 减法
	uint32_t appleBoxes = apples * 10; // 乘法
	uint32_t fruitsPerFriend = totalFruits / 2; // 除法
	uint32_t remainingFruits = totalFruits % 3; // 取模

	printf("共有 %"PRIu32"个水果\n", totalFruits);
	printf("吃掉两个，剩下 %"PRIu32"个苹果\n", remainingApples);
	printf("若有十个盒子，可装 %"PRIu32"个苹果\n", appleBoxes);
	printf("共有15个水果，平均分给两个人每人分到 %"PRIu32"个水果\n", fruitsPerFriend);
	printf("共有15个水果，平均分给三个人还剩下 %"PRIu32"个水果\n", remainingFruits); // 15/3=5 无余数
	// 浮点数和浮点数相除得到浮点数 整数和整数相除只能得到整数 即无小数位



	// 一元运算符
	int32_t number_7 = -10;
	int32_t number_8 = -number_7;

	printf("number_7: %"PRId32"\n", number_7);
	printf("number_8: %"PRId32"\n", number_8);

	// 二元运算符
	int32_t total_number = number_7 + number_8;
	printf("total_number: %"PRId32"\n", total_number);



	// 递增递减运算符
	// 即++在前为前缀 前递增 ++在后为后缀 后递增


	// 后缀递增 
	int32_t value = 5;
	int32_t result;

	result = value++; // 使用value的当前值（5） →然后value+1变成6 先赋值再++
	printf("After postfix increment, result =%" PRId32", value = %" PRId32"\n", result, value);

	// result = value + 1; 为 先使value+1然后赋值给result
	// result = value++; 为 先把value赋值给result 然后+1


	// 前缀递增
	value = 5;

	result = ++value; // 先++再赋值

	printf("After postfix increment, result = %" PRId32 ", value = %" PRId32 "\n", result, value);


	// 后缀递减
	value = 5;

	result = value--;
	// value = value-1;

	printf("After postfix increment, result = %" PRId32 ", value = %" PRId32 "\n", result, value);


	// 前缀递减
	value = 5;

	// value = value-1;
	result = --value;

	printf("After posifix increment, result = %" PRId32 ", value = %" PRId32 "\n", result, value);



	// 按位移位运算符 
	// 处理二进制数据 操作二进制位置 
	// 左移位运算符 << 低位补0
	// 右移位运算符 >> 高位补0

	uint32_t num3 = 22;
	// 22的二进制位为 00010110

	num3 << 2;  // 左移
	// 将00010110 每一位向左移动两位 末尾补0
	// 22→88

	printf("Original number: %" PRIu32 " (binary:00010110)\n", num3);


	uint32_t num4 = 22;

	num4 >> 2;  // 右移

	printf("Original number: %" PRIu32 " (binary:00010110)\n", num4);
	// 所有位向右移动两位
	// 22→


	// 左移
	uint8_t left_shifted = num3 << 2;

	printf("Left shifted by 2: %" PRIu8 " (binary: 01011000)\n", left_shifted);

	// 右移
	uint8_t right_shifted = num4 >> 2;

	printf("Right shifted by 2: %" PRIu8 " (binary: 00000101)\n", right_shifted);


	// 左移10位 相当于乘以 2^10 即1024
	// ALU 算术逻辑单元 算术处理 



	// 关系运算符练习

	int aa = 10;
	int bb = 20;

	bool greater = aa > bb;
	printf("aa > bb: %d\n", greater);

	bool less = aa < bb;
	printf("aa < bb: %d\n", less);

	bool equal = aa == bb;
	printf("aa == bb: %d\n", equal);

	bool not_equal = aa != bb;
	printf("aa != bb: %d\n", not_equal);

	bool greater_or_equal = aa >= bb;
	printf("aa >= bb: %d\n", greater_or_equal);

	bool less_or_equal = aa <= bb;
	printf("aa <= bb: %d\n", less_or_equal);



	// 条件表达式运算符

	bool greater_1 = aa > bb;
	printf("aa > bb: %s\n", greater_1 ? "true" : "false");

	bool less_1 = aa < bb;
	printf("aa < bb: %s\n", less_1 ? "true" : "false");

	bool equal_1 = aa == bb;
	printf("aa == bb: %s\n", equal_1 ? "true" : "false");

	bool not_equal_1 = aa != bb;
	printf("aa != bb: %s\n", not_equal_1 ? "true" : "false");

	bool greater_or_equal_1 = aa >= bb;
	printf("aa >= bb: %s\n", greater_or_equal_1 ? "true" : "false");

	bool less_or_equal_1 = aa <= bb;
	printf("aa <= bb: %s\n", less_or_equal_1 ? "true" : "false");

	// xxx ? xxx : xxx
	// %s为输出文字 %d输出0 1



	int score = 89;

	printf("你的成绩等级：%s\n", score >= 90 ? "A" : "不及格");

	return 0;
}