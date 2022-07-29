![a](https://s1.328888.xyz/2022/04/13/fPSGZ.jpg)


<h2 align="center">Tool-Asoul-Fanart</h2>


*A tool for telegram channal delivery,and it can help you to deliver the photo file by asking bilibili api.*


Asoul 二创图片机器人，基于 asoul.cloud ,main.py 即所有配置

## 使用


### 两个版本

- `singe.py` 一个文件实现，leancloud数据存储版本，到处运行

- `main.py` 规范架构，本地json文件版本

如果选择单文件版本，需要在 leancloud.app 国际版拿到额外的密钥ID与key.

Token是用户ID或者某些频道ID（需要拉机器人入频道） use tg@getidsbot |

*关于推送服务*
1.申请一个Bot,向BotFather索取Token
2.使用ID机器人查看目标频道ID
3.将机器人添加至频道并只赋予发消息权限 ，将自己机器人设为频道管理员(邀请界面搜索)


**Python 3.8 或更高版本** 
```shell
python -m pip install --upgrade pip
pip3 install -r requirements.txt
```

### Colab 调试

```
!rm -f -r /content/*
!git clone https://github.com/sudoskys/Tool-Asoul-Fanart
!rsync -r /content/Tool-Asoul-Fanart/* /content/
!python -m pip install --upgrade pip
!pip3 install -r requirements.txt
```








**配置程序定时运行**

对于乌班图，配置如下(不同服务器不同路径呃)

*授权*

```bash
cd Tool-Asoul-Fanart
chmod 777 main.py
date
```

*crontab 执行*

```bash
crontab -l
crontab -e

```

*每天5和17执行任务语法*

```0 5,17 * * *  /user/local/python  /path/xxx.py```

>如果脚本中会有涉及读取配置文件或者读写文件的动作,一般定时任务都不会执行. 
>脚本在执行时,由于是通过crontab去执行的,他的执行目录会变成当前用户的家目录,如果是root,就会在/root/下执行.

所以把执行python的命令放到shell脚本里，然后crontab 定时执行
详见`cron.sh`

*cron用法*

```
chmod +x cron.sh
```

cron 服务的启动与停止，命令如下
    1）service cron start  /*启动服务*/

    2）service cron stop /*关闭服务*/

    3）service cron restart /*重启服务*/

    4）service cron reload /*重新载入配置*/

    5）service cron status /*查看crond状态*/ 


*使用`crontab -e`*

```
00 08   * * *  /bin/sh /root/Tool-Asoul-Fanart/cron.sh
```
https://blog.csdn.net/xys2333/article/details/112469461
https://blog.csdn.net/GX_1_11_real/article/details/86535942

**记得在main文件头部添加类似语句**

```
import sys
sys.path.insert(0, '/root/Tool-Asoul-Fanart')
```


#### Support

如果你感觉这对你有帮助，可以试着我赞助我一点～

[![s](https://img.shields.io/badge/Mianbaoduo-support-DB94A2)](https://mianbaoduo.com/o/Sky2023)