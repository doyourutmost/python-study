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

可变序列

- list、bytearray、array.array、collections.deque 和 memoryview。

不可变序列

- tuple、str 和 bytes。

![可变序列（MutableSequence）和不可变序列（Sequence）的差异](static/img.png)

**列表或元组的方法和属性（那些由object类支持的方法没有列出来）**

| 方法                         | 列表  | 元组  | 描述                                        |
|:---------------------------|:----|:----|:------------------------------------------|
| `s.__add__(s2)`            | ✅   | ✅   | s + s2，拼接                                 |
| `s.__iadd__(s2)`           | ✅   | ❌   | s += s2，就地拼接                              | 
| `s.append(e)`              | ✅   | ❌   | 在尾部添加一个新元素                                |    
| `s.clear()`                | ✅   | ❌   | 删除所有元素                                    |
| `s.__contains__(e)`        | ✅   | ✅   | s 是否包含 e                                  |
| `s.copy()`                 | ✅   | ❌   | 列表的浅复制                                    |
| `s.count(e)`               | ✅   | ✅   | e 在 s 中出现的次数                              |
| `s.__delitem__(p)`         | ✅   | ❌   | 把位于 p 的元素删除                               |
| `s.extend(it)`             | ✅   | ❌   | 把可迭代对象 it 追加给 s                           |
| `s.__getitem__(p)`         | ✅   | ✅   | s[p]，获取位置 p 的元素                           |
| `s.__getnewargs__()`       | ❌   | ✅   | 在 pickle 中支持更加优化的序列化                      |
| `s.index(e)`               | ✅   | ✅   | 在 s 中找到元素 e 第一次出现的位置                      |
| `s.insert(p, e)`           | ✅   | ❌   | 在位置 p 之前插入元素 e                            |
| `s.__iter__()`             | ✅   | ✅   | 获取 s 的迭代器                                 |
| `s.__len__()`              | ✅   | ✅   | 获取 元素的数量                                  |
| `s.__mul__(n)`             | ✅   | ✅   | s * n，n 个 s 的重复拼接                         |
| `s.__imul__(n)`            | ✅   | ❌   | s *= n，就地重复拼接                             |
| `s.__rmul__(n)`            | ✅   | ✅   | n * s，反向拼接                                |
| `s.pop([p])`               | ✅   | ❌   | 删除最后或者是（可选的）位于 p 的元素，并返回它的值               |
| `s.remove(e)` `            | ✅   | ❌   | 删除 s 中的第一次出现的 e                           |
| `s.reverse()`              | ✅   | ❌   | 就地把 s 的元素倒序排列                             |
| `s.__reversed__()`         | ✅   | ❌   | 返回 s 的倒序迭代器                               |
| `s.__setitem__(p, e)`      | ✅   | ❌   | s[p] = e，把元素 e 放在位置 p，替代已经在那个位置的元素        |
| `s.sort([key], [reverse])` | ✅   | ❌   | 就地对 s 中的元素进行排序，可选的参数有键（key）和是否倒序（reverse） |

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

### 2.3、常见的映射方法
映射类型的方法其实很丰富。下表为我们展示了 dict、defaultdict 和 OrderedDict 的常 见方法，后面两个数据类型是 dict 的变种，位于 collections 模块内。

| 方法                           | dict | defaultdict | OrderedDict | 描述                                                          |
|:-----------------------------|:-----|:------------|:------------|:------------------------------------------------------------|
| `d.clear()`                  | ✅    | ✅           | ✅           | 移除所有元素                                                      |
| `d.__contains__(k)`          | ✅    | ✅           | ✅           | 检查 k 是否在 d 中                                                | 
| `d.copy()`                   | ✅    | ✅           | ✅           | 浅复制                                                         |    
| `d.__copy__()`               | ❌    | ✅           | ❌           | 用于支持 copy.copy                                              |
| `d.default_factory`          | ❌    | ✅           | ❌           | 在 __missing__ 函数中被调用的函数，用以给未找到的元素设置值                        |
| `d.__delitem__(k)`           | ✅    | ✅           | ✅           | 列表的浅复制                                                      |
| `d.fromkeys(it, [initial])`  | ✅    | ✅           | ✅           | 将迭代器 it 里的元素设置为映射里的键，如果有 initial 参数，就把它作为这些键 对应的值（默认是 None） |
| `d.get(k, [default])`        | ✅    | ✅           | ✅           | 返回键 k 对应的值，如果字典里没有键k，则返回 None 或者 default                    |
| `d.__getitem__(k)`           | ✅    | ✅           | ✅           | 让字典 d 能用 d[k] 的形式返回键 k 对应的值                                 |
| `d.items()`                  | ✅    | ✅           | ✅           | 返回 d 里所有的键值对                                                |
| `d.__iter__()`               | ✅    | ✅           | ✅           | 获取键的迭代器                                                     |
| `d.keys()`                   | ✅    | ✅           | ✅           | 获取所有的键                                                      |
| `d.__len__()`                | ✅    | ✅           | ✅           | 可以用 len(d) 的形式得到字典里键值对的数量                                   |
| `d.__missing__(k)`           | ❌    | ✅           | ❌           | 获 __getitem__ 找不到对应键的时候，这个方法会被调用                            |
| `d.move_to_end(k, [last])`   | ❌    | ❌           | ✅           | 把键为 k 的元素移动到最靠前或者最靠后的位置（last 的默认值是 True）                    |
| `d.pop(k, [default])`        | ✅    | ✅           | ✅           | 返回键 k 所对应的值，然后移除这个键值对。如果没有这个键，返回 None 或者 default            |
| `d.popitem()`                | ✅    | ✅           | ✅           | 随机返回一个键值对并从字典里移除它                                           |
| `d.__reversed__()`           | ❌    | ❌           | ✅           | 返回倒序的键的迭代器                                                  |
| `d.setdefault(k, [default])` | ✅    | ✅           | ✅           | 若字典里有键 k，则直接返回 k 所对应的值；若无，则让 d[k] = default，然后返 回 default   |
| `d.__setitem__(k, v)`        | ✅    | ✅           | ✅           | 实现 d[k] = v 操作，把 k 对应的值设为 v                                 |
| `d.update(m, [**kargs])`     | ✅    | ✅           | ✅           | m 可以是映射或者键值对迭代器，用来更新 d 里对应的条目                               |
| `d.values()`                 | ✅    | ✅           | ✅           | 返回字典里的所有值                                                   |
|

### 2.3、常见的集合方法
集合的数学运算：这些方法或者会生成新集合，或者会在条件允许的情况下就地 修改集合

| 数学符号  | Python运算符 | 方法                                       | 描述                                                 |
|:------|:----------|:-----------------------------------------|:---------------------------------------------------|
| S ∩ Z | s & z     | `s.__and__(z)`                           | s 和 z 的交集                                          |
|       | z & s     | `s.__rand__(z)`                          | 反向 & 操作                                            | 
|       |           | `s.intersection(it, ...)`                | 把可迭代的 it 和其他所有参数转化为集合，然后求它们与 s 的交集                 |    
|       | s &= z    | `s.__iand__(z)`                          | 把 s 更新为 s 和 z 的交集                                  |
|       |           | `s.intersection_update(it, ...)`         | 把可迭代的 it 和其他所有参数转化为集合，然后求得它们与 s 的交 集，然后把 s 更新成这个交集 |
| S ∪ Z | s&#124;z  | `s.__or__(z)`                            | s 和 z 的并集                                          |
|       | z&#124;s  | `s.__ror__(z)`                           | &#124; 的反向操作                                       |
|       |           | `s.union(it, ...)`                       | 把可迭代的 it 和其他所有参数转化为集合，然后求它们和 s 的并集                 |
|       | s&#124;=z | `s.__ior__(z)`                           | 把 s 更新为 s 和 z 的并集                                  |
|       |           | `s.update(it, ...)`                      | 把可迭代的 it 和其他所有参数转化为集合，然后求它们和 s 的并集，并把 s 更新成这个并集    |
| S \ Z | s - z     | `s.__sub__(z)`                           | s 和 z 的差集，或者叫作相对补集                                 |
|       | z - s     | `s.__rsub__(z)`                          | - 的反向操作                                            |
|       |           | `s.difference(it, ...)`                  | 把可迭代的 it 和其他所有参数转化为集合，然后求它们和 s 的差集                 |
|       | s -= z    | `s.__isub__(z)`                          | 把 s 更新为它与 z 的差集                                    |
|       |           | `s.difference_update(it, ...)`           | 把可迭代的 it 和其他所有参数转化为集合，求它们和 s 的差集，然 后把 s 更新成这个差集    |
|       |           | `s.symmetric_difference(it)`             | 把求 s 和 set(it) 的对称差集                               |
| S ∆ Z | s ^ z     | `s.__xor__(z)`                           | 求 s 和 z 的对称差集                                      |
|       | z ^ s     | `s.__rxor__(z)`                          | ^ 的反向操作                                            |
|       |           | `s.symmetric_difference_update(it, ...)` | 把可迭代的 it 和其他所有参数转化为集合，然后求它们和 s 的对称 差集，最后把 s 更新成该结果 |
|       | s ^= z    | `s.__ixor__(z)`                          | 把 s 更新成它与 z 的对称差集                                  |

**集合的比较运算符，返回值是布尔类型**

| 数学符号  | Python运算符 | 方法                   | 描述                            |
|:------|:----------|:---------------------|:------------------------------|
|       |           | `s.isdisjoint(z)`    | 查看 s 和 z 是否不相交（没有共同元素）        |
| e ∈ S | e in s    | `s.__contains__(e) ` | 元素 e 是否属于 s                   | 
| S ⊆ Z | s <= z    | `s.__le__(z)`        | s 是否为 z 的子集                   |    
|       |           | `s.issubset(it)`     | 把可迭代的 it 转化为集合，然后查看 s 是否为它的子集 |
| S⊂ Z  | s < z     | `s.__lt__(z)`        | s 是否为 z 的真子集                  |
| S ⊇ Z | s >= z    | `s.__ge__(z)`        | s 是否为 z 的父集                   |    
|       |           | `s.issuperset(it) `  | 把可迭代的 it 转化为集合，然后查看 s 是否为它的父集 |
| S ⊃ Z | s > z     | `s.__gt__(z)`        | s  是否为 z 的真父集                 |   

**集合类型的其他方法**

| 方法             | set | frozenset | 描述                                      |
|:---------------|:----|:----------|:----------------------------------------|
| `s.add(e)`     | ✅   | ❌         | 把元素 e 添加到 s 中                           |
| `s.clear() `   | ✅   | ❌         | 移除掉 s 中的所有元素                            | 
| `s.copy() `    | ✅   | ✅         | 对 s 浅复制                                 |
| `s.discard(e)` | ✅   | ✅         | 如果 s 里有 e 这个元素的话，把它移除                   |
| `s.__iter__()` | ✅   | ✅         | 返回 s 的迭代器                               |    
| `s.__len__()`  | ✅   | ❌         | len(s)                                  |
| `s.pop()`      | ✅   | ❌         | 从 s 中移除一个元素并返回它的值，若 s 为空，则抛出KeyError 异常 |  
| `s.remove(e)`  | ✅   | ❌         | 从 s 中移除 e 元素，若 e 元素不存在，则抛出 KeyError 异常  |  


## 2、异常结构
```markdown
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

