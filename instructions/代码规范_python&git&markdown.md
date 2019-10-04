# 代码规范

1. 顶级定义之间空两行, 比如函数或者类定义. 方法定义, 类定义与第一个方法之间, 都应该空一行. 函数或方法中, 某些地方要是你觉得合适, 就空一行.

2. 空格

   1. 括号内不要有空格.

   ```p&amp;#39;y
   Yes: spam(ham[1], {eggs: 2}, [])
   ```

   2. 不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾).
   3. 参数列表, 索引或切片的左括号前不应加空格.
   4. 在二元操作符两边都加上一个空格
   5. 当’=’用于指示关键字参数或默认参数值时, 不要在其两侧使用空格.

3. 函数文档实例

   ```
   def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
       """Fetches rows from a Bigtable.
   
       Retrieves rows pertaining to the given keys from the Table instance
       represented by big_table.  Silly things may happen if
       other_silly_variable is not None.
   
       Args:
           big_table: An open Bigtable Table instance.
           keys: A sequence of strings representing the key of each table row
               to fetch.
           other_silly_variable: Another optional variable, that has a much
               longer name than the other args, and which does nothing.
   
       Returns:
           A dict mapping keys to the corresponding table row data
           fetched. Each row is represented as a tuple of strings. For
           example:
   
           {'Serak': ('Rigel VII', 'Preparer'),
            'Zim': ('Irk', 'Invader'),
            'Lrrr': ('Omicron Persei 8', 'Emperor')}
   
           If a key from the keys argument is missing from the dictionary,
           then that row was not found in the table.
   
       Raises:
           IOError: An error occurred accessing the bigtable.Table object.
       """
       pass
   ```

4. ***命名规范***

   module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.

5. 函数传入的参数 _para_name

# git

1. git 回退

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

你可以发现，Git会告诉你，`git checkout -- file`可以丢弃工作区的修改：

```
$ git checkout -- readme.txt
```

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

2. Git同样告诉我们，用命令`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage），重新放回工作区：

```
$ git reset HEAD readme.txt
Unstaged changes after reset:
M	readme.txt
```

3. -u参数：关联本地分支和远程分支
4. git merge $branch_name 如果有冲突要手动解决(一般是两个分支有不同的提交内容)
5. git branch -d $branch_name 删除分支
6. git rm --cached $doc_name    删除文件（会影响到远程
7. git branch --set-upstream-to=origin/$name
8. git branch -vv     查看本地分支和远程分支的对应关系
9. git pull <远程主机名> <远程分支名>:<本地分支名>

# markdown

链接格式：\[显示文字\]\(网址\)

不要用base64！！！！

# mac

+ **窗口快速切换桌面**

   defaults write com.apple.dock workspaces-edge-delay -float 0;killall Dock

  defaults delete com.apple.dock workspaces-edge-delay;killall Dock

+ quick player可以录屏

+ source命令作用

   在当前bash环境下读取并执行FileName中的命令。

   比如您在一个脚本里export $KKK=111 ,假如您用./a.sh执行该脚本，执行完毕后，您运行 echo $KKK，发现没有值，假如您用source来执行 ，然后再echo，就会发现KKK=111。因为调用./a.sh来执行shell是在一个子shell里运行的，所以执行后，结构并没有反应到父shell里，但是source不同他就是在本shell中执行的，所以能够看到结果。

   **sh是新起一个子shell运行	source和. 命令都是在父shell里直接运行，可以改变父shell参数**

- 有线网，无线网，wifi：

  - wifi是wlan的一种实现形式

  - ip：

    IP 地址是指互联网协议地址，是 IP 协议提供的一种统一的地址格式，它为互联网上的每一个网络和每一台主机分配一个逻辑地址，以此来屏蔽物理地址的差异。IP 地址编址方案将 IP 地址空间划分为 A、B、C、D、E 五类，其中 A、B、C 是基本类，D、E 类作为多播和保留使用，为特殊地址。

    每个 IP 地址包括两个标识码（ID），即网络 ID 和主机 ID。同一个物理网络上的所有主机都使用同一个网络 ID，网络上的一个主机（包括网络上工作站，服务器和路由器等）有一个主机 ID 与其对应。A~E 类地址的特点如下：

    A 类地址：以 0 开头，第一个字节范围：0~127；

    B 类地址：以 10 开头，第一个字节范围：128~191；

    C 类地址：以 110 开头，第一个字节范围：192~223；

    D 类地址：以 1110 开头，第一个字节范围为 224~239；

    E 类地址：以 1111 开头，保留地址

  - mac地址是身份证号, ip地址是邮编 你一生下来, 身份证号就已经定了, 你换个地方, 每个地方的邮编都不一样 这就是区别

  - tcp三次握手

    最初客户端和服务端都处于 CLOSED(关闭) 状态。本例中 A（Client） 主动打开连接，B（Server） 被动打开连接。

    一开始，B 的 TCP 服务器进程首先创建传输控制块TCB，准备接受客户端进程的连接请求。然后服务端进程就处于 LISTEN(监听) 状态，等待客户端的连接请求。如有，立即作出响应。

    第一次握手：A 的 TCP 客户端进程也是首先创建传输控制块 TCB。然后，在打算建立 TCP 连接时，向 B 发出连接请求报文段，这时首部中的同步位 SYN=1，同时选择一个初始序号 seq = x。TCP 规定，SYN 报文段（即 SYN = 1 的报文段）不能携带数据，但要消耗掉一个序号。这时，TCP 客户进程进入 SYN-SENT（同步已发送）状态。

    第二次握手：B 收到连接请求报文后，如果同意建立连接，则向 A 发送确认。在确认报文段中应把 SYN 位和 ACK 位都置 1，确认号是 ack = x + 1，同时也为自己选择一个初始序号 seq = y。请注意，这个报文段也不能携带数据，但同样要消耗掉一个序号。这时 TCP 服务端进程进入 SYN-RCVD（同步收到）状态。

    第三次握手：TCP 客户进程收到 B 的确认后，还要向 B 给出确认。确认报文段的 ACK 置 1，确认号 ack = y + 1，而自己的序号 seq = x + 1。这时 ACK 报文段可以携带数据。但如果不携带数据则不消耗序号，这种情况下，下一个数据报文段的序号仍是 seq = x + 1。这时，TCP 连接已经建立，A 进入 ESTABLISHED（已建立连接）状态。