# Author：github@sudoskys
# !pip install pyTelegramBotAPI
# !pip install leancloud
# !pip3 install python-telegram-bot
# --------------------------------------------------------

import time
import random
import requests
import os
import urllib
import telebot
import shutil
from telegram import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo
import telegram


def random_sleep(mu=5, sigma=2.7):
    """正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    """
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)


# 机器人实例
class robotPush:
    # robotPush(token,groupID).postAudio(fileroad,info,name):
    def __init__(self, token, ID):
        import telebot
        import telegram
        import os
        self.home = os.getcwd()
        self.token = token
        self.BOT = telebot.TeleBot(token, parse_mode="HTML")  # You can set parse_mode by default. HTML or MARKDOWN
        self.objectID = ID
        self.Bots = telegram.Bot(token)

    def sendMessage(self, msg):
        self.BOT.send_message(self.objectID, str(msg))

    # 發送media_group

    @staticmethod
    def listConvery(pathlist):
        x = []
        for i in pathlist:
            x.append({'D': i})
        return x

    def making_media_group(InputMedias: tuple):
        media_type = {'A': InputMediaAudio,  # 聲音
                      'D': InputMediaDocument,  # 壓縮文件
                      'P': InputMediaPhoto,  # 圖片
                      'V': InputMediaVideo  # 影片
                      }
        reset_media_group = []
        try:
            for media in InputMedias:
                if media[0] == 'P' or 'D':  # 圖片
                    m = media_type[media[0]](media=open(media[1], 'rb'))
                else:
                    m = media_type[media[0]](media=media[1])  # 一般的
                reset_media_group.append(m)
            return reset_media_group
        except:
            print('error making!')

    def get_size(self, FilePath):
        import os, sys
        size = os.path.getsize(FilePath)
        fsize = size / float(1024 * 1024)
        return fsize, str(fsize) + 'MB'

    def get_media_group(self, rmedia_group: list, content):
        # media_group = [('D', photo1), ('D', photo2), ('D', data)]
        # sending_media_group(who, media_group)
        # media_group = [InputMediaDocument(media=p,caption = content if num == 0 else '') for p in rmedia_group]
        media_group = []
        try:
            Doc = False
            for i in range(len(rmedia_group)):
                io, sio = self.get_size(rmedia_group[i])
                if int(io) > 9:
                    Doc = True

            for i in range(len(rmedia_group)):
                print(rmedia_group[i])
                # 文件组
                if Doc:
                    m = InputMediaDocument(media=open(rmedia_group[i], 'rb'),
                                           caption=content if i == len(rmedia_group) - 1 else '')
                # 图片组
                else:
                    m = InputMediaPhoto(media=open(rmedia_group[i], 'rb'), caption=content if i == 0 else '')
                media_group.append(m)
            return media_group
        except Exception as e:
            print('error making!' + str(e))
        # print(type(media_group))
        print(media_group)
        # reset_media_group = self.making_media_group(media_group)
        return media_group

    '''
    def sending_media_group(self,rmedia_group:list,content):
        #media_group = [('D', photo1), ('D', photo2), ('D', data)]
        #sending_media_group(who, media_group)
        #media_group = [InputMediaDocument(media=p,caption = content if num == 0 else '') for p in rmedia_group]
        media_groups=[]
        print(rmedia_group)
        try:
          for i in range(len(rmedia_group)):
             m = InputMediaDocument(media=open(rmedia_group[i], 'rb') ,caption = content if i == 0 else '')
             media_groups.append(m)
          return media_groups
        except:
           print('error making!')
        #print(type(media_group))
        print(media_groups)
        #reset_media_group = self.making_media_group(media_group)
        try:
            import telegram
            telegram.Bot(token =self.token).send_media_group(self.objectID, media_groups)
            #self.Bots.send_media_group(self.objectID, media_group)
            print("============Already upload============")
        except Exception as e:
            print(e)
    '''

    def postPhoto(self, file, name):
        import os
        if os.path.exists(file):
            photo = open(file, 'rb')
            try:
                self.BOT.send_photo(self.objectID, photo, caption=name)
            except:
                try:
                    self.BOT.send_document(self.objectID, photo, caption=name)
                except Exception as e:
                    print("错误--->" + str(e))
                    pass
            print("============Already upload============")
            photo.close()
            return file


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

    def tag(self, text):
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

    def dog(self, ids):
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
            '''
            #[#]\S+[^# ]
            import re
            pattern = re.compile("[#]\S+[^# ]")
            lists=pattern.findall(tag)
            tag=(" ".join(lists))
            '''
        return comment, star, artTag


