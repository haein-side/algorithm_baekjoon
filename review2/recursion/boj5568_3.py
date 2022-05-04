import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
visited = [0 for _ in range(n)]
tmp = [] # 수정이 되는가?
answer = []

def dfs(depth):
    if depth == k:
        answer.append("".join(map(str, tmp)))
        return
    for i in range(n):
        if not visited[i]: 
            # visited 해주는 이유? : 재귀를 타고 들어갔을 때 **i가 0에서부터 다시 시작되므로 (새로운 함수를 호출했으니까) 
            # 이미 방문한 것은 방문하지 않기 위해
            
            # 재귀 한 번 타고 들어갈 때 재귀 전에 써놓은 것들은 해제해주지 않는 이상 계속 유지됨!
            visited[i] = 1
            tmp.append(cards[i])
            
            dfs(depth+1)
            
            tmp.pop() # depth가 k-1일 때로 다시 돌아옴 (재귀가 끝나고 그 함수를 호출했던 단계에서 초기화해주는 것임)
            # 그리고 depth가 k-1일 때에서 계속 재귀를 도는 것 (for문)
            # 어차피 for문에서 다음 원소가 들어와서 초기화해줘도 해당레벨에선 재방문 X
            # for문이 종료되면 리턴값이 None인 상태로 다시 첫 레벨로 돌아가서 for문에서 i+1 일 때로 재귀가 똑같이 실행됨
            visited[i] = 0
dfs(0)

print(len(set(answer)))
