#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 12:00:04
# @Author  : emmmmm


import requests
import json
import os
import threading
import time


thread_lock = threading.BoundedSemaphore(value = 5)

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        return resp
    else:
        return None


# url = "http://www.tingban.cn/webapi/audios/list?id=1100001475776&pagesize=20&pagenum={pagenum}&sorttype=1&_=1547133654328"

def data_json(resp):
    url_singal_list = []
    audioName_list = []
    download_list = {}
    # fetchJSON_comment98vv13288();
    if resp.text:
        url_fmdata = resp.content.decode('utf-8') # gbkTypeStr = unicodeTypeStr.encode("GBK", 'ignore');
        # with open('url_fmdata.json', 'w') as f:
        #     f.write(url_fmdata)
        # print(url_fmdata)
        result = json.loads(url_fmdata).get("result")
        # print(type(result))
        dataList = result["dataList"]
        # print(dataList)
        # print(len(dataList))
        for data in dataList:
            """
            音频格式可选.aac/.mp3
            mp3PlayUrl/aacPlayUrl
            """
            url_singal = data['aacPlayUrl']
            audioName = data["audioName"]
            # print(url_singal)
            # print(audioName)
            url_singal_list.append(url_singal)
            audioName_list.append(audioName)
        singal_data = zip(audioName_list, url_singal_list)
        download_list.update(singal_data)
        # print(download_list)
        return download_list


def download_pics(url,download_name,n):
    path = 'pics1/'+ download_name + url[-4:]
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            #下载完了解锁
    thread_lock.release()
    print("%d is ok" %n)
    time.sleep(1)


def main(pages):
    # pages = pages_from_duitang(label)
    # pic_urls = pic_urls_from_pages(pages)
    download_list_all = {}
    for page_num in range(1,pages+1): # max = 14
        url22 = "http://www.tingban.cn/webapi/audios/list?id=1100001475776&pagesize=20&pagenum={i}&sorttype=1&_=1547133654328".format(i=page_num)
        resp = get_html(url22)
        url_list = data_json(resp)
        # print(url_list)
        download_list_all.update(url_list)
    # print(download_list_all)
    all_url_name = list(download_list_all.keys())
    # follow_img_url = all_url
    n = 0
    for i in range(len(all_url_name)):
        download_name = all_url_name[n]
        n += 1
        url = download_list_all[download_name]
        print('download {} mp3 '.format(download_name))
        path = 'pics1/'+ download_name + url[-4:]
        if not os.path.exists(path):
            #上锁
            thread_lock.acquire()
            t = threading.Thread(target = download_pics,args = (url,download_name,n))
            t.start()
        else:
            print("%d is ok" %n)


if __name__ == '__main__':
    main(14)
