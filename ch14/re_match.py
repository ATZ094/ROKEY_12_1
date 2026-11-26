# re_match()

import re

# 패턴 객체 = re.compile(메타문자를 활용한 정규 표현식이 내부에 들어감)
# 매치객체  = 패턴객체.match("패턴과 일치 여부를 확인할 문자열이 들어감") = 검색 대상 문자열

# class 클래스명 :
#         def match(self) :
#             return 매치 객체
        
#         def search(self) :
#             패턴 객체 = 클래스명()
#             return



# m = re.compile("[a-z]+")
# p = m.match("python")
# print(p)


p = re.compile("[a-z]+[0-9]")
print(p.match("3python"))
print(p.match("python9"))

m = p.match("python8")

if m :
    print(f"Match Founded : {m.group()}")    # match 데이터의 모든걸 그룹화 하여 가져옴
    print(f"start at : {m.start()}")         # match 한 데이터의 시작점을 출력
    print(f"end at : {m.end()}")             # match 한 데이터의 끝 부분 
    print(f"span : {m.span()}")              # match 한 데이터의 튜플로 표현
else :
    print("Not Matched Founded")

print("\n")

text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more"
aa = re.compile("Python")
m = aa.search(text)
print(m)