## 3、标准库中的生成器函数
### 3.1、用于过滤的生成器函数
第一组是用于过滤的生成器函数：从输入的可迭代对象中产出元素的子集，而且不修改元
素本身

| 模块        | 函数                                                 | 说明                                                                                      |
|-----------|----------------------------------------------------|-----------------------------------------------------------------------------------------|
| itertools | compress(it, selector_it)                          | 并行处理两个可迭代的对象；如 selector_it 中的元素是 真值，产出 it 中对应的元素                                        |
| itertools | dropwhile(predicate, it)                           | 处理 it，跳过 predicate 的计算结果为真值的元素，然后 产出剩下的各个元素（不再进一步检查）                                    |
| （内置）      | filter(predicate, it)                              | 把 it 中的各个元素传给 predicate，如果 predicate(item) 返回真值，那么产出对应的元素；如果 predicate 是 None，那么只产出真值元素 |
| itertools | filterfalse(predicate, it)                         | 与 filter 函数的作用类似，不过 predicate 的逻辑是相反的：predicate 返回假值时产出对应的元素                            |
| itertools | islice(it, stop) 或 islice(it, start, stop, step=1) | 产出 it 的切片，作用类似于 s[:stop] 或 s[start:stop:step]， 不过 it 可以是任何可迭代的对象，而且这个函数实现的是惰 性操作        |
| itertools | takewhile(predicate, it)                           | predicate 返回真值时产出对应的元素，然后立即停止，不 再继续检查                                                   |
### 3.2、用于映射的生成器函数

