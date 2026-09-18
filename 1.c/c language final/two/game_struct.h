#ifndef GAME_STRUCTS_H
#define GAME_STRUCTS_H

#include "game_types.h"
#include "game_abilities.h"
// 在头文件中引用头文件使用 ""

// 定义一个嵌套结构体  将以上全部头文件内容进行引用
typedef struct {
	char name[50];
	CharacterClass char_class;
	Ability ability;
	int32_t level;
	int32_t health;
	int32_t exp;
}Player;

typedef struct {
	EnemyType type;
	Ability ability;
	int32_t level;
	int32_t health;
	int32_t exp;
}Enemy;

typedef struct {
	char name[50];
	ItemType type;
	int32_t power;
}ItemType;


#endif // GAMNE_STRUCTS_H
