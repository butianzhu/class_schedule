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