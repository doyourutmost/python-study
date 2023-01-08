## 1、[python 特殊方法](https://docs.python.org/3/reference/datamodel.html)

**跟运算符无关的特殊方法**

| 类别             | 方法名                                                                             |
|:---------------|:--------------------------------------------------------------------------------|
| 字符串 / 字节序列表示形式 | `__repr__`、`__str__`、`__format__`、`__bytes__`                                   |
| 数值转换           | `__abs__`、`__bool__`、`__complex__`、`__int__`、`__float__`、`__hash__`、`__index__` |
| 集合模拟           | `__len__`、`__getitem__`、`__setitem__`、`__delitem__`、`__contains__`              |
| 迭代枚举           | `__iter__`、`__reversed__`、`__next__`                                            |
| 可调用模拟          | `__call__`                                                                      |
| 上下文管理          | `__enter__`、`__exit__`                                                          |
| 实例创建和销毁        | `__new__`、`__init__`、`__del__`                                                  |
| 属性管理           | `__getattr__`、`__getattribute__`、`__setattr__`、`__delattr__`、`__dir__`          |
| 属性描述符          | `__get__`、`__set__`、`__delete__`                                                |
| 跟类相关的服务        | `__prepare__`、`__instancecheck__`、`__subclasscheck__`                           |

**跟运算符相关的特殊方法**

| 类别        | 方法名和对应的运算符                                                                                                                                       |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| 一元运算符     | `__neg__ -`、`__pos__ +`、`__abs__ abs()`                                                                                                          |
| 众多比较运算符   | `__lt__ <`、`__le__ <=`、`__eq__ ==`、`__ne__ !=`、`__gt__ >`、`__ge__ >=`                                                                            |
| 算术运算符     | `__add__ +`、`__sub__ -`、`__mul__ *`、`__truediv__ /`、`__floordiv__ //`、`__mod__ %`、`__divmod__ divmod()`、`__pow__ ** 或 pow()`、`__round__ round()` |
| 反向算术运算符   | `__radd__`、`__rsub__`、`__rmul__`、`__rtruediv__`、`__rfloordiv__`、`__rmod__`、`__rdivmod__`、`__rpow__`                                              |
| 增量赋值算术运算符 | `__iadd__`、`__isub__`、`__imul__`、`__itruediv__`、`__ifloordiv__`、`__imod__`、`__ipow__`                                                            |
| 位运算符      | `__invert__ ~`、`__lshift__ <<`、`__rshift__ >>`、`__and__ &`、`__or__`                                                                              |、`__xor__                                                                     |
| 反向位运算符    | `__rlshift__`、`__rrshift__`、`__rand__`、`__rxor__`、`__ror__`                                                                                      |
| 增量赋值位运算符  | `__ilshift__`、`__irshift__`、`__iand__`、`__ixor__`、`__ior__`                                                                                      |

## 2、数据结构

### 2.1、内置序列类型

容器序列

- list、tuple 和 collections.deque 这些序列能存放不同类型的数据。

扁平序列

- str、bytes、bytearray、memoryview 和 array.array，这类序列只能容纳一种类型。

![可变序列（MutableSequence）和不可变序列（Sequence）的差异](static/img.png)

### 2.2、Python数组的使用

创建数组需要一个类型码，形如 array(‘d’），这个类型码是用来表示在底层实现的 C 语言的数据类型。一般我们用的 Python 底层是用 C
语言编写实现的 ，所以又称为 CPython。

Python 定义了以下这些类型码：

| 类型码 | C 类型               | Python 类型  | 所占字节 |
|:----|:-------------------|:-----------|:-----|
| ‘b’ | signed char        | int        | 1    |
| ‘B’ | unsigned char      | int        | 1    | 
| ‘u’ | Py_UNICODE         | Unicode 字符 | 2    |    
| ‘h’ | signed short       | int        | 2    |
| ‘H’ | unsigned short     | int        | 2    |
| ‘i’ | signed int         | int        | 2    |
| ‘I’ | unsigned int       | int        | 2    |
| ‘l’ | signed long        | int        | 4    |
| ‘L’ | unsigned long      | int        | 4    |
| ‘q’ | signed long long   | int        | 8    |
| ‘Q’ | unsigned long long | int        | 8    |
| ‘f’ | float              | float      | 4    |
| ‘d’ | double             | float      | 8    |

'u' 类型码对应于 Python 中已过时的 unicode 字符 (Py_UNICODE 即 wchar_t)。 根据系统平台的不同，它可能是 16 位或 32
位。

比如 b 类型码表示的是有符号字符（ signed char ），array('b')创建出的数组就只能存放一个字节大小的整数，范围从 -128 到 127
。通过这样的限制，即使序列很长，拥有很多数字，也能节省空间。

**数组定义好类型，就不能存放非定义类型的数据。**