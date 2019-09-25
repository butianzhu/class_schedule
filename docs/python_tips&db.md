# python_tips

## 没啥用的关键词？

***global***	python如果想使用作用域之外的全局变量，则需要加global前缀。

```python
a = 5
 
def test():
    global a
 #此处声明，告诉执行引擎：我要用全局变量a，不要整成局部的了！
    a = 1
    print 'In test func: a = %d' % a
 
test()
print 'Global a = %d' % a

In test func: a = 1
Global a = 1
```

**pycache文件**	是产生的二进制文件，如果存在，下次执行代码就可不用编译节省时间

**extend & append**	extend将参数list里的每一个元素加到列表中，append将整个对象加入列表中

**切片**	L[0:3] 取列表L的前三个元素

**foo&bar&baz**	意思就是张三李四王二麻子

## 数据类型转换

1. str float bytes 转 int

   int()

2. str int bytes 转 float

   float()

3. str float bytes 转 complex

   complex()

4. str()可转换任意类型

5. str 转 bytes

   bytes()

6. list() tuple()

## 循环

1. while，for循环可以用else

2. for i in sequence

# GUI

### tkinter包

说明：py自带包，跨平台，简单

直接看文档就行

布局：grid pack place

master 父组件，frame一般认为master=None

StringVar

## 线程

### threading包

先创建，再start，join主线程，分线程结束后主线程才结束

**线程安全**	

## format函数

## string转time

```python
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
```

## 下划线

1. _var	单个下划线是一个Python命名约定，表示这个名称是供内部使用的。 它通常不由Python解释器强制执行，仅仅作为一种对程序员的提示。

2. Var_    有时候，一个变量的最合适的名称已经被一个关键字所占用。 因此，像class或def这样的名称不能用作Python中的变量名称。 在这种情况下，你可以附加一个下划线来解决命名冲突

3. __var    双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。这也叫做名称修饰（name mangling） - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。

   ```python
   class Test:
      def __init__(self):
          self.foo = 11
          self._bar = 23
          self.__baz = 23
   >>> t = Test()
   >>> dir(t)#内置函数
   ['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
   '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
   '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
   '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
   '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
   '__weakref__', '_bar', 'foo']
   ```

4. \_\_var\_\_    Python保留了有双前导和双末尾下划线的名称，用于特殊用途。 这样的例子有，\_\_init\_\_对象构造函数，或\_\_call\_\_ --- 它使得一个对象可以被调用。而且不会有名称修饰

5. \_    单下划线表示一个临时变量。除了用作临时变量之外，“_”是大多数Python REPL中的一个特殊变量，它表示由解释器评估的最近一个表达式的结果。

## 装饰器

@符号的意义

就是将一个函数包装起来，而且能保持代码结构不变

[参考网站：装饰器](https://foofish.net/python-decorator.html)

## 迭代器

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：**iter()** 和 **next()**。

字符串，列表或元组对象都可用于创建迭代器：

## with

with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。

（１）紧跟with后面的语句被求值后，返回对象的“–enter–()”方法被调用，这个方法的返回值将被赋值给as后面的变量；
（２）当with后面的代码块全部被执行完之后，将调用前面返回对象的“–exit–()”方法。

## 字符串格式化

* %\[数据名称\]\[对齐标志\]\[宽度\]\.\[精度\]类型

  ![img](https://pic4.zhimg.com/80/v2-2a0bf9157e7c09926093f91636d91177_hd.jpg)

* str.format函数

  ```text
  [[填充字符]对齐方式][符号标志][#][宽度][,][.精度][类型]
  '{:S^+#016,.2f}'.format(1234)  # 输出'SSS+1,234.00SSSS'
  ```

  ![preview](https://pic1.zhimg.com/v2-0340c7e376d8215515f33c1c05c388f0_r.jpg)

* f-string

  ```python
  'My name is %s and i'm %s years old.' % (name, age)
  'My name is {} and i'm {} years old.'.format(name, age)
  f'My name is {name} and i'm {age} years old.'
  ```

# 数据库

修改密码

```
格式：mysqladmin -u用户名 -p旧密码 password 新密码 
例子：mysqladmin -uroot -p123456 password 123
```

登入数据库(pyuser@localhost pw:pyuser)

```
mysql -u $username -p
```

权限设置

```
GRANT privileges ON databasename.tablename TO 'username'@'host'
```

基本操作样例

```
create table user (id varchar(20) primary key, name varchar(20))
insert into user (id, name) values (%s, %s)', ['1', 'Michael']
```

select操作顺序（可以加逻辑）

```
select栏位	from表格	where查询条件	group by分组设定	having分组条件	order by排序设定	limit限制设定
字符串匹配：% _
order: ASC升序DESC降序
limit: 传回记录数量
各种函式

```



## tensorflow

pip install --index-url https://pypi.douban.com/simple tensorflow快速安装库（国内源）



# 去补数学！！！！

