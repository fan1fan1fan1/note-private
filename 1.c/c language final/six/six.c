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

void read_config_safe(const char* file_name);
void append_log_safe(const char* filename, const char* msg);
void clear_log(const char* filename);

typedef struct GameSettings {
	float volume;
	int resolution_x;
	int resolution_y;
	int difficulty;
}GameSettings;
void save_game_settings(const GameSettings* settings, const char* filename);
void load_game_settings(GameSettings* settings, const char* filename);

int main(void) {
	// 写入文件
	FILE* file_ptr = NULL;

	// 定义错误
	errno_t err = fopen_s(&file_ptr, "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt", "w");
	// w会把文件内容全部销毁覆盖 再写入

	if (err != 0 || file_ptr == NULL) {
		perror("Failed to open file");
		return EXIT_FAILURE;

		// 文件没能成功打开出现错误
	}

	// fputc()    fputs()    fprintf_s()    用于写入函数

	fputc('H', file_ptr);   // 写入单个字符
	fputc('i', file_ptr);
	fputc('\n', file_ptr);

	fputs("This is a line written by fputs.\n", file_ptr);   // 写入一行字符

	double pi = 3.14;
	fprintf_s(file_ptr, "Numbers: %d, %lf, %s\n", 10, pi, "End of example.");    // 格式化写入



	// r+ 读取后可以进行操作

	// ftell fseek rewind

	// 使用ftell 获取当前文件指针的位置 -> 第一行位置为0 第二行位置为1
	// ftell 返回值是long
	long position = ftell(file_ptr);       // 获取指针位置
	printf("当前位置: %ld\n", position);    // 输出

	// 开始读取
	char buffer[100];
	if (fgets(buffer, sizeof(buffer), file_ptr) != NULL) {
		// 第一次获取第一行指针位置并读取 下标从0开始
		printf("从文件读取: %s", buffer);

		// 再次使用ftell获取新的位置 获取第二行 
		// 到第二行使下标为4 第一行 0、换行符 算两个位置
		position = ftell(file_ptr);
		printf("读取后的新位置: %ld\n", position);
	}

	// 使用fseek函数 移动到文件开始
	// 当执行完上述语句后 光标即刻恢复到第一行首位
	fseek(file_ptr, 0, SEEK_SET);
	// fseek自带宏定义 SEEK_SET

	printf("使用fseek后移动到开始位置, SEEK_SET = 0 : %ld\n", ftell(file_ptr));  // 调用函数ftell() 获取当前指针的位置

	// 使用rewind 重新输出
	rewind(file_ptr);
	printf("使用rewind直接移动到开始位置: %ld\n", ftell(file_ptr));


	// 关闭文件
	fclose(file_ptr);

	puts("File '目录.txt' has been written successfully.\n");



	// fscanf_s 
	// 从流中 格式化读取数据 
	// 把文件fscanf到缓冲区 要有_s   fprintf: 把文件从缓冲区输入到文件
	/*
		定义一个文件位置

		获取文件file

		定义错误err

		读取:
		if(err) {
			printf_s("The file fscanf.out was not opened\n");
		}
		else{
		// 分不同情况出现的错误

			if(fscanf_s(stream, "%80s", s, (unsigned)_countof(s)) !=1) {
										  // ⬆ 强制类型转换
			printf("读取字符串失败!\n");
			}

			if(fscanf_s(stream, "%lds", &1) != 1) {
				printf("读取id失败!\n");
			}

			if(fscanf_s(stream, "%f", &fp) != 1) {
				printf("读取lf失败!\n");
			}

			if(fscanf_s(stream, " %c", &c, 1) != 1) {
				// %c 前要有一个空格否则读不出来

				printf("读取c失败!\n");
			}

			// 开始读取
			printf("%s", s, (unsignde)_countof(s));
			printf("%ld", &l);
			printf("%f", &fp);
			printf("%c", 1);
		}
	*/



	// fprintf()
	/*
		FILE* 定义指针
		定义类型

		定义错误

		if(err != 0) {
			printf_s("无法打开文件进行写入操作!\n");
			return EXIT_FAILURE;
		}

		定义类型
		// 写入文件 此时文件中真正的内容会随着fprint改变 终端中输出什么 打开文件的内容就会是什么

		frintf(指针名称, "内容"， 名称);
		fprintf(stream, "ID %d\n", id);
		fprintf(stream, "Name: %s\n", name);
		fprintf(stream, "Temperature: %.lf\n", temperature);
		fprintf(stream, "Grade: %c\n", grade);

		结束fclose

		printf("数据写入完成!\n");
		return 0;
	*/



	// 对错误的处理
	// ferror feof -> 错误检查
	// clearerr -> 清除错误 

	// ferror 检查文件是否有错误发生如果有错误返回一个非零值 
	// feof 检查文件流是否达到文件末尾UF 如果文件指针达到了末尾 返回一个非零值 常用于检查循环是否达到末尾
	// clearerr 清除与文件流相关的错误和标志 错误标志: 两个函数都输出了同样的错误 -> 错误标志 

	char buffer1[100];

	while (fgets(buffer1, sizeof(buffer1), file_ptr) != NULL) {
		printf("%s", buffer1);
	}

	if (ferror(file_ptr)) {
		// ferror 错误检查
		printf("读取文件时发生了错误!\n");

		// clearerr 清除错误
		clearerr(file_ptr);

		// ferror 文件进行到一半出现错误 在执行过程中出现错误
	}


	if (feof(file_ptr)) {
		// feof 错误检查
		printf("已经到达文件的末尾...\n");
	}
	else {
		printf("文件未到达末尾，可能发生错误!\n");
	}

	fclose(file_ptr);



	// 函数形式写入文件
	const char* file_name = "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt";
	read_config_safe(file_name);



	// "r" 读        "r+" 便携读取写入 文件必须存在     
	// "w" 替换      "w+"  在空文件中读取写入 若不是空文件无效 

	// "a" 末尾追加 使用fseek rewind

	// 读取一个已存在的文件
	const char* config_filename = "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt";

	// 定义一个用来追加的空文件
	const char* log_filename = "D:\\22820\\Desktop\\前端 c python\\C\\log.txt";

	read_config_safe(config_filename);

	const char* str = "select * from students";

	append_log_safe(log_filename, str);
	// 此时会在空文件所写位置上创建了一个log.txt文件  内容是追加后的内容


	// 最后一个环节 将所有的流全部关闭
	int numclosed = _fcloseall();
	printf("Number of files closed by _fcloseall: %u\n", numclosed);



	// "w" 在企业中常用于销毁文件
	clear_log(log_filename);



	// fflush(); 调用该函数 将缓冲区内容立刻保存到内存
	// 相当于 输入代码 代码进入缓冲区 点击ctrl+s 代码即刻进入内存
	// 用于错误日志



	// fread
	// fwrite   四个参数：  指向缓冲区的指针 数据量大小 读取数据的数量(重复次数) 文件指针
	// GameSettings 读写二进制 主要用于处理二进制文件

	// 写二进制
	GameSettings settings = { 0.75, 1920, 1000, 2 };
	//	save_game_settings(&settings, "D:\\22820\\Desktop\\前端 c python\\C\\game_settings.bin");  
		// 给这个文件定义路径及名称  则在该路径新建了一个文件 该行运行一遍即可


		// 加载
	GameSettings loaded_settings;
	load_game_settings(&loaded_settings, "D:\\22820\\Desktop\\前端 c python\\C\\game_settings.bin");

	printf("游戏设置已经加载!\n");
	printf("音量: %f\n分辨率: %dx%d\n难度: %d\n",
		loaded_settings.volume,
		loaded_settings.resolution_x,
		loaded_settings.resolution_y,
		loaded_settings.difficulty);
	// 分别定义 音量 xy坐标 难度



	// 复制文件
	FILE* source_file, * target_file;  // 定义两个指针

	char source_path[] = "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt";      // 取一个文件
	char target_path[] = "D:\\22820\\Desktop\\前端 c python\\C\\frank.txt";     // 定义一个文件
	// 把目录复制进frank.txt

	char buffer2[1024];

	size_t bytes_read;

	errno_t err1 = fopen_s(&source_file, source_path, "rb");   // 二进制 读source
	if (err1 != 0 || source_file == NULL) {
		perror("无法打开源文件");
		return EXIT_FAILURE;
	}

	err1 = fopen_s(&target_file, target_path, "wb");           // 二进制 写target
	if (err1 != 0 || target_file == NULL) {
		perror("无法打开目标文件");

		fclose(source_file);

		return EXIT_FAILURE;
	}


	// 循环两个文件流
	while ((bytes_read = fread(buffer2, 1, sizeof(buffer2), source_file)) > 0) {
		fwrite(buffer2, 1, bytes_read, target_file);
	}

	_fcloseall();

	puts("文件复制完成!\n");


	return 0;
}