| 模块        | 函数                              | 说明                                                                           |
|-----------|---------------------------------|------------------------------------------------------------------------------|
| itertools | accumulate(it, [func])          | 产出累积的总和；如果提供了 func，那么把前两个元素传给它，然后把计算结果和下一个元素传给它，以此类推， 最后产出结果                 |
| （内置）      | enumerate(iterable, start=0)    | 产出由两个元素组成的元组，结构是 (index, item)，其中 index 从 start 开始计数，item 则从 iterable 中获取    |
| （内置）      | map(func, it1, [it2, ..., itN]) | 把 it 中的各个元素传给 func，产出结果；如果传入 N 个可 迭代的对象，那么 func 必须能接受 N 个参数，而且要并行 处理各个可迭代的对象 |
| itertools | starmap(func, it)               | 把 it 中的各个元素传给 func，产出结果；输入的可迭代对 象应该产出可迭代的元素 iit，然后以 func(*iit) 这种形 式调用 func  |

### 3.3、合并多个可迭代对象的生成器函数

| 模块        | 函数                                         | 说明                                                                                |
|-----------|--------------------------------------------|-----------------------------------------------------------------------------------|
| itertools | chain(it1, ..., itN)                       | 先产出 it1 中的所有元素，然后产出 it2 中的所有元素，以此类 推，无缝连接在一起                                      |
| itertools | chain.from_iterable(it)                    | 产出 it 生成的各个可迭代对象中的元素，一个接一个，无缝连接 在一起；it 应该产出可迭代的元素，例如可迭代的对象列表                      |
| itertools | product(it1, ..., itN, repeat=1)           | 计算笛卡儿积：从输入的各个可迭代对象中获取元素，合并成由 N 个元素组成的元组，与嵌套的 for 循环效果一样；repeat 指明重复 处理多少次输入的可迭代对象 |
| （内置）      | zip(it1, ..., itN)                         | 并行从输入的各个可迭代对象中获取元素，产出由 N 个元素组成 的元组，只要有一个可迭代的对象到头了，就默默地停止                          |
| itertools | zip_longest(it1, ..., itN, fillvalue=None) | itertools 并行从输入的各个可迭代对象中获取元素，产出由 N 个元素组 成的元组，等到最长的可迭代对象到头后才停止，空缺的值使用fillvalue 填充  |


