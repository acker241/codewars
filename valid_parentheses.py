def valid_parentheses(string):
    if (str.count(string,'(') + str.count(string,')')) == 0:
        return True
    elif str.count(string,'(') == str.count(string,')'):
        ListOpen = [-1]
        ListClose = [-1]
        ListTuples = []
        for x in range(str.count(string,'(')):
            ListOpen.append(str.index(string,'(',(max(ListOpen)+1)))
        for y in range(str.count(string,')')):
            ListClose.append(str.index(string,')',(max(ListClose)+1)))
        x, y = 0,0
        for x in range(1,len(ListOpen)):
            ListTuples.append((ListOpen[x],ListClose[x]))
        for y in range(len(ListTuples)):
            if ListTuples[y][0]> ListTuples[y][1]:
                return False
            elif y == len(ListTuples)-1:
                return True
    else:
        return False

testList = ["  (",")test","","hi())(","hi(hi)()"]

for stg in range(len(testList)):

    print(str(valid_parentheses(testList[stg]))+ " - "+ testList[stg])
