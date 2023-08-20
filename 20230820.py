# 백준 2884번 알람시계
H,M = input().split()          # 변수 H와 M에 입력한 값을 공백을 기준으로 분리시키고,
                               # 리스트화 된 값을 변수 H와 M에 순서대로 넣는다
                               # 변수 H에 들어있는 값을 정수로 바꾼 값을 H에 다시 넣는다
                               # 변수 M에 들어있는 값을 정수로 바꾼 값을 M에 다시 넣는다
                               # M에 있는 값에서 45를 뺀 값을 다시 M에 넣는다.

                               # 분이 0보다 작으면 == 분이 음수라면
                               # H에 들어 있는 값에서 -1을 한 값을 다시 H에 넣는다
                               # M에 들어 있는 값에서 60을 더한 값을 다시 M에 넣는다

H = int(H)
M = int(M)
M = M - 45

if M < 0:
    H -= 1
    M += 60
    if H < 0:
        H += 24

print(H, M)

#백준 2525번

A,B = input().split()
A = int(A)
B = int(B)
C = int(input())
B += C



if B >= 60:
    A += A // 60
    B = B % 60
    if A >= 24:
        A %= 24

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print(10000 + a * 1000)
elif a == b and a != c:
    print(1000 + a * 100)
elif a == c and a != b:
    print(1000 + a * 100)
elif b == c and b != a:
    print(1000 + b * 100)
else :
    print(max(a,b,c) * 100)

