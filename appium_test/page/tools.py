# coding=utf-8
import yaml
import os
import jinja2
import json

# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath = os.path.join(basepath, 'pageelement')


def parseyaml():
    # 遍历读取yaml文件
    pageElements = {}
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if '.yaml' in str(yaml_file_path):
                with open(yaml_file_path, 'r') as f:
                    page = yaml.safe_load(f)
                    pageElements.update(page)
    return pageElements


# 提取yaml数据
def get_page_list(yamlpage):
    """
    把yaml对象转成需要的页面对象数据：页面对象-->定位list
    args：yaml解析的对象->dict类型
    return：{‘HomePage’：[‘城市选择’，‘首页搜索’]，'Mypage':['我的','请点击登录']}
    """
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        # 获取所有的loctors定位方法
        locs = names['locators']
        # 添加name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object


# 生成pages.py文件
def creat_page_py(page_list):
    """
    用jinja2将templetage模板生成pages.py文件
    args：传get_page_list返回的内容：
    {‘HomePage’：[‘城市选择’，‘首页搜索’]，'Mypage':['我的','请点击登录']
   return：None
    """
    print os.path.join(basepath, 'templetpage')
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)
    templateVars = {
        'page_list': page_list
    }
    template = template_env.get_template('temoletpage')
    with open(os.path.join(basepath, 'pages.py'), 'w') as f:
        f.write(template.render(templateVars))


if __name__ == '__main__':
    a = parseyaml()
    print a
    b = get_page_list(a)
    #creat_page_py(b['HomePage'])