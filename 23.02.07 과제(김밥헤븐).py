import sys

kimbap_info = {"김밥": 2500, "참치김밥": 3000, "돈가스김밥":3500, "고추참지김밥":3500,
             "소고기김밥":4500, "치즈김밥":3000, "샐러드김밥":2500, "꼬마김밥":1200,
             "충무김밥":20000, "꽈리김밥":3500, "진미김밥":3700}

noodle_info = {"라면": 4000, "치즈라면": 4500, "된장라면":4700, "떡라면":4800,
             "만두라면":4500, "떡만두라면":5000, "카레라면":4500, "해물라면":5500,
             "짜장라면":4200, "비빔라면":4200}

dongas_info = {"돈가스":8000, "치즈돈가스":9000, "고치돈":10000, "등심돈가스":7500,
               "안심돈가스":7500, "피카츄돈가스":500, "새우돈가스":7500, "대왕돈가스":12000,
               "치킨돈가스":6000, "함박스테이크":9500}

rice_info = {"제육덮밥":7000, "오무라이스":7000, "하이라이스":7000, "오징어덮밥":7500,
             "짜장덮밥":6500, "소고기덮밥":8000, "카레덮밥":6500, "돌솥비빔밥":7000, "김치덮밥":6500}

guk_info = {"김치찌개":6500, "된장찌개":6500, "순두부찌개":6500, "내장찌개":6500,
            "해물된장찌개":8500, "부대찌개":7800}

dukboki_info = {"떡볶이":3000, "치즈떡볶이":4500, "라볶이":5000, "마약떡볶이":99900,
                "컵떡볶이":500}

woodong_info = {"우동":3000, "튀김우동":4500, "김치우동":4500, "유부우동":4500}

gukbap_info = {"육개장":6000, "알탕":7500, "갈비탕":8000, "황태해장국":7000,
               "순대국밥":5500, "명태국밥":7000, "공기밥":1000}

action_info = {"주문하기":1, "매출보기":2, "종료하기":0}

menu_info = {"김밥류":1, "라면류":2, "돈가스류":3, "밥류":4, "찌개류":5, "떡볶이":6, "우동류":7, "국밥류":8, "결제":9, "뒤로가기":0}

delivery_info = {"포장(10% 할인)":1, "매장식사(할인없음)":2, "배달(배달료 8900원 추가)":3, "뒤로가기":0}

#주문,매출,종료
action_save = {}
#포장,매장식사,배달
delivery_save = {}
#선택한 메뉴정보
menu_save = {}
#주문메뉴이름, 금액
order_save = {}
#주문메뉴이름, 수량
order_save2 = {}
#결제확인 매출메뉴이름, 금액
sales_save = {}
#결제확인 매출 수량
sales_save2 = {}
#결제확인 매출 총합 금액
sales_amt = {}

def line_divide():
    return  print("-----------------------------------------------------------------------------------------------------------")

def action_check():
    line_divide()

    for key, value in action_info.items():
        print(str(value) + ".", key)

    print('무엇을 하시겠습니까?')
    action = sys.stdin.readline().rstrip()
    line_divide()
    action_saving(action)

def action_saving(action):
    action_save.clear()

    if action == "1":
        action_save["주문"] = action
        delivery_check()
    elif action == "2":
        action_save["매출"] = action
        sales_print()
    elif action == "0":
        action_save["종료"] = action
        exit()
    else:
        print("다시 선택해주세요.")
        action_check()

def delivery_check():
    for key, value in delivery_info.items():
        print(str(value) + ".", key)

    print('포장,매장식사,배달 여부를 선택해주세요.')
    delivery = sys.stdin.readline().rstrip()

    line_divide()
    delivery_saving(delivery)

