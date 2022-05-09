import sys
input = sys.stdin.readline

n, target = map(int, input().split())
tree = sorted(list(map(int, input().split())))

def binary_search(target):
    start = 0
    end = tree[-1]
    answer = []
    while(start <= end):
        mid = (start + end) // 2
        tmp = 0
        for i in range(n):
            if tree[i] > mid:
                tmp += tree[i] - mid
        if tmp >= target: # 자른 나무의 합이 target 이상일 때
            start = mid + 1 # 절단기의 길이를 늘려줌
            answer.append(mid) 
            # 어차피 절단기의 길이는 늘어나므로
            # 그냥 리스트 안 쓰고 변수의 값을 갱신해주는 식으로 해도 됨!
        elif tmp < target:
            end = mid - 1

    return max(answer)
        
print(binary_search(target))