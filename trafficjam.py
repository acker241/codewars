def traffic_jam(main_road, side_streets):
    SideStEmpty = False
    SideStArray = []
    MainExit = []
    while SideStEmpty == False:
        SideStCond = 0
        for x in range(len(side_streets)):
            if side_streets[x] == '':
                SideStCond +=1
            else:
                SideStQueue = side_streets[x]
                SideStArray.append((SideStQueue[len(SideStQueue)-1],x))
                if len(SideStQueue) == 1:
                    side_streets[x] = ''
                else:
                    side_streets[x] = SideStQueue[0:len(SideStQueue)-1]
        if SideStCond == len(side_streets):
            SideStEmpty = True
    print(SideStArray)
    MyVehic = False
    while MyVehic == False:
        FirstVehic = main_road[0]
        MainExit.append(FirstVehic)
        SideStJoin = SideStArray.pop(0)
        main_road = main_road[1:SideStJoin[1]+1] + SideStJoin[0] + main_road[SideStJoin[1]+1:len(main_road)-1]
        if FirstVehic == 'X':
            MyVehic = True

    return ''.join(MainExit)

print(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]))

#"abcCdCeCECX"