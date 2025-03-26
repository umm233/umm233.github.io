#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-19 17:16:27
# @Author  : emmmmm

import requests
import re
import time
import os


def get_html(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
    proxies = {'http':"http://61.135.217.7:80"}
    try:
        headers = {'User-Agent': user_agent}
        html = requests.get(url, headers=headers,proxies = proxies)
        # print("html status code is",html.status_code)
        if html.status_code == 200: # 判断请求是否成功
            # print(html)
            return html.text # 返回网页内容
    except Exception as e:
        print ('Wrong!!!',e)

def get_sha(user, repo_name): # 用户的每个repo对应一个commit sha
    url = "https://github.com/{user}/{repo_name}/commits/master".format(user=user, repo_name=repo_name)
    html = get_html(url)
    commit_sha = re.findall(r'href="https://github.com/.*commit/(.*?)"', html)[0]
    return commit_sha

def get_all_repo(user):
    url = 'https://github.com/{user}'.format(user=user)
    html = get_html(url)
    all_repo = re.findall(r'<span class="repo js-repo" title="(.*)"', html)
    return all_repo

def single_repo_commits(user, repo_name):
    num = 0
    page_flag = 66 # 设置页面初始标志
    page_num = 0
    data_num = 0
    commit_sha = get_sha(user, repo_name)
    all_date = [] # 储存时间数据

    while (page_flag and page_num<5) :
        url = "https://github.com/{user}/{repo_name}/commits/master?after={commit_sha}+{num}".format(user=user, repo_name=repo_name, commit_sha=commit_sha, num=num)
        html = get_html(url)
        time_data = re.findall(r'<relative-time datetime=(.*)</relative-time>', html)
        page_flag = len(time_data)
        num = num + 34 # 进入下一页
        page_num = page_num+1
        data_num = data_num+len(time_data)
        print("page %d is ok\n get %d date" % (page_num, len(time_data)))
        for date in time_data:
            all_date.append(date[1:20])
        time.sleep(1)
    print("the repo <%s> totally get %d commits'date" % (repo_name, data_num))
    return all_date

def all_repo_commits(user,limit_num):
    all_repo = get_all_repo(user)
    all_repo_commit = []

    for i in range(len(all_repo)):
        repo_name = all_repo[i]
        repo_commit1 = single_repo_commits(user, repo_name)
        all_repo_commit += repo_commit1
        print(repo_name,"<- repo is ok")
        time.sleep(1) #适当延时一下 单位：s
        if len(all_repo_commit)>limit_num:
            return all_repo_commit


def write_data(user, data):
    savepath = './'+user+'.txt'
    if os.path.exists(savepath):
        return ("%s is exist" % user)
    else:
        with open(savepath, 'a+', encoding='utf-8') as f:
            for item in data:
                f.write(item)
                f.write(',')
    print("Write data is ok")

# user = 'facer'
# repo_name = 'python-data-structure-cn'
def main(limit_num):
    # 要爬取的github用户列表 
    user_list = [
    'octocat','torvalds','StylishThemes','sindresorhus',
    'vinta','TheAlgorithms','tensorflow','donnemartin',
    'justjavac','pallets','nvbn','requests',
    'pytorch','certbot','aymericdamien','scrapy'
    ]
    savepath = ''

    for i in range(0,10):
        print("\n-----open new task-----\n")
        commit = []
        user = user_list[i]
        savepath = './'+user+'.txt'
        if os.path.exists(savepath):
            print("%s is exist\n" % user)
        else:
            commits = all_repo_commits(user, limit_num)
            write_data(user, commits)
            print("---Get all %d data Successfully!!!---" %len(commits))

if __name__ == '__main__':
    # main的参数是指每个仓库限制最多爬取200条commit数据 
    main(200)


