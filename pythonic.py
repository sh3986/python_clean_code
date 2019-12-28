# coding=utf-8
my_numbers = (4, 5, 3, 9)
my_numbers[-1]  # 9

my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
my_numbers[2:5]  # 2,3,5

my_numbers[3:]  # 3,5,7,13,21
my_numbers[:3]  # 1,1,2
my_numbers[::]  # (1,1,2,3,5,8,13,21)
my_numbers[1:7:2]  # 1,3,8

# => 모두 slice 내장 객체를 전달하는 것
interval = slice(1, 7, 2)
my_numbers[1:7:2]
my_numbers[interval]

interval = slice(None, 3)
my_numbers[:3]
my_numbers[interval]
# range(1,100)[25:50]

# => 위의 기능은 __getitem__ 이라는 매직 메서드를 통해동작
# myobject[key]를 호출하도록
# __getitem__, __len__ 모두 구현한 객체는 반복 가능(리스트, 튜플, 문자열)

# __getitem__ 구현 방법
# 표준 라이브러리 객체를 감싸는 래퍼 클래스인 경우 해당 객체에 동작을 위임하면 된다.
# ※ 다른 클래스의 __foo나 _bar와 같은 형식의 변수에는 접근하지 않는 것이 원칙
class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


