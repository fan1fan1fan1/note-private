#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdbool.h>


// 递归
uint32_t factorical(uint32_t n);


// 斐波那契函数
uint32_t fibonacci_iterative(uint32_t n);


// 全局变量 共享数据 1.定义一个globalVar为100
int globalVar = 100;
void demonstrateGlobalVariable(void);


// 静态变量
void increment_counter(void);


// 全局静态变量
int g_static_var = 10;

void access_g(void);


// 静态全局变量 仅在本文中可见 在其他文件中不能使用
// static int g_static_var = 10;


// 寄存器
void demo_reg_var();


// 块作用域
void demo(void);




int main(void) {


	// 递归
	// 套娃 无限套娃 一层一层进来 并进行检查修改 最后一层一层退出

	// 阶乘 5！ 1*2*3*4*5      0！ 1

	// 输入了一个数字5 执行下方函数
	uint32_t number = 5;

	printf("%u的阶乘是 %u\n", number, factorical(number));



	// 例子 斐波那契数列 递推关系 F(0)=0  F(1)=1  F(n)=F(n-1)+F(n-2)
	uint32_t shuzi = 10;  // 55
	printf("%u 项: %u\n", shuzi, fibonacci_iterative(10));



	// void greet();   可以传递参数
	// void greet(void); 不能传递参数 有警告  JAVA则直接报错



	// 作用域 
	// 一个函数内，一个文件内，整个程序内 (配置文件)
	// 一个函数内的变量有效范围: 局部作用域 local scope
	// 一个函数内有效范围内变量，或者局部作用内的变量，局部变量

	// 在声明函数外 整体中 全局变量 global scope


	// 链接性 linkage
	// 块作用域 block scope

	int a = 10;         // 'a'具有块作用域 仅在demo()中可见

	if (a > 5) {
		int b = a + 5;  // 'b'也具有块作用域 仅在if语句中 
	}

	// 在函数内部 函数作用域 function scope

	// 内部链接 该文件内链接
	// 外部链接 从其他文件引用该文件内的东西
	// 无连接 只在一个函数内实现 



	// 生命周期 last time
	// 从变量被创建(初始化) 到变量被销毁(或被回收)的整个过程
	// 函数被创建->函数获得生命   函数执行完毕->生命结束

	// 全局变量 -> 内存泄漏 访问已经被销毁的变量(悬挂引用)，过度消耗资源



	// 局部变量 local variables
	// 作用域限定 

	// 局部变量通常具有 自动存储期
	// 即当主部分存在函数的变量时 函数会调用这个变量 这个变量在函数中会被自动创建

	// 局部变量的初始值是没有被定义的  初始值未定义 -> 所占内存值不会被清零 
	// 当变量被调用后 所占内存会被回收 即函数生命结束



	// 全局变量声明 
	// 跨越函数边界 共享数据
	// 减少函数的参数 使用全局变量可以减少需要传递给函数的参数数量 简化调用 


	// 例 定义一个globalVar
	globalVar++;
	demonstrateGlobalVariable();

	// 在main函数中访问全局变量
	// 此时 globalVar值为101

	printf("Global variable in main: %d\n", globalVar);


	// 程序范围内的可见性
	// 静态存储期
	// 默认初始化 全局变量若没有初始化 则视为初始化值为0 默认指针初始化为NULL

	// 使用过多全局变量 降低可读性 增加错误风险



	// 线程安全问题: 在多线程环境中，未加锁的全局变量可能会导致数据竞争和不一致 



	// 静态变量 static varables
	for (int i = 0; i < 3; i++) {
		increment_counter();
	}


	// 静态全局变量
	printf("Main before : %d\n", g_static_var);
	// 输出结果为15



	// 全局变量可以在全部文件中使用 
	// 若在其他文件中引用全局变量 在其他文件中需要引用关键字 extern int 变量名;
	// 通过extern关键字声明对外部文件的全局变量的访问



	// 寄存器  使用register关键字
	// CPU用来暂时存储一些数据 在CPU里的一个小的空间

	// 声明寄存器变量
	// 我们建议编译器，尽可能将counter放在寄存器中
	demo_reg_var();

	// 编译器不一定会把变量放在寄存器中 寄存器会自己决定 选择性





	return 0;
}







