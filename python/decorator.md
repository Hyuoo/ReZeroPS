# 파이썬 데코레이터 (Decorator)

데코레이터는 함수에 `@deco` 이런식으로 붙여서 쓸 수 있는
함수 래핑하는 역할을 데코레이터라고 한다.

#### 언제 데코레이터 씀?

데코레이터 자체가 패턴이 있는 경우에서 그 패턴에 대한 추상화가 명확할 때 사용해야 한다.

불필요한 데코레이터는 오히려 복잡성만 증가시킬 뿐이다.

#### 잘 만든 데코레이터는

- 실제 함수가 하는 일과, 데코레이터가 하는 일을 명확히 분리한다. (**독립성**)
- 여러 함수에 대해서 **재사용성**이 보장되어야 한다.
    - 그게 아니면 데코레이터가 아니라 함수를 쓰자.


### 함수를 매개변수로 받아 실행하는 데코레이터

``` python
def deco(func):
    def foo():
        print(func.__name__, "함수 실행.")
        func()
        print("끝.")
    return foo

@deco
def abc():
    print("Hello")

abc()
```

```
> abc 함수 실행.
> Hello
> 끝.
```


### 매개변수가 존재하는 함수의 데코레이터 (가변인자 처리)

``` python
# 매개변수도 그대로 매핑하려면 args, kwargs를 사용한다.
def deco(func):
    def foo(*args, **kwargs):
        print("+----{:^22}----+".format("func:"+func.__name__))
        func(*args, **kwargs)
        print("+----{:-^22}----+".format(""))
    return foo


@deco
def asdf(a=1, b=2):
    print("FOO", a, b)

@deco
def zxcv():
    print("zxcv")


asdf(3,b=(10, 20))  # a=3, b=(10, 20)
asdf(*(100, 200))   # a=100, b=200
asdf(**{"a":1000, "b":2000})    # a=1000, b=2000

zxcv()  # 매개변수가 없어도 정상으로 동작
```

```
> +----      func:asdf       ----+
> FOO 3 (10, 20)
> +------------------------------+

> +----      func:asdf       ----+
> FOO 100 200
> +------------------------------+

> +----      func:asdf       ----+
> FOO 1000 2000
> +------------------------------+

> +----      func:zxcv       ----+
> zxcv
> +------------------------------+
```


### 데코레이터에 파라미터 넣기

데코레이터에 (찐)데코레이터를 넣어서 데코레이터를 붙일 때 파라미터를 지정 할 수도 있다.

``` python
def decorator_factory(option=1):
    def decorator(func):
        def foo(*args, **kwargs):
            print("<<<<<<<<", option)
            func(*args, **kwargs)
            print(">>>>>>>>")
        return foo
    return decorator


@decorator_factory(option=10)
def foo1(a, b=20):
    print(a, b)

@decorator_factory("FF")
def foo2(a, b=20):
    print(a, b)

@decorator_factory()
def foo3(a, b=20):
    print(a, b)


foo1(30)

foo2(*(300, "@"))

foo3(**{"a": "hi"})
```

```
> <<<<<<<< 10
> 30 20
> >>>>>>>>

> <<<<<<<< FF
> 300 @
> >>>>>>>>

> <<<<<<<< 1
> hi 20
> >>>>>>>>
```

- 단 이렇게 구현하면 괄호를 안쓰면 안된다.
    ```
    # XXX 안 됨 XXX
    @decorator_factory
    def foo(a, b):
        print(a, b)
    ```


### 완성형? 데코레이터 (아님)

이런 식으로 괄호를 안써도 되고, 옵션이 필요 할 경우 쓰는 방식으로 구현 할 수 있다.

``` python
def decorator_factory(func_=None, option=1):
    def _decorator(func):
        def wrapper(*args, **kwargs):
            print(f"func name: {func.__name__} (option:{option})")
            func(*args, **kwargs)
            print("END.")
        return wrapper
    if callable(func_):
        return _decorator(func_)
    else:
        return _decorator


@decorator_factory
def foo1(a, b=20):
    print(f"Hello, {a}, {b}")

@decorator_factory()
def foo2(a, b=20):
    print(f"Hello, {a}, {b}")

@decorator_factory(option=100)
def foo3(a, b=20):
    print(f"Hello, {a}, {b}")


foo1(30)
foo2(a=99)
foo3(**{"a":None})
```

```
> func name: foo1 (option:1)
> Hello, 30, 20
> END.

> func name: foo2 (option:1)
> Hello, 99, 20
> END.

> func name: foo3 (option:100)
> Hello, None, 20
> END.
```


## 다수의 데코레이터

다음과 같이 실행 시간을 체크해주는 데코레이터와, 함수 이름을 출력해주는 데코레이터 2개를 만들었다.

함수 정보도 출력하고, 시간도 체크하기 위해서 두 데코레이터를 모두 사용하고싶으면 둘 다 쓰면 된다.

다만, 지금까지의 구현으로는 원치않은 동작을 할 수 있다.
어떤 문제점이 있는지 살펴보자.

``` python
def runtime(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}() running time: {end-start} seconds")
        return ret
    return wrapper

def info(func):
    def wrapper(*args, **kwargs):
        print("func_name:", func.__name__, "\t", type(func))
        ret = func(*args, **kwargs)
        return ret
    return wrapper


@runtime
def run_foo(a=None):
    for _ in range(22000000): ...

@info
def my_foo(a=None):
    print("print", a)


run_foo()

my_foo()
```

```
> run_foo() running time: 0.3177511692047119 seconds

> func_name: my_foo        <class 'function'>
> print None
```

이런 두 데코레이터를 같이 사용한다.

데코레이터를 여러개 사용하면 아래쪽의 데코레이터부터 적용이 된다.

``` python
@info
@runtime
def mix_foo(a=None):
    for _ in range(22000000): ...
    print("print", a)

mix_foo()
```

```
> func_name: wrapper_rt    <class 'function'>
> print None
> mix_foo() running time: 0.3551807403564453 seconds
```

runtime이 먼저 적용되고, runtime의 리턴값인 wrapper_rt 함수로 info데코레이터가 적용된 결과.

``` python
@runtime
@info
def mix_foo(a=None):
    for _ in range(22000000): ...
    print("print", a)

mix_foo()
```

```
> func_name: mix_foo       <class 'function'>
> print None
> wrapper_if() running time: 0.3604855537414551 seconds
```

반대로 info데코레이터 실행 후, 리턴값인 wrapper_if가 runtime데코레이터로 들어갔다.


### 해결

functool의 wraps를 래핑하는 함수에 데코레이터로 적용하면 된다.

``` python
from functools import wraps

def runtime(func):
    import time

    @wraps(func)
    def wrapper_rt(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}() running time: {end-start} seconds")
        return ret
    
    return wrapper_rt

def info(func):
    @wraps(func)
    def wrapper_if(*args, **kwargs):
        print("func_name:", func.__name__, "\t", type(func))
        ret = func(*args, **kwargs)
        return ret
    return wrapper_if


@info
@runtime
def mix_foo(a=None):
    for _ in range(22000000): ...
    print("print", a)

mix_foo()
```

```
> func_name: mix_foo       <class 'function'>
> print None
> mix_foo() running time: 0.3466227054595947 seconds
```


### 아까 그 완성형이라던 녀석에도

wraps를 써서 만들어주자.

``` python
import functools

def decorator_factory(func_=None, option=1):
    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"func name: {func.__name__} (option:{option})")
            result = func(*args, **kwargs)
            print("END.")
            return result
        return wrapper
    if callable(func_):
        return _decorator(func_)
    else:
        return _decorator
```