### 3.4、把输入的各个元素扩展成多个输出元素的生成器函数

| 模块        | 函数                             | 说明                                                              |
|-----------|--------------------------------|-----------------------------------------------------------------|
| itertools | combinations(it, out_len)      | 把 it 产出的 out_len 个元素组合在一起，然后产出 itertools combinations_with_re   |
| itertools | placement(it, out_len)         | 把 it 产出的 out_len 个元素组合在一起，然后产出，包含相同元素的组合                        |
| itertools | count(start=0, step=1)         | 从 start 开始不断产出数字，按 step 指定的步幅增加                                 |
| itertools | cycle(it)                      | 从 it 中产出各个元素，存储各个元素的副本，然后按顺序重复不断地产出各个元素                         |
| itertools | permutations(it, out_len=None) | 把 out_len 个 it 产出的元素排列在一起，然后产出这些排列；out_len 的默认值等于 len(list(it)) |
| itertools | repeat(item, [times])          | 重复不断地产出指定的元素，除非提供 times，指定次数                                    |

### 3.5、用于重新排列元素的生成器函数

| 模块        | 函数                    | 说明                                                                |
|-----------|-----------------------|-------------------------------------------------------------------|
| itertools | groupby(it, key=None) | 产出由两个元素组成的元素，形式为 (key, group)，其中 key 是分组标准， group 是生成器，用于产出分组里的元素 |
| （内置）      | reversed(seq)         | 从后向前，倒序产出seq中的元素；seq必须是序列，或者是实 现了__reversed__ 特殊方法的对象             |
| itertools | tee(it, n=2)          | 产出一个由 n 个生成器组成的元组，每个生成器用于单独产出输入的可迭代对象中的元素                         |

