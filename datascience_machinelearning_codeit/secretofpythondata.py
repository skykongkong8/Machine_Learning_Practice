# 01 Aliasing - alias 가명이라는 뜻

x = 5
y = x #y가 x의 alis가 된것--x에 추후 변형을 가하면 y가 변형된다
y = 3
print(x, y)
#예를 들어,
x = ["이가훈", "김민주", "최고은", "우설희", "최규호"]
y = list(x)
z = x

y[0] = "강귀윤"
x[1] = "김원일"
z[2] = "성재훈"

print(x) #의 경우, z리스트를 변형했음에도 불구하고 그 결과가 x를 print한 값에 반영된다.

# def sum_digit(num):
#     result = 0
#     n = len(str(num))
#     if num//(10**n) ==0:
#         for k in range(1,n):
#             result += ((num%(10**k))-(num%(10**(k-1))))/10**(k-1)
#             return result
#     elif num//(10**n) !=0:
#         return result, '계산이 완료되었습니다!'

# absolute_result = 0
# for i in range(1,1001):
#     absolute_result += sum_digit(i)
# print(absolute_result)

# print(sum_digit(1234))

# #   num = int(input('자릿수의 합을 구할 수를 입력하세요 : '))


# def suum(num):
#     total = 0
#     str_num = str(num)
#     for i in range(len(str_num)):
#         digit = str_num[i]
#         total += int(digit)
#     return total




for i in range(1,101):
        if i%8 ==0:
            if i%12 !=0:
                print(i)
#다른 풀이
while i <= 100:
    if i%8 ==0:
        if i%12 != 0:
            print(i)
    i +=1

for n in range(1,1001):
    Sum = 0
    if n%2 ==0:
        Sum += n
    elif n%3 ==0:
        Sum += n
    elif n%6 ==0:
        Sum -= n
print(Sum)


n = 1
while n < 1000:
    sigma = 0
    if n%2 ==0:
        sigma += n
    elif n%3 ==0:
        sigma += n
    elif n%6 ==0:
        sigma -=n
    n+=1
print(sigma)

i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)


# string = ''
# for b in range(1,121):
#     if 120%b==0:
#         string+=str(b)

# print(string)

string = ''
bnumber = 0
b=1
while b <=120:
    if 120%b ==0:
        string+=str(b)
        string += '\n'
        bnumber += 1
    b+=1
print(string,end='');print('120의 약수는 총 %d개입니다.'%(bnumber)) #print를 하면 자동으로 \n이 되어서 출력되는데, 이때 이걸 없애고 싶으면 ,end=''쓰면 된다

N = 120
i = 1
count = 0

while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i += 1

om=50000000
year=1988
while year <2016:
    om *= 1.12
    year += 1
Eunma = 1100000000
if om >= Eunma:
    print('%d원 차이로 동일 아저씨 말씀이 맞습니다.'%(abs(om-Eunma)))
else:
    print('%d원 차이로 미란 아주머니 말씀이 맞습니다.'%(abs(om-Eunma)))

print(om)

a = 1
fn = 1
print(a)
if fn == 1:
    print(a)
    a+=1
    fn+=1
    print(a)
while 1<fn<=50:
    a+=a
    fn+=1
    print(a)

fn = 2
fl = [1,1]
print(fl[0]);print(fl[1])
while 2<=fn<50:
    a = fl[(fn-1)]+fl[(fn-2)]
    fl.append(a)
    print(fl[fn])
    fn+=1


a=1
while a<=9:
    b=1
    while b<=9:
        print('%d * %d = '%(a,b), a*b)
        b+=1
    a+=1

# def is_evenly_divisible(number):
#     if int(number)%2==0:
#         return True
#     elif:
#         return False
def calculate_change(payment, cost):
    no50000 = (payment-cost)//50000
    no10000 = ((payment-cost)%50000)//10000
    no5000 = ((payment-cost)%10000)//5000
    no1000 = ((payment-cost)%5000)//10000
    print('50000원 지폐: %d장\n10000원 지폐: %d장\n5000원 지폐: %d장\n1000원 지폐: %d장'%(no50000, no10000, no5000, no1000))

print(calculate_change(100000, 33000))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력
for i in range(0,6):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]),1)
# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

def krw_to_usd(krw):
    return 0.001*krw
    # 코드를 입력하세요.


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return 125*usd
    # 코드를 입력하세요.


# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))
 
# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.

# 달러($)로 각각 얼마인가요?
for i in range(0,8):
    amounts[i] = krw_to_usd(amounts[i])
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.

# 엔화(￥)으로 각각 얼마인가요?
for j in range(0,8):
    amounts[j] = usd_to_jpy(amounts[j])
print("일본 화폐: " + str(amounts))

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)

print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
for i in range(0,8):
    if numbers[i]%2 != 0:
        numbers[i]='z'
while 'z' in numbers:
    numbers.remove('z') #remove는 직접 원소를 밝히는거고 del는 index를 말하는 거죠?
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0,20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)

for i in range(11):
    print('2^',end='');print(i,'=',2**i)

for a in range(1,1000):
    for b in range(1,1000):
        c= 1000-a-b
        if a*a + b*b == c*c and a<b<c:
            print(a*b*c)

# 1. 단어장 만들기
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
# 코드를 입력하세요.
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)

A = [1,1,1,1,2,2]
print(A.count(1))

print(360-155)
print(205/2)

a = 'idonthavetolearnpythonshit'
print(a.replace('shit','fuck'))

print(a[::-1])

import os
print(os.getlogin())

# import random
# chance = 4
# a = int(input("기회가 {0}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance)))
# b = random.randint(1,20)
# while a != b:
#     if a > b:
#         print('Down')
#         chance -= 1
#     elif a < b:
#         print('Up')
#         chance -=1
#     if chance == 0:
#         print('아쉽습니다. 정답은 {0}였습니다.'.format(b))
# if a == b:
#     print('축하합니다. %d번만에 숫자를 맞히셨습니다.'%(chance))

# from random import randint
# realtarget = []
# target = []
# def generate_numbers(n):
#     if n == 7:
#         for i in range(0,6):
#             realtarget.insert(i,randint(1,45))
#         realtarget.sort()
#         realtarget.insert(6,randint(1,45))
#         return(realtarget)
#     else:
#         for i in range(0,n):
#             target.insert(i,randint(1,45))
#         target.sort()
#         return(target)
# print(generate_numbers(6))
# print(generate_numbers(7))

# def draw_winning_numbers():
#     return realtarget
# print(draw_winning_numbers())    # 코드를 작성하세요.

# def count_matching_numbers(list_1, list_2):
#     similies = 0
#     for a in list_1:
#         for b in list_2:
#             if a == b:
#                 similies += 1
#     return similies

# def check(target, realtarget):
#     if count_matching_numbers(target, realtarget) == 3:
#         return 5000
#     if count_matching_numbers(target, realtarget) == 4:
#         return 50000
#     if count_matching_numbers(target, realtarget) == 5:
#         if realtarget[6] in target:
#             return 50000000
#         else:
#             return 1000000
#     if count_matching_numbers(target, realtarget) == 6 and realtarget[6] not in target:
#         return 1000000000
#     # 코드를 작성하세요.


# # 테스트
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