void read_config_safe(const char* file_name) {
	FILE* file_ptr = NULL;
	errno_t err = fopen_s(&file_ptr, file_name, "r");     // 定义一个错误 
	// 使用fopen打开文件 传入指针信息 (三个标准格式信息)


	// 企业对于文件错误的标准写法
	if (err != 0 || file_ptr == NULL) {

		// 当输出错误时 返回标准错误流 stderr
		// 正常输出没有错误时 err = 0 file_ptr != NULL 若输出结果不正常 执行下方if语句 用于存储错误信息

		char error_msg[256];

		strerror_s(error_msg, sizeof(error_msg), errno);
		// 错误信息 包括(发生错误位置的目标数组 错误大小 系统设置错误码)

		fprintf(stderr, "Failed to open config file for reading: %s\n", error_msg);   // 操作屏幕
		// 调用 stderr将信息输出到标准错误流 格式化字符串 输出错误结果及错误原因

		// 此时不适合使用return退出函数 我们使用exit
		exit(EXIT_FAILURE);
	}

	// 文件输入正确 输出
	char buffer[256];
	while (fgets(buffer, sizeof(buffer), file_ptr) != NULL) {
		printf("%s", buffer);
	}

	fclose(file_ptr);
}


void append_log_safe(const char* filename, const char* msg) {
	FILE* file_ptr = NULL;

	errno_t err = fopen_s(&file_ptr, filename, "a");

	if (err != 0 || file_ptr == NULL) {
		char error_msg[256];

		strerror_s(error_msg, sizeof(error_msg), errno);

		fprintf(stderr, "Failed to open log file for appending: %s\n", error_msg);

		exit(EXIT_FAILURE);
	}

	fprintf(file_ptr, "%s\n", msg);

	fclose(file_ptr);
}


