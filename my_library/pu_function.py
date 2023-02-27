import unicodedata # 한글이 포함된 문자열에 간격 맞추기 솔루션을 제공하는 라이브러리
from wcwidth import wcswidth  # 한글이 포함된 문자열에 간격 맞추기 솔루션을 제공하는 라이브러리

def line_divide():
    return  print("------------------------------------------------------------------------------------------------" +
                  "------------------------------------------------------------------------------------------------")

def preFormat(string, width, align='<', fill=' '):
    count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in string))
    return {
        '>': lambda s: fill * count + s, # lambda 매개변수 : 표현식
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2)
                       + s
                       + fill * (count / 2 + count % 2)
    }[align](string)

def fmt(x, w, align='r'): # align의 기본값은 'r : right'
    x = str(x) # 해당 문자열
    l = wcswidth(x) # 문자열이 몇자리를 차지하는지를 계산.
    s = w-l # 남은 너비 = 사용자가 지정한 전체 너비 - 문자열이 차지하는 너비
    if s <= 0:
        return x
    if align == 'l':
        return x + ' '*s
    if align == 'c':
        sl = s//2 # 변수 좌측
        sr = s - sl # 변수 우측
        return ' '*sl + x + ' '*sr
    return ' '*s + x