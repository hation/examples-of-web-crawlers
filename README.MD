# <p align="center">一些非常有趣的python爬虫例子,对新手比较友好</p>


<p align="center">
    <a href="https://github.com/shengqiangzhang/examples-of-web-crawlers"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
    <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.7-FF1493.svg"></a>
    <a href="https://opensource.org/licenses/mit-license.php"><img src="https://badges.frapsoft.com/os/mit/mit.svg"></a>
    <a href="https://github.com/shengqiangzhang/examples-of-web-crawlers/graphs/contributors"><img src="https://img.shields.io/github/contributors/shengqiangzhang/examples-of-web-crawlers?color=blue"></a>
    <a href="https://github.com/shengqiangzhang/examples-of-web-crawlers/stargazers"><img src="https://img.shields.io/github/stars/shengqiangzhang/examples-of-web-crawlers.svg?logo=github"></a>
    <a href="https://github.com/shengqiangzhang/examples-of-web-crawlers/network/members"><img src="https://img.shields.io/github/forks/shengqiangzhang/examples-of-web-crawlers.svg?color=blue&logo=github"></a>
    <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
</p>
<br />

## 项目简介
一些常见的网站爬虫例子，代码通用性较高，时效性较久。**项目代码对新手比较友好**，尽量用简单的python代码，并配有大量注释。





<br />
<br />

## 如何下载

没有或不懂如何设置代理的![chinese_flag](./chinese_flag.png)**中国用户**, 可跳转至镜像仓库[码云Gitee](https://gitee.com/shengqiangzhang/examples-of-web-crawlers)进行下载, 以便获得较快的下载速度。





<br />
<br />

## [12.一键导出微信读书的书架信息][weread]

> 本项目基于[@arry-lee](https://github.com/arry-lee)的项目[wereader](https://github.com/arry-lee/wereader/issues/20)修改而来，感谢原作者提供的源代码。

<br />

### 简介

全民阅读的时代已经来临，目前使用读书软件的用户数2.1亿，日活跃用户超过500万，其中19-35岁年轻用户占比超过60%，本科及以上学历用户占比高达80%，北上广深及其他省会城市/直辖市用户占比超过80%。**本人习惯使用微信读书，为了方便整理书籍和导出笔记，便开发了这个小工具。**


### 功能截图

在开始写代码思路之前，我们先看看最终生成的效果。

![](12.一键导出微信读书的书籍和笔记/demo1.png)
![](12.一键导出微信读书的书籍和笔记/demo2.png)


### 如何运行

```bash
# 跳转到当前目录
cd 目录名
# 先卸载依赖库
pip uninstall -y -r requirement.txt
# 再重新安装依赖库
pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 开始运行
python pyqt_gui.py
```








<br />
<br />

## 补充

项目持续更新，欢迎您[star本项目][5]





<br />
<br />

## License
[The MIT License (MIT)][6]


[taobao_login]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/1.%E6%B7%98%E5%AE%9D%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95

[tmall_crawler]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/2.%E5%A4%A9%E7%8C%AB%E5%95%86%E5%93%81%E6%95%B0%E6%8D%AE%E7%88%AC%E8%99%AB(%E5%B7%B2%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95)

[taobao_buy_crawler]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/3.%E6%B7%98%E5%AE%9D%E5%B7%B2%E4%B9%B0%E5%88%B0%E7%9A%84%E5%AE%9D%E8%B4%9D%E6%95%B0%E6%8D%AE%E7%88%AC%E8%99%AB(%E5%B7%B2%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95)

[say_to_lady]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/4.%E6%AF%8F%E5%A4%A9%E4%B8%8D%E5%90%8C%E6%97%B6%E9%97%B4%E6%AE%B5%E9%80%9A%E8%BF%87%E5%BE%AE%E4%BF%A1%E5%8F%91%E6%B6%88%E6%81%AF%E6%8F%90%E9%86%92%E5%A5%B3%E5%8F%8B

[crawler_5K_wallpaper]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/5.%E7%88%AC%E5%8F%965K%E5%88%86%E8%BE%A8%E7%8E%87%E8%B6%85%E6%B8%85%E5%94%AF%E7%BE%8E%E5%A3%81%E7%BA%B8

[getMovieInRankingList]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/6.%E7%88%AC%E5%8F%96%E8%B1%86%E7%93%A3%E6%8E%92%E8%A1%8C%E6%A6%9C%E7%94%B5%E5%BD%B1%E6%95%B0%E6%8D%AE(%E5%90%ABGUI%E7%95%8C%E9%9D%A2%E7%89%88)

[fund_data]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/7.%E7%88%AC%E5%8F%96%E5%A4%A9%E5%A4%A9%E5%9F%BA%E9%87%91%E7%BD%91%E6%89%80%E6%9C%89%E5%9F%BA%E9%87%91%E6%95%B0%E6%8D%AE

[generate_wx_data]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/8.%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90%E5%BE%AE%E4%BF%A1%E4%B8%AA%E4%BA%BA%E4%B8%93%E5%B1%9E%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A(%E4%BA%86%E8%A7%A3%E4%BD%A0%E7%9A%84%E5%BE%AE%E4%BF%A1%E7%A4%BE%E4%BA%A4%E5%8E%86%E5%8F%B2)

[generate_qq_data]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/9.%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90QQ%E4%B8%AA%E4%BA%BA%E5%8E%86%E5%8F%B2%E6%8A%A5%E5%91%8A

[generate_friend_group_data]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/10.%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90%E4%B8%AA%E4%BA%BA%E5%BE%AE%E4%BF%A1%E6%9C%8B%E5%8F%8B%E5%9C%88%E6%95%B0%E6%8D%AE%E7%94%B5%E5%AD%90%E4%B9%A6

[chrome_history_data]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/11.%E4%B8%80%E9%94%AE%E5%88%86%E6%9E%90%E4%BD%A0%E7%9A%84%E4%B8%8A%E7%BD%91%E8%A1%8C%E4%B8%BA(web%E9%A1%B5%E9%9D%A2%E5%8F%AF%E8%A7%86%E5%8C%96)

[weread]:https://github.com/shengqiangzhang/examples-of-web-crawlers/tree/master/12.%E4%B8%80%E9%94%AE%E5%AF%BC%E5%87%BA%E5%BE%AE%E4%BF%A1%E8%AF%BB%E4%B9%A6%E7%9A%84%E4%B9%A6%E7%B1%8D%E5%92%8C%E7%AC%94%E8%AE%B0


[1]:https://www.google.com/chrome/
[2]:http://chromedriver.storage.googleapis.com/index.html
[3]:https://account.weibo.com/set/bindsns/bindtaobao
[4]:https://raw.githubusercontent.com/shengqiangzhang/examples-of-web-crawlers/master/1.%E6%B7%98%E5%AE%9D%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95/example.gif
[5]:https://github.com/shengqiangzhang/examples-of-web-crawlers
[6]:http://opensource.org/licenses/MIT
[7]:https://raw.githubusercontent.com/shengqiangzhang/examples-of-web-crawlers/master/3.%E6%B7%98%E5%AE%9D%E5%B7%B2%E4%B9%B0%E5%88%B0%E7%9A%84%E5%AE%9D%E8%B4%9D%E6%95%B0%E6%8D%AE%E7%88%AC%E8%99%AB(%E5%B7%B2%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95)/example.gif
[8]:http://paper.meiyuan.in/
[9]:http://chromedriver.storage.googleapis.com/index.html