// 递归函数
uint32_t factorical(uint32_t n) {

	if (n == 0) {
		return 1;
	}
	else {

		// 尾递归
		return n * factorical(n - 1);
		// return 5 * f(4)
			// return 4 * f(3)
				// return 3 * f(2)
					// return 2 * f(1) 
						// return 1 * f(0) -> n == 0 结束
							// return 1

		//返回这个数乘以这个数减一 输入一个5 一次返回4 3 2 1 并与5相乘
	}
}



// 上一个函数另一种写法 
/*
  uint32_t factorical(uint32_t n, uint32_t acc) {
	if (n == 0) {
		return 1;
	}
	else {

		// 尾递归

		 return factorical(n - 1, n * acc);

		// 返回值为递归值 return acc

		// return f(4, 5)
			// return f(3, 20) 此处递归的acc为上一次套用的结果
				// return f(2, 60)
					// return f(1, 120)
						// return f(0)
							// return 1

		// 4 5 套进来之后变成了 4->n 5->acc
		// 3->n 20->acc
		}
 }
*/



// 循环调用多次 性能不好
// win11 编译器  MSVC微软编译器
// 编译器 Clang GCC 编译原理: 讲解尾递归优化方法



// 斐波那契函数
uint32_t fibonacci_iterative(uint32_t n) {
	if (n <= 1) {
		return 0;
	}

	uint32_t fib_n_minus_2 = 0;   // 数列第0项
	uint32_t fib_n_minus_1 = 1;   // 数列第1项

	uint32_t fib_n = 0;           // 定义当n>=2 时 首次位置为0 则有

	for (uint32_t i = 2; i <= n; ++i) {
		fib_n = fib_n_minus_1 + fib_n_minus_2; // 递推关系 F(n)=F(n-1)+F(n-2)

		fib_n_minus_2 = fib_n_minus_1;  // 第二次循环时 fib_n_minus_2替代上一次的fib_n_minus_1
		fib_n_minus_1 = fib_n;          // 第二次循环时 fib_n替代上一次的fib_n_minus_2
	}
	return fib_n;  // 返回 fib_n 重复该递推关系式 至 n<=1 结束
}



// 访问全局变量
void demonstrateGlobalVariable(void) {
	globalVar++;
	//访问全局变量
	printf("Global variable inside function: %d\n", globalVar);

	// 此时globalVar值为102
}



// 静态变量
void increment_counter(void) {

	// 静态局部变量
	// 只在调用函数的时候使用
	static int counter = 0;

	// 静态局部变量在函数内部声明，并且程序的期间只初始化一次 
	// 即使函数调用结束 静态变量的值也不会消失 而是保持在下次函数的调用 跨函数调用保持着状态和计数

	counter++;

	printf("Counter: %d\n", counter);

	// 若是变量 输出结果为 1 1 1
	// 静态局部变量 输出结果为 1 2 3
}


// 静态全局变量
void access_g(void) {

	g_static_var += 5;   // 使 a + 5 然后再赋值给a   10 + 5 -> 15

	printf("Inside access global var : %d\n", g_static_var);
	// 输出结果为15
}



// 寄存器
void demo_reg_var(void) {
	register int counter;

	for (counter = 0; counter < 10; counter++) {
		printf("%" PRId32 "\n", counter);
	}
	// 不能使用&counter获得地址 寄存后放在寄存器里再内存里不显示 不能取地址
}



// 块作用域
void demo(void) {

	// 函数注释

/* 中间有 * 且顶格 中间不能空格
*  注释尽可能写成英文 不开发国际项目可使用中文
*
*
* 格式:
*  1.第一块 简写一个函数名称和用途 简单功能介绍
* - *******
*
*  2.第二块 Parameters:
* - 参数有哪些 参数代表意义是什么
*
*  3.第三块 Returns:
* - return + 返回值内容;
*
*  4.第四块 Notes:
* - The function uses *******
*
*/
}