// 用于写自定义头文件的主函数及函数运行 格式如下


#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>  
#include <math.h>

#include "math_operations.h"

// 比较函数 比较两个数
int compare_ints(const int a, const int b);

// 如果比较两个结构体 比较两个函数指针 则上方函数可适用性低 
// 因此我们使用泛型编程 高可用    void*意味着可以接受任何类型
int compare_value(const void* a, const void* b);

// 对数组进行排序
void generic_sort();



int main(void) {
	int result = add(1, 3);
	printf("%d\n", result);


	// 排序算法中的自定义比较函数
	/*
		设计概述: 1.抽象层
				 2.策略模式
				 3.模块化
				 4.安全性和跨平台
	*/

	// 泛型编程 (解释案例 比较两个数)
	int num1 = 1;
	int num2 = 2;
	printf("%d\n", compare_value(&num1, &num2));   // 输出-1



	return EXIT_SUCCESS;
}

int compare_ints(const int a, const int b) {
	if (a < b) return -1;
	if (a > b) return 1;
}

// 泛型编程 int类型展示 强制转换成int类型
int compare_value(const void* a, const void* b) {
	int arg1 = *(const int*)a;
	int arg2 = *(const int*)b;
	if (arg1 < arg2) return -1;
	if (arg1 > arg2) return 1;

	return 0;
}
