def cycle(sequence):
    seqtrue, x = False, 0
    while seqtrue == False:
        if list(sequence).count(sequence[x]) > 1:
            deltapos = list(sequence).index(sequence[x],list(sequence).index(sequence[x]+1))
            for y in range(deltapos):
                