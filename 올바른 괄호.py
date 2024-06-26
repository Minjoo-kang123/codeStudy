def solution(s):
    answer = True
    sol = list()
    for a in s:
        if a == "(":
            sol.append("(")
        else:
            if len(sol) == 0:
                return False;
            elif sol.pop() != "(":
                return False;
    if len(sol) != 0:
        return False
    return answer
