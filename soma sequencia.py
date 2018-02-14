def sequence_sum(num_in, num_fin, gap):
    if num_in > num_fin and gap > 0: return 0
    if num_fin == num_in: return num_in
    else:
        num_de_inter = int(divmod(int(num_fin)-int(num_in),gap)[0])
        num_total = num_de_inter+1
        ult_num = int((gap*num_de_inter)+num_in)
        soma = ((num_in+ult_num)*num_total)/2
        soma_int = int(soma)
        if soma != soma_int:
            print('Erro')

        return soma


list_to_test = [((2, 6, 2),12),((1, 5, 1), 15),((1, 5, 3), 5),((-1, -5, -3), -5),((16, 15, 3), 0),((-24, -2, 22), -26),
                ((-2, 4, 658), -2),((780, 6851543, 5), 4694363402480),((9383, 71418, 2), 1253127200),
                ((20, 673388797, 5), 45345247259849570)]

for x in range(len(list_to_test)):
    seq_in = list_to_test[x][0][0]
    seq_fin = list_to_test[x][0][1]
    seq_gap = list_to_test[x][0][2]
    script_test = sequence_sum(seq_in,seq_fin,seq_gap)
    if script_test == list_to_test[x][1]:
        print('Teste',x,'sucedido -',script_test,sep=' ')
    else:
        print('Teste', x, 'falhou - ',script_test, sep=' ')
        print(list_to_test[x][1]-script_test)