# https://api.asoul.cloud:8000/getPic?nocache=1656484885707&page=2&tag_id=0&sort=3&part=0&rank=0&ctime=0&type=1
class Renew(object):
    def __init__(self):

        import os
        self.home = os.getcwd()
        self.url = 'https://api.asoul.cloud:8000/getPic'
        self.data = {'page': 1,
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
            for p in (i.get('pic_url')):
                art.append(p.get('img_src'))
            Art_Data = dict(id=artid, artist_name=artist_name, artist_uid=artist_id, content=art)
            Art_list[artid] = Art_Data

        return Art_list

    def Id_take(self, rlist):
        Todo = leancloud.Object.extend('Todo')
        query = Todo.query
        todo = query.get('62bc手动获取,下面还有一个也是7a65')
        try:
            loaded = todo.get('record')  # json.loads(todo.get('record'))
        except Exception as e:
            print('Error.....' + str(e))
            loaded = []
        # print(type(loaded))
        ret = [i for i in rlist if i not in loaded]
        return ret, rlist, loaded
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
        random_sleep()
        return path


###########################
class Runner(object):
    def __init__(self, token, ids) -> None:
        super().__init__()
        self.token = token
        self.Id = ids

    def Push(self):
        BotTask = []
        datas = Renew().GetArt()
        target, orgin, old = Renew().Id_take(list(datas))
        if target:
            print(target)
            for key in target:
                Id = datas.get(key).get("id")
                Url = 'https://t.bilibili.com/' + Id
                Name = datas.get(key).get("artist_name")
                uid = str(datas.get(key).get("artist_uid"))
                co, star, t = Claw().dog(Id)
                if co > 25 and star > 100:
                    content = '作者 #' + Name + '  #UID' + uid + ' \n' + Url + ' \n' + t
                    path_list = Renew().getPic(datas.get(key), key)
                    print("---------------------")
                    if len(path_list) > 1:
                        # media_group = robotPush.listConvery(path_list) #淘汰的方法
                        lists = robotPush(self.token, self.Id).get_media_group(path_list, content)
                        import telegram
                        try:
                            telegram.Bot(token=self.token).send_media_group(self.Id, lists)
                        except Exception as e:
                            print("图片上传失败" + str(e))

                        # self.Bots.send_media_group(self.objectID, media_group)
                        print("============Already upload============")
                    # for i in path_list:
                    #    robotPush(self.token,self.Id).postPhoto(i,'作者 #'+Name +'  UID-'+ uid +' \n'+Url +' \n'+t)
                    else:
                        robotPush(self.token, self.Id).postPhoto(path_list[0], content)
                # 删除键文件夹
                shutil.rmtree(os.getcwd() + '/' + key, ignore_errors=True, onerror=None)  # 删除存储的视频文件
            # cloud

        Todo = leancloud.Object.extend('T已经有的表请看文档新建o')
        todo = Todo.create_without_data('62bc7手动获取,上面还有一个也是！！537a65')
        todo.set('record', orgin + old)
        todo.set('qurrey', 'listData')
        todo.save()


# 一个动态的全部图片
import leancloud

leancloud.init("npvi密钥ID在这里IYXbMMI", "密钥---S2")
Runner("504xxxxxx机器人token,而且要设为管理员只有发布权限pdmQM", "频道ID").Push()
