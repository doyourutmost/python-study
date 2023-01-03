def tag(name, *content, cls=None, **attrs):
    """
    Generate one or more HTML tags
    tag 函数用于生成 HTML 标签；使用名为 cls 的关键字参数传入“class”属性，这是一种变通方法，因为“class”是 Python 的关键字
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<{name}{attr}>{content}</{name}>'.format(name=name, attr=attr_str, content=c)
                         for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('br'))  # <br />
    print(tag('p', 'hello'))  # <p>hello</p>
    # print(print(tag('p', 'hello', 'world')))
    print(tag('p', 'hello', id=33))  # <p id="33">hello</p>
    print(tag('p', 'hello', 'world', cls='sidebar'))  # <p class="sidebar">hello</p> \n <p class="sidebar">world</p>
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))  # <img class="framed" src="sunset.jpg" title="Sunset Boulevard" />
