#!/usr/bin/env python3
from brain_games.games.game_calc import game_calc
from brain_games.games.game_engine import game_cycle


def main():
    game_cycle(game_calc())


if __name__ == '__main__':
    main()
