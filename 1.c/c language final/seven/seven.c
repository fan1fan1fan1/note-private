#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>  
#include <math.h>

/*
	写成 void (*Callback)(int);         只能引用一次 不能重复引用

	写成 typedef void (*Callback)(int);
	在主函数中
	callback = 1;
	callback = 2;
	callback = 3;
	可以多次被引用
	此时callback不只是一个变量名 而是一个类型
*/
typedef void (*Callback)(int);

void traverse(int* array, int size, Callback callback);
// 函数传递了三个元素           第三个元素: ⬆ 是一个指向函数的指针
void printElement(int element);
void doubleElement(int element);


// 1.为事件定义签名
typedef enum {
	PLAYER_ATTACK,  // 玩家登记
	PLAYER_MOVE,    // 玩家移动
	EVENT_COUNT     // 事件总数
}GameEventType;
typedef void (*Handler)(const char* playerName);

// 2.制作一个机制callback 为不同的事件分发函数机制
Handler Handlers[EVENT_COUNT];  // 事件处理函数的数组 数组里的元素都是EventHandlers类型的函数指针 

// 3.注册事件处理函数
void registerHandler(GameEventType eventType, Handler handler);

// 4.分发事件
void dispatch(GameEventType eventType, const char* playerName);

// 5.定义具体事件
void handlerPlayerAttack(const char* playerName);
void handlerPlayerMove(const char* playerName);




int mainn(void) {
	int numbers[] = { 1, 2, 3, 4, 5 };

	int size = sizeof(numbers) / sizeof(numbers[0]);

	traverse(numbers, size, printElement);
	traverse(numbers, size, doubleElement);
	// ⬆ 将一个函数参入这个指针位置 
// 该指针位置 callback指向一个void返回值的int类型指针
// 回调函数: 传递给另一个函数的函数，允许在后者中调用前者(类型必须对应) 
//          能够在不同的时间点或机制下根据许哟啊执行特定的功能 

/* 函数指针和回调函数的应用:

	1.事件处理 2.异步编程 3.定时器函数 4.插件构架中的扩展点定义 5.排序算法中的自定义比较函数
	6.多线程或并发编程中的线程启动送函数 7.用户界面组件中的自定义渲染策略 8.网络请求中的新协议解析器
	9.状态机实现中的状态转化触发器 10.资源管理器中的资源释放策略回调
*/


// 事件处理Event Handing Framework案例 
// 事件处理框架
/*
 组织一场派对 你是主人 比如有人敲门(事件 Event) 你要去开门(根据这个特定事件你要做的行动 Action Function)
 当音乐停止(Event) 你要切换下一个音乐(Action)

 Event -> Function  函数指针

 1.定义事件类型和事件处理函数签名：首先我们定义游戏中可能发生的事件类型，以及处理这些函数的签名
 2.实现事件注册和分发机制：实现一个机制，允许为不同类型的事件注册处理函数，并且在相应的事件发生时调用这些函数
 3.定义事件处理函数: 现在我们为游戏中的每一种事件类型定义具体的时间处理函数
 4.在游戏中使用事件处理系统: main中注册事件处理函数，并且模拟事件的发生来演示系统的工作流程
*/


// 6.调用 注册事件处理函数
	registerHandler(PLAYER_ATTACK, handlerPlayerAttack);
	registerHandler(PLAYER_ATTACK, handlerPlayerMove);

	dispatch(PLAYER_ATTACK, "Hero");
	dispatch(PLAYER_MOVE, "Hero");



	/* 头文件 索引卡
	1.组织性
	2.重用性
	3.编译效率
	4.避免重复包含

	外部依赖项 -> 头文件 -> 新建 头文件名.h
	资源文件 -> 头文件名.c
	注意这两个头文件名要相同 (重要)

	# ifndef 头文件名
	...
	# endif // 头文件名

	*/




















	return EXIT_SUCCESS;
}

void traverse(int* array, int size, Callback callback) {
	// 用于遍历
	for (int i = 0; i < size; i++) {
		callback(array[i]);
		/*
			该说明作用：
			callback可以效果为
			printElement();
			doubleElement();
			意味着callback可以为任意种函数
		*/
	}
}

void printElement(int element) {
	printf("%d\n", element);
}

void doubleElement(int element) {
	printf("%d doubled is %d\n", element, element * 2);
}


void registerHandler(GameEventType eventType, Handler handler) {
	if (eventType < EVENT_COUNT) {
		Handlers[eventType] = handler;
	}
}

void dispatch(GameEventType eventType, const char* playerName) {
	if (Handlers[eventType] != NULL) {
		Handlers[eventType](playerName);
	}
	// 如果evertType合法 就传入handler到Handlers中对应的eventType的位置
}

void handlerPlayerAttack(const char* playerName) {
	printf("%s attacks!\n", playerName);
}

void handlerPlayerMove(const char* playerName) {
	printf("%s moves!\n", playerName);
}
