### first commit
#说明
1.为了防止代码丢失当前git master分支是存储hexo源码的库和分支
- 添加完文章推送源码git push origin master
- 源码git库配置如下(.git/config)：
```
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
[remote "origin"]
    url = git@github.com:thehappyTree/sourceofhexo.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master
```
2.hexo发布构建的分支配置在（_config.yml)
- 添加完文章推送方式hexo clean & hexo g & hexo d
- hexogit配置如下(_config.yml)
```
deploy:
  type: git
  repo: git@github.com:thehappyTree/thehappyTree.github.io.git
  branch: master
```
