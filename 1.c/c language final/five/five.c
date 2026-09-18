#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>   // 不知到第多少个头文件 用于写字符串型
#include <errno.h>    // 同 用于处理c引入文件时对错误的处理



// 结构体
// 定义一个表示日期的结构体 date
// 其中 整个结构体包含了三个int类型的成员
struct date {
	int day;
	int month;
	int year;
};

// 调用结构体 struct + 定义名称 + 变量
// today 作为一个结构体 保存了三种数据 年月日
// 初始化结构体变量
struct date today = { 12, 11, 2024 };


struct Person {
	char name[50];
	int age;
	float high;
	// ...
};
struct Person frank = { "frank", 77, 280 };
struct Person zhangsan = { "zhangsan", 15, 100 };



// 调用时不引用struct方法 使用 typedef
typedef struct Date {
	int second;
}Date;   // 此处名称可以与上方不同 相当于起一个别名 但引用时引用下方别名

Date todays = { 1 }; // 定义类型名 不使用 struct



// 匿名结构体 隐式结构体
typedef struct {
	// 不写结构体名称 直接引用别名

	char name[50];   // 数组
	int id;
	float score;
}Student;

void print_stu(Student stu);  // 传递整个数据类型

// 修改学生分数score   结构体加指针
void update_score_by_value(Student* stu, float new_score);


// 通过函数值返回结构体    返回一个坐标(x, y)
typedef struct {
	int x;
	int y;
}Point;

Point get_point();   // 函数返回值类型为结构体


// 案例 候选人投票
typedef struct {
	int name[20];   // 姓名
	int votes;      // 票数
}Candidate;


// 结构体的嵌套
typedef struct {
	char street[50];
	char city[50];
	char country[50];
}Address;

typedef struct {
	char name[50];
	int age;
	Address address;  // 嵌套了上一个结构体
}Person;


// 枚举 定义一周的枚举
typedef enum {
	MONDAY,       // 0 
	TEUSDAY,      // 1
	WEDNESDAY,    // 2
	THURSDAY,     // 3
	FRIDAY,       // 4
	SATURDAY,     // 5
	SUNDAY        // 6
}weekday;

// 如果输出结果是一个字符 则需要写一个函数
const char* get_weekday_name(weekday day);


// 联合 共用体
typedef union {
	int int_value;
	float float_value;
	char* string_value;
}Data;

// 使用一个枚举来包含联合
typedef enum {
	INT,
	FLOAT,
	STRING
}DataType;
// enum Datatype r11, r12;


// 使用一个结构体来包含枚举
typedef struct {
	DataType type;   // 枚举
	Data data;       // 联合 引用了上方共用体

	// 也可以直接写下来
	/* union{
			int int_value;
			float float_value;
			char* string_value;
		}
	*/
}TypeData;


// 输出
void print_data(TypeData* typed_data) {
	switch (typed_data->type) {
	case INT: printf("Integer: %d\n", typed_data->data.int_value);
		break;
	case FLOAT: printf("Float: %f\n", typed_data->data.float_value);       // 浮点用%f
		break;
	case STRING: printf("String: %s\n", typed_data->data.string_value);    // 字符串用%s
		break;
	}
}