### 3.6、可迭代的归约函数

| 模块        | 函数                         | 说明                                                                        |
|-----------|----------------------------|---------------------------------------------------------------------------|
| （内置）      | all(it)                    | it 中的所有元素都为真值时返回 True，否则返回 False；all([]) 返回 True                          |
| （内置）      | any(it)                    | 只要 it 中有元素为真值就返回 True，否则返回 False；any([]) 返回False                          |
| （内置）      | max(it, [key=,][default=]) | 返回 it 中值最大的元素；key 是排序函数，与 sorted 函数中的一样； 如果可迭代的对象为空，返回 default            |
| （内置）      | min(it, [key=,][default=]) | 返回 it 中值最小的元素；key 是排序函数，与 sorted 函数中的一样； 如果可迭代的对象为空，返回 default            |
| functools | reduce(func, it,[initial]) | 把前两个元素传给 func，然后把计算结果和第三个元素传给 func，以此类推，返回最后的结果；如果提供了 initial，把它当作第一个元素传入 |
| （内置）      | sum(it, start=0)           | it 中所有元素的总和，如果提供可选的 start，会把它加上（计算浮点数的加法时，可以使用 math.fsum 函数提高精度）          |

## 4、Python 方法的底层特殊方法查找逻辑
首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它
们。也就是说没有 my_object.__len__() 这种写法，而应该使用 len(my_object)。在执行
len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会自己去调
用其中由你实现的 __len__ 方法。

然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、字节序列（bytearray）
等，那么 CPython 会抄个近路，__len__ 实际上会直接返回 PyVarObject 里的 ob_size 属
性。PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。直接读取这个值比
调用一个方法要快很多。
### 4.1、自定义的布尔值
尽管 Python 里有 bool 类型，但实际上任何对象都可以用于需要布尔值的上下文中（比如 if 或 while 语句，或者 and、or 和 not 运算符）。为了判定一个值 x 为真还是为假，Python 会调用 bool(x)，这个函数只能返回 True 或者 False。

默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对 `__bool__` 或者 `__len__` 函数有自己的实现。bool(x) 的背后是调用 `x.__bool__()` 的结果；如果不存在 `__bool__` 方法，那么 
bool(x) 会尝试调用 `x.__len__()`。若返回 0，则 bool 会返回 False；否 则返回 True。


- `__repr__` 和 `__str__` 的区别在于，后者是在 `str()` 函数被使用，或是在用 `print` 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。(如果你只想实现这两个特殊方法中的一个，`__repr__` 是更好的选择，因为如果一个对象没 有`__str__` 函数，而 Python 又需要调用它的时候，解释器会用 `__repr__` 作为替代)
- `for i in x:` 这个语句，背后其实用的是 `iter(x)`，而这个函数的背后则是 `x.__iter__()` 方法
- `+=` 背后的特殊方法是 `__iadd__`（用于“就地加法”）。但是如果一个类没有实现这个方法的 话，Python 会退一步调用 `__add__`。
- `==` a == b 是语法糖，等同于 `a.__eq__(b)`。继承自 object 的 `__eq__` 方法比较两个对象的 ID，结果与 is 一样。但是多数内置类型使用更有意义的方式覆盖了 `__eq__` 
  方法，会考虑对象属性的值。
- `a + b`
  1. 如果 a 有 `__add__` 方法，而且返回值不是 NotImplemented，调用 `a.__add__(b)`，然后返回结果
  2. 如果 a 没有 `__add__` 方法，或者调用 `__add__` 方法返回 NotImplemented，检查 b 有没有
     `__radd__` 方法，如果有，而且没有返回 NotImplemented，调用 `b.__radd__(a)`，然后返回结果
  3. 如果 b 没有 `__radd__` 方法，或者调用 `__radd__` 方法返回 NotImplemented，抛出 TypeError， 并在错误消息中指明操作数类型不支持
