genbank_ac_list = [1, 2, 3, 5, 8, 4, 2, 1, 1, 6, 8]

genbank_ac_list.sort()
i = 0
while i < (len(genbank_ac_list)-1):
    if genbank_ac_list[i] == genbank_ac_list[i+1]:
        genbank_ac_list.pop(i+1)
    else:
        i = i+1


print(genbank_ac_list)

genbank_ac_list_2 = [1, 2, 3, 5, 8, 4, 2, 1, 1,
                     6, 456465, 5, 1, 68, 2, 4, 5, 5, 6, 3, 2, 48]
genbank_ac_list_2 = set(genbank_ac_list_2)
genbank_ac_list_2 = list(genbank_ac_list_2)
print(genbank_ac_list_2)
