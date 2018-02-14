def zeros(n):
    FacDiv = n
    Zeroes = 0
    while int(FacDiv) != 0:
        FacDiv = FacDiv/5
        Zeroes = Zeroes+int(FacDiv)
    return (Zeroes)

print(zeros(12))