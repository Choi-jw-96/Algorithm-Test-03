import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    ans = []

    for i in range(1, n + 1):
        if i not in submit:
            ans.append(i)

    print(f'#{tc}', *ans)
