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


# 컨텍스트 관리자 (context manager)
fd = open("filename")
try:
    None
    # process_file(fd)
finally:
    fd.close()

# => with (컨텍스트 관리자)
with open("filename") as fd:
    None
    # process_file(fd)

# 컨텍스트 관리자는 __enter__와  __exit__ 두 개의 매직 메서드로 구성
# 예외가 발생한다고 하더라도 __exit__는 자동으로 호출된다
# 예외가 __exit__의 파라미터로 입력된다.
def stop_database():
    None
    # run("systemctl stop postgresql.service")

def start_database():
    # run("systemctl start postgresql.service")

class DBHandler:
    def __enter__(self):
        stop_database()
        return self
    # __exit__가 True 0를 반환하면 잠재적으로 발생한 예외를 호출자에게 전파하지 않고
    # 멈춘다는 것을 뜻한다.( 일반적으로 발생된 예외를 삼키는 것은 좋지 않은 습관이다.)
    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()

def db_backup():
    None
    # run("pg_dump database")

def main():
    with DBHandler():
        db_backup()


# 컨텍스트 관리자 구현
# 특정 개체에 속하지 않은 컨텍스트 관리자가 필요한 경우 사용
import contextlib

@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()

with db_handler():
    db_backup()


# 프로퍼티 : 객체의 어떤 속성에 대한 접근을 제어할 때 사용
# @property : getter
# @<property name>.setter : setter
import re
EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")
def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None

class User:
    def __init__(self, username):
        self.username = username
        self._email = None
@property
def email(self):
    return self._email

@email.setter
def email(self, new_email):
    if not is_valid_email(new_email):
        raise ValueError(f"유효한 이멜이 아니므로 {new_email} 값을 사용할 수 없음")
    self._email = new_email

u1 = User("jsmith")
u1.email = "jsmith@outlook.com" # setter 자동 호출
u1.email # getter 자동 호출



from datetime import timedelta, date

class DataRangeIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration

        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

for day in DataRangeIterable(date(2019,1,1), date(2019,1,5)):
    print(day)


# 컨테이너 이터러블
# 호출할 때 마다 새오룬 이터레이터를 만드는 객체


class DataRangeIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

r1 = DataRangeIterable(date(2019,1,1), date(2019,1,5))
print(",".join(map(str, r1)))