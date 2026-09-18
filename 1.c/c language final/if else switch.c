#include <stdio.h>
#include <stdint.h>      // int16_t ，运算符
#include <inttypes.h>    // int类型最大值 , 运算符
#include <stdbool.h>     // bool类型

int main(void) {
	// if else语句
	// （一）
	uint32_t numbb = 100;

	if (numbb > 10) {
		printf("这个数大于10\n");
	}
	else {
		printf("这个数小于等于10\n");
	}




	// （二）
	float current_temperature = 35.0f;

	if (current_temperature > 30.0) {
		printf("天气热了，需要开空调冷气\n");
	}
	else if (current_temperature < 15.0) {
		printf("天气太冷了，需要开空调制暖\n");
	}
	else if (current_temperature < -15.0) {
		printf("等着冻死\n");
	}
	else {
		printf("不需要开空调\n");
	}



	// （三）
	// if嵌套-在线超市会员优惠简单判断
	// 根据用户的购物车总额和会员等级，系统提供不同等级的折扣


	/*
		1.如果用户时VIP，购物车总额超过100，提供20%折扣
		2.如果用户不是VIP，但购物车总额超过50，提供10%折扣
		3.如果用户购物车总额不超过50%，没有折扣
		4.如果用户是VIP，但购物车总额不超过100，也提供5%折扣
	*/


	double cart_total;

	bool is_vip;

	double discount_rate = 0.0;

	// 设置
	cart_total = 120;

	is_vip = true;

	// 判断
	if (is_vip) {
		if (cart_total >= 100) {   // VIP，购物车总额超过100，20%
			discount_rate = 0.20;
		}
		else {                     // VIP，不然的话
			discount_rate = 0.05;
		}
	}
	else if (cart_total >= 50) {
		discount_rate = 0.10;
	}
	else {
		discount_rate = 0.0;
	}

	printf("您的折扣为:%.2f%%\n", discount_rate * 100);


	// 过多的嵌套层次会使得代码难以阅读和维护， 尽可能避免if else嵌套循环

	// 策略模式 Strategy Pattern



	// （四）
	// 天气晴朗和场地可用的情况下，可以举行高尔夫球运动

	bool is_weather_sunny = false;  // 假如天气不晴朗
	bool is_venue_available = false;  // 假如场地可用

	// 使用逻辑AND && 来处理if-else的短路行为
	if (is_weather_sunny && is_venue_available) {
		printf("如期举行\n");
	}
	else {
		printf("活动无法举行\n");
		if (!is_weather_sunny) {
			printf("原因: 天气不晴朗");
		}
		if (!is_venue_available) {
			printf("原因: 场地不可用\n");
		}
	}




	// （五）
	// 计划晚上出去吃完饭，你的决策取决于两个条件
	// 是否有优惠券，或饭店有其他活动

	bool has_coupon = true;
	bool is_special_event = false;

	if (has_coupon || is_special_event) {
		printf("决定出去吃饭\n");
	}
	else {
		printf("在家吃饭\n");
	}




	// (六)
	// 游戏 玩家可以选择进入不同的房间 进入房间有不同的条件

	/*
		房间1：玩家需要有VIP身份
		房间2：玩家需要至少有10个金币，或者是一个特殊道具
		房间3：玩家需要有VIP身份，同时金币不能少于20
		房间4：玩家需要有VIP或特殊道具，并且金币数量不少于5
	*/


	// 玩家属性（在真实程序中可能来自于用户输入或者是游戏逻辑）
	bool is_VIP = true;
	uint32_t coins = 15;
	bool has_special_item = false;

	// 检查房间1的条件
	if (is_vip) {
		puts("玩家可以进入房间\n");
	}
	else {
		puts("玩家不能进入房间，缺少VIP身份\n");
	}
	// puts简单输出 无格式化 不需要\n

	// 检查房间2的条件
	if (coins >= 10 || has_special_item) {
		puts("玩家可以进入房间\n");
	}
	else {
		puts("玩家不能进入房间，缺少金币或特殊道具\n");
	}

	// 检查房间3的条件
	if (is_vip && coins >= 20) {
		printf("玩家可以进入房间\n");
	}
	else {
		printf("玩家不能进入房间，需要VIP身份及20金币");
	}

	// 检查房间4的条件
	if ((is_vip || has_special_item) && coins >= 5) {
		printf("玩家可以进入房间\n");
	}
	else {
		printf("玩家不能进入房间，需要VIP身份或特殊道具，及5金币");
	}




	// (七)
	// 公司内部的权限问题
	// 员工可以访问不同的系统资源，这取决于他们的职位和完成数量，权限规则如下


	/*
		1.经理manager 总是可以访问所有的资源
		2.普通员工employee 如果完成5个以上任务后，可以访问资源
		3.实习生intern            10个        ，必修经过经理的批准，才能访问资源
	*/


	uint8_t role = 2; // 1=manager 2=employee 3=intern

	uint8_t completed_tasks = 6;

	bool is_manager_approved = false; // 经理批准

	// if else


	// 经理
	if (role == 1) {
		puts("允许访问: 您是经理！");
	}
	else if (role == 2 && completed_tasks >= 5) {
		puts("允许访问，您是员工！并且达到任务数量");
	}
	else if (role == 3 && completed_tasks >= 10 && is_manager_approved) {
		puts("允许访问，您是实习生！并且达到任务数量，并得到批准");
	}

	else {
		puts("拒绝访问");
	}


	// 优化写法: 检查访问条件(规则) 降低可读性 逻辑复杂
	bool access_allowed = (role == 1) || (role == 2 && completed_tasks >= 5) || (role == 3 && completed_tasks >= 10 && is_manager_approved);

	if (access_allowed) {
		puts("允许访问");
	}
	else {
		puts("拒绝访问");
	}




	// switch else语句
	// 控制复杂的条件和分支运算

	/*
		不进行条件真假判断 符合则输出
		每个条件类型为case 类型名: ;
				  后一定要写break;
	*/

	switch (role) {
	case 1:                              // 电梯 role == 1 , manager
		access_allowed = true;
		break;                            // 跳出，到站了 下车, 结束语 
	case 2:                              // role == 2 , employee
		if (completed_tasks >= 5) {
			access_allowed = true;
		}
		break;
	case 3:                              // role == 3 , intern
		if (completed_tasks >= 10 && is_manager_approved) {
			access_allowed = true;
		}
		break;
	default:                              // 默认情况下，若都不满足
		access_allowed = false;
		break;
	}

	if (access_allowed) {
		puts("允许访问");
	}
	else {
		puts("拒绝访问");
	}




	// 条件运算符 判断效果 ? :
	uint32_t scoree = 85;

	char grade;    // grade 分级

	grade = (scoree >= 90) ? 'A' :
		(scoree >= 80) ? 'B' :
		(scoree >= 70) ? 'C' :
		(scoree >= 60) ? 'D' : 'F';

	printf("得分：%u , 等级: %c\n", scoree, grade);




	// (八)
	// 检查账户密码锁定

	uint32_t wrong_attempts = 2;  // 假设密码输入错误了四次
	bool is_locked = wrong_attempts >= 3;  // 当密码输入三次及以上错误则锁定

	if (is_locked) {
		puts("账户被锁定！");
		return 0;     // 输出 若账户被锁定了，从此行开始后面代码将无法输出
	}




	// (八)
	// 租车案例
	// 条件： age >= 21 ,驾驶经验一年及以上

	uint8_t age = 23;
	uint8_t driving_exp_years = 2;  // 驾驶经验

	if (age >= 21 && driving_exp_years >= 1) {
		puts("满足条件，租给你");
	}
	else {
		puts("滚蛋，不租");
	}

	// 优化写法
	// 卫语句：无else 无嵌套（排除项 否定写法）

	if (age < 21) {
		puts("不符合条件，年龄不足。");
		return 0;
	}

	if (driving_exp_years < 1) {
		puts("不符合条件，经验不足。");
		return 0;
	}

	// 所有的都满足
	puts("满足租车条件。");



	// 简化逻辑表达式
	// eg. 
	bool is_weekend = true;
	bool has_invitation = true;  // 如果有邀请函

	bool can_enter_club = (is_weekend && has_invitation) || (!is_weekend && has_invitation);  // 进入会场
	// 有没有周末多余 

	// 简化写法：(一）
	bool can_enter_clubb = has_invitation;

	//（二）
	if (has_invitation) {
		puts("可以进入会场！");
		// return 0;     
	}




	// 状态机
	// 管理复杂状态的转换，使用switch case
	// 枚举

	// switch红绿灯 
	uint8_t traffic_ligt_state = 2;  // 默认为红灯

	switch (traffic_ligt_state)
	{
	case 0:
		puts("红灯");
		traffic_ligt_state = 1;
		break;                       // 在break前面改变灯的状态
	case 1:
		puts("绿灯");
		traffic_ligt_state = 2;
		break;
	case 2:
		puts("黄灯");
		traffic_ligt_state = 0;
		break;
	default:
		puts("?");
		break;

	}




	// if else与switch case的区别：
	// 1. switch case要求必须是int类型 ，比if else快
	// 2. if else使用bool 有真假概念 switch case无真假之分



	// 循环
	// 开始 计数 结束
	// 作用：1.避免重复 提高效率
	//      2.处理大量内容
	//      3.灵活控制程序行为：条件不同，计次不同


	return 0;
}