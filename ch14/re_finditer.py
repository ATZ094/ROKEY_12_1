# re_finditer.py
import re

# 패턴 객체     = re.compile(메타문자를 활용한 정규 표현식이 내부에 들어감)
# 매치 객체들의 묶음(matchliter)  = 패턴객체.finditer("패턴과 일치 여부를 확인할 문자열")_


text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more"
aa = re.compile("Python")
result = aa.finditer(text)

print(result,"\n")
print(list(result))

print("\n")

# 반복된 객체 형태이기 때문에 리스트를 for문에 적용시켜 출력 시켜 볼 수 있다.
for matchobj in result :
    print(matchobj)

print("----------------------\n")

text = "i am super lucky"
p = re.compile("[a-z]+")
m = p.finditer(text)

for matchobj in m :
    print(matchobj.group(), end=" / ")
    print(matchobj.span())



