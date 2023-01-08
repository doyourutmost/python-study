def use_anonymous_function():
    """使用匿名函数"""

    # 使用 lambda 表达式反转拼写，然后依此给单词列表排序
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1]))
    pass


if __name__ == '__main__':
    use_anonymous_function()
    print([callable(obj) for obj in (abs, str, 13)])
    pass
