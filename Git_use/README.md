Git团队协作工具的常用命令:
===
###
> 本文档主要是对Git工具学习过程的总结  
包含主要的使用场景、常用命令等等
---
#### 准备材料:
1. GitHub的账号 (GitHub.com)
2. Git团队协作工具 下载地址:(https://git-scm.com/)
3. Git工具的打开方法: 右键->点击Git Bash here    //在当前位置打开Git
---
按使用场景分类:
---

* 场景一: 一穷二白,什么都没有的时候:  
> 1.首先在GitHub上新建一个仓库,并copy仓库的URL  
2.本地操作:在你本机想创建项目的地方打开Git    
3.用 `git clone url` 这里的URL就是刚刚copy的URL  
4.此时会出现一个新的文件夹,这个就是我们GitHub上面的仓库  
5.把你的项目，代码放入这个文件夹后，在此打开Git.  
6.我们先用`git remote add origin url` 来关联本地仓库和GitHub仓库  
7.然后用`git add .`把刚刚添加的项目、源码添加到暂存区  
8.再用`git commit -m "<你要提交的描述信息>"` //把暂存区中的文件提交到本地仓库中并添加描述信息    
9.之后用 `git push -u origin master`将本地仓库推送到GitHub上  //第一次将本地仓库推送到GitHub上.  
---
* 场景二: 当我们写了一些新的代码的时候.
> 1.将文件复制到文件夹,打开Git  
2.同样先用`git add -A`命令将文件所有修改、已删除、新增的文件到暂存区中  
3.用`git commit -m "<你要提交的描述信息>"` 同理将暂存区的文件提交到本地仓库  
4.用`git pull`从远处仓库获取最新版本  
5.再用`git push`将本地仓库提交推送到远程仓库.  
---
* 场景三: 当我们需要用到开发分支时.
> 1.先用`git branch`查看本地的所有branch(分支).`*`号表示当前分支  
2.这里用分步的方法进行创建和切换分支,用`git branch <分支名>`来创建新的分支,用`git checkout <分支名称>`切换到已存在的指定分支(当然也可以用`git checkout --b <分支名称>`来一步创建并切换到新的分支)   
3.剩下的提交到远程仓库步骤和主分支一样.
---
* 场景四: 在本地创建仓库.
> 1. 用`git init` # 初始化本地仓库，在当前目录下生成 .git 文件夹
> 2. 剩下操作和上面类似


```Git
    # 默认在当前目录下创建和版本库名相同的文件夹并下载版本到该文件夹下
    git clone url #用来

    # 查看本地仓库的状态
    git status

    # 添加所有修改、已删除、新增的文件到暂存区中，省略 <文件路径> 即为当前目录
    git add -A [<文件路径>]
    git add .    #注意，这里add和`.`之间有个空格

    # 把暂存区中的文件提交到本地仓库中并添加描述信息
    git commit -m "描述信息"

    # 把所有修改、已删除的文件提交到本地仓库中
    # 不包括未被版本库跟踪的文件，等同于先调用了 git add -u
    git commit -a -m "<提交的描述信息>"

    #从远程仓库获取最新版本并合并到本地。
    git pull
    
    #把本地仓库的分支推送到远程仓库的指定分支
    git push

    # 打印所有的提交记录
    git log
```

### 参考文档:
* https://www.jianshu.com/p/93318220cdce
* https://www.jianshu.com/p/93318220cdce
* https://blog.csdn.net/tomatozaitian/article/details/73515849
* https://www.cnblogs.com/libin-1/p/5918468.html

### 扩展阅读->MarkDown基础教程
* https://www.jianshu.com/p/335db5716248

#### 扩展阅读->了解Git的分支左用:
* https://www.jianshu.com/p/c2aefcf6b2b7