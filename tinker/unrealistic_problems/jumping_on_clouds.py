clouds = [0, 0, 1, 0, 0, 1, 0]

def jumping_on_clouds(c):
    isSafe = 0
    jumps = 0
    position = 0
    while position < len(c) - 1:
        oneAway = c[position+1]
        twoAway = c[position + 2] if position + 2 <= (len(c) - 1) else None
        if twoAway is not None and twoAway == isSafe:
            position += 2
        elif oneAway == isSafe:
            position += 1
        jumps += 1
    return jumps
