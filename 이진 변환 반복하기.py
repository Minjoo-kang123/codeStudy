def solution(s):
    zsum = 0
    cnt = 0
    while(int(s) != 1):
        cnt += 1
        zsum += s.count('0')
        result = s.count('1')
        s = ''
        while(result != 0):
            s = str(result % 2) + s
            result = result // 2
    answer = [cnt, zsum]
    return answer
