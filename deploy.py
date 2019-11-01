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
        os.system("hexo clean & hexo g & hexo s")
    # 推送git
    elif master_hexo:
        print("推送git")
        os.system("hexo clean & hexo g & hexo d")
        os.system("git add . & git commit -m '{}' & git push origin master".format(master_hexo))
