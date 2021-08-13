from random import randint
from docx.shared import RGBColor
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

    color_dict = {1: 'FF0000', 2: 'FFCA00',
                  3: '88D0FF', 4: '007800', 5: 'A8A9AD'}
    mydoc = docx.Document()

    for single_list in rand_list:
        para = mydoc.add_paragraph()
        for point in single_list:
            if point == 6:
                # n is a full square in Wingdings
                current_run = para.add_run('p')
                current_run.font.name = 'Wingdings'
            else:
                # n is a full square in Wingdings
                current_run = para.add_run('n')
                current_run.font.name = 'Wingdings'
                current_run.font.color.rgb = RGBColor.from_string(
                    color_dict[point])

    mydoc.save('my_word.docx')

    '''
    para = mydoc.add_paragraph()
    p = para.add_run("nnnnnn")

    p.font.name = 'Wingdings'
    z = para.add_run("ggg")

    '''


rand_list = create_rand_list(30, 5, 6)

write_to_file(rand_list)
