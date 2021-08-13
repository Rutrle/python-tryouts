from random import randint
import docx


def create_rand_list(main_length, list_length, max_num):
    """
    creates list of random lists, each unique containing numbers in range from 1 to max_num

    :param main_length: int length of the main list
    :param list_length: int lengths of the random lists
    :param max_num: int 
    """
    rand_list = []
    while len(rand_list) < main_length:
        single_list = []

        for i in range(list_length):
            single_list.append(randint(1, max_num),)

        if single_list not in rand_list:
            rand_list.append(single_list)

    return rand_list


def write_to_file(rand_list):
    mydoc = docx.Document()
    mydoc.add_paragraph("This is first paragraph of a MS Word file.")
    mydoc.save('my_word.docx')


print(create_rand_list(5, 5, 6))

write_to_file(5)
