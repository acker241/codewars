def is_valid_coordinates(coordinates):
    FirstVar = ''
    SecondVar = ''
    if coordinates.count(',') == 0:
        return False
    for x in range(coordinates.index(',')):
        FirstVar = FirstVar+coordinates[x]
    if FirstVar.count('.') > 0:
        try: float(FirstVar)
        except: return False
    else:
        try: int(FirstVar)
        except: return False
    for x in range(coordinates.index(',')+2,len(coordinates)):
        SecondVar = SecondVar+coordinates[x]
    if SecondVar.count('.') > 0:
        try: float(SecondVar)
        except: return False
    else:
        try: int(SecondVar)
        except: return False

    FirstVar = int(float(FirstVar))
    SecondVar = int(float(SecondVar))
    if -90 <= FirstVar <= 90:
        if -180 <= SecondVar <= 180:
            return True
        else:
            return False
    else:
        return False

print(is_valid_coordinates("-23, 25"))