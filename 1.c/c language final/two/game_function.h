#ifndef GAME_FUNCTIONS_H
#define GAME_FUNCTIONS_H

#include "game_struct.h"

// 定义了一些包含角色属性的函数名 并进行声明 在资源文件中 对函数进行具体描述

// 函数原型
void create_player(Player* player, const char* name, CharacterClass char_class);   // 定义玩家属性

Enemy generateEnemy(EnemyType type, int32_t level);   // 定义敌人属性


void battle(Player* player, Enemy* enemy);   // 战斗属性

void print_player_info(const Player* player);   // 玩家信息值  

void print_enemy_info(const Enemy* enemy);  // 敌人信息值

#endif // !GAME_FUNCTIONS_H