>如果中缀运算符方法抛出异常，就终止了运算符分派机制。对 TypeError 来
说，通常最好将其捕获，然后返回 NotImplemented。这样，解释器会尝试调
用反向运算符方法，如果操作数是不同的类型，对调之后，反向运算符方法
可能会正确计算

- 序列可以迭代的原因：iter函数
  1. (1) 检查对象是否实现了 __iter__ 方法，如果实现了就调用它，获取一个迭代器。
  2. (2) 如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方法，Python 会创建一个迭代器，尝试按顺序（从索引 0 开始）获取元素。
  3. (3) 如果尝试失败，Python 抛出 TypeError 异常，通常会提示“C object is not iterable”（C
  对象不可迭代），其中 C 是目标对象所属的类。
> 从 Python 3.4 开始，检查对象 x 能否迭代，最准确的方法是：调用 iter(x)
函数，如果不可迭代，再处理 TypeError 异常。这比使用 isinstance(x,
abc.Iterable) 更准确，因为 iter(x) 函数会考虑到遗留的 __getitem__ 方
法，而 abc.Iterable 类则不考虑
> 检 查对象 x 是否为迭代器最好的方式是调用 isinstance(x, abc.Iterator)。得 益于 Iterator.__subclasshook__ 方法，即使对象 x 所属的类不是 Iterator 类的真实子类或虚拟子类，也能这样检查
>可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现`__iter__` 方法，但不能实现 `__next__` 方法。 另一方面，迭代器应该一直可以迭代。迭代器的 __iter__ 方法应该返回自身



## 5、最佳实践
### 5.1、元组
- 不要把可变对象放在元组里面。
- 增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了操作。

### 5.2、数组
虽然列表既灵活又简单，但面对各类需求时，我们可能会有更好的选择。比如，要存放
1000 万个浮点数的话，数组（array）的效率要高得多，因为数组在背后存的并不是 float
对象，而是数字的机器翻译，也就是字节表述。这一点就跟 C 语言中的数组一样。再比如
说，如果需要频繁对序列做先进先出的操作，deque（双端队列）的速度应该会更快。

如果我们需要一个只包含数字的列表，那么 `array.array` 比 `list` 更高效。数组支持所有跟
可变序列有关的操作，包括 `.pop`、`.insert` 和 `.extend`。另外，数组还提供从文件读取和存
入文件的更快的方法，如 `.frombytes` 和 `.tofile`。
Python 数组跟 C 语言数组一样精简。创建数组需要一个类型码，这个类型码用来表示在
底层的 C 语言应该存放怎样的数据类型。比如 b 类型码代表的是有符号的字符（signed
char），因此 array('b') 创建出的数组就只能存放一个字节大小的整数，范围从 -128 到
127，这样在序列很大的时候，我们能节省很多空间。而且 Python 不会允许你在数组里存 放除指定类型之外的数据。
### 5.3、处理找不到的键的一个选择

