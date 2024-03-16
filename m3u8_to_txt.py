import re
import requests

def contains_chinese(s):
    return re.search('[\u4e00-\u9fa5]', s) is not None

def m3u8_to_txt(url, output_file_name):
    response = requests.get(url)
    lines = response.text.split('\n')

    output = {"中文合集": []}  # 创建一个名为"中文合集"的分组
    lines_iter = iter(lines)  # 将列表转换为迭代器
    for line in lines_iter:
        if line.startswith('#EXTINF'):
            group_title = line.split('group-title="')[-1].split('"')[0]
            title = line.split(',')[-1].strip()
            url = next(lines_iter).strip()  # 使用迭代器获取下一个元素
            if contains_chinese(title):  # 检查标题是否包含中文
                output["中文合集"].append(f'{title},{url}')  # 将包含中文的标题添加到"中文合集"分组中
            else:
                if group_title not in output:
                    output[group_title] = []
                output[group_title].append(f'{title},{url}')  # 将标题添加到相应的分组中

    with open(output_file_name, 'w', encoding='utf-8') as file:  # 指定编码为'utf-8'
        for group_title, items in output.items():
            file.write(f'{group_title},#genre#\n')
            for item in items:
                file.write(item + '\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m3u8_to_txt('https://iptv-org.github.io/iptv/index.m3u', 'output6.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
