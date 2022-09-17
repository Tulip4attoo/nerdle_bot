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
