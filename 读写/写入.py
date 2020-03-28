"""

@date: 2020/3/26 12:17 
@author：Spring
"""

# file1 = open('./test/a.txt', 'a+', encoding='utf-8')
# file1.write('spring')
# file1.writelines(['xu', 'mei', 'jun'])
# file1.close()

with open('./test/a.txt', 'a+', encoding='utf-8') as file_obj:
    file_obj.writelines('123\n')
