def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        arr_len = len(answer)
        if answer[arr_len-1] != arr[i]:
            answer.append(arr[i])
            
    return answer
            
