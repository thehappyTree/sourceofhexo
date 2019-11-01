# -*- coding:utf-8 -*-
# /usr/bin/env python
# coding=utf8
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mh", "--master-hexo", default="", help="推送hexo和git源码库")
    parser.add_argument("-s", "--start", default="", help="推送hexo和git源码库", action="store_true")
    args = parser.parse_args()
    return args


if __name__=="__main__":
    args = parse_args()
    master_hexo = args.master_hexo
    start = args.start
    # 开启hexo服务
    if start:
        print("开启服务")
        current_path = os.path.dirname(os.path.abspath(__file__))
        print current_path
        os.system("cd {} & hexo clean & hexo g & hexo s".format(current_path))
    # 推送git
    elif master_hexo:
        print("推送git")
        current_path = os.path.dirname(os.path.abspath(__file__))
        os.system("cd {} & hexo clean & hexo g & hexo d".format(current_path))
        os.system("cd {} & git add . & git commit -m '{}' & git push origin master".format(current_path,master_hexo))
