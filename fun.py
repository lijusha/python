def solution(a,b):
    sum1 = (a**2+b**3)+(a**2+b**3)**2+(a**2+b**3)**3
    print(sum1)




for i in range(3):
    a,b = map(int,input().split())
    solution(a,b)