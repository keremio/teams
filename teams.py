from itertools import permutations
teams = ["bjk", "fb", "gs", "ts"]
scores = [0, 0, 0, 0]
fixture = permutations(teams, 2)
results = [0]*12
lx = list(fixture)
for i in range (0,12):
    print("enter the result of" , lx[i])
    results[i] = input()
    ha = results[i].split()
    home = int(ha[0])
    away = int(ha[1])
    print(home, away)
    if (home > away):
        print(lx[i][0], "wins")
        if (lx[i][0] == teams[0]):
            scores[0] = scores[0] + 3
        if (lx[i][0] == teams[1]):
            scores[1] = scores[1] + 3
        if (lx[i][0] == teams[2]):
            scores[2] = scores[2] + 3
        if (lx[i][0] == teams[3]):
            scores[3] = scores[3] + 3
    elif (home < away):
        print(lx[i][1], "wins")
        if (lx[i][1] == teams[0]):
            scores[0] = scores[0] + 3
        if (lx[i][1] == teams[1]):
            scores[1] = scores[1] + 3
        if (lx[i][1] == teams[2]):
            scores[2] = scores[2] + 3
        if (lx[i][1] == teams[3]):
            scores[3] = scores[3] + 3
    else:
        print("draw")
        if (lx[i][0] == teams[0] and lx[i][1] == teams[1]):
            scores[0] += 1
            scores[1] += 1
        if (lx[i][0] == teams[0] and lx[i][1] == teams[2]):
            scores[0] += 1
            scores[2] += 1
        if (lx[i][0] == teams[0] and lx[i][1] == teams[3]):
            scores[0] += 1
            scores[1] += 1
        if (lx[i][0] == teams[1] and lx[i][1] == teams[2]):
            scores[1] += 1
            scores[2] += 1
        if (lx[i][0] == teams[1] and lx[i][1] == teams[3]):
            scores[1] += 1
            scores[3] += 1
        if (lx[i][0] == teams[2] and lx[i][1] == teams[3]):
            scores[2] += 1
            scores[3] += 1
    print(teams[0], ":", scores[0], end="\n")
    print(teams[1], ":", scores[1], end="\n")
    print(teams[2], ":", scores[2], end="\n")
    print(teams[3], ":", scores[3], end="\n")
if (max(scores) == scores[0]):
    print("the winner is", teams[0])
if (max(scores) == scores[1]):
    print("the winner is", teams[1])
if (max(scores) == scores[2]):
    print("the winner is", teams[2])
if (max(scores) == scores[3]):
    printf("the winner is", teams[3])
