# re_match()

import re

# 패턴 객체     = re.compile(메타문자를 활용한 정규 표현식이 내부에 들어감)
# 검색된 리스트  = 패턴객체.findall("패턴과 일치 여부를 확인할 문자열")_


text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more"
aa = re.compile("Python")
m = aa.findall(text)
result = len(m)
print(m)
print(result)

