参考：[廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017804782304672)

# HTTP

header 一个响应码，一个字典

body 内容



# HTML

[html速查列表](https://www.runoob.com/html/html-quicklist.html)

- 注释	<!-- blablabla --> 

- 属性

  color(color: red), font-size(font-size: 16px), font-family, 

类选择器

```html
<style>
  h2 {color: blue;}
  .red-text {color: red;}<!--注意.-->
</style>
```

常用属性：class, id, style, title

- 导入链接，可以链接css样式表，rel="stylesheet" type="text/css"

  <link href="https://fonts.gdgdocs.org/css?family=Lobster" rel="stylesheet" type="text/css">

- head标签：里面插入各种meta信息

- img src width alt默认文字

- 格式化标签<b><i>

- 边框

- anchor nesting    target="_blank"在新标签页打开

- 无序列表ul

  有序列表ol

-  #### input

  Type: text, password, radio, checkbox

   placeholder    <input type="text" placeholder="this is placeholder text">

  label 选择框

- ```<form>可以提交到表单服务器```

- button 点击提交

- body 元素定义文档的主体。

  body 元素包含文档的所有内容（比如文本、超链接、图像、表格和列表等等。）

- #### 布局

  - table 表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。
  - ```<div>```

- rgb(0,0,0)

- 字符实体 #

# CSS

- 引入：

```<head>
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

- id: #id

  Class: .class

- [web安全字体](https://www.runoob.com/cssref/css-websafe-fonts.html)
- 单位长度

# Django

```
django-admin startproject mysite

```

- urls.py    指定域名与对应view的关系

- views.py.   处理请求

- **render**    

  ```python
  def render(request, template_name, context=None, content_type=None, status=None, using=None):
      """
      Return a HttpResponse whose content is filled with the result of calling
      django.template.loader.render_to_string() with the passed arguments.
      """
      content = loader.render_to_string(template_name, context, request, using=using)
      return HttpResponse(content, content_type, status)
  ```

  

- 运行manage.py时可能会遇到问题，需要跟踪修改一些文件，还要改一下\_\_init_\_.py
- __url&path__    path与url是两个不同的模块,效果都是响应返回页面, path调用的是python第三方模块或框架,而url则是自定义的模块,如Views下的def函数对应你url中的参数值.

# WSGI(py)

参考：[理解wsgi](https://www.letiantian.me/2015-09-10-understand-python-wsgi/)

- 回调函数

  你到一个商店买东西，刚好你要的东西没有货，于是你在店员那里留下了你的电话，过了几天店里有货了，店员就打了你的电话，然后你接到电话后就到店里去取了货。在这个例子里，你的电话号码就叫回调函数，你把电话留给店员就叫登记回tazsdeeeh调函数，店里后来有货了叫做触发了回调关联的事件，店员给你打电话叫做调用回调函数，你到店里去取货叫做响应回调事件。回答完毕。

- FLASK(web 框架)

需要下载（用pycharm自带的下载就行，不用conda或者console（命令行））







