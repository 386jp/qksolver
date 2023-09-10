import solver

if __name__ == "__main__":
    while True:
        nums = input("解きたい数字をスペース区切りで入力後、最後に解を入力してください\n> ")
        nums_list = [int(n) for n in nums.split(" ")]

        numbers = nums_list[:-1]
        answer = nums_list[-1]

        for eq in solver.equation_maker(numbers):
            if solver.equation_solver(eq, answer):
                print(eq)
                break
