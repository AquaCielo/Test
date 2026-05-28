print("hello world")
print(10)
print(3.14)
print(5*5)
print('장성겸 안녕?')
print('ㅋㅋ'*10)
print(5>19)
print(4<9)
print(not True)
print(not False)

name = '둘쨰'
animal = '딸'
age = 4
hobby = '뱃속'
is_adult = age >= 5

print('우리집' + animal + '이름은' + name + '이에요')
print(name, '는', str(age), '살이고', hobby + '을 잘쳐요')
print(name + '는 어른일까요?' + str(is_adult))

station1 = '사당'
station2 = '신도림'
station3 = '인천공항'

print(station1, '열차가 들어오고 있습니다.')
print(station2, '열차가 들어고오 있습니다.')
print(station3, '열차가 들어오고 있습니다.')

print (5%3)
print (5//3)
print (10>3)
print (5>=5)
print (3==3)
print (1!=3)

print((3>0)and(3<5))
print((3>0)&(3<5))
num = 3+4*2
num = num+4
print(num)
num = num+9
print(num)
num = num*4
print(num)

print(abs(-5))
print(pow(4,2))
print(max(5,20))
print(min(4,10))
print(round(3.14))
print(round(4.99))

from math import*
print (floor(4.99))
print (ceil(3.14))
print (sqrt(16))

from random import*
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " ,str(date), "일로 선정 되었습니다.")

print((2+3)/3)

day = randrange(3,30)
print("다음달 모임 날짜는",str(day), "입니다 ")

sentance = '나는 유치원생 입니다'
print (sentance)
sentance2 = "파이썬 c보다 쉬워요"
print (sentance2)
sentance3 = """
나는 유치원 생이고,
파이썬은 쉬워요
"""
print(sentance3)

minbn = "891011-1234567"
print("성별 : " + minbn[7])
print("연 : " + minbn[0:2])
print("월 : " + minbn[2:4])
print("앞자리 : " + minbn[:6])
print("뒷자리 : " + minbn[7:14])
print("연 : " + minbn[-7:])

python = "Python is Amaging"
print(python.lower())
print(python.upper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "java"))
print(python.replace("Amaging", "very hard"))

index = python.index("g")
print(index)
index = python.index("g", index + 1)
print(index)
print(python.find("i"))
print(python.count("a"))

print("나는 %d 살 입니다." %38)
print("나는 %s는 을 좋아해요" %'먹을거')
print("apple은 %c로 시작해요" % "a")
print("나는 %s와 %s 을 좋아해요" %("마","바"))

print("나는 {}살 입니다." .format(29))
print("나는 {}색과 {}색을 좋아해요." .format("파", "빨"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파", "빨"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파", "빨"))

print("나는 {age}살이고 {color}색을 좋아해요." .format(age = 34, color="빨강"))

age=34
color="red"
print(f"나는 {age}살이고 {color}색을 좋아해요.")

print("백문이 불여일견\n 백견이 불여잁타")
print("저는 \"장영조\" 입니다.")

add = 'http://daum.com'
addlst = add[7:]
addlst = addlst[:5]
password = addlst[:3] + str(len(addlst)) +str(addlst.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 압나다.".format(add, password))

add = 'http://google.com'
addlst = add.replace("http://", "")
addlst = addlst[:addlst.index(".")]
password = addlst[:3] + str(len(addlst)) +str(addlst.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 압나다.".format(add, password))

print("깃허브 테스트 중입니다 진짜 넘 복잡합니다 ㅜ ")
print("왜 안되는 걸까요? 나도 공유를 하고 싶어요")