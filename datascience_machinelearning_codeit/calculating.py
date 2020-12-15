from itertools import combinations

class Fellas:
    """사람들 클래스"""
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.point = 0

    # def __str__(self):


    def is_bigger_than(self,A):
        if self.weight > A.weight and self.height > A.height:
            self.point-=1
        elif self.weight < A.weight and self.height < A.height:
            A.point-=1
        else:
            A.point-=1
            self.point-=1

# A=Fellas(55,185)
# B=Fellas(58,183)
# C=Fellas(88,186)
# D=Fellas(60,175)
# E=Fellas(46,155)
# Fellas_list=[A,B,C,D,E]


N = int(input("횟수를 입력하시오:"))
Fellas_list=[]
for i in range(N):
    Fellas_list.append(Fellas(int(input("weight: ")),int(input("height: "))))
print(Fellas_list)



#2명씩 짝지어서 대결시키기
battle_list = list(combinations(Fellas_list,2))
for match in battle_list:
    match[0].is_bigger_than(match[1])

#계산된 포인트 리스트 만들기
point_list=[]
for fella in Fellas_list:
    point_list.append(fella.point)

#포인트 리스트 정답처럼 만들기
while min(point_list) != 1:
    for i in range(len(point_list)):
        point_list[i]+=1


print(point_list)

