"""

@date: 2020/3/26 11:41 
@author：Spring
"""



file_name = ('./test/a.txt')
try:
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        file_content = ''
        chunk = 100
        while True:
            content = file_obj.read(chunk)
            if not content:
                print('读取完成')
                break
            file_content += content
except FileNotFoundError:
    print(f'{file_content}这个文件不存在')
print(file_content)
file_obj.close()


