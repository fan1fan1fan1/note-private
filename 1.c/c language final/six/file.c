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


typedef struct Character {
	char* name;
	int level;
	int hp;
}Character;
Character* create_character(const char* name, int level, int hp);
// 释放内存的函数
void free_character(Character* character);

typedef struct Employee {
	char* name;
	int* taskList;
	int taskCount;
}Employee;
Employee* create_employee(const char* name, int taskCount);
void free_employee(Employee* employee);

typedef struct {
	int id;
	float price;

	// 多级指针
	const char* manufacturer;
}Product;
// 返回一个product地址
Product* create_product(int id, float price, const char* manufacturer);

// update 根据批发商更新
void update_by_wholesaler(Product* product, int new_id, float new_price);

// 根据零售商更新
void update_by_retailer(Product* product, int new_id, float new_price);

// 多级指针用途
const char* get_manufacturer_info(Product** product_ptr);


/* 函数指针
	1.如何声明一个函数指向指针
	返回类型 (*指针变量名)（参数类型）;
*/
int (*myFuctionPointer)(int, int);   // 函数参数为int类型 返回值是int类型  ->  int f(int num1, int num2);
int add(int a, int b);

// 函数指针用途案例
typedef int32_t(*operation_t)(int32_t, int32_t);
int32_t add1(int32_t a, int32_t b);
int32_t subtract(int32_t a, int32_t b);
int32_t multiply(int32_t a, int32_t b);
int32_t divide(int32_t a, int32_t b);

// 通过函数指针数组，包含各种操作
operation_t operations[4] = { add, subtract, multiply, divide };     // 数组内存储函数名称


