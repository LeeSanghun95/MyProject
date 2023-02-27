a = ["이창훈",85,80,65,0,"평균"] #학생1
b = ["전승훈",85,75,95,0,"평균"] #학생2
c = ["채수원",85,90,80,0,"평균"] #학생3
d = ["최수연",85,65,70,0,"평균"] #학생4
e = ["한지훈",85,70,40,0,"평균"] #학생5

g = 0

#학생별 파이썬 점수 입력
while g <= 4:
 if g == 0 : #학생1
  f = int(input(a[0] + " 의 파이썬 성적 입력 : "))
  a[4] = int(f)
  print(a[0] + " 의 파이썬 점수는 : " + str(a[4]) + "입니다.")
 elif g == 1: #학생2
  f = input(b[0] + " 의 파이썬 성적 입력 : ")
  b[4] = int(f)
  print(b[0] + " 의 파이썬 점수는 : " + str(b[4]) + "입니다.")
 elif g == 2: #학생3
  f = input(c[0] + " 의 파이썬 성적 입력 : ")
  c[4] = int(f)
  print(c[0] + " 의 파이썬 점수는 : " + str(c[4]) + "입니다.")
 elif g == 3: #학생4
  f = input(d[0] + " 의 파이썬 성적 입력 : ")
  d[4] = int(f)
  print(d[0] + " 의 파이썬 점수는 : " + str(d[4]) + "입니다.")
 else:  # 학생5
  f = input(e[0] + " 의 파이썬 성적 입력 : ")
  e[4] = int(f)
  print(e[0] + " 의 파이썬 점수는 : " + str(e[4]) + "입니다.")

 g += 1

#학생별 평균점수 계산
avg_a = (a[1] + a[2] + a[3] + a[4]) / 4
a[5] = round(avg_a,1)
avg_b = (b[1] + b[2] + b[3] + b[4]) / 4
b[5] = round(avg_b,1)
avg_c = (c[1] + c[2] + c[3] + c[4]) / 4
c[5] = round(avg_c,1)
avg_d = (d[1] + d[2] + d[3] + d[4]) / 4
d[5] = round(avg_d,1)
avg_e = (e[1] + e[2] + e[3] + e[4]) / 4
e[5] = round(avg_e,1)

#성적표 출력
print("성적표".center(60) ) #print("%22s" % "성적표")
print("---------------------------------------------------------------")
print("".center(5),"국어".center(10),"영어".center(10),"수학".center(10),"파이썬".center(10),"평균".center(5) )
print(str(a[0]).center(0), str(a[1]).center(13), str(a[2]).center(10), str(a[3]).center(12), str(a[4]).center(10), str(a[5]).center(10))
print(str(b[0]).center(0), str(b[1]).center(13), str(b[2]).center(10), str(b[3]).center(12), str(b[4]).center(10), str(b[5]).center(10))
print(str(c[0]).center(0), str(c[1]).center(13), str(c[2]).center(10), str(c[3]).center(12), str(c[4]).center(10), str(c[5]).center(10))
print(str(d[0]).center(0), str(d[1]).center(13), str(d[2]).center(10), str(d[3]).center(12), str(d[4]).center(10), str(d[5]).center(10))
print(str(e[0]).center(0), str(e[1]).center(13), str(e[2]).center(10), str(e[3]).center(12), str(e[4]).center(10), str(e[5]).center(10))
print("평 균".center(0), str( (a[1]+b[1]+c[1]+d[1]+e[1]) / 5).center(13), str( (a[2]+b[2]+c[2]+d[2]+e[2]) / 5).center(10),
      str( (a[3]+b[3]+c[3]+d[3]+e[3]) / 5).center(12), str( (a[4]+b[4]+c[4]+d[4]+e[4]) / 5).center(10))
print("---------------------------------------------------------------")