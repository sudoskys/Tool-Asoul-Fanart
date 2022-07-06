# -*- coding: utf-8 -*-
from telegram import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo


# 机器人实例
class robotPush(object):
    # robotPush(token,groupID).postAudio(file road,info,name):
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

    '''
    def sending_media_group(self,rmedia_group:list,content):
        #media_group = [('D', photo1), ('D', photo2), ('D', data)]
        #sending_media_group(who, media_group)
        media_group = [InputMediaDocument(media=self.home+p, caption=content) for p in rmedia_group]
        print(type(media_group))
        print((media_group))
        #reset_media_group = self.making_media_group(media_group)
        self.BOT.send_media_group(self.objectID, media_group)


    '''

    def get_size(self, FilePath):
        import os
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
