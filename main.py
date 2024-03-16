# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def m3u8_to_txt(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:  # 指定编码为'utf-8'
        lines = file.readlines()

    output = {}
    lines_iter = iter(lines)  # 将列表转换为迭代器
    for line in lines_iter:
        if line.startswith('#EXTINF'):
            group_title = line.split('group-title="')[-1].split('"')[0]
            title = line.split(',')[-1].strip()
            url = next(lines_iter).strip()  # 使用迭代器获取下一个元素
            if group_title not in output:
                output[group_title] = []
            output[group_title].append(f'{title},{url}')

    with open('output.txt', 'w', encoding='utf-8') as file:  # 指定编码为'utf-8'
        for group_title, items in output.items():
            file.write(f'{group_title},#genre#\n')
            for item in items:
                file.write(item + '\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    m3u8_to_txt('iptv-org-index.m3u')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
