#include <stdio.h>
#include "game_types.h"
#include "game_struct.h"
#include "game_function.h"
#include "game_abilities.h"

int main(void) {
	puts("welcome to the Text RPG Game!\n");

	Player player;
	create_player(&player, "Hero", Warrior);
	print_player_info(&player);

	return 0;
}
