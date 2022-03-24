# str = input("how old are you: ")
# print(str ,'years old', sep=' ')



# x = int(input('number : '))
# print(x)


# x = float(input('number : '))
# print(x)

# year = input("this year: ")
# year = eval(year)
# year = year + 1
# print("next year:, year")


# i = 0
# result = 0
# while i < 5:
#     print(f'{i} 번째 ',end=" ")
#     a =input("성적 입력 : ")
#     result += int(a)
#     i += 1

# print(f'합 : {result}')
# print(f'평균 : {result / 5}')


# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# for i in range(1,10):
#     print(i)


# result = 0
# for a in range(1,101): # 1 ~ 100
    
#     result = result + a
#     print(f"{a} sum = {result}")

# print(result)



# result = 0
# for a in range(1,101): # 1~ 100
#     result = result + a
#     print(f'{a} : sum + {result}')   #그때의 a값을 출력
#     if result > 100: # result가 100이 넘었을때
#         break

# print(result)


# index = 0
# s = "BlockDMask"
# for a in s:
#     print(a,end=' ')
#     if a == 'k':
#         break  # 'k'를 찾았으니 for문에서 나와랏!
# 
#     index = index + 1


# print(index)  # 'k'가 첫번째로 존재하는 위치 출력


# student = [100, 170, 164, 199, 182, 172, 177]
# for a in student:
#     if a > 170:
# 
#         continue # 키가 170보다 크면 continue
# 
#    print(a)



# result = 0
# for a in range(1,101): #1 ~ 100
#     if a % 2 == 1:
#         result = result + a #2로 나누었을때 나머지가 1

# print(result)

# result = 0 
# for a in range(1,101): #1~100
#     if a % 2 == 0:     #2로 나누었을때 나머지가 1
       
#         continue
#     result = result + a
    
# print(result)

# l = ['Alice', 'Bob', 'Charlie']

# for name in l:
#     if name == 'bob':
#         print("break!")
#         break
#     print(name)
# else:
#     print("!! Finish")


# sr = ['father', 'mother', 'brother']
# cnt = 0
# for s in sr:
#     print(s)
#     for c in s:
#         print(c,end= ' ')
#         if c == 'r':
#             print(' ')
#             cnt += 1        
# print(cnt)


# a = [] # 빈 리스트 생성

# for i in range(10):
#     a.append(i)  # append로 요소 추가

# print(a)

# a = []

# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(j+i)
#     a.append(line)

# print(a)


# for i in range(3):
   
#    print(i)

l = ['Alice', 'Bob', 'Charlie']

# for name in l:
#     print(name)


for i, name in enumerate(l,42):
    print(i, name)