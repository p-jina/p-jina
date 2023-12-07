def solution(my_string, k):
    answer = ''
    
    if(k>=1) and (k<=100):
        for i in range (k):
            answer += my_string
    
    return answer