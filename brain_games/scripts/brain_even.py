#!/usr/bin/env python3
from brain_games.games.game_even import game_even
from brain_games.games.game_engine import game_cycle


def main():
    game_cycle(game_even())


if __name__ == '__main__':
    main()
