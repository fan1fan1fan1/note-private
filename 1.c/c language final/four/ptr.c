#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdbool.h>


// 使用指针查找数组索引号
bool find_index_of_vallues(const int32_t* array, size_t size, int32_t target_vallue, size_t* index);



int main(void) {
	// 地址 address
	// 唯一标识内存中数据存储的位置

	// 取地址

	int building_floors[5] = { 101,102,103,104,105 };

	int target_floor = 103;    // 快递员需要找到的目标用户

	int found = 0;             // 标记是否找到目标用户

	printf("快递员开始在大楼中寻找 %d...\n", target_floor);

	for (int i = 0; i < 5; i++)
	{
		if (building_floors[i] == target_floor) {
			printf("快递员找到了楼层 %d 的地址: %p\n", target_floor, (void*)&building_floors[i]);
			// * 取地址符

			found = 1;
			break;
		}
	}

	if (!found) {
		puts("快递员没有找到该住户!");
	}


	// 输出所有住户的地址
	for (int i = 0; i < 5; i++) {
		printf("住户 %d 的地址: %p\n", building_floors[i], &building_floors);
		// %p 信号p
		// &building_floors 取地址符
	}
	// 数组一旦创建 里边的数据必须是连续的 输出结果为16进制

	// 根据输出结果可知 将101住户的地址 + 四个字节 -> 102住户的地址 (int数据类型占四个字节)



	// 指针
	// 指针是一种特殊的变量 指针不存储具体的数值 指针只存储数据变量的地址

	// 就像快递员的地图上的标记 每个楼层的门牌号(地址)

	// ptr_floor_103 -> (指向) &building_floors[2]
	int* ptr_floor_103 = &building_floors[2];
	// 意为用地址为103的用户地址 被存储到了ptr_floor_103的变量里 

	// ptr_floor_103 的数据类型为 int* 整型指针

	// 输出103用户的地址
	printf("&building_floors[2]的地址是: %p\n", &building_floors[2]);
	printf("ptr_floor_103指针变量保存的地址是: %p\n", (void*)ptr_floor_103);


	// printf("快递员通过 *(指针相当于一个地图工具) 它带着ptr_floor_103这个指针变量(它存储了业主的地址) 去寻找...\n");
	// printf("于是它找到了...%d\n", *ptr_floor_103);

	// 不带* 意为一个地址名词 %d
	// 带*   意为快递员带着地址在找你的动作 最后找到了 %p 



	// 指针与修改
	// 新的要求: 快递员找到你了 ... 你要求快递员: 我要搬家了，我会搬到106 -> 快递员返回给后台 更改地址位置
	int* ptr_new_106 = ptr_floor_103;

	*ptr_new_106 = 106;

	// 输出结果
	printf("building_floors[2] = %d\n", building_floors[2]);

	// 外挂最基本的原理 原理 通过外部的操作修改代码内部的东西
	// 指针可以通过外部服务进行更简单的处理   外部服务器的访问


	// 权限: 指针把数据的地址交给程序员进行修改



	// *的位置

	// int* p;  微软写法，表明强调p这个变量是一个int* (整型指针) 类型的变量
	// int *p;  强调这个变量是一个指针0

	int* p, q;        // p为int* 类型    q为int类型 int    *p，q同理
	int* p1, * q1;    // p q 都为int*

	int value = 100;
	p = &value;       // p保存了value的地址
	q = 123;

	printf("通过指针p访问的值: %d\n", *p);
	printf("变量q的值: %d\n", q);



	// 快捷方式 -> 指针    快捷方式就是保存一个程序地址    *快捷方式
	// 在桌面上双击快捷方式 -> 软件真正的地址 


	// 指针也有地址 快递员也有家
	// 指针保存的是数据的地址



	// 野指针: 指向了一个无效地址或已经释放的地址的指针  即该数据已经搬家了 不见了 删除了 
	// 访问野指针非常危险 进入野指针后会访问一个不可描述的空间 一个不可预测的行为



	// 空指针: 没有指向任何楼层的地址

	uint32_t* ptr_to_floor = NULL;

	if (ptr_to_floor == NULL) {

		printf("没有指定楼层的地址\n");

		// shortout 不做任何处理 即双击没有反应
	}
	else {
		printf("楼层的地址是:%p ,楼层号: %d\n", (void*)ptr_to_floor, *ptr_to_floor);
	}


	// 若给该指针增加一个地址
	uint32_t* ptr_to_floor1 = NULL;

	uint32_t number1 = 100;     // 增加一个数据number

	ptr_to_floor1 = &number1;   // 把number的地址给ptr_to_floor1

	if (ptr_to_floor1 == NULL) {
		printf("没有指定楼层的地址\n");
	}
	else {
		printf("楼层的地址是:%p ,楼层号: %d\n", (void*)ptr_to_floor1, *ptr_to_floor1);
	}




	// 指针的算术运算
	// 使用数组计算

	uint32_t numbers[] = { 10,20,30,40,50,60,70,80,90,100 };
	int* ptr = &numbers;  // = &numbers[0] = 10



	/* 取地址取的是某一个数据
		若没有说明取的是数组中的哪一个元素 默认为第0个元素 即取数组的首元素地址 -> &numbers[0];   10

		数组在内存当中是连续的   numbers(数组名)表示一个地址 起始地址(即数组首元素地址 numbers[0])
		10 -> (地址为) 000000090    20 -> 000000094 每个数据是连续的 并相差4个字节    30 -> 000000098
		下一个数据的地址就是上一个数据+单位长度

		使用数组进行指针计算时 没有必要指出每一个数据的地址 每个数据的地址相差4 用差数来表示
		即计算时 只需要找到首地址 就可以进行指针计算
	 */




	 // 计算数组的大小
	int size = sizeof(numbers) / sizeof(numbers[0]);

	// sizeof(numbers) 计算整个数组所占用的内存大小 单位是字节 会返回整个数组的空间所占大小
	// sizeof(numbers[0])  计算第一个元素的大小 单位是字节

	printf("size = %d\n", size);
	printf("size = %" PRIu32 "\n", size);



	// 输出数组元素
	printf("数组原始数据\nnumbers[] = {");

	for (uint32_t i = 0; i < size; i++) {
		printf("%" PRIu32 "", numbers[i]);
	}

	printf("}\n");  // 美观
	for (uint32_t i = 0; i < size; i++) {
		printf("numbers[%d]", numbers[i]);
	}



	// 使用指针加法移动格子 右移
	printf("使用指针加法访问第五个元素: \n");

	ptr += 1;    // 原本指针在首地址(10) ptr += 1 -> 往后越一个格子 越4个字节 -> 20

	printf("numbers[ptr += 1] : %d\n\n", *ptr);  // 输出结果为 数组中数据20的地址


	// 使用指针减法移动格子 左移
	ptr -= 1;

	printf("回到第一个元素numbers[ptr -= 1] : %d\n\n", *ptr);



	// 指针之间的减法 计算距离
	int* start_ptr = &numbers[0];

	int* end_ptr = &numbers[size - 1];   // size 每个数据作占大小 - 1 -> 输出第九个数据的地址(最后一个数据) 

	printf("数组首尾之间的距离是: %td\n\n", end_ptr - start_ptr);
	// 输出结果为 最后一个数据地址和首数据地址间距离

	// 使用vs输出两个指针相减 输出结果不是int类型32位 -> 64位 不能使用%d 使用%td
	// 指针相减 输出类型为 ptrdif 类型 专门用来表示两个指针间距离的类型 使用%td  
	// 此时使用输入类型通常为long int 类型(64位)



	// 指针之间的比较
	puts("比较指针指向的元素: ");

	if (start_ptr < end_ptr) {
		puts("start_ptr 指向的元素在 end_ptr 所指向的元素之前\n");
	}
	else {
		puts("start_ptr 指向的元素在 end_ptr 所指向的元素之后\n");
	}


	// 使用指针遍历数组
	puts("使用指针遍历数组:");

	for (int* p = start_ptr; p <= end_ptr; p++) {
		printf("%d ", *p);
	}

	printf("\n\n");


	// 使用指针减法逐个访问数组中的每个元素的反向顺序
	printf("使用指针减法逐个访问数组中的每个元素的反向顺序*p = { ");

	for (int* p = end_ptr; p >= start_ptr; p--) {
		printf("%d ", *p);
	}

	printf("}\n\n");


	// 指针加减整数访问特定元素
	puts("指针加减整数访问特定元素:");

	int offset = 3;

	printf("第四个元素(使用加法) : %d\n\n", *(start_ptr + offset));

	// 回退到第二个元素
	printf("回退到第三个元素(使用减法) : %d\n\n", *(start_ptr + offset - 1));


	// 比较两个指针
	int* middle_ptr = &numbers[size / 2];    // 指向数组中间的元素 数组中值地址

	printf("比较两个指针指向的位置:\n");

	if (start_ptr < middle_ptr) {
		printf("start_ptr 指向的元素在 middle_ptr 所指向的元素之前\n");
	}
	else {
		printf("start_ptr 指向的元素在 middle_ptr 所指向的元素之后\n");
	}



	// 案例
	// 数组与size_t与指针的使用


	// 数组名作为指针的使用
	int32_t arrays[] = { 10,20,30,40,50,60,70,80,90,100 };

	// 直接把数组名字给指针，就相当于把数组首地址(index = 0)给它
	int32_t* ptr1 = arrays;      // &arrays 

	size_t arrays_size = sizeof(arrays) / sizeof(arrays[0]);

	// size_t 无符号的整数类型 
	// 专门用于表示数据大小 长度和索引 可以避免使用%d %td的歧义 -> 直接使用size_t
	// 可以提高程序在不同平台的可移植性和安全性


	puts("输出原始数组:");
	for (size_t i = 0; i < arrays_size; ++i) {

		printf("%" PRId32 " ", arrays[i]);

		// 此位置上的++i与i++在性能上没有太大差别 ++i会比i++快 推荐使用++i 个人风格
	}
	printf("\n");

	// 通过指针增加数组的每个元素的值
	for (size_t i = 0; i < arrays_size; ++i) {

		*(ptr1 + i) += 5;  // 直接通过指针修改数组中的值  首地址+5 输出15 25 35 45 55...
	}

	printf("修改后的数组: \n");
	for (size_t i = 0; i < arrays_size; ++i) {
		printf("%" PRId32 " ", *(ptr1 + 1));
	}



	// 案例 选修
	// 指针查找特定元素的索引并返回 
	int32_t values[] = { 10, 20, 30, 40, 50 };

	int32_t* start_ptr1 = values;

	size_t values_size = sizeof(values) / sizeof(values[0]);

	int32_t target_value = 30;   // 需要寻找30的索引值
	int32_t* target_ptr = NULL;

	size_t index = 0;

	bool found1 = false;

	for (size_t i = 0; i < values_size; ++i)
	{
		if (*(start_ptr1 + i) == target_value) {
			// 我的目标数据 = 首地址 + 未知数i   -> 寻找i

			// 顺手保存目标的地址值
			target_ptr = start_ptr1 + i;

			// 找到了目标地址下表index -> 找到了i 
			index = i;

			found1 = true;
			break;
		}
	}

	if (found) {
		printf("元素 %" PRId32 " 的index: %zu\n", target_value, index);
		// %zu 专门用于输出size_t 
	}
	else {
		printf("元素 %" PRId32 " 未找到!\n", target_value);
	}



	// 优化方法: 将上述案例使用函数输出 
	int32_t vallues[] = { 10, 20, 30, 40, 50 };

	int32_t* start_ptr2 = values;

	size_t vallues_size = sizeof(vallues) / sizeof(vallues[0]);

	int32_t target_vallue = 30;   // 需要寻找30的索引值

	int32_t i;

	bool founded = find_index_of_vallues(vallues, size, target_vallue, &index);  // 调用函数

	if (founded) {
		printf("元素 %" PRId32 " 的index: %zu\n", target_vallue, index);
		// %zu 专门用于输出size_t
	}
	else {
		printf("元素 %" PRId32 " 未找到!\n", target_vallue);
	}


	return 0;

}

// 使用指针查找数组索引号
bool find_index_of_vallues(const int32_t* array, size_t size, int32_t target_vallue, size_t* index) {
	for (size_t i = 0; i < size; ++i)
	{
		if (*(array + i) == target_vallue) {
			*index = i;
			return true;
		}
	}
	return false;   // else
}

