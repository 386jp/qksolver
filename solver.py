import itertools
from typing import Union

def equation_solver(equation: str, answer: int) -> bool:
    try:
        return eval(equation) == answer
    except:
        return False

def equation_maker(numbers: list[int]) -> list[str]:
    EQ_SIGNS = ["+", "-", "*", "/"]
    sign_combinations = list(itertools.product(EQ_SIGNS, repeat=len(numbers) - 1))

    combinations = set(itertools.permutations(numbers))

    eq = []

    for com in combinations:
        for sign in sign_combinations:
            eq_tmp = "".join([str(x) + y for x, y in zip(com, sign)]) + str(com[-1])
            for br_s in range(0, (len(numbers)-1)*2, 2):
                t = eq_tmp[:br_s] + "(" + eq_tmp[br_s:]
                for br_e in range(4, len(numbers)*2, 2):
                    if br_s < br_e:
                        eq.append(t[:br_e] + ")" + t[br_e:])
    return eq
