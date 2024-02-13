# #ödev6 örnek: list1[10,11,12] / list2[13,14,15] / output:yeni liste [10,12,13,15]

def cagır(list1, list2):

    bos_list = [ ]

    for i in list1:
        if i % 2 == 0:
            bos_list.append(i)

    for ii in list2 :
        if ii % 2 == 1:
            bos_list.append(ii)

    return bos_list

list1 = [10,11,12]
list2 = [13,14,15]

yeni_list = cagır(list1,list2)

print("output: " , yeni_list)

