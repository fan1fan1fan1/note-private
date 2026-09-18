#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>   // 不知到第多少个头文件 用于写字符串型
#include <errno.h>    // 同 用于处理c引入文件时对错误的处理

int main(void) {
	// 字符串

// 单个字符
	char c = 't';
	// 很多个字符组合起来 串起来->字符串 string   一段文本


	// 'H' 'e' 'l' 'l' 'o' 对于字符串 结尾的不是'o' 是\0   \0告诉了我们字符串在哪里结束
	// 想象字符串是一个珍珠项链 \0就是扣子 连接处 开口

	char string[6] = "hello";  // 第六个数据为\0
	// ❌char strint[5] = "hello";    相当于珍珠没有串起来 散落了一地  
	// 这个问题在定义字符串的时候容易被忽略 因此在定义字符串数组的时候 不要显示着定义 要隐式定义


	// 数组 定义字符串常量const 不可修改
	char arr[] = { "hello" };
	// const char[] = { "hello" }; 定义后里面内容不能被修改 只能被读取 定义为const的内容不能被修改
	printf("%s\n", arr);


	// 指针 使用指针对字符串内数据进行修改
	char* ptr3 = "hello";
	// ptr指向数组中第一个数据 指向字符串的第一个字母h   通过ptr移动来写完整个字符串

	// 修改数组内第一个字母为w
	// ❌ptr3[0]  = 'w'; 
	arr[0] = 'w';
	printf("%s\n", arr);


	// 显式
	char str[100] = "hello";
	// H e l l o \0 \0 \0 \0.......


	char* s = "hello";
	// 当定义成这种类型时 修改会报错 ->

	const char* src = "hello";   // 使用指针定义一个不修改的字符串 一定要使用const 否则修改时会报错 烫烫烫烫烫....



	// 函数
	// strcpy_s() 
	// 将一个字符串定义到另一个字符串当中     stringcopy 

	char dest[50];
	//strcpy(dest, src);   输出dest则输出hello   但vs不支持这种输出 有溢出风险 烫烫烫烫烫.....
	// 然而将strcpy加_s处理后将可以输出 但strcpy_s 要求指明数据长度size
	strcpy_s(dest, 50, src);

	printf("src = %s\n", src);   // 定义了一个dest 又定义了一个src输出了dest的内容

	// 上述定义中的50 可以在main外使用#define SIZE 50 定义一个大小 在之后直接引用 SIZE 也是可以运行的

	// strcpy有返回值类型 类型为error_t类型
	errno_t err = strcpy_s(dest, 50, src);
	printf("err = %d\n", err);



	// strlen()
	// 计算整个字符串的长度   不需要_s

	char best[50] = "hello";

	// strcpy_s(best, 50, "Hello");

	printf("%zd\n", strlen(best));   // 输出5  best内容的字节长度

	// hello -> 5个 不包括\0    事实上有烫烫烫烫烫.....的警告
	// 想要让微软认为安全 在printf前输入 -> strcpy_s(best, 50, "Hello");

	// 安全写法
	char desq[50] = { 0 };
	const char* srcc = ", world!";
	strcpy_s(desq, sizeof(desq), "hello");     // sizeof(desq) = 50



	// strcat_s()
	// 拼接字符串    concatenate string

	char desp[50] = "Hello";
	const char* arc = ", world!\n";
	// 效果为 desp = "hello , world!"


	// 由上述案例可知 这种输入方式有安全隐患 安全写法:

	char desk[50] = { 0 };
	strcpy_s(desk, sizeof(desk), "Hello");
	// 上述两行相当于 char desk[50] = "Hello"; 但写法上歌更加安全 

	const char* crs = ", world!\n";   // 拼接字符串结果为 desk = "Hello, world"


	// sizeof(desk) desk一共定义了50个位置 hello字符串一共占了6个 剩下44个


	// strlen() 计算字符串长度
	// rsize_t 计算剩余可容纳字符长度
	rsize_t desk_size = sizeof(desk) - strlen(desk) - 1;   // - 1 为\0   
	// 该数组还能装44个字符 未溢出

	// 使用strcat()
	strcat_s(desk, desk_size, crs);   // 计算可使用的字符长度
	printf("%s", desk);



	// sprintf_s()
	// 格式化输出字符串      s printf

	// c11标准支持 _s通用 使用其他编译器也可使用_s

	// 烫烫烫烫烫 缓冲区溢出
	// hello一共有六个格子 如果内容超出了六个格子 就会溢出 烫烫烫烫烫

	char buffer[50] = { 0 };
	int number = 3;
	double pi = 3.14159;

	int ret = sprintf_s(buffer, sizeof(buffer), "Integer: %d, Double: %.2f", number, pi);
	// 效果: 把整个的%d %f格式化成一个字符串 存到buffer里
	// 但使用这种输入后 不能进行输出 要求一定要写出返回值 用于检测是否溢出 需要在前面加入 int ret

	if (ret > 0) {
		printf("Formatted string: %s\n", buffer);

		/*  整个过程运行到这里 相当于在第一行时输入
			   char buffer[50] = "Integer: 3, Double: 3.14";
			   并输出
			   但此方法更加安全
		*/
	}
	else {
		// 溢出情况
		printf("Error Formatting string!\n");
	}



	// strncpy_s() 
	// string n copy 复制 拷贝
	// 有四个参数 拷贝目标 拷贝大小 拷贝数量 最大值 

	char desv[20];
	const char* cra = "hello, world!\n";

	size_t max_copy = 10; //  hello world->10 最多要求复制10个字符

	// 输出时 需要有返回值
	errno_t result = strncpy_s(desv, sizeof(desv), cra, max_copy);

	if (result == 0) {
		// 正常情况
		printf("Copied string: %s\n", desv);
	}
	else {
		printf("Error copying string.\n");
	}



	// strncat_s()
	// string n concatenate 最多追加、拼接多少个字符

	// char desn[20] = "Hello";
	char desn[20] = { 0 };
	strcpy_s(desn, sizeof(desn), "Hello");

	/*
		直接写char desn[20] = "Hello";   会因为安全问题在后面报错 烫烫烫烫烫....

		安全写法 char desn[20] = { 0 };
				strcpy_s(desn, sizeof(desn), "Hello");
	*/


	const char* nrc = ", world!\n";

	size_t max_append = 7;  // 最多追加7个字符

	// 返回值
	int result1 = strncat_s(desn, sizeof(desn), nrc, max_append);

	if (result == 0) {
		printf("Concatenated string: %s\n", desn);
	}
	else {
		printf("Error concatenating string.\n");
	}



	// puts()  
	// 输出 替代printf() 自动换行 

	// puts与printf
	const char* str1 = "Hello!";

	puts(str1);     // 纯输出字符串
	printf(str1);   // 输出字符串 并有格式化的意思 更复杂



	// gets() 不限制长度 很容易缓冲溢出 烫烫烫烫烫....  在c11中已经被舍弃了 变成了gets_s() 更安全
	// gets_s()  输入                  scanf_s() 输入

	char butter[100];

	/*
	输出方式一
	gets_s(butter, sizeof(butter));
	printf("you entered: %s\n", butter);
	*/

	// 输出方式二 更安全
	printf("Enter a string: ");
	if (gets_s(butter, sizeof(butter)) == NULL) {
		printf("Error or end of file encountered.\n");
	}
	else {
		printf("you entered: %s\n", butter);
	}



	// strtok_s()
	// 早期 strtok安全隐患非常大
	// 按照要求分解字符串

	// 传递参数 Inout context delim(规则)

	char str2[] = "This is a sample string.";
	char delim[] = " ";   // 按照空格的规则将上述字符串拆分
	char* token;
	char* context = { 0 };    // 保存strtok_s函数在其内部位置之间的上下文指针

	token = strtok_s(str2, delim, &context);     // 参数分别为 字符串内容 分割符号或方式 修改所用的指针

	// &context -> char* context(上一行) ;  context -> char** context(此方法可能报错)   
	// context 多级指针 char** 用来保存上下文的一个指针

	while (token != NULL) {
		printf("Token: %s\n", token);  // 输出字符串中被隔开的每一段内容  -> this
		token = strtok_s(NULL, delim, &context);   // 继续上一次调用 在停下来的地方开始  -> is

		// context 保存了地址的位置 context是一个指针变量 用于连续调用保存的函数状态
	}



	// strcmp()
	// 比较两个字符串 string compare 没有下划线_s
	/*
		字符之间比较: 通过ASCII值对比，每个字母都对应ASCII的一个数字，97 - 97 = 0
					 当对比后值为0->证明相等。通过一个字符一个字符对比
					 当不相等时 后根据ASCII有大小排序
	*/

	const char* str3 = "Hello, world!";
	const char* str4 = "Hello, gugs!";

	if (strcmp(str3, str4) == 0) {
		// 说明两个字符串相等
		printf("str3 and str4 are equal!\n");
	}
	else {
		// 说明两个字符串不相等
		printf("str3 and str4 are not equal!\n");
	}


	// strncmp()
	// 在if前加入 size_t num = 7;   比较前7个字符
	//           if(strncmp(str3, str4, num) {



	// strstr()
	// 在一个字符串中查找另一个子字符串
	const char* text = "This is a simple text simple string.";    // 母字符串
	const char* sub = "simple";    // simple在text中已有 则sub称text的子字符串

	// 返回值
	char* result3 = strstr(text, sub);   // 寻找子字符串 若没有找到 则返回 NULL空

	if (result != NULL) {
		printf("Found '%s' in \"%s\" at position: %td\n", sub, text, result3 - text + 1);
	}
	else {
		printf("Sustring '%s' not found in \"%s\". \n", sub, text);
	}



	// strspn()
	// 计算两个字符串从开头开始 相同的字符数
	const char* str5 = "12345abcdefghi678910";
	const char* str6 = "12345678910";

	// 返回值
	size_t len1 = strspn(str5, str6);

	printf("%zu\n", len1);   // 输出5，    "12345"相同 



	// strcspn()
	// 计算两个字符串从开头开始 直到两个有相同字符 的前面不相同的字符的个数
	const char* str7 = "abcdef123456";
	const char* str8 = "1234567890";

	size_t len = strcspn(str7, str8);

	printf("%zu\n", len);    // 输出6 "abcdef"
	// 应用: 寻找字符串 寻找不包含某些分隔符的字符开头部分


	// 案例: 验证一个字符串是否有非法字符
	char input[] = "filename.txt";
	char invalid_chars[] = "/\\:*?\"<>|";

	if (strcspn(input, invalid_chars) < strlen(input)) {

		// strcspn相同字符小于字符串总长 即没到字符串最后一个字符就开始计入 即字符串与检验字符串有重合部分 有非法字符
		printf("Input contains invalid character.\n");
	}
	else {
		// 无非法字符
		printf("Input is valid.\n");
	}



	// 案例
	// 修改字符车串中其中一个字符
	char stri[] = "Hello";

	// 字符串指针 存储地址 通过字符串指针可以修改字符串
	char* ptri = stri;   // 保存了stri的首地址  相当于 char* ptri = &stri[0];

	ptri[1] = 'a';
	printf("%s\n", stri);


	// 指针遍历字符串
	while (*ptri != '\0') {
		// 从第一个字符 -> \0

		printf("%c", *ptri);
		ptri++;
	}


	/* 只是一个字符串是不能更改的

	char* p[] = "hello";  即使定义了一个指针变量 这个指针仍然指向了一个常量
	p[0] = "q";
	printf("%s\n",*p);

	改动无法实现 因为定义p为一个字符串常量 相当于 const char* p = "hello";

	但这种非法更改元素并不会报错 且没有输出结果

	如果定义为指针 则可以进行修改 char* p[0] = 'q';
	*/


	return 0;
}