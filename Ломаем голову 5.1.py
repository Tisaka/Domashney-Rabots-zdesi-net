'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
my_list = 'Это красиабвво, является наабв чем-то грабвуша! хорошим!'

udalit = list(filter(lambda item: 'абв' not in item, my_list.split()))
print(udalit)