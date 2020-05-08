def solution(n):
    answer = 0
    is_prime =[True]*(n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    for i in range(2, n+1):
        if is_prime[i]:
            answer += 1
    return answer
