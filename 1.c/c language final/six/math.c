#define _USE_MATH_DEFINES         // 定义Π
#define _CRT_SECURE_NO_WARNINGS   // 使用scanf, 允许使用c语言中的非安全函数，忽略警告

#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>  
#include <math.h>

// DBL_MIN
#include <float.h>

#include <time.h>

void check_float(double number);

void printBudgets(double* budgets, int size);

int main(void) {

	// 库函数 math.h 头文件 数学相关
	/*
	   按住ctrl 点击该头文件 进入math文件
	   再次按住ctrl 点击#include <corecrt_math.h>
	*/


	// 案例一 计算三角函数
	// 定义三角函数使用double 否则丢失精度

	double input_angle_degress = 0.0;
	double input_angle_radians = 0.0;
	double sin_value = 0.0;
	double cos_value = 0.0;
	double tan_value = 0.0;

	printf("请输入角度(度°): \n");
	scanf_s("%lf", &input_angle_degress);

	// 将角度转换为弧度
	input_angle_degress = input_angle_degress * (M_PI / 180.0);
	// ⬆ 派Π  要定义在include前面 即文件最前面

// 计算三角函数值
	sin_value = sin(input_angle_degress);
	cos_value = cos(input_angle_degress);
	tan_value = tan(input_angle_degress);

	printf("The sin of %.2f degress is : %.2f\n", input_angle_degress, sin_value);
	printf("The cos of %.2f degress is : %.2f\n", input_angle_degress, cos_value);
	printf("The tan of %.2f degress is : %.2f\n", input_angle_degress, tan_value);



	// 案例二 反三角函数
	// 反三角函数 asin_value = asin(input_angle_degress);    ...    即在计算位置 前面加a 

	// 将弧度转换为度
	double sin_valuee = 0.5;
	double cos_valuee = 0.5;
	double tan_valuee = 1.0;

	// 计算三角函数值
	double asin_valuee = asin(sin_valuee) * (180.0 / M_PI);
	double acos_valuee = acos(cos_valuee) * (180.0 / M_PI);
	double atan_valuee = atan(tan_valuee) * (180.0 / M_PI);

	printf("The asin of %.2f degress is : %.2f\n", input_angle_degress, asin_valuee);
	printf("The acos of %.2f degress is : %.2f\n", input_angle_degress, acos_valuee);
	printf("The atan of %.2f degress is : %.2f\n", input_angle_degress, atan_valuee);



	// 案例三 双曲线函数 
	// 三角函数+h -> 双曲线函数   sinh cosh tanh

	double input_value = 1.0;   // 假设

	double sinh_value = sinh(input_value);
	double cosh_value = cosh(input_value);
	double tanh_value = tanh(input_value);

	printf("sinh(%f) = %f\n", input_value, sinh_value);



	// 案例四 指数对数函数

	double input_exp = 1.0;           // 指数函数的值
	double input_log = 2.71828;       // e 自然对数值
	double input_log10 = 10.0;        // 以10为底对数

	// 计算指数函数值
	double result_exp = exp(input_exp);

	// 计算自然对数函数值
	double result_log = log(input_log);

	// 以10为底对数函数计算
	double result_log10 = log10(input_exp);

	printf("exp(%.2f) = %f\n", input_exp, result_exp);



	// 常见math类别函数汇总

	// sqrt() 开方
	double num_sqrt = 16.0;   // 要求的平方根的数
	double num_fabs = -5.7;   // 要求的绝对值的数
	double num_ceil = 2.3;    // 向上取整的数 
	double num_floor = 2.7;   // 向下取整的数
	double num1_fmod = 5.5;   // 求余数的被除数
	double num2_fmod = 2.0;   // 求余数的除数

	double result_sqrt = sqrt(num_sqrt);
	double result_fabs = fabs(num_fabs);
	double result_ceil = ceil(num_ceil);
	double result_floor = floor(num_floor);
	double result_fmod = fmod(num1_fmod, num2_fmod);

	printf("sqrt(%.2f) = %f\n", num_sqrt, result_sqrt);
	printf("fabs(%.2f) = %f\n", num_fabs, result_fabs);
	printf("ceil(%.2f) = %f\n", num_ceil, result_ceil);
	printf("floor(%.2f) = %f\n", num_floor, result_floor);
	printf("fmod(%.2f) = %f\n", num1_fmod, result_fmod);
	printf("fmod(%.2f) = %f\n", num2_fmod, result_fmod);



	// 案例五 pow函数
	double radius = 0.0;            // 圆的半径
	double square_size = 0.0;       // 正方形边长
	double circle_area = 0.0;       // 圆的面积
	double square_area = 0.0;       // 正方形面积

	printf("请输入圆的半径: \n");
	scanf_s("%lf", &radius);

	circle_area = M_PI * pow(radius, 2);    // 面积: Π * 半径的平方

	square_size = 2 * radius;       // 正方形边长 -> 圆直径

	square_area = pow(square_size, 2);            // 计算机正方形面积

	printf("圆的面积: %.2f\n", circle_area);
	printf("边长等于圆直径的正方形面积为: %.2f\n", square_area);



	// scanf 不带_s 需要一个宏
	double number = 0.0;
	double result = 0.0;

	printf("请输入一个数字以计算其平方根：\n");
	scanf("%lf", &number);

	errno = 0;

	result = sqrt(number);

	// 检查 sqrt函数是否出错
	if (errno == EDOM) {
		// EDOM 负数 定义域错误
		printf("错误: 输入值为负数，无法计算其平方根!\n");
	}
	else if (errno == ERANGE) {
		// ERANGE 超出范围
		printf("错误: 结果超出范围!\n");
	}
	else if (errno == HUGE_VAL) {
		// HUGE_VAL 超出范围
		printf("错误: 结果超出范围!返回HUGE_VAL!\n ");
	}
	else {
		printf("数字 %.2f的平方根为: %.2f\n", number, result);
	}



	// 案例 检查浮点数类别和属性

	// 静态分析
//	double numbers[] = { 0.0, 1.0, -1.0, 1.0 / 0.0, -1.0 / 0.0, 0.0 / 0.0, DBL_MIN / 2.0 };
	// DBL_MIN 处需要引用头文件

	double numbers[] = { 1.0 };
	int size = sizeof(numbers) / sizeof(numbers[0]);

	for (size_t i = 0; i < size; i++) {
		check_float(numbers[i]);
	}



	// 浮点数的比较于差值
	double group1_max_temp = 35.5;
	double group2_max_temp = 37.2;

	double group1_min_temp = -5.0;
	double group2_min_temp = -3.8;

	// 比较两个浮点数 并输出更大的浮点数 更小的浮点数
	double max_temp = fmax(group1_max_temp, group2_max_temp);

	printf("max_temp : %.2f °C\n", max_temp);
	printf("min_temp : %.2f °C\n", fmin(group1_min_temp, group2_min_temp));

	// 比较两者的差值 当第一个参数小于第二个参数->返回0    倒过来写就会返回差值
	double temp_diff_max = fdim(group1_max_temp, group2_max_temp);
	printf("%.2f\n", temp_diff_max);

	double temp_diff_min = fdim(group1_min_temp, group2_min_temp);
	printf("%.2f\n", temp_diff_min);



	// 舍入
	/*
		time_t 获得当前的时间戳
		时间戳: 字符串编码用于记录当前时间，国际标准为ISO 8601
	*/
	time_t now = time(NULL);

	// printf("%td\n", now);   输出结果为一段数字

	// 转换为本地时间
	// 相当于一个结构体 struct 没定义别名 因此在主函数里写 struct + 结构体名称
	struct tm local_time;
	localtime_s(&local_time, &now);

	// 转换为协调世界时 (UTC) -> 由于世界上的地区不同，时区不同，每个时区的本地时间都不一样
	// 将时间转换为一种全球统一的时间标准
	struct tm utc_time;
	gmtime_s(&utc_time, &now);

	// 格式化输出字符串
	char local_time_str[80];
	char utc_time_str[80];
	strftime(local_time_str, sizeof(local_time_str), "%Y-%m-%d %H:%M:%S", &local_time);
	// 将时间的结构转化为字符串
	strftime(utc_time_str, sizeof(utc_time_str), "%Y-%m-%d %H:%M:%S", &utc_time);

	// c语言时间结构 int tm_sec     int tm_min    int tm_hour     int tm_mday     int tm_mon     int tm_year......
	// 范围:        [0-60]          [0-59]        [0-23]          [1-31]          [0-11]         [since 1900]

	printf("当前时间戳: %" PRIdMAX "\n", (intmax_t)now);
	printf("本地时间: %s\n", local_time_str);
	printf("UTC时间: %s\n", utc_time_str);



	/*
	 #include <errno.h>
	 保存最后一次发生错误的代码

	 函数perror(); 也是该头文件内函数 用来打印上一个错误

	 函数strerror(); 解释当前的值 打印字符串不打印标号   需要头文件 #include <string.h>
	*/



	return 0;
}

