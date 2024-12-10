"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2023 ; day=1 ; task=1)
"""

import sys


def is_word_num(sub_str, word_graph, i=0):
    if type(word_graph) is str:
        return word_graph
    elif i >= len(sub_str):
        return False
    elif sub_str[i] in word_graph:
        return is_word_num(sub_str, word_graph[sub_str[i]], i + 1)
    return False


def find_first_word_num(text, word_graph):
    for i in range(len(text)):
        word_num = is_word_num(text[i:], word_graph)
        if word_num:
            return word_num
    return False


def main():
    result = 0
    word_nums = {"one": "1",
                 "two": "2",
                 "three": "3",
                 "four": "4",
                 "five": "5",
                 "six": "6",
                 "seven": "7",
                 "eight": "8",
                 "nine": "9"}
    word_graph = {
        "o": {
            "n": {
                "e": "one"
            }
        },
        "t": {
            "w": {
                "o": "two"
            },
            "h": {
                "r": {
                    "e": {
                        "e": "three"
                    }
                }
            }
        },
        "f": {
            "o": {
                "u": {
                    "r": "four"
                }
            },
            "i": {
                "v": {
                    "e": "five"
                }
            }
        },
        "s": {
            "i": {
                "x": "six"
            },
            "e": {
                "v": {
                    "e": {
                        "n": "seven"
                    }
                }
            }
        },
        "e": {
            "i": {
                "g": {
                    "h": {
                        "t": "eight"
                    }
                }
            }
        },
        "n": {
            "i": {
                "n": {
                    "e": "nine"
                }
            }
        }
    }
    word_graph_reversed = {
        "e": {
            "n": {
                "i": {
                    "n": "nine"
                },
                "o": "one"
            },
            "e": {
                "r": {
                    "h": {
                        "t": "three"
                    }
                }
            },
            "v": {
                "i": {
                    "f": "five"
                }
            }
        },
        "o": {
            "w": {
                "t": "two"
            }
        },
        "r": {
            "u": {
                "o": {
                    "f": "four"
                }
            }
        },
        "x": {
            "i": {
                "s": "six"
            }
        },
        "n": {
            "e": {
                "v": {
                    "e": {
                        "s": "seven"
                    }
                }
            }
        },
        "t": {
            "h": {
                "g": {
                    "i": {
                        "e": "eight"
                    }
                }
            }
        }
    }
    for line in sys.stdin:
        line_strip = line.strip("\n")

        two_digit_num = ""
        has_digits = False
        # first digit from the front
        for i in range(len(line_strip)):
            if line_strip[i].isdigit():
                has_digits = True
                have_word_num = find_first_word_num(line_strip[0:i],
                                                    word_graph)
                if have_word_num:
                    two_digit_num += word_nums[have_word_num]
                else:
                    two_digit_num += line_strip[i]
                break

        if not has_digits:
            two_digit_num += word_nums[find_first_word_num(line_strip,
                                                           word_graph)]
            two_digit_num += word_nums[find_first_word_num(line_strip[::-1],
                                                           word_graph_reversed
                                                           )]

        # first digit from the back
        reversed_line_strip = line_strip[::-1]
        for i in range(len(reversed_line_strip)):
            if reversed_line_strip[i].isdigit():
                have_word_num = find_first_word_num(reversed_line_strip[0:i],
                                                    word_graph_reversed)
                if have_word_num:
                    two_digit_num += word_nums[have_word_num]
                else:
                    two_digit_num += reversed_line_strip[i]
                break

        result += int(two_digit_num)

    print(result)


if __name__ == "__main__":
    main()
