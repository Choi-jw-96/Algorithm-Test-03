# 암호생성기
"""
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
 

[1 사이클]

 
 
[암호 도출]
 
[제약 사항]

주어지는 각 수는 integer 범위를 넘지 않는다.

마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.
 
[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.
 
[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
"""
import collections

while True:
    try:
        t = int(input())
    except:
        break
    org_input = collections.deque(map(int, input().split()))

    while True:
        subtractor = 1
        for _ in range(5):
            org_input.append(org_input.popleft() - subtractor)
            if org_input[-1] <= 0:
                org_input[-1] = 0
                break
            subtractor += 1
        if org_input[-1] <= 0:
            org_input[-1] = 0
            break

    print(f'#{t}', *org_input)