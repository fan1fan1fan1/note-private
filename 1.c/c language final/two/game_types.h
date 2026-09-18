#ifndef GAME_TYPES_H    // 定义职业
#define GAME_TYPES_H

// 第一步定义了一个头文件 game_types.h

/* 固定格式
			#ifndef 定义的名称
			#define 定义的名称

			#include
			主体内容

			#endif // 定义的名称
*/

// 定义结构体
typedef enum {
	Warrior,   // 战士
	Mage,      // 法师
	Rogue      // 流氓
}CharacterClass;

typedef enum {
	Goblin,    // 妖怪
	Troll,     // 巨魔
	Dragon,    // 巨龙
}EnemyType;

typedef enum {
	// 武器装备道具
	WEAPON,
	POTION,
	ARMOR
}ItemType;

typedef enum {

};





#endif 
