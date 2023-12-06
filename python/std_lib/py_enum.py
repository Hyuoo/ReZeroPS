"""
class enum.Enum
class enum.auto
class enum.IntEnum
"""
import enum
hr = lambda:print("-"*50)

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    ORANGE = 7
    BLACK = 0
    # 같은 값을 가진 멤버는 ALIAS로써 쓰인다.
    # 이터레이션 시 제공안된다.
    OTHER_RED = 1


# unpacking이 유효함. 각 멤버 리턴
print(*Color)
# 리스트로 바꾸면 그냥 print시 모양이 살짝 다름. 각 멤버인건 동일
print(list(Color))
print([*Color])

hr()

print("Color:", Color)
print("Color.RED:",Color.RED, "\ttype(Color.RED):", type(Color.RED),
      "\trepr(Color.RED):", repr(Color.RED),
      "\nColor.RED.name:", Color.RED.name,
      "\tColor.RED.value:", Color.RED.value)
print(Color.GREEN)
hr()
a = Color
print("a:", a)
print("a.RED:",a.RED, "\ttype(a.RED):", type(a.RED),
      "\trepr(a.RED):", repr(a.RED),
      "\na.RED.name:", a.RED.name,
      "\ta.RED.value:", a.RED.value)
print(a.GREEN)

hr()

print("for:")
for i in Color:
    print(i, i.name, i.value, sep="\t")

hr()

# 멤버변수로 접근
# 잘못된 멤버변수 접근: AttributeError: name
print(Color.RED)
# 상수로 접근
# 없는 상수 접근: ValueError: {const} is not a valid {class(Enum)}
print(Color(3))
# name으로 접근
# 없는 키 접근: KeyError
print(Color["GREEN"])

hr()
# 해시 가능
didi = {}
didi[Color.RED] = "is red"
didi[Color["BLACK"]] = "is black"
print(didi)
print(didi[Color.BLACK], didi[Color["BLACK"]], didi[Color(0)])

hr()

print(
    Color.BLACK == 0,  # False  # 상수와 직접 비교를 하려면 IntEnum을 사용
    Color.BLACK.value == 0,  # True
    Color.BLACK == Color(0) == Color["BLACK"],  # True
    Color.BLACK == "BLACK",  # False
    Color.BLACK.name == "BLACK",  # True
    sep="\n")

hr()

class auto_enum(enum.Enum):
    # enum.auto로 상수값을 자동으로 할당.
    A = enum.auto()
    B = enum.auto()
    C = 10
    D = enum.auto()
    # 다시 역순으로 내려가도 되긴 하지만,
    # E = 6
    # 역순 이후에 다시 auto는 에러 발생한다.
    # F = enum.auto()

for mem in auto_enum:
    print(repr(mem), mem, mem.name, mem.value, sep="\t")

hr()

class int_enum(enum.IntEnum):
    """
    IntEnum의 멤버변수는 모두 상수 자체로써 연산이 가능하다.
    """
    A = 65
    B = 66
    C = 67
    D = enum.auto()
    two = 2

print(*int_enum)
print(
    int_enum.A,
    int_enum.A == 65,
    int_enum.A == int_enum.B-1
)
print("012345"[int_enum.two])
