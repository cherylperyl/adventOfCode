"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=13 ; task=1)
"""

import sys


def get_move(behaviour):
    return int(behaviour.split("+")[1])


def get_loc(location):
    return int(location.split("=")[1])


def main():
    machines = []
    machine = []
    for line in sys.stdin:
        line = line.strip("\n")
        if line:
            button, behaviour = line.split(": ")
            x, y = behaviour.split(", ")
            if "Button" in button:
                machine.append((get_move(x), get_move(y)))
            else:
                machine.append((get_loc(x), get_loc(y)))
        else:
            machines.append(machine)
            machine = []
    machines.append(machine)

    total_tokens = 0
    for machine in machines:
        button_ax, button_ay = machine[0]  # 3 tokens
        button_bx, button_by = machine[1]  # cheaper (1 token)
        prize_pos_x, prize_pos_y = machine[2]

        factor_a = round((prize_pos_y - ((button_by*prize_pos_x)/button_bx)) /
                         (button_ay - ((button_by*button_ax)/button_bx)))
        factor_b = round((prize_pos_x - (button_ax*factor_a)) / button_bx)

        # for factor_a, factor_b in [(factor_a1, factor_b1)]:
        if (button_ax*factor_a + button_bx*factor_b == prize_pos_x and
                button_ay*factor_a + button_by*factor_b == prize_pos_y) \
                and factor_a >= 0 and factor_b >= 0:
            total_tokens += factor_a*3 + factor_b

    print(int(total_tokens))


if __name__ == "__main__":
    main()
