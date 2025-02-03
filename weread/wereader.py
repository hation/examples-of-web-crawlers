#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@project: PyCharm
@file: wereader.py
@author: Shengqiang Zhang
@time: 2022-03-16 22:30:52
@mail: sqzhang77@gmail.com
"""

"""
@origin: https://github.com/arry-lee/wereader
@author: arry-lee
@annotation: modified from arry-lee
"""

from collections import namedtuple, defaultdict
from operator import itemgetter
from itertools import chain

import requests
import json
import clipboard
import urllib3
# 禁用安全警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 书籍信息
Book = namedtuple('Book', ['bookId', 'title', 'author', 'translator', 'cover', 'type', 'price', 'total_words',
                           'chapter_size','publish_time','copyright_info_name','rating_title','rating_count',
                           'rating_good','rating_fair','rating_poor','rating_deep_v','intro','ai_summary', 'cate'])



def get_bookmarklist(bookId, headers):
    """获取某本书的笔记返回md文本"""
    url = "https://i.weread.qq.com/book/bookmarklist"
    params = dict(bookId=bookId)
    r = requests.get(url, params=params, headers=headers, verify=False)

    if r.ok:
        data = r.json()
        # clipboard.copy(json.dumps(data, indent=4, sort_keys=True))
    else:
        raise Exception(r.text)
    chapters = {c['chapterUid']: c['title'] for c in data['chapters']}
    contents = defaultdict(list)

    for item in sorted(data['updated'], key=lambda x: x['chapterUid']):
        # for item in data['updated']:
        chapter = item['chapterUid']
        text = item['markText']
        create_time = item["createTime"]
        start = int(item['range'].split('-')[0])
        contents[chapter].append((start, text))

    chapters_map = {title: level for level, title in get_chapters(int(bookId), headers)}
    res = ''
    for c in sorted(chapters.keys()):
        title = chapters[c]
        res += '#' * chapters_map[title] + ' ' + title + '\n'
        for start, text in sorted(contents[c], key=lambda e: e[0]):
            res += '> ' + text.strip() + '\n\n'
        res += '\n'

    return res


def get_bestbookmarks(bookId, headers):
    """获取书籍的热门划线,返回文本"""
    url = "https://i.weread.qq.com/book/bestbookmarks"
    params = dict(bookId=bookId)
    r = requests.get(url, params=params, headers=headers, verify=False)
    if r.ok:
        data = r.json()
        # clipboard.copy(json.dumps(data, indent=4, sort_keys=True))
    else:
        raise Exception(r.text)
    chapters = {c['chapterUid']: c['title'] for c in data['chapters']}
    contents = defaultdict(list)
    for item in data['items']:
        chapter = item['chapterUid']
        text = item['markText']
        contents[chapter].append(text)

    chapters_map = {title: level for level, title in get_chapters(int(bookId))}
    res = ''
    for c in chapters:
        title = chapters[c]
        res += '#' * chapters_map[title] + ' ' + title + '\n'
        for text in contents[c]:
            res += '> ' + text.strip() + '\n\n'
        res += '\n'
    return res


def get_chapters(bookId, headers):
    """获取书的目录"""
    url = "https://i.weread.qq.com/book/chapterInfos"
    data = '{"bookIds":["%d"],"synckeys":[0]}' % bookId

    r = requests.post(url, data=data, headers=headers, verify=False)

    if r.ok:
        data = r.json()
        clipboard.copy(json.dumps(data, indent=4, sort_keys=True))
    else:
        raise Exception(r.text)

    chapters = []
    for item in data['data'][0]['updated']:
        if 'anchors' in item:
            chapters.append((item.get('level', 1), item['title']))
            for ac in item['anchors']:
                chapters.append((ac['level'], ac['title']))

        elif 'level' in item:
            chapters.append((item.get('level', 1), item['title']))

        else:
            chapters.append((1, item['title']))

    return chapters

def get_chapter_md(level, title):
    # #书籍_作者
    # ##一级章
    # ###二级节
    # ####小节
    
    try:
        if level < 0:
            return ""
        else:
            str = "##"
            for i in range(level):
                str += "#"
            str += " "
            str += title
            str += "\n"
            #print(str)
            return str
    except Exception as e:
        print(f"发生异常: {e}")
        return  ""

def get_chapters1(bookId, headers, book, author):
    """获取书的目录"""
    url = "https://i.weread.qq.com/book/chapterInfos"
    data = '{"bookIds":["%d"],"synckeys":[0]}' % bookId

    r = requests.post(url, data=data, headers=headers, verify=False)

    if r.ok:
        data = r.json()
        clipboard.copy(json.dumps(data, indent=4, sort_keys=True))
    else:
        raise Exception(r.text)
    chapters = ""
    book_name = ""
    book_name = "## " + book + "_" + author + "\n"
    
    chapters += book_name
    
    for item in data['data'][0]['updated']:
        
        if 'anchors' in item:
            #chapters.append((item.get('level', 1), item['title']))
            chapters += get_chapter_md(item.get('level', 1), item['title'])
            for ac in item['anchors']:
                #chapters.append((ac['level'], ac['title']))
                chapters += get_chapter_md(ac['level'], ac['title'])

        elif 'level' in item:
            chapters += get_chapter_md(item.get('level', 1), item['title'])

        else:
            chapters += get_chapter_md(1, item['title'])

    return chapters

def get_bookinfo(bookId, headers):
    """获取书的详情"""
    url = "https://i.weread.qq.com/book/info"
    params = dict(bookId=bookId)
    r = requests.get(url, params=params, headers=headers, verify=False)

    if r.ok:
        data = r.json()
    else:
        raise Exception(r.text)
    return data

def merge_book(book, book_info, chapter):
    #['bookId', 'title', 'author', 'translator', 'cover', 'type', 'price', 'total_words',
                           #'chapter_size','publish_time','copyright_info_name','rating_title','rating_count',
                           #'rating_good','rating_fair','rating_poor','rating_deep_v','intro','ai_summary', 'cate']
    translator = ""
    copyright_info = ""
    category = ""
    try:
        translator = book['translator']
    except:
        translator = ""
    try:
        copyright_info = book_info['copyrightInfo']['name']
    except:
        copyright_info = ""
    try:
        category = book_info['category']
    except:
        category = ""
    
    return Book(book['bookId'], book['title'], book['author'], translator, book['cover'], category, book['price'], book_info['totalWords'], book_info['chapterSize'],
                book['publishTime'], copyright_info, book_info['newRatingDetail']['title'], book_info['newRatingCount'], book_info['newRatingDetail']['good'],
                book_info['newRatingDetail']['fair'], book_info['newRatingDetail']['poor'], book_info['newRatingDetail']['deepV'], book_info['intro'], book_info['AISummary'], chapter)


def get_bookshelf(userVid, headers):
    """获取书架上所有书"""
    url = "https://i.weread.qq.com/shelf/friendCommon"
    params = dict(userVid=userVid)
    r = requests.get(url, params=params, headers=headers, verify=False)
    if r.ok:
        data = r.json()
    else:
        raise Exception(r.text)

    books_finish_read = set() # 已读完的书籍
    books_recent_read = set() # 最近阅读的书籍
    books_all = set() # 书架上的所有书籍
    #print(headers)
    #print(get_chapters(bookId=3300110038,headers=headers))
    #return 
    for book in data['finishReadBooks']:
        if ('bookId' not in book.keys()) or (not book['bookId'].isdigit()):  # 过滤公众号
            continue
        finish_book_info = get_bookinfo(int(book['bookId']), headers)
        finish_book_chapter = get_chapters1(int(book['bookId']), headers, book['title'], book['author'])
        b = merge_book(book, finish_book_info, finish_book_chapter)
        books_finish_read.add(b)
    books_finish_read = list(books_finish_read)
    books_finish_read.sort(key=itemgetter(-1)) # operator.itemgetter(-1)指的是获取对象的最后一个域的值，即以category进行排序
    #return dict(finishReadBooks=books_finish_read, recentBooks=books_recent_read, allBooks=books_all)
    for book in data['recentBooks']:
        if ('bookId' not in book.keys()) or (not book['bookId'].isdigit()): # 过滤公众号
            continue
        recent_book_info = get_bookinfo(int(book['bookId']), headers)
        recent_book_chapter = get_chapters1(int(book['bookId']), headers, book['title'], book['author'])
        b = merge_book(book, recent_book_info, recent_book_chapter)
        books_recent_read.add(b)
    books_recent_read = list(books_recent_read)
    books_recent_read.sort(key=itemgetter(-1)) # operator.itemgetter(-1)指的是获取对象的最后一个域的值，即以category进行排序

    books_all = books_finish_read + books_recent_read

    return dict(finishReadBooks=books_finish_read, recentBooks=books_recent_read, allBooks=books_all)



def get_notebooklist(headers):
    """获取笔记书单"""
    url = "https://i.weread.qq.com/user/notebooks"
    r = requests.get(url, headers=headers, verify=False)

    if r.ok:
        data = r.json()
    else:
        raise Exception(r.text)
    books = []
    for b in data['books']:
        book = b['book']
        b = Book(book['bookId'], book['title'], book['author'], book['cover'])
        books.append(b)
    books.sort(key=itemgetter(-1))
    return books


def login_success(headers):
    """判断是否登录成功"""
    url = "https://i.weread.qq.com/user/notebooks"
    r = requests.get(url,headers=headers,verify=False)

    if r.ok:
        return True
    else:
        return False