int main(void) {
	// 动态内容来分配指针和动态内存 

	// 动态内存分配
	char buffer3[100];

	/*
		定义数组时定义了内存大小 10太小 100太大【预设编译大小】不够灵活，我们使用动态分配内存 方便对大小定义
		传统数组: 1.灵活性降低 整个程序走下来 都依赖于【预设编译前的大小】
				 2.内存的浪费和安全隐患 烫
				 3.应用受限 (超出范围)

		动态内存分配: 1.处理可变大小的数据
					 2.高效的数据结构
					 3.资源优化
	*/


	/*
		计算机操作系统内存管理机制：
		1.栈内存 stack memory
			a.自动管理机制: 函数调用的时候 局部变量会被分配到栈上 当函数返回即函数调用完毕时 局部变量全部销毁释放
			b.速度快 但是是线性数据结构
			c.大小有限制 在程序启动的一刹那就意味着已经确定 改动几乎变成了笑话 如果栈的内存被耗尽 就意味着崩溃 栈溢出

			int arr[4];             编译的时候就确定是4个字节

		2.堆内存 heap memory
			a.动态管理: 手动管理   malloc calloc realloc free 使用这些函数来操作管理
			b.速度慢 需要在内存中寻找足够大的连续空间块
			c.大小灵活 堆的大小通常受到可用系统内存的限制 而非栈本身的限制 能够支持动态按需分配大量内存
			d.用于存储函数的局部变量 函数参数 函数调用的返回地址

		程序运行：编译 运行
	*/


	// 静态数组内存分配到栈上 动态数组内存分配到堆上
	// 动态数组内存分配 malloc    需要头文件 stdlib


	// int arr[5];
	int* dynamic_arr = (int*)malloc(5 * sizeof(int));

	// malloc返回值为void， void* -> 在c语言中用于泛型编程， 可强制转换为int*类型

	// 手动释放堆内存 因为不是简单的局部变量 局部变量会在函数结束后自动释放 而堆不会

	// 判断指针是否为空指针
	if (dynamic_arr == NULL) {
		perror("动态数组分配失败!");
		exit(EXIT_FAILURE);
	}

	for (size_t i = 0; i < 5; i++) {
		dynamic_arr[i] = (i + 1) * 10;
	}

	puts("动态数组的内容:");

	for (size_t i = 0; i < 5; i++) {
		printf("%d", dynamic_arr[i]);
	}

	free(dynamic_arr);



	// realloc函数 在程序执行过程中增加内存位置

	// 动态调整部门预算列表
	int size1 = 3;   // 初始预算项数

	double* budgets = (double*)malloc(size1 * sizeof(double));
	if (budgets == NULL) {
		perror("Failed to allocate initial budgets");
		return EXIT_FAILURE;
	}

	// 假设初始预算分配
	budgets[0] = 1000;
	budgets[1] = 1500;
	budgets[2] = 1200;

	printBudgets(budgets, size1);

	// 增加预算项 
	// 在原先的基础上扩展 realloc
	int newSize = 5;
	double* newBudgets = (double*)realloc(budgets, newSize * sizeof(double));

	if (newBudgets == NULL) {
		perror("Failed to rallocate initial budgets");

		// 如果新扩展的内容是空NULL 那么旧的内容将会被释放
		free(budgets);

		return EXIT_FAILURE;
	}

	// 当添加了扩展项之后 更新指针
	// 这样数组就达到了动态效果
	budgets = newBudgets;

	budgets[3] = 2000;
	budgets[4] = 1000;

	printBudgets(budgets, newSize);

	// 释放全部
	free(budgets);

	// 当主函数main结束时 return 0; 可写为 return EXIT_SUCCESS;



	// 如何防止内存泄漏案例

	// 创建一个角色系统
	Character* hero = create_character("Hero", 1, 100);
	if (hero == NULL) {
		return EXIT_FAILURE;
	}
	// ...
	free_character(hero);



	/*
	 calloc()函数
	 初始化任务列表 将所有位置设置为0
	 不仅可以分配内存 还可以将所有位置设置为0
	*/

	// 创建每一个员工时 都给他一个初始大小的任务列表 并确保所有任务id为0 表示没有分配任何任务
	Employee* developer = create_employee("Frank", 5);

	if (developer == NULL) {
		return EXIT_FAILURE;
	}
	// 也可以写成 if(developer == NULL) return EXIT_FAILURE;

	developer->taskList[0] = 101;   // 将[0]改成其他数字 输出内容可能有所不同

	printf("Assigned Task ID for %s : %d\n", developer->name, developer->taskList[0]);

	free_employee(developer);



	// 多级指针 指向指针的指针
	int a = 10;
	int* ptr = &a;    // 一个指向a的指针 保存了变量a的地址 指针ptr指向a

	int** pptr = &ptr; // 一个指向指针的指针


	// 案例 零售商从批发商那购买工厂制作的商品  
	// 工厂
	Product* product = create_product(1, 10.0, "1");
	printf("Product ID: %d, Price: %.2f\n", product->id, product->price);

	// 批发商
	update_by_wholesaler(product, 222, 15.0);
	printf("update_by_wholesaler --- product ID: %d, price: %.2f\n", product->id, product->price);

	// 零售商
	update_by_retailer(product, 333, 20.0);
	printf("ipdate_by_retailer --- product ID: %d, price: %.2f\n", product->id, product->price);

	free(product);



	// 多级指针用途
	// 相当于不经过批发商 零售商直接找工厂进货
	Product* product1 = create_product(1, 10.0, "衡水工厂");
	printf("Factory---Product ID: %d, Price: %.2f, Manufacturer: %s\n", product1->id, product1->price, product1->manufacturer);

	// 批发商从工厂获取产品
	Product* wholesaler_product = product1;

	// 零售商获取产品并联系工厂
	Product** retailer_product = &wholesaler_product;

	printf("Retailer---Product ID: %d, Price: %.2f, Manufacturer: %s\n", (*retailer_product)->id, (*retailer_product)->price, (*retailer_product)->manufacturer);
	// 解引 '->'      (*retailer_product)->price  ==  (**retailer_product).price  

	const char* manufacturer_info = get_manufacturer_info(retailer_product);

	printf("Retailer contacted factory through wholesaler: Manufacturer : %s\n", manufacturer_info);

	free(product1);



	// 函数指针 function pointer    指针指向函数

	// 函数指针的最大用途: 实现回调函数
	// 回调函数: 允许将一个函数作为参数传递给另一个函数 这样当特定的事件发生 可以调用传递的参数

	// 2.指向函数 通过指针调用函数
	myFuctionPointer = add;

	// 3.调用函数
	int result1 = myFuctionPointer(2, 3);
	printf("The result is %d\n", result1);



	// typedef 
	typedef unsigned long ulong;    // 数据类型为unsigned long ，别名为ulong 
	typedef uint32_t u32;
	// 给这个基本数据类型起一个别名 

	// 引用
	ulong number1 = 123456;

	/*
		typedef struct {
			int x;
			int y;
		} Point;

		Point p = 1;
	*/



	// 函数指针用途案例
	int32_t c = 10, b = 5;
	int32_t result2 = 0;

	result2 = operations[0](c, b);
	printf("%d\n", result2);

	result2 = operations[1](c, b);
	printf("%d\n", result2);

	result2 = operations[2](c, b);
	printf("%d\n", result2);

	result2 = operations[3](c, b);
	printf("%d\n", result2);


	return 0;
}