int main() {


	// 结构体 Structure

	// 结构体通常定义在main函数外面 为全局类型 在使用跨函数时结构体为单独一个文件

	// struct 表示结构体类型 date为定义的数据类型 today为类型名
	struct date today = { 12, 11, 2024 };


	// 访问结构体元素方法  

	// 1.定义类型名称: 通过结构体成员访问 
	// 数据名称.成员名称  
	// "."表示引用
	printf("Today's date is : %d-%d-%d\n", today.day, today.month, today.year);

	// 2.通过指针访问
	struct date* date_ptr = &today;   // Date 保存了一个结构体的地址 date类型的地址

	// 通过*导入一个地址计算类型 相当于使用指针计算格式    &today指向today的地址 相当于一个名词

	printf("Today's date is : %d-%d-%d\n", date_ptr->day, date_ptr->month, date_ptr->year);
	// 指针名->结构体成员名



	// 匿名结构体
	Student stu = { "Joy", 132, 95 };

	puts("Before update: \n");

	print_stu(stu);   // 引用一个函数


	// 通过指针修改结构体成员数值
	update_score_by_value(&stu, 100);  // 取地址

	puts("After update by value");

	print_stu(stu);



	// 通过函数值返回结构体
	Point my_point = get_point();   // 返回一个函数 函数里是一个结构体 

	printf("Point: (%d,%d)\n", my_point.x, my_point.y);
	// 输出结果为10，20   输出一个坐标 (x, y) 输出方式通过结构体 

	/*
	   值语义 values emantics
	   通过函数返回值来进行创建结构体并初始化

	   不使用结构体+函数时 我们通常在main里定义一个 get_point = (10, 20) 这样的定义放在main里是不安全的
	   但当我们使用结构体函数 我们定义一个my_point = get_point 并声明一个函数 在函数中定义(10，20) 并返
	   回给my_point 这样的定义是安全的，降低意外改数据的风险

	   使用这种方式操作也更简单 当函数执行完毕时 即函数在调用完10 20立刻销毁 没有任何东西可以操作这个函数
	   即没有任何方式获得10 20的地址(消失了) 从而改变坐标 （反外挂），从而更加安全
	*/



	// 结构体数组
	Point points[2] = {
		{1,2},{3,4}
	};
	// 定义一个包含2个Point结构体的数组

	for (int i = 0; i < 2; i++) {
		printf("Point %d: (%d, %d)\n", i, points[i].x, points[i].y);
	}   // 遍历这个结构体数组 输出结果为 (1,2)  (3,4)	



	// 案例 候选人投票
	// 1.初始化五名候选人
	Candidate candidates[6] = { {""}, {"张三", 0}, {"李四", 0}, {"王五", 0}, {"赵六", 0}, {"周七", 0} };

	// 2.初始化投票(结构体属性)
	int n, i, j;
	char voteName[20];

	// 3.初始化投票次数
	printf("请输入投票次数");
	scanf_s("%d", &n);  // 5

	for (i = 0; i < n; i++) {
		// 4.进行投票
		printf("请输入第%d张选票姓名", i + 1);
		scanf_s("%s", voteName);

		// 5.获取投票后的数据
		candidates[i].votes++;
	}

	// 6.输出
	printf("\n投票结果: \n");
	for (i = 0; i < 5; i++) {
		printf("%s: %d票\n", candidates[i].name, candidates[i].votes);
	}




	// 结构体的嵌套
	Person frank = {
		"frank",190, {"xxxxxx", "yyyyy", "zzzz"}
	};
	// 嵌套结构体用{"", "", ""}

	printf("Name: %s\n", frank.name);
	printf("Address: %s, %s, %s\n", frank.address.street, frank.address.city, frank.address.country);



	// 指针写法
	Person* ptr2 = &frank;
	printf("Name: %s\n", ptr2->name);
	printf("Address: %s, %s, %s\n", ptr2->address.street, ptr2->address.city, ptr2->address.country);

	// 对结构体指针的写法
	Person s1;
	Person* sp;
	sp = &s1;  // *sp = s1
	s1.age = '12';
	(*sp).age = 101;
	sp->age = 101;




	// 枚举 Enumeration
	// 数据类型 用枚举替代 #define
	weekday day = FRIDAY;
	printf("%d\n", day);

	printf("%d\n", FRIDAY);	  // 输出4



	// 联合 Union
	/*
	   它允许在相同的内存位置上存储不同的数据类型
	   联合体的所有成员共享一块内存空间，其大小为最大成员内存大小
	   即在任意时刻联合体只能存储一个成员的值

	   使用情况: 一个变量存储了多个数据类型 但在某一时刻(给定时间)只使用其中一个变量数据类型 节省内存
	*/
	TypeData data1 = { INT,{.int_value = 10} };   // 嵌套结构体转枚举 枚举转联合

	TypeData data2 = { FLOAT, {.float_value = 10.0} };

	TypeData data3 = { STRING,  {.string_value = "hello, union!"} };

	print_data(&data1);
	print_data(&data2);
	print_data(&data3);



	// 案例 c two
	/*
		使用定义头文件 简单制作一个游戏

		一.定义多个头文件     1.职业 角色(玩家 敌人(电脑) ->枚举
							 2.职业属性 职业能力        ->联合
							 3.嵌套包含以上内容         ->嵌套结构体
							 4.函数名头

		二.定义两个资源文件   5.初始化角色属性值 函数具体内容
							 6.运行 int main()

		原理 : 结构体单独一个文件(根据不同属性可能有多个)
			   函数单独一个文件(2个文件 一个函数名 一个函数内容)
			   运行主体 int main()单独一个文件
	*/



	return 0;
}

// 匿名结构体
void print_stu(Student stu) {
	printf("Student Name: %s\n", stu.name);      // 输出字符 %s
	printf("Student ID: %d\n", stu.id);          // 输出数字 %d
	printf("Student Score: %.2f\n", stu.score);  // 输出浮点数 %.2f
}

void update_score_by_value(Student* stu, float new_score) {

	// 函数参数可以是结构体
	stu->score = new_score;   // 通过指针访问结构体 使用箭头指向 ->
}

// 通过值返回结构体
Point get_point() {

	// 函数值可以是结构体

	Point p = { 10,20 };   // 一个含x y坐标的结构体
	return p;    // return 一个结构体
}


const char* get_weekday_name(weekday day) {
	switch (day) {
	case MONDAY: return "MONDAY";
	default:
		break;
	}
}
