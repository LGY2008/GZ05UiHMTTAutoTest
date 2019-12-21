# 导包
import yaml
from config import BASE_PATH
import os


# 编写读取函数
def read_yaml(filename):
    file_path = BASE_PATH+os.sep+"data"+os.sep+filename
    with open(file_path, "r", encoding="utf-8")as f:
        arr = []
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    print(read_yaml("mp_article.yaml"))
