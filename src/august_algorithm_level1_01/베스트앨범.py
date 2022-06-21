def solution(genres, plays):
    dict = {}
    plist = {}
    for i in range(len(plays)):
        dict[i] = [plays[i], genres[i]]
        plist[genres[i]] = []
    
    # dict {0: [500, 'classic'], 1: [600, 'pop'], 2: [150, 'classic'], 3: [800, 'classic'], 4: [2500, 'pop']}
    
    gen = {}
    for i in genres:
        gen[i] = 0
        
    for i in dict:
        for j in genres:
            if dict[i][1] == j:
                gen[dict[i][1]] += dict[i][0]
    
    # gen {'classic': 4350, 'pop': 6200}
    # dict[i] = [plays[i], genres[i]] 
    
    for i in range(len(plays)):
        plist[genres[i]] += [[i, plays[i]]]

    for v in plist.values():
        v.sort(key=lambda x:(-x[1], x[0]))
        # plist[i] = sorted(plist[i], key=lambda x: (-x[1], x[0]))
    
    gen = sorted(gen.items(), key=lambda x: -x[1])
    # print(gen)
    
    # plist {'classic': [[3, 800], [0, 500], [2, 150]], 'pop': [[4, 2500], [1, 600]]}
    # gen {'classic': 4350, 'pop': 6200}
    # gen [('pop', 6200), ('classic', 4350)]
    
    answer = []
    
    for g, p in gen:
        for k in range(min(len(plist[g]), 2)):
            answer.append(plist[g][k][0])
    
    print(answer)            
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)