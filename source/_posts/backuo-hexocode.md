---
title: 修改hexo默认端口
date: 2019-01-23 17:58:52
tags: hexo
---
# 如何修改hexo端口
hexo有两种方法修改端口

### 1.启动修改
```
hexo s -p 80 ```改方法为启动时候暂时修改每次都要添加。

### 2.配置文件修改
node_modules/hexo-server/index.js该文件是配置默认的4000端口。