void clear_log(const char* filename) {
	FILE* file_ptr = NULL;

	errno_t err = fopen_s(&file_ptr, filename, "w");

	if (err != 0 || file_ptr == NULL) {
		char error_msg[256];

		strerror_s(error_msg, sizeof(error_msg), errno);

		fprintf(stderr, "Failed to open config file for reading: %s\n", error_msg);

		exit(EXIT_FAILURE);
	}

	// 文件已经打开为"w"模式 我们什么都不操作，文件内容会被清空，无须写入任何内容
	fclose(file_ptr);
}


void save_game_settings(const GameSettings* settings, const char* filename) {
	FILE* file;
	errno_t err = fopen_s(&file, filename, "wb");    // wb二进制字节 读

	if (err != 0 || file == NULL) {
		perror("无法打开文件进行写入操作");
		return;
	}

	fwrite(settings, sizeof(GameSettings), 1, file);
	fclose(file);
}

void load_game_settings(GameSettings* settings, const char* filename) {
	FILE* file;
	errno_t err = fopen_s(&file, filename, "rb");    // rb二进制字节 写

	if (err != 0 || file == NULL) {
		perror("无法打开文件进行读取操作");
		return;
	}

	fread(settings, sizeof(GameSettings), 1, file);
	fclose(file);
}