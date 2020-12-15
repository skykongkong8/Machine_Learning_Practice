from random import randint
realtarget = []
target = []
def generate_numbers(n):
    if n == 7:
        for i in range(0,6):
            realtarget.insert(i,randint(1,45))
        realtarget.sort()
        realtarget.insert(6,randint(1,45))
        return(realtarget)
    else:
        for i in range(0,n):
            target.insert(i,randint(1,45))
        target.sort()
        return(target)
print(generate_numbers(6))
print(generate_numbers(7))

def draw_winning_numbers():
    return realtarget
print(draw_winning_numbers())    # 코드를 작성하세요.

def count_matching_numbers(list_1, list_2):
    similies = 0
    for a in list_1:
        for b in list_2:
            if a == b:
                similies += 1
    return similies

def check(target, realtarget):
    if count_matching_numbers(target, realtarget) == 3:
        return 5000
    if count_matching_numbers(target, realtarget) == 4:
        return 50000
    if count_matching_numbers(target, realtarget) == 5:
        if realtarget[6] in target:
            return 50000000
        else:
            return 1000000
    if count_matching_numbers(target, realtarget) == 6 and realtarget[6] not in target:
        return 1000000000
    # 코드를 작성하세요.


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))  