Character* create_character(const char* name, int level, int hp) {

	// malloc 用于动态分配堆内存
	Character* new_character = (Character*)malloc(sizeof(Character));
	// 此处只创建一个sizeof(),若创建多个 n * sizeof(); ⬆

	// 错误处理
	if (new_character == NULL) {
		perror("Failed to allocate memory for new character");

		return NULL; // 该函数执行结束
		// 创建引用的是一个指针 若为NULL 直接返回一个空指针即可 NULL
	}


	// 指定一个新的角色 
	// 动态数组定义 给结构体的成员name定义 不需要指出具体内容是多少 使用malloc
	new_character->name = (char*)malloc(strlen(name) + 1);

	if (new_character->name == NULL) {
		perror("Failed to allocate memory for new character_name");

		// 防止内存泄漏
		// 释放内存， 创建完成后 由于新建角色为空 因此需要释放
		free(new_character);

		return NULL;
	}


	strcpy_s(new_character->name, strlen(name) + 1, name);  // strcpy字符串复制
	new_character->level = level;
	new_character->hp = hp;

	return new_character;
}

// 释放内存函数
void free_character(Character* character) {
	if (character != NULL) {
		free(character->name);   // 释放名字字符串占用的内存
		free(character);
	}
}

Employee* create_employee(const char* name, int taskCount) {
	Employee* new_employee = (Employee*)malloc(sizeof(Employee));

	if (new_employee == NULL) {
		perror("Failed to allocate memory for new employee");
		return NULL;
	}

	new_employee->name = (char*)malloc(strlen(name) + 1);

	if (new_employee->name == NULL) {
		perror("Failed to allocate memory for new employee");
		free(new_employee);
		return NULL;
	}

	strcpy_s(new_employee->name, strlen(name) + 1, name);
	new_employee->taskCount = taskCount;
	new_employee->taskList = (int*)calloc(taskCount, sizeof(int));

	if (new_employee->taskList == NULL) {
		perror("Failed to allocate memory for task list");
		free(new_employee->name);
		free(new_employee);
		return NULL;
	}

	return new_employee;
}

void free_employee(Employee* employee) {
	if (employee != NULL) {
		free(employee->name);
		free(employee->taskList);
		free(employee);
	}
}

Product* create_product(int id, float price, const char* manufacturer) {

	/* 错误的写法:
	  Product p;       这个p被分配在栈上 是局部变量
	  p.id = id;
	  p.price = price;

	  return &p;

	  导致的结果：是p1的地址没变 但内容被p2取代了
	*/


	// 多级指针函数正确写法 使用malloc函数 
	// 堆
	Product* product = (Product*)malloc(sizeof(Product));

	if (product == NULL) {
		perror("Failed to allocate memory");
		exit(EXIT_FAILURE);
	}

	product->id = id;
	product->price = price;

	// 多级指针
	product->manufacturer = manufacturer;

	printf("Inside---ID: %d, Price: %.2f, Address: %p\n", product->id, product->price, (void*)product);

	return product;
}

void update_by_wholesaler(Product* product, int new_id, float new_price) {
	product->id = new_id;
	product->price = new_price;
}

void update_by_retailer(Product* product, int new_id, float new_price) {
	product->id = new_id;
	product->price = new_price;
}

const char* get_manufacturer_info(Product** product_ptr) {
	return (*product_ptr)->manufacturer;
	// (**product_ptr).manufacturer;
}

int add(int a, int b) {
	return a + b;
}


int32_t add1(int32_t a, int32_t b) {
	return a + b;
}
int32_t subtract(int32_t a, int32_t b) {
	return a - b;
}
int32_t multiply(int32_t a, int32_t b) {
	return a * b;
}
int32_t divide(int32_t a, int32_t b) {
	if (b == 0) {
		printf("Error: Division by zero!\n");
		return 0;
	}
	return a / b;
}