#### 5.3.1、collections.defaultdict
在实例化一个 defaultdict 的时候，需要给构造方法提供一个可调用对象，这 个可调用对象会在 __getitem__ 碰到找不到的键的时候被调用，让 __getitem__ 返回某种 默认值。
比如，我们新建了这样一个字典：`dd = defaultdict(list)`，如果键 'new-key' 在 dd 中还
不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。
(1) 调用 list() 来建立一个新列表。
(2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。
(3) 返回这个列表的引用
#### 5.3.2、特殊方法 `__missing__`
所有的映射类型在处理找不到的键的时候，都会牵扯到 __missing__ 方法。这也是这个方法
称作“missing”的原因。虽然基类 dict 并没有定义这个方法，但是 dict 是知道有这么个
东西存在的。也就是说，如果有一个类继承了 dict，然后这个继承类提供了 __missing__ 方
法，那么在 __getitem__ 碰到找不到的键的时候，Python 就会自动调用它，而不是抛出一个
KeyError 异常。

>`__missing__` 方法只会被 `__getitem__` 调用（比如在表达式 d[k] 中）。提供
`__missing__` 方法对 get 或者 `__contains__`（in 运算符会用到这个方法）这些 方法的使用没有影响。这也是我在上一节最后的警告中提到，defaultdict 中 的 default_factory 只对 `__getitem__` 有作用的原因。

### 5.4、字典
#### 5.4.1、键必须是可散列的
一个可散列的对象必须满足以下要求。
(1) 支持 hash() 函数，并且通过 __hash__() 方法所得到的散列值是不变的。
(2) 支持通过 __eq__() 方法来检测相等性。
(3) 若 a == b 为真，则 hash(a) == hash(b) 也为真。
所有由用户自定义的对象默认都是可散列的，因为它们的散列值由 id() 来获取，而且它们 都是不相等的。

> 如果你实现了一个类的 __eq__ 方法，并且希望它是可散列的，那么它一定要
有个恰当的 __hash__ 方法，保证在 a == b 为真的情况下 hash(a) == hash(b)
也必定为真。否则就会破坏恒定的散列表算法，导致由这些对象所组成的字
典和集合完全失去可靠性，这个后果是非常可怕的。另一方面，如果一个
含有自定义的 __eq__ 依赖的类处于可变的状态，那就不要在这个类中实现
__hash__ 方法，因为它的实例是不可散列的。

#### 5.4.2、字典在内存上的开销巨大
  由于字典使用了散列表，而散列表又必须是稀疏的，这导致它在空间上的效率低下。举例 而言，如果你需要存放数量巨大的记录，那么放在由元组或是具名元组构成的列表中会是 比较好的选择；最好不要根据 JSON 的风格，用由字典组成的列表来存放这些记录。用元 组取代字典就能节省空间的原因有两个：其一是避免了散列表所耗费的空间，其二是无需 把记录中字段的名字在每个元素里都存一遍。

  在用户自定义的类型中，__slots__ 属性可以改变实例属性的存储方式，由 dict 变成 tuple。
  记住我们现在讨论的是空间优化。如果你手头有几百万个对象，而你的机器有几个 GB 的 内存，那么空间的优化工作可以等到真正需要的时候再开始计划，因为**优化往往是可维护性的对立面**。

#### 5.4.3、键查询很快
#### 5.4.4、键的次序取决于添加顺序
当往 dict 里添加新键而又发生散列冲突的时候，新键可能会被安排存放到另一个位置。
#### 5.4.5、 往字典里添加新键可能会改变已有键的顺序
无论何时往字典里添加新的键，Python 解释器都可能做出为字典扩容的决定。扩容导致的
结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化。要注意的是，上面提到的这些变
化是否会发生以及如何发生，都依赖于字典背后的具体实现，因此你不能很自信地说自己
知道背后发生了什么。如果你在迭代一个字典的所有键的过程中同时对字典进行修改，**那
么这个循环很有可能会跳过一些键——甚至是跳过那些字典中已经有的键**。

### 5.4、集合
set 和 frozenset 的实现也依赖散列表，但在它们的散列表里存放的只有元素的引用（就
像在字典里只存放键而没有相应的值）。在 set 加入到 Python 之前，我们都是把字典加上
无意义的值当作集合来用的。

- 集合里的元素必须是可散列的。 
- 集合很消耗内存。
- 可以很高效地判断元素是否存在于某个集合。
- 元素的次序取决于被添加到集合里的次序。
- 往集合里添加元素，可能会改变集合里已有元素的次序。

### 5.5、继承
直接子类化内置类型（如 dict、list 或 str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型，用户自己定义的类应 该继承 collections 模块中 的类，例如 UserDict、UserList 和 UserString，这些类做了特殊设计，因此 易于扩展

## 6、装饰器

### 6.1、functools.wraps
标准库 functools 中的 wrap 函数用于包装函数, 不改变原有函数的功能, 仅改变原有函数的一些属性, 例如 __name__, __doc__, __annotations__ 等属性。
functools.wrap 可用于装饰器的内层函数, 抵消装饰器的副作用, 因为使用装饰器后, 原函数被内层函数赋值覆盖, 函数名称等信息丢失了(装饰器仅仅是不改变函数原有功能)

### 6.2、使用functools.lru_cache做备忘
functools.lru_cache 是非常实用的装饰器，它实现了备忘（memoization）功能。这是一 项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。LRU 三 个字母是“Least Recently Used”的缩写，表明缓存不会无限制增长，一段时间不用的缓存 条目会被扔掉。

### 6.3、单分派泛函数(类似 Java 方法重载)
