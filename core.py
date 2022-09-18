import utils

def gen_all_cases():
    return utils.gen_chars(8, 4) + utils.gen_chars(8, 5) + utils.gen_chars(8, 6)


if __name__ == "__main__":
    print("Loading, please wait for about 10 seconds.")
    all_cases = gen_all_cases()
    utils.solve_curr_answer(all_cases)
