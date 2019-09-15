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

### tkinter

说明：py自带包，跨平台，简单

直接看文档就行

布局：grid pack place

master 父组件，frame一般认为master=None

StringVar

## 线程

### threading

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

