# -*- coding: utf-8 -*-
import json
import os
import random
import time
import urllib

import leancloud
import requests


class jsonUtil(object):
    def __init__(self, key):
        import json
        from pathlib import Path
        self.key = key
        rfile = Path(self.key + '.json')
        if not rfile.is_file():
            with open(self.key + '.json', 'w+') as f:
                pass

    def wjson(self, lists, add=True):
        if add:
            old = self.rjson()
            if old:
                lists = list(set(lists) | (set(old)))
        with open(self.key + '.json', 'w+') as f:
            json.dump(lists, f)

    def rjson(self):
        with open(self.key + '.json', 'r', encoding='utf-8') as load_f:
            str_f = load_f.read()
            if len(str_f) > 0:
                datas = json.loads(str_f)
            else:
                datas = {}
        return datas


class Claw(object):
    def __init__(self) -> None:
        super().__init__()
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate ,br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Referer': 'https://api.bilibili.com/',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
            # 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Cookie': '1P_JAR=2022-02-09-02;SEARCH_SAMESITE=CgQIv5QB;ID=CgQIsv5QB0',

            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
        }

    def tag(self, text: str):
        """基本描述
            Args:
                text (str): origin data from bilibili.com
            Returns: Tags: formal tags Tag: a list of tag
        """
        Tag = []
        s = text.split('#')
        ava = ["向晚", '嘉晚饭', '向晚大魔王', 'AVA', 'ava']
        diana = ['嘉然', '嘉然今天吃什么', '嘉心糖的手账本', '嘉晚饭']
        carol = ['珈乐', '珈乐Carol', 'Carol', '小狗说']
        bella = ['贝拉', '贝拉Bella', '乃贝', '贝拉kira', '贝拉KIRA', '贝极星空间站的日常']
        ellen = ['乃琳', '乃琳Queen', '乃琳', '乃贝']
        rom = (list(filter(lambda x: x != '', s)))
        if list(set(carol) & set(rom)): Tag.append("珈乐")
        if list(set(diana) & set(rom)): Tag.append("嘉然")
        if list(set(ava) & set(rom)): Tag.append("向晚")
        if list(set(bella) & set(rom)): Tag.append("贝拉")
        if list(set(ellen) & set(rom)): Tag.append("乃琳")
        if {'乃琳', '贝拉'} == set(Tag): Tag.append("乃贝")
        if {'嘉然', '向晚'} == set(Tag): Tag.append("嘉晚饭")
        Tags = ('#' + " #".join(Tag))
        return Tags, Tag

    def dog(self, ids: str):
        """基本描述
            :param ids: 动态ID
            :type ids: str
        """
        try:
            # https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id=676770838894084134
            apiUrl = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id=' + ids
            Data = requests.get(url=apiUrl, headers=self.header).json()
            comment = (Data.get("data").get("item").get('modules').get('module_stat').get("comment")['count'])
            star = (Data.get("data").get("item").get('modules').get('module_stat').get("like")['count'])
            tag = str(Data.get("data").get("item").get('modules').get('module_dynamic').get("desc")['text'])
            artTag, tagList = self.tag(tag)
        except:
            star = 0
            comment = 0
            artTag = "被删除的动态"
            print(ids)
        return comment, star, artTag


# https://api.asoul.cloud:8000/getPic?nocache=1656484885707&page=2&tag_id=0&sort=3&part=0&rank=0&ctime=0&type=1
class Renew(object):
    def __init__(self):

        import os
        self.home = os.getcwd()
        self.url = 'https://api.asoul.cloud:8000/getPic'
        self.data = {'page': 4,
                     'nocache': time.time(),
                     'type': 1, 'tag_id': 0,
                     'sort': 3, 'part': 0,
                     'rank': 0, 'ctime': 0,
                     }
        self.headers = {'content-type': 'application/json'}

    def GetArt(self):
        art = requests.get(self.url, self.data, headers=self.headers, verify=False)
        Art_list = {}

        for i in art.json():
            artid = (i.get("dy_id"))
            artist_id = i.get("uid")
            artist_name = i.get("name")
            art = []
            for i in (i.get('pic_url')):
                art.append(i.get('img_src'))
            Art_Data = dict(id=artid, artist_name=artist_name, artist_uid=artist_id, content=art)
            Art_list[artid] = Art_Data
            # 插入单条数据
            # sql = 'INSERT INTO art (ID, Artist ,ArtistId ,Content) VALUES("'+ str(artid) +'", "'+str(artist_name)+'", "'+str(artist_id) +'", "'+ str(art)+'")'
            # print(sql)
            # cs.execute(sql)

        # cs.close()
        # conn.commit()
        # conn.close()
        return Art_list

    def Id_take(self, rlist, config):
        try:
            loaded = jsonUtil(config.get('data')[1]).rjson()  # json.loads(todo.get('record'))
        except:
            print('初始化Json')
            loaded = []
        # print(type(loaded))
        ret = [i for i in rlist if i not in loaded]
        return ret, rlist, list(loaded)
        # with open('Data.json', 'w') as f:
        #    f.write(json.dumps(list(Art_list)))

    def getPic(self, item, dirname):
        if not os.path.exists(dirname):  # 创建为文件夹
            os.makedirs(dirname)
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),
            ('Referer', 'https://t.bilibili.com/' + item.get("id")),  # referer 验证
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        path = []
        for i in item.get("content"):
            name = i[i.rindex('/') + 1:]
            urllib.request.urlretrieve(url=i, filename=os.path.join(dirname, name))
            path.append(self.home + '/' + os.path.join(dirname, name))

        # 回调函数
        # print(str(round(ed-st,2))+' seconds download finish:',title)
        def random_sleep(mu=3, sigma=0.7):
            """正态分布随机睡眠
            :param mu: 平均值
            :param sigma: 标准差，决定波动范围
            """
            secs = random.normalvariate(mu, sigma)
            if secs <= 0:
                secs = mu  # 太小则重置为平均值
            time.sleep(secs)

        random_sleep()
        return path
