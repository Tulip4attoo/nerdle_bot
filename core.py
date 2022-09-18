from config import color

ops = "+-*/"
all_chars = {True: "0123456789+-*/", False: "123456789"}

def gen_chars(target_length=8, ops_length=4):
    results = []
    last_gathers = [["", False]]
    for i in range(ops_length):
        curr_gathers = []
        for last_gather, curr_ops_trigger in last_gathers:
            avail_chars = all_chars[curr_ops_trigger]
            for chr in avail_chars:
                curr_gathers.append([last_gather + chr, chr not in ops])
        last_gathers = curr_gathers[:]
    for gather in curr_gathers:
        string_ops, check = get_string_ops_result(gather, target_length)
        if check:
            results.append(string_ops)
    return results


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def get_string_ops_result(a_gather, target_length):
    if not a_gather[1]:
        return a_gather, False
    ops_result = eval(a_gather[0])
    if (ops_result > 0) and is_integer_num(ops_result):
        ops_result = int(ops_result)
        string_constructed = a_gather[0] + "=" + str(ops_result)
        if len(string_constructed) == target_length:
            return string_constructed, True
    return a_gather, False


def gen_all_cases():
    return gen_chars(8, 4) + gen_chars(8, 5) + gen_chars(8, 6)


def get_guess_result(guess_str, target_str):
    """
    There are 8 characters in an operation. We create a result list
    that response for each character.
    There are 3 values in result list, that we label:
    + 0 as not in the target operation, default value.
    + 1 as in the position but wrong spot.
    + 2 as correct spot.
    In short, the larger value = better precision.
    """
    # print(guess_str + "\n" + target_str)
    result = [0] * 8
    checked_guess_positions, checked_target_positions = [], []
    # check correct position
    for i in range(8):
        if guess_str[i] == target_str[i]:
            result[i] = 2
            checked_guess_positions.append(i)
            checked_target_positions.append(i)
    # check wrong spot position
    for i in range(8):
        for j in range(8):
            if i in checked_guess_positions:
                continue
            if j in checked_target_positions:
                continue
            if guess_str[i] == target_str[j]:
                result[i] = 1
                checked_guess_positions.append(i)
                checked_target_positions.append(j)
    render_result(guess_str, target_str, result)
    return result


def render_result(guess_str, target_str, result):
    print("GUESS:   " + "  ".join(list(guess_str)))
    result_string = "RESULT: "
    for i in result:
        result_string += color.color_encoded[i]
    print(result_string)
    print("TARGET:  " + "  ".join(list(target_str)))

