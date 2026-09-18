#include "game_function.h"

#include <stdio.h>
#include <string.h>
#include <errno.h>


// 引用 定义的头文件 game_function.h 
void create_player(Player* player, const char* name, CharacterClass char_class) {
	errno_t err;

	err = strncpy_s(player->name, sizeof(player->name), name, _TRUNCATE);

	if (err != 0) {
		printf("Error copying name: %d\n", err);
	}

	// 确保字符串以NULL结尾


	player->char_class = char_class;
	player->level = 1;
	player->health = 100;

	// 根据角色初始化特定能力
	switch (char_class) {
	case Warrior: player->ability.strength = 10;
		break;
	case Mage: player->ability.mana = 50;
		break;
	case Rogue: player->ability.stealth = 30;
		break;
	}
}

Enemy generateEnemy(EnemyType type, int32_t level) {
	Enemy enemy;
	enemy.type = type;
	enemy.level = level;
	enemy.health = level * 20;  // 假设敌人的健康是等级的两倍

	switch (type) {
	case Goblin: enemy.ability.strength = 5 * level;
		break;
	case Troll: enemy.ability.strength = 10 * level;
		break;
	case Dragon: enemy.ability.mana = 100.0f * (float)level;   // 强制类型转换
		break;
	}
	return enemy;
}

void battle(Player* player, Enemy* enemy) {
	// 战斗
	printf("%s encountersv a level %d %d! A battle begins... \n", player->name, enemy->level, enemy->type);

	// 假设战斗总能赢
	player->exp += 50;   // 每次获胜玩家经验值+50
	printf("%s has defeated the enemy and gained 50 exp points!\n, player->name");   // 玩家打败了敌人并获得了经验值
}

// 战斗结束后玩家信息值
void print_player_info(const Player* player) {
	printf("Player info : %s \n", player->name);  // 输入玩家信息
	printf("Class : %d, Level : %d, Health : %d\n", player->char_class, player->level, player->health);
}

// 战斗结束后敌人信息
void print_enemy_info(const Enemy* enemy) {
	printf("Enemy info: Type %d, Level %d, Health %d\n", enemy->type, enemy->level, enemy->health);
}



