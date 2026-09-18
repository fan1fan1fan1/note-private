#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>   // 不知到第多少个头文件 用于写字符串型
#include <errno.h>    // 同 用于处理c引入文件时对错误的处理

int main(void) {
	// 输入输出
	/*
		输入流input stream   输出流output stream

		buffer 缓冲区 批量读取用户的数据 并存到内存 提高效率   类似于缓存的概念

		输入流的数据会被暂存到缓冲区的内存区域
		相当于每个人要寄包裹 将包裹放到一个打包站 然后打包站将货物投放到你的目的地  缓冲区就相当于这个打包站

		标准输入 stdin 从键盘上输入数据 (scanf是一个标准输入)
		标准输出 stdout (printf, puts)

		scanf_s
		_s ->在修改字符串时 避免缓冲区溢出 从而引发烫烫烫烫烫错误
	*/

	char name[50];

	printf("Enter your name: ");
	scanf_s("%49s", name, 50);
	// 此位置50 可写为 sizeof(name) 但有一个强制类型转化为uint的警告, 标准写法: (unsigned int)sizeof(name)
	// 也可以在头文件处定义一个#define SIZE 50

	// scanf与scanf_s 区别  scanf_s要求有三个参数 : 数据内容 名称 数量(必须写)

	printf("Hello, %s!\n", name);


	// 出现某种不知名错误无法输出 但重新输入一遍就可以输出 ⬇
	char ch;
	printf("Enter a character: \n");
	scanf_s("%c", &ch, 1);
	printf("you entered: %c\n", ch);


	char sh;

	printf("Enter a character: ");
	scanf_s("%c", &sh, 1);

	printf("you entered: %c\n", sh);



	// scanf_s()返回值 提供了返回是否成功及细节
	int number1;
	int result2;

	puts("Enter an integer: ");

	result2 = scanf_s("%d", &number1);
	if (result2 == 1) {
		// 输入合法 可以输出
		printf("You entered the integer: %d\n", number1);
	}
	else if (result2 == EOF) {
		// EOF == End of file 文件标识结束 没有任何数据可以在输入流中被读取 输入流结束了 输入完毕
		// 专门用来指示文件读入读取 或输入操作已经到了数据源的末尾

		// 在终端 ctrl+c 可以结束输入 -> EOF触发

		printf("An error occurred or end of file was reached.\n");
		return 1;
	}
	else {
		printf("Invalid input for integer.\n");
		return 1;
	}



	// 文件保存
	/*
		在文件中 当输入了一段内容或数据 未进行保存时(窗口右侧会有一个点，提示为未保存)
		此时文件在电脑中和缓冲区 当保存文件触发时 文字直接被保存到内存 这是电脑存储文件的过程(流程)
		如果输入文件没有进行保存 当退出文件时 文件自动被释放 消失

		临时保存 保存到内存中 -> 缓冲区 -> 保存 -> 临时数据转换成永久数据 -> 硬盘

		流 stream 六种
		1. 文件流
			硬盘 用户用于读取与写入在磁盘上面的文件

		2. 标准L/O流
			stdio  标准输入 默认连接到键盘，用于程序输入                scanf_s()
			stdout 标准输出 默认连接到控制台(cmd)，用于程序输出         printf()
			stderr 默认连接到控制台或屏幕 专门输出错误和警告 使其能够被区分开来或者是重定向到不同的目的地

		3. 管道流
			用于进程之间的通信(IPC) 允许一个进程的输出成为另一个输入     popen()

		4. 内存流
			允许你将流与内存缓冲区关联，使得你可以向内存读取数据，就像操作文件一样   POSIX -> fmemopen

		5. 网络流
			套接字 Sockets c语言本身不支持网络编程 但可通过套接字IP网络流的数据发送传输

		6. 设备流
			打印机

		类型 FILE* stream; 包含了上述各种各样的流
	*/



	// 通过c语言读取文件 fopen_s()
	/* 参数
		1.指明参数是什么流
		2.文件名字(文件路径(地址 有*和&)，在c语言中 \\ 需要两个 表示一个'\')
		3.模式(读和写)
	*/

	// 第一步 在c中定义一个文件位置
	FILE* file_stream = NULL;
	// FILE* file_ptr = NULL;  文件流指针


   // 第二步 给这个位置创建一个字符范围 c语言可供读取的范围 不能超过的范围	
	char buffer1[3];  // 字符范围 超过3个字符就读不出来了


	// 第三步 打开文件 设定文件路径要读取的文件，设定文件操作模式
	fopen_s(&file_stream, "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt", "r");   // r "read" 读 


	// 第四步 处理报错 (若不处理 下面内容将会波浪线警告)
	 // 报错: 文件路径不对 或者文件不存在 文件出现了异常 文件没有权限访问 
	 // 查看读取文件返回值
	errno_t err1 = fopen_s(&file_stream, "D:\\22820\\Desktop\\前端 c python\\C\\目录.txt", "r");
	if (err1 != 0 || file_stream == NULL) {

		/*	printf("%d\n", err1);
			输出时若使用的是Debug窗口 当文件错误时 会弹出错误窗口 及错误类型代码
			若使用Release窗口 则不弹出窗口 直接出现错误类型
		*/

		// 对错误的处理方式
		// 此处需要引用头文件 <stdlib.h>  <errno.h>
		perror("Error opening file");
		return EXIT_FAILURE;

		// 若有错误则输出 Error opening file: 错误类型
	}


	// 读取代码 gets_s()

   // 第五步 读取文件的一行(第一行) fgets()    
	// 相当于把文件第一行的内容放到了缓冲区里
	fgets(buffer1, sizeof(buffer1), file_stream);   // 缓冲区 缓冲区大小(长度) 文件名称


	// 第六步 想要读取文件全部 读取文件全部内容
	while (fgets(buffer1, sizeof(buffer1), file_stream) != NULL) {
		printf("%s", buffer1);
	}
	printf("%s", buffer1);


	// 第七步 丢掉程序
	 // 当程序执行结束完毕后 需要处理程序 将buffer1丢掉 使内存得到释放
	memset(buffer1, 0, sizeof(buffer1));


	printf("\n");
	rewind(file_stream);  // 使指针回到第一个位置 重新输出
	/*
	   在第一次按行输出时 当循环结束 指针就停止了 因此只输出一次
	   若实现两种形式同时输出 函数rewind()
	   当第一次循环结束时 使用rewind 指针直接跑到第一个位置 重新循环
	*/


	// 第五步第六步第二种实现形式 一个字 一个字的读取 fgetc()    putchar
	int zh;

	while ((zh = fgetc(file_stream)) != EOF) {
		putchar(zh);
	}
	// fgetc()返回值是int类型 即fgetc将字符转换为了ASCII码


   // 第八步 关闭文件
	// 处理错误
	if (fclose(file_stream) != 0) {
		perror("Error closing file");   // perror -> p error 指针错误
		return EXIT_FAILURE;
	}

	// 文件读取结束 用EOF 或!=NULL
	// 只涉及读时 可以只fclose();  涉及读写时 需要写上述if


	return 0;
}