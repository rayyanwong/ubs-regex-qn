import re

# from testcases import getTestCases


def all_matched(expression, valid_strings):
    collated = []
    for s in valid_strings:
        collated.append(re.fullmatch(expression, s))
    return all(collated)


def none_matched(expression, invalid_strings):
    collated = []
    for s in invalid_strings:
        collated.append(not re.fullmatch(expression, s))
    return all(collated)


def satisfies_both(expression, valid_strings, invalid_strings):
    return all_matched(expression, valid_strings) and none_matched(
        expression, invalid_strings
    )


def partial_matched(expression, string):
    return re.match(expression, string)


def compactGree(expression, valid_strings, invalid_strings):
    # we know that curr expression works and want to make it smaller
    # first compression is always to reduce from multiple |w\w\w\w to \w{numTimes}
    ret = expression
    # print("initial: ", expression)
    tokens = []
    exp = expression[1:-1]  # remove the ^ and $
    i = 0
    while i + 1 <= len(exp):
        # print(exp[i])
        if exp[i] == "\\":
            tokens.append(exp[i : i + 2])
            i += 1
        else:
            tokens.append(exp[i])
        i += 1
    # print("tokens: ", tokens)
    # rebuild expression
    newExp = r"^"
    stack = []
    greedyTokens = []
    ptr = 0
    while ptr < len(tokens):
        # peek at the top of stack, if stack is same as current token, we push into stack
        # print(tokens[ptr])
        if stack and tokens[ptr] == stack[-1]:
            stack.append(tokens[ptr])
        elif stack and stack[-1] != tokens[ptr]:
            # print(stack)
            occurence = len(stack)
            if occurence == 1:
                newExp += rf"{stack[-1]}"
                greedyTokens.append(rf"{stack[-1]}")
            else:
                newExp += rf"{stack[-1]}{{{occurence}}}"
                greedyTokens.append(rf"{stack[-1]}{{{occurence}}}")
            stack = [tokens[ptr]]
        else:
            stack.append(tokens[ptr])
        ptr += 1
    # print(stack)
    if stack:
        occurence = len(stack)
        if occurence == 1:
            newExp += rf"{stack[-1]}"
            greedyTokens.append(rf"{stack[-1]}")
        else:
            newExp += rf"{stack[-1]}{{{occurence}}}"
            greedyTokens.append(rf"{stack[-1]}{{{occurence}}}")

    # print("newExp: ", newExp + "$")
    # test if satisfies_both
    if satisfies_both(newExp + "$", valid_strings, invalid_strings):
        ret = newExp + "$"
    # print(greedyTokens)
    greedyExp = r"^"
    superGreedyTokens = []

    # to further reduce, want to see if can greedy it by replacing away the \D, \d and \w
    for sak in greedyTokens:
        if sak.startswith("\\") and re.match(r"^\\[wdWD]\{\d+\}$", sak):
            # print(rf"{sak[1]}+")
            # ASSUMPTION: requires to be very specific (for security) on how to validate string where cant loosely be "."
            greedyExp += rf"{sak[0:2]}+"
            superGreedyTokens.append(rf"{sak[0:2]}+")
        elif re.match(r"^\.\{\d+\}$", sak):
            greedyExp += rf"{sak[0]}+"
        else:
            greedyExp += sak
            superGreedyTokens.append(rf"{sak}")
    if satisfies_both(greedyExp + "$", valid_strings, invalid_strings):
        ret = greedyExp + "$"

    return ret


def generate_gree_expression(valid_strings, invalid_strings):
    gree = r"^"  # always start with ^
    # ASSUMPTION: that all valid strings are same length
    max_length = len(valid_strings[0])

    for i in range(max_length):
        charsAtIdx = []
        for s in valid_strings:
            charsAtIdx.append(s[i])
        charsSet = set(charsAtIdx)
        if len(charsSet) == 1:
            char = re.escape(list(charsSet)[0])
            gree += char
        elif all(c.isdigit() for c in charsAtIdx):
            gree += r"\d"
        elif all(c.isalpha() for c in charsAtIdx):
            if satisfies_both(gree + r"\w.+$", valid_strings, invalid_strings):
                gree += r"\w"
            else:
                gree += r"\D"
        else:
            # print("not alpha or digit")
            gree += r"."

    if all_matched(gree + r"$", valid_strings) == none_matched(
        gree + r"$", invalid_strings
    ):
        return compactGree(gree + r"$", valid_strings, invalid_strings)
    print("\n\n\n\n\nSKILL ISSUE\n\n\n\n")
    return "skill issue" + gree + r"$"


#
# if __name__ == "__main__":
#     testCases = getTestCases()
#     test = testCases[3]
#     print(generate_gree_expression(test["valid"], test["invalid"]))
