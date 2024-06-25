def solution(s):
    answer = -1
    
    a = []
    
    for i in s:
        if i not in a:
            a.append(i)
        else:
            if a[-1] == i:
                a.pop()
            else:
                a.append(i)
                
            
    return int(len(a) == 0)
