def namelist(names):
    if len(names) == 1:
        return(str(names[0]['name']))
    else:
        if len(names) == 2:
            return(str(str(names[0]['name'])+ " & "+ str(names[1]['name'])))
        else:
            if len(names) == 3:
                return (str(str(names[0]['name']+', '+str(names[1]['name']) + " & " + str(names[2]['name']))))
            else:
                if len(names) > 3:
                    string = str(names[0]['name'] + ', ')
                    for x in range(len(names)):
                        if (len(names) == x+3):
                            string = string + str(str(names[x]['name']+', '+str(names[x+1]['name']) \
                            + " & " + str(names[x+2]['name'])))
                            return(string)
                        else:
                            if x != 0:
                                string = string + str(str(names[x]['name']+', '))
                else:
                    return (str(''))


#Examples:
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))