def delivery_saving(delivery):
    delivery_save.clear()

    if delivery == "1":
        delivery_save["포장"] = delivery
        menu_check1()
    elif delivery == "2":
        delivery_save["매장식사"] = delivery
        menu_check1()
    elif delivery == "3":
        delivery_save["배달"] = delivery
        menu_check1()
    elif delivery == "0":
        delivery_save["뒤로가기"] = delivery
        action_check()
    else:
        print("다시 선택해주세요.")
        delivery_check()

def menu_check1():
    menu_save.clear()

    if "주문" in action_save:
        for key, value in menu_info.items():
            print(str(value) + ".", key)

        print('무엇을 보시겠습니까?')
        menu = sys.stdin.readline().rstrip()
        line_divide()
        menu_saving(menu)

def menu_check2():
    i = 0
    global menu_info_temp

    if "김밥류" in menu_save:
        print("%50s" % "메뉴표(김밥류)")
        for key, value in list(kimbap_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "김밥류"

    elif "라면류" in menu_save:
        print("%50s" % "메뉴표(라면류)")
        for key, value in list(noodle_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "라면류"

    elif "돈가스류" in menu_save:
        print("%50s" % "메뉴표(돈가스류)")
        for key, value in list(dongas_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "돈가스류"

    elif "밥류" in menu_save:
        print("%50s" % "메뉴표(밥류)")
        for key, value in list(rice_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "밥류"

    elif "찌개류" in menu_save:
        print("%50s" % "메뉴표(찌개류)")
        for key, value in list(guk_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "찌개류"

    elif "떡볶이" in menu_save:
        print("%50s" % "메뉴표(떡볶이)")
        for key, value in list(dukboki_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "떡볶이"

    elif "우동류" in menu_save:
        print("%50s" % "메뉴표(우동류)")
        for key, value in list(woodong_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "우동류"

    elif "국밥류" in menu_save:
        print("%50s" % "메뉴표(국밥류)")
        for key, value in list(gukbap_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + str(value) + ")")
        menu_info_temp = "국밥류"

    elif "결제" in menu_save:
        payment_print()

    print("0. " + "뒤로가기")

    order_check1()
    menu_info_temp = ""

def menu_saving(menu):
    menu_save.clear()

    if menu == "1":
        menu_save["김밥류"] = menu
        menu_check2()
    elif menu == "2":
        menu_save["라면류"] = menu
        menu_check2()
    elif menu == "3":
        menu_save["돈가스류"] = menu
        menu_check2()
    elif menu == "4":
        menu_save["밥류"] = menu
        menu_check2()
    elif menu == "5":
        menu_save["찌개류"] = menu
        menu_check2()
    elif menu == "6":
        menu_save["떡볶이"] = menu
        menu_check2()
    elif menu == "7":
        menu_save["우동류"] = menu
        menu_check2()
    elif menu == "8":
        menu_save["국밥류"] = menu
        menu_check2()
    elif menu == "9":
        menu_save["결제"] = menu
        menu_check2()
    elif menu == "0":
        menu_save["뒤로가기"] = menu
        delivery_check()
    else:
        print("다시 선택해주세요.")
        menu_check1()

def menu_check2():
    i = 0
    global menu_info_temp

    if "김밥류" in menu_save:
        print("%50s" % "메뉴표(김밥류)")
        for key, value in list(kimbap_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "김밥류"

    elif "라면류" in menu_save:
        print("%50s" % "메뉴표(라면류)")
        for key, value in list(noodle_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "라면류"

    elif "돈가스류" in menu_save:
        print("%50s" % "메뉴표(돈가스류)")
        for key, value in list(dongas_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "돈가스류"

    elif "밥류" in menu_save:
        print("%50s" % "메뉴표(밥류)")
        for key, value in list(rice_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "밥류"

    elif "찌개류" in menu_save:
        print("%50s" % "메뉴표(찌개류)")
        for key, value in list(guk_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "찌개류"

    elif "떡볶이" in menu_save:
        print("%50s" % "메뉴표(떡볶이)")
        for key, value in list(dukboki_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "떡볶이"

    elif "우동류" in menu_save:
        print("%50s" % "메뉴표(우동류)")
        for key, value in list(woodong_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "우동류"

    elif "국밥류" in menu_save:
        print("%50s" % "메뉴표(국밥류)")
        for key, value in list(gukbap_info.items()):
            i += 1
            print(str(i) + ".", key + "(" + format(round(value),",") + ")")
        menu_info_temp = "국밥류"

    elif "결제" in menu_save:
        payment_print()

    print("0. " + "뒤로가기")

    order_check1()
    menu_info_temp = ""

def menu_saving(menu):
    menu_save.clear()

    if menu == "1":
        menu_save["김밥류"] = menu
        menu_check2()
    elif menu == "2":
        menu_save["라면류"] = menu
        menu_check2()
    elif menu == "3":
        menu_save["돈가스류"] = menu
        menu_check2()
    elif menu == "4":
        menu_save["밥류"] = menu
        menu_check2()
    elif menu == "5":
        menu_save["찌개류"] = menu
        menu_check2()
    elif menu == "6":
        menu_save["떡볶이"] = menu
        menu_check2()
    elif menu == "7":
        menu_save["우동류"] = menu
        menu_check2()
    elif menu == "8":
        menu_save["국밥류"] = menu
        menu_check2()
    elif menu == "9":
        menu_save["결제"] = menu
        menu_check2()
    elif menu == "0":
        menu_save["뒤로가기"] = menu
        delivery_check()
    else:
        print("다시 선택해주세요.")
        menu_check1()

def order_check1():
    global order_cnt

    print("무엇을 주문하시겠습니까?")
    order = sys.stdin.readline().rstrip()

    if not order.isdigit():
        print("다시 선택해주세요.")
        menu_check2()
    else:
        order = int(order)

    order_cnt = 0

    #뒤로가기
    if order == 0:
        line_divide()
        menu_check1()

    if menu_info_temp == "김밥류":
        if order > len(list(kimbap_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(kimbap_info.keys())[order-1],list(kimbap_info.values())[order-1])
        order_saving2(list(kimbap_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "라면류":
        if order > len(list(noodle_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(noodle_info.keys())[order-1],list(noodle_info.values())[order-1])
        order_saving2(list(noodle_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "돈가스류":
        if order > len(list(dongas_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(dongas_info.keys())[order-1],list(dongas_info.values())[order-1])
        order_saving2(list(dongas_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "밥류":
        if order > len(list(rice_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(rice_info.keys())[order-1],list(rice_info.values())[order-1])
        order_saving2(list(rice_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "찌개류":
        if order > len(list(guk_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(guk_info.keys())[order-1],list(guk_info.values())[order-1])
        order_saving2(list(guk_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "떡볶이":
        if order > len(list(dukboki_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(dukboki_info.keys())[order-1],list(dukboki_info.values())[order-1])
        order_saving2(list(dukboki_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "우동류":
        if order > len(list(woodong_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(woodong_info.keys())[order-1],list(woodong_info.values())[order-1])
        order_saving2(list(woodong_info.keys())[order-1], order_cnt)
        order_check2()

    if menu_info_temp == "국밥류":
        if order > len(list(gukbap_info))  or  order < 0:
             print("다시 선택해주세요.")
             order_check1()

        order_cnt += 1
        order_saving(list(gukbap_info.keys())[order-1],list(gukbap_info.values())[order-1])
        order_saving2(list(gukbap_info.keys())[order-1], order_cnt)
        order_check2()

    order_cnt = 0

#현재 주문현황 출력
def order_check2():
    print("현재 주문한 갯수:",str(sum(order_save2.values())),"현재 가격:", format( round( sum(order_save.values() ) ), "," ) )
    line_divide()
    menu_check2()

#주문메뉴이름, 금액 저장
def order_saving(key, value):
        if key in order_save:
            order_save[key] += value
        else:
            order_save[key] = value

#주문메뉴이름, 개수 저장
def order_saving2(key, value):
    if key in order_save2:
        order_save2[key] += value
    else:
        order_save2[key] = value

#결제 계산서 출력
def payment_print():
    i = 0
    dis_amt1= 0
    dis_amt2 = 0
    dis_amt3 = 0
    global total_sales_amt

    print("%50s" % "계산서")

    print("주문내역:")
    for key, value in list(order_save.items()):
        i += 1
        print(str(i) + ".", key + "(" + format(value,",") + ")")

    print("%100s" % "총 주문수량: ",str(sum(order_save2.values())) )

    #포장, 식사, 배달 할인
    for key, value in list(delivery_save.items()):
        if key == "포장":
            dis_amt1 = sum(order_save.values()) * 0.1
            print("%100s" % "종 결제금액: " + format(sum(order_save.values()), ","))
            print("%100s" % "포장 할인금액: " + format(round(dis_amt1), ","))
        elif key == "매장식사":
            pass
        else :
            dis_amt2 = 8900
            print("%100s" % "종 결제금액: " + format(sum(order_save.values()), ","))
            print("%100s" % "배달 추가금액: " + format(dis_amt2, ","))

    #세트 할인
    if sum(order_save2.values()) >= 4 :
       dis_amt3 = sum(order_save.values()) * 0.3
       print("%100s" % "4개이상 30% 할인금액: " + format(round(dis_amt3), ","))
    elif sum(order_save2.values()) >= 3:
        dis_amt3 = sum(order_save.values()) * 0.25
        print("%100s" % "3개이상 25% 할인금액: " + format(round(dis_amt3), ","))
    elif sum(order_save2.values()) >= 2:
        dis_amt3 = sum(order_save.values()) * 0.2
        print("%100s" % "2개이상 20% 할인금액: " + format(round(dis_amt3), ","))

    print("%100s" % "최종 결제금액: " + format(round(sum(order_save.values()) - dis_amt1 - dis_amt3 + dis_amt2),","))
    line_divide()

    total_sales_amt = round(sum(order_save.values()) - dis_amt1 - dis_amt3 + dis_amt2)

    payment_check()

#결제 확인
def payment_check():
    print("1. 결제확인")
    print("2. 주문초기화")
    print("3. 뒤로가기")

    print("결제 하시겠습니까?")
    payment = sys.stdin.readline().rstrip()

    if payment == "1":
        #총 매출금액
        if len(list(sales_amt)) <= 0:
            sales_amt["매출금액"] = total_sales_amt
        else:
            sales_amt["매출금액"] = sales_amt.get("매출금액") + total_sales_amt

        print("결제완료")
        init_orders()
        action_check()
    elif payment == "2":
        print("주문초기화 완료")
        order_save.clear()
        order_save2.clear()
        action_check()
    elif payment == "3":
        menu_check1()
    else:
        print("다시 선택해주십시요.")
        payment_check()

def init_orders():

    #매출내역 갱신
    sales_save.update(order_save)

    #매출수량 누적
    temp = list(order_save2.keys())
    for i in range(len(order_save2)):
        if temp[i] in sales_save2:
            sales_save2[temp[i]] += order_save2[temp[i]]
        else:
            sales_save2[temp[i]] = order_save2[temp[i]]

    order_save.clear()
    order_save2.clear()

#매출 총합 출력
def sales_print():
    i = 0

    print("총 매출내역:")
    for key, value in list(sales_save.items()):
        i += 1
        print(str(i) + ".", key + "(" + format(value,",") + ")")

    print("%100s" % "총 매출수량: ", str(sum(sales_save2.values())))

    if len(list(sales_amt)) <= 0:
        print("%100s" % "총 매출금액: ", str("0"))
    else:
        print("%100s" % "총 매출금액: " + format(sales_amt.get("매출금액"), ","))

    print("0. 뒤로가기")

    sales = sys.stdin.readline().rstrip()
    if sales == "0":
        action_check()
    else:
        print("다시 선택해주십시요.")
        sales_print()


action_check()