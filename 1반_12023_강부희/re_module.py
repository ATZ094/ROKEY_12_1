# re_module.py
import re



text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more"
aa = re.compile("[a-z]+")
result = aa.match("python")

print(result)



# re 와 접근 연산자 .  match() 메서드를 활용한 코드
result = re.match("[a-z]+", "python")
print(result)


print("\n")

# p = re.compile("[a-c]^",re.DOTALL)      # *re.DOTALL 은 하나의 옵션
p = re.compile("a.b",re.DOTALL)      # *re.DOTALL 은 하나의 옵션

print(p.match("dante"))
print(re.match("a-c","all day"))
print(p.match("a\nb"))

print("\n")


text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. Learn more"
p = re.compile("python",re.I)      # *re.DOTALL 은 하나의 옵션
p = re.compile("[a-z]+",re.I)      # *re.DOTALL 은 하나의 옵션


print(p.findall("python"))
print(p.match("python"))


rs1 = p.finditer("the of python")

for m in rs1 :
    print(m.group(),end=" \ ")
    print(m.span())



print("\n")

# p = re.compile("^python\s\w+")

poem = "my life is for Aiur"

p = re.compile("^i\s\w+",re.M)

print(p.findall(poem))      # ["python"]


print("\n")

# VERBOSE
p = re.compile(r''
               '&[#]'
               '('
               '0[0-7]+'
               '|[0-9]+'
               '|x[0-9a-fA-F]+'
               ');',
               re.X)

# HTML / XML 문자 참조에 사용되는 기호 (딱히 건드릴 필요는 없음 궁금하면 조사)
data = "&#07; &#8; &#x0A;"

print(p.findall(data))

# OR 연산자 : | (파이프 라인)
# 