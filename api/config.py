# -*- coding: utf-8 -*-

import shutil
import os
from .Utils import Renew, Claw
from .bot import robotPush


class Runner(object):
    def __init__(self, token, idk) -> None:
        super().__init__()
        self.token = token
        self.Id = idk

    def Push(self, config):
        BotTask = []
        datas = Renew().GetArt()
        target, orgin, old = Renew().Id_take(list(datas), config)
        if target:
            print(target)
            for key in target:
                Id = datas.get(key).get("id")
                Url = 'https://t.bilibili.com/' + Id
                Name = datas.get(key).get("artist_name")
                uid = str(datas.get(key).get("artist_uid"))
                try:
                   co, star, t = Claw().dog(Id)
                except Exception as e:
                   print("获取动态信息出错，已跳过 动态 "+str(Url)+'\n '+str(e))
                   co=0;star=0
                if co > 10 and star > 50:
                    content = '作者 #' + Name + '  UID-' + uid + ' \n' + Url + ' \n' + t
                    path_list = Renew().getPic(datas.get(key), key)
                    print("---------------------")
                    if len(path_list) > 1:
                        # media_group = robotPush.listConvery(path_list) #淘汰的方法
                        lists = robotPush(self.token, self.Id).get_media_group(path_list, content)
                        import telegram
                        telegram.Bot(token=self.token).send_media_group(self.Id, lists)
                        # self.Bots.send_media_group(self.objectID, media_group)
                        print("============Already upload============")
                    # for i in path_list:
                    #    robotPush(self.token,self.Id).postPhoto(i,'作者 #'+Name +'  UID-'+ uid +' \n'+Url +' \n'+t)
                    else:
                        robotPush(self.token, self.Id).postPhoto(path_list[0], content)
                # 删除键文件夹
                shutil.rmtree(os.getcwd() + '/' + key, ignore_errors=True, onerror=None)  # 删除存储的视频文件
            # cloud
            if config.get('data')[0]:
                from .Utils import jsonUtil
                jsonUtil(config.get('data')[1]).wjson(orgin + old)


