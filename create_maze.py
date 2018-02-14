import random

#criar um lab de n dimensões e x saídas
#estabeleço uma função que eu coloco as medidas que eu quero e quantas saídas devem ter
#como faço a lógica do labirinto?

def c_m(medx,medy):
    block = '#'
    free = ' '
    lab_comps = [block, free]
    elements, elements_extra = divmod((medx-1)*(medy-1),2)[0], divmod((medx-1)*(medy-1),2)[1]
    block_n, free_n = elements, elements+elements_extra
    end_lab = []
    for y in range(medy):
        line = block
        for x in range(1,medx):
            if y == 0 or y == medy-1:
                line = block*medx
                break
            else:
                ele_choice = random.choice(lab_comps)
                if x == medx-1:
                    line += block
                    continue
                if ele_choice == block and block_n > 0:
                    line += block
                else:
                    line += free

        end_lab.append(line)
    return end_lab


r_list = []
for n in range(5,40):
    r_list.append(n)

t_list = []
negativo = 0
fl = 0
inte = 0
for x in range(10):
    ch1 = random.choice(r_list)
    ch2 = random.choice(r_list)
    final_lab = c_m(ch1,ch2)
    for lin in range(len(final_lab)):
        print(final_lab[lin])
    print('-'*20)

