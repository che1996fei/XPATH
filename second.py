from lxml import etree

# 所有节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

# 指定节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)

# 子节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

# 父节点
html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 属性匹配
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

# 文本获取
html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')   # 选取直接子节点
# result = html.xpath('//li[@class="item-0"]/a/text()')   # 先取li节点，再选取直接子节点a,最后获取文本
result = html.xpath('//li[@class="item-0"]/a/text()')   # 使用//
print(result)

# 属性获取
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# 多属性匹配
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

# 按序选择
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/a/text()')  # 选取第一个li节点
print(result)
result = html.xpath('//li[last()]/a/text()')  # 选取最后一个li节点
print(result)
result = html.xpath('//li[position()<3]/a/text()')  # 选取位置小于3的li节点
print(result)
result = html.xpath('//li[last()-2]/a/text()')  # 选取倒数第三个li节点
print(result)

# 节点轴选择
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/ancestor::*')  # 调用ancestor轴，获取所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div')  # 只获取div的祖先节点
print(result)
result = html.xpath('//li[1]/attribute::*')  # 调用attribute轴，获取所有属性值
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')  # 调用child轴，获取所有直接子节点
print(result)
result = html.xpath('//li[1]/descendant::span')  # 调用descendant轴，获取所有子孙节点，返回节点只包含span节点
print(result)
result = html.xpath('//li[1]/following::*[2]')  # 调用following轴，第二个后续节点
print(result)
result = html.xpath('//li[1]/following-sibling::*')  # 调用following-sibling轴，第二个后续同级节点
print(result)
