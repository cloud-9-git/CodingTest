def solution(clothes):
    answer = 1
    closet = {}
    for i in clothes:
        if i[1] in closet:
            closet[i[1]] = closet[i[1]] + 1
        else:
            closet[i[1]] = 1
    for i in closet.values():
        answer = answer * (i+1)
    answer = answer - 1
    return answer