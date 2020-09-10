def calculateCGs(sequence):
    sequence = sequence.replace("\n", "").replace(" ", "")
    cgs = count_cgs_on_places(sequence)
    totalall = len(sequence)
    return (
        sum(cgs) / totalall * 100,
        cgs[0] / (totalall / 3) * 100,
        cgs[1] / (totalall / 3) * 100,
        cgs[2] / (totalall / 3) * 100,
    )


def count_cgs_on_places(sequence):
    cgs = [0, 0, 0]
    for place, letter in enumerate(sequence):
        if letter in ["C", "G"]:
            if place % 3 == 0:
                cgs[0] += 1
            elif place % 3 == 1:
                cgs[1] += 1
            elif place % 3 == 2:
                cgs[2] += 1
    return cgs
