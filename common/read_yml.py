import yaml, os

base_path = os.path.dirname(os.path.abspath(__file__))
yml_path = os.path.join(base_path, "test_somedata.yml")

def readMyYml():
    if not os.path.isfile(yml_path):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确: % s"%yml_path)
    f = open(yml_path, 'r', encoding='utf-8')
    cfg = f.read()
    print(cfg, type(cfg))

    r = yaml.load(cfg)
    print(r, type(r))
    return r

if __name__ == '__main__':
    readMyYml()






