import sys
input = sys.stdin.readline
# https://kspsd.tistory.com/7


arr = []

while 1:
    f_arr = list(map(int, input().rstrip().split()))
    if f_arr[0] == 0: # 0이 입력되면 끝내고 나오기
        break
    ans = 0
    st = []
    arr = f_arr[1:] # 사각형의 높이 2 1 4 5 1 3 3

    for val in arr: # val : 현재 사각형의 높이
        tmp = 0
        while len(st) != 0 and st[-1][0] > val: # 현재 사각형의 높이보다 스택에 있던 높이가 더 클 경우 높이가 스택에 있는 건 높이가 안됨
            tmp += st[-1][1]  # 스택이 갖고 있던 밑변 값을 넘겨준다
            ans = max(ans, tmp * st[-1][0]) # tmp에 쌓인 밑변 값 * 유효한 높이 => max 사각형의 넓이로 갱신해줌
            st.pop() # 기존 스택이 높이가 현재 꺼보다 커서 쓸모 없어졌으므로 pop()

        tmp += 1 # 사각형의 높이가 하나 넘어갈 때마다 밑변의 길이는 1씩 늘어가므로!
        st.append([val, tmp])  # 높이와 밑변

    tmp = 0
    while len(st) != 0:  # 남은 값들 처리
        tmp += st[-1][1]
        ans = max(ans, tmp*st[-1][0])
        st.pop()

    print(ans)