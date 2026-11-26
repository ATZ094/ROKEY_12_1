import re                       # 데이터 전처리에서 많이 쓰인다고 함.

# 정규 표현식을 정의해서 컴파일 함수 인수로 전달하면, 패턴 객체를 반환 함
# 패턴 객체 = re.compile("정규 표현식") , (Regular Expression - re)
#            검색 대상 문자열에서 패턴의 발견을 도와주는 객체
#       pattern = re.compile("정규 표현식")

        # match() 메서드 : 문자열의  "처음!" 부터 정규식과 매치되는지 조사함.

p = re.compile("[abc]")         # p -> 컴파일된 패턴 객체
m = p.match("Python")     # 매치 객체 -> 패턴객체.match("문자열")

print(m)        # 현재 함수값이 없을때 return값이 None이라 출력 됨
                # (정규 표현식이 있는지 패턴을 찾아야 하는데 없어서 None)

print("----------------------------------------------------------")
                       ## match()라는 메서드에 "a" 문자열을 추가 했을 경우
p = re.compile("[a-c]")         
m = p.match("a")        ## 정규표현 검색에 a라는 compile함수에 "a"라는 문자열을 검색
print(m)

m = p.match("before")        ## 정규표현 검색에 p라는 "before"라는 문자열을 검색
print(m)

m = p.match("dude")        ## 정규표현 검색에 p라는 "dude" 와 매치되는 문자열 검색
print(m)

m = p.match("a-c")        ## 정규표현 검색에 p라는 "dude" 와 매치되는 문자열 검색
print(m)

print("----------------------------------------------------------")

p = re.compile("[0-5]")
print(p.match("1:apple"))   # match - 1
print(p.match("2:banana"))  # match - 2
print(p.match("5:watermelon"))  # match - 5


print("----------------------------------------------------------")

p = re.compile("[abc][abc]")

print(p.match("aapple"))   # match - aa
print(p.match("cba"))


print("----------------------------------------------------------")

p = re.compile("[^a-c]")  # ^ -> 부정(not)의 의미 따라서 , a 부터 c 까지가 아닌 d부터 시작한다.

print(p.match("aapple"))   
print(p.match("banana"))
print(p.match("watermelon"))

print("----------------------------------------------------------")

p = re.compile("[^a-z]")  # 부정(not)의 의미 따라서 , a 부터 c 까지가 아닌 d부터 시작한다.

print(p.match("aapple"))   
print(p.match("banana"))
print(p.match("watermelon"))
print(p.match("3123:1231"))


print("----------------------------------------------------------")

p = re.compile("[\^a-z]")       # \ -> 의미 있는문자 => 의미 없는 문자  

print(p.match("aapple"))   
print(p.match("banana"))
print(p.match("watermelon"))
print(p.match("3123:1231"))

print("----------------------------------------------------------")

# p = re.compile("[\^a\-c]")       # \ -> 의미 있는문자 => 의미 없는 문자  

print(p.match("aapple"))   
print(p.match("banana"))
print(p.match("watermelon"))
print(p.match("^watermelon"))


print("----------------------------------------------------------")

p = re.compile("\D")      
# p = re.compile("[\D]")      

print(p.match("1:apple"))   
print(p.match("banana"))
print(p.match("banana"))
print(p.match("3:watermelon"))

print("----------------------------------------------------------")

# p = re.compile("\s")      
p = re.compile("\S")      

print(p.match("1:apple"))   
print(p.match("banana"))
print(p.match("banana"))
print(p.match("3:watermelon"))


print("----------------------------------------------------------")

p = re.compile("..")

print(p.match("1:apple"))   
print(p.match("banana"))
print(p.match("banana"))
print(p.match("1apple"))
print(p.match("+apple"))
print(p.match("@apple"))
print(p.match("가apple"))
print(p.match("가appl"))


print("----------------------------------------------------------")

p = re.compile("a.b")   # a 와 b 사이에 문자열이 하나는 있어야 한다

print(p.match("ab"))   
print(p.match("aab"))
print(p.match("banana"))
print(p.match("1apple"))
print(p.match("+apple"))
print(p.match("@apple"))
print(p.match("가apple"))
print(p.match("가appl"))


print("----------------------------------------------------------")

#       [] 대괄호 의 의미
#   1. 대괄호 내 문자들과 매칭
#   2. 일반 문자 : 대괄호 내 한개의 문자와 매치
#   3. 메타 문자 : 특수한 기능 업이 사용 (단, 일부는 *예외)
#   4. *예외의 경우 : [.] , + 이 둘은 문자 자체로 인식
#                    \ 뒤에 쓰인 메타문자 -> 문자 자체로 인식 ex) \* 등등
#   5. 하이픈(-) : 범위 표시 [a-b] , [0-9] , [1-9]
#   6. 별도 표기법 : \d, \D , \s , \w , \W

p = re.compile("a[.]b")           # . 을 []인덱스 처리를 하게 되면 . 그자체로 판단 한다.

print(p.match(".b"))
print(p.match("/t"))
print(p.match("[.b]"))


print("----------------------------------------------------------")


# p = re.compile("ca*t")           # . 을 []인덱스 처리를 하게 되면 . 그자체로 판단 한다.
p = re.compile("[ca*]t")           # . 을 []인덱스 처리를 하게 되면 . 그자체로 판단 한다.

print(p.match("cat"))
print(p.match("c[at]"))
print(p.match("caaaaaat"))
print(p.match("ca.at"))
print(p.match(""))


print("----------------------------------------------------------\n")


p = re.compile("c+at")           # . 을 []인덱스 처리를 하게 되면 . 그자체로 판단 한다.
           

print(p.match("cat"))
print(p.match("c[at]"))
print(p.match("caaaaaat"))
print(p.match("ca.at"))
print(p.match(""))


print("----------------------------------------------------------\n")


p = re.compile("ca{2}t")
           

print(p.match("ctct"))
print(p.match("caaaat"))
print(p.match("caat"))
print(p.match("caacaat"))
print(p.match("caatcaatcaatcaat"))


print("----------------------------------------------------------\n")


p = re.compile("ca?t")
           

print(p.match("ab?c"))
print(p.match("ca??t"))
print(p.match("cat"))
print(p.match(""))
print(p.match(""))


print("----------------------------------------------------------\n")

#       ^ 부정(not)의 논리 연산자
p = re.compile("^hello") # ^ 는 부정의 의미 따라서 
                         # 인덱스는 0부터 시작 하므로 공백을 생략함.
           

print(p.match("hello World"))
print(p.match(" hello world"))
print(p.match("\nhello world"))
print(p.match("pello world"))



print("----------------------------------------------------------\n")

p = re.compile("world")        # $는 앞의 wordl로 끝나야 한다라는 의미.

print(p.match("hello World"))
print(p.match(" hello world"))
print(p.match("\nhello world"))
print(p.match("pello world"))


# search() 메서드       : 문자열의 전체를 검색하여 정규식과 매치가 되는지 조사한다.
print(p.search("hello world"))
print(p.search("world 123"))
print(p.search("hello world"))
print(p.search("world 123"))