// 案例 检查浮点数的分类
void check_float(double number) {
	switch (fpclassify(number)) {
	case FP_INFINITE:printf("%.2f 是无穷大\n", number); break;
	case FP_NAN:printf("%.2f 不是一个数字(NaN)\n", number); break;
	case FP_NORMAL:printf("%.2f 是一个正常值\n", number); break;
	case FP_SUBNORMAL:printf("%.2f 是次正规数\n", number); break;
	case FP_ZERO:printf("%.2f 是零\n", number); break;
	}

	if (isfinite(number))  printf("%.2f 是有限的.\n", number);
	if (isinf(number))     printf("%.2f 是无穷大.\n", number);
	if (isnan(number))     printf("%.2f 是NaN.\n", number);
	if (isnormal(number))  printf("%.2f 是正常数.\n", number);
	if (signbit(number))   printf("%.2f 是有限的.\n", number);
	else                   printf("%.2f 的符号位是正或零.\n", number);

	printf("\n");
}


// realloc 在程序运行中添加内容
void printBudgets(double* budgets, int size) {
	printf("Current budgets:\n");
	for (size_t i = 0; i < size; i++)
	{
		printf("Department %zd: $%.2f\n", i + 1, budgets[i]);
		// ⬆ size_t 使用 %zd
	}
}