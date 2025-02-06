def solution(players, callings):
    ply_dic = {val:idx for idx, val in enumerate(players)}

    for i in callings:
        idx = ply_dic[i]
        players[idx], players[idx-1] = players[idx-1],  players[idx]
        ply_dic[i] -= 1
        ply_dic[players[idx]] += 1
    return players