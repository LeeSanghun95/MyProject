import sys
import pu_function 
import pu_class
import numpy as np
import datetime as dt


main_menu_info = {"도서관 선택":1, "조회":2, "대여":3, "반납":4, "반납내역 조회":5, "종료":6}
library_info =  {"장덕도서관":1, "첨단도서관":2, "신가도서관":3, "뒤로가기":4}

user = pu_class.Global_var()
library = pu_class.book_list()
cart = pu_class.cart_list()
rental = pu_class.rental_list()
return_ = pu_class.return_list()

now = dt.datetime.now()
td = dt.timedelta

def action_chk():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('도서관리 화면',user.g_user_info_list[2], user.g_cur_library_nm) )

    for key, value in main_menu_info.items():
        print(str(value) + ".", key)

    print('\n무엇을 하시겠습니까?')
    action = sys.stdin.readline().strip().replace(" ","")

    if action == "1":
        library_select()
    elif action == "2":
        if user.g_cur_library_nm == '':
            print('\n도서관을 먼저 선택 해주세요.') 
            library_select()           
        else:
            book_join()
    elif action == "3":     
        if user.g_cur_library_nm == '':
            print('\n도서관을 먼저 선택 해주세요.') 
            library_select() 
        else:
            book_rental()       
    elif action == "4":
        if user.g_cur_library_nm == '':
            print('\n도서관을 먼저 선택 해주세요.')
            library_select() 
        else:
            book_return()     
    elif action == "5":
        return_join()
    elif action == "6":
        print('프로그램을 종료합니다.')
        exit()
    else:
        print('다시 선택해주세요.')
        action_chk()

#반납내역 조회
def return_join():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('반납내역 조회화면',user.g_user_info_list[2], user.g_cur_library_nm) )    
 
    return_.join(user.g_user_info_list[0])
    print('\n반납내역 조회완료.(나가기: Q)')

    action = sys.stdin.readline().strip().replace(" ","")

    while action.upper() != 'Q':
        print('\n다시 입력해주세요.') 
        return_join()

    print('\n반납내역 조회화면을 나갑니다.') 
    action_chk()

#도서관 선택
def library_select():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('도서관 선택 화면',user.g_user_info_list[2], user.g_cur_library_nm) )    
    for key, value in library_info.items():
        print(str(value) + ".", key)    

    print('\n이용하실 도서관의 순번을 선택해주세요.(나가기: Q)')
    action = sys.stdin.readline().strip().replace(" ","")
    if action.upper() == 'Q':
        print('\n도서관 선택 화면을 나갑니다.') 
        action_chk()

    if action not in [str(i) for i in list(library_info.values())]:
        print('\n검색결과에 없는 순번입니다. 다시 선택해주세요.')    
        library_select()         
 
    if int(action) <= 3:
        #user.g_cur_library = library_info.get( list(library_info)[int(action)-1] )
        user.g_cur_library_nm = list(library_info)[int(action)-1]

        print("%s를 선택하였습니다." % ( list(library_info)[int(action)-1] ) )  
        action_chk()
    elif int(action) == 4:
        print("%s를 선택하였습니다." % ( list(library_info)[int(action)-1] ) )  
        action_chk()
    else:
        print('다시 선택해주세요.')
        library_select()

def book_join():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('도서조회 화면',user.g_user_info_list[2], user.g_cur_library_nm) )    
    
    print('\n검색할 도서를 입력하세요.(도서명, 저자)')
    print('\n도서관별 5권씩 최대 15권까지 검색됩니다.(나가기: Q)')

    action = sys.stdin.readline().strip().replace(" ","")

    if action.upper() == 'Q':
        print('\n조회 화면을 나갑니다.') 
        action_chk()

    library.library = user.g_cur_library
    library.book_nm = action
    library.author_nm = action

    library.book_join()

    book_cart()

def book_cart():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('장바구니 추가 화면',user.g_user_info_list[2], user.g_cur_library_nm) )  

    print('\n장바구니에 추가할 도서의 순번을 선택해주세요.(나가기: Q)')   
    no = sys.stdin.readline().strip().replace(" ","")

    # b = [i[0] for i in user.g_cur_book_join_list]
    # print(b)
    if no.upper() == 'Q':
        print('\n장바구니 화면을 나갑니다.') 
        action_chk()

    if no not in [str(i[0]) for i in user.g_cur_book_join_list]:
        print('\n검색결과에 없는 순번입니다. 다시 선택해주세요.')    
        book_cart()
    else:
        cart_saving(int(no)-1)

#장바구니 추가
def cart_saving(no):   
    cart_save = np.empty((0,len(user.g_cur_book_join_list[0])), int)

    for i, v in enumerate(user.g_cur_book_join_list):
        if i == no:
            cart_save = np.append(cart_save, np.array([v]), axis=0)

            # print(user.g_user_info_list[0], cart_save[0,1], cart_save[0,4], cart_save[0,5], cart_save[0,2], cart_save[0,3], 
            #             now.date().strftime("%Y년-%m월-%d일"))

            #현재 이용자가 이미 해당 도서를 장바구니에 추가를 하였다면
            if cart.dup_chk(user.g_user_info_list[0], cart_save[0,1]) >= 1:
                print('이미 장바구니에 추가한 도서입니다. 다시 선택해주세요.')
                book_cart()
            else:
                cart.add( user.g_user_info_list[0], cart_save[0,1], cart_save[0,4], cart_save[0,5], cart_save[0,2], cart_save[0,3], 
                            now.date().strftime("%Y년-%m월-%d일") )
                print('%s 번의  "%s"  도서 장바구니 추가완료' % (cart_save[0,0], cart_save[0,4]))
                book_cart()

def book_rental():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('대여등록 화면',user.g_user_info_list[2], user.g_cur_library_nm) ) 

    #장바구니에 추가한 도서가 있다면
    if cart.is_cart_chk(user.g_user_info_list[0]) >= 1:
        cart.join(user.g_user_info_list[0])
    else: 
        print('\n장바구니가 비어있습니다. 장바구니를 추가해주세요.') 
        action_chk()        

    #한명이 대여할 수 있는 도서 권수 5권 제한
    if rental.max_rental_cnt_chk(user.g_user_info_list[0]) >= 5:
        print('대여제한 권수 5권을 초과합니다 현재 대여권수: %s. 반납 후 다시 대여해주세요.' % (rental.is_rental_chk(user.g_user_info_list[0])) )
        book_return()        

    print('\n대여제한 권수: 5권, 현재 대여권수: %s권, 반납일자: 대여일로부터 5일까지' % (rental.is_rental_chk(user.g_user_info_list[0])))   
    print('\n대여하실 도서의 순번을 선택해주세요.(나가기: Q)')  
    no = sys.stdin.readline().strip().replace(" ","")

    if no.upper() == 'Q':
        print('\n대여등록 화면을 나갑니다.') 
        action_chk()

    if no not in [str(i[0]) for i in user.g_cur_cart_join_list]:
        print('\n검색결과에 없는 순번입니다. 다시 선택해주세요.')    
        book_rental()
    else:
        rental_saving(int(no)-1)

#대여내역 추가
def rental_saving(no):
    rental_save = np.empty((0,len(user.g_cur_cart_join_list[0])), int)

    #반납일자 5일 후 지정
    td_now = now + td(days=5)

    for i, v in enumerate(user.g_cur_cart_join_list):
        if i == no:
            rental_save = np.append(rental_save, np.array([v]), axis=0)   
             
            #현재 이용자 대여내역 중복 존재 확인
            if rental.dup_chk(user.g_user_info_list[0], rental_save[0,1]) >= 1:
                print('이미 대여등록하신 도서입니다. 다시 선택해주세요.')
                book_rental()
            #다른 이용자 대여내역 중복 존재 확인
            elif rental.dif_dup_chk(user.g_user_info_list[0], rental_save[0,1]) >=1:
                print('다른 이용자가 대여중인 도서입니다. 다시 선택해주세요.')
                book_rental()                
            else:
                rental.add( user.g_user_info_list[0], rental_save[0,1], rental_save[0,2], rental_save[0,3], rental_save[0,4], rental_save[0,5],
                            now.date().strftime("%Y년-%m월-%d일"), td_now.date().strftime("%Y년-%m월-%d일")
                            )
                print('%s 번의  "%s"  도서 대여완료' % (rental_save[0,0], rental_save[0,2]))

                cart.remove(user.g_user_info_list[0], rental_save[0,1])
                print('%s 번의  "%s"  도서 장바구니 삭제 완료' % (rental_save[0,0], rental_save[0,2]) )
                

                book_rental()               

def book_return():
    pu_function.line_divide()
    print("%50s(접속자: %s, 현재 도서관: %s)" % ('반납등록 화면',user.g_user_info_list[2], user.g_cur_library_nm) ) 

    #대여목록에 추가한 도서가 있다면
    if rental.is_rental_chk(user.g_user_info_list[0]) >= 1:
        rental.join(user.g_user_info_list[0])
    else: 
        print('\n대여목록이 비어있습니다.') 
        action_chk()   

    print('\n반납하실 도서의 순번을 선택해주세요.(나가기: Q)')   
    no = sys.stdin.readline().strip().replace(" ","")

    if no.upper() == 'Q':
        print('\n반납등록 화면을 나갑니다.') 
        action_chk()
 
    # b = [i[0] for i in user.g_cur_rental_join_list]
    # print(b)   
    if no not in [str(i[0]) for i in user.g_cur_rental_join_list]:
        print('\n검색결과에 없는 순번입니다. 다시 선택해주세요.')    
        book_return()
    else:
        return_saving(int(no)-1)

#반납내역 추가
def return_saving(no):
    return_save = np.empty((0,len(user.g_cur_rental_join_list[0])), int)

    for i, v in enumerate(user.g_cur_rental_join_list):
        if i == no:
            return_save = np.append(return_save, np.array([v]), axis=0)   

            #이전에 반납한 책과 동일한 책이 있다면 삭제
            if return_.is_return_chk(user.g_user_info_list[0], return_save[0,1]) >= 1:
                    return_.remove(user.g_user_info_list[0], return_save[0,1])

            return_.add( user.g_user_info_list[0], return_save[0,1], return_save[0,2], return_save[0,3], return_save[0,4], return_save[0,5],
                        now.date().strftime("%Y년-%m월-%d일")
                        )
            
            print('%s 번의  "%s"  도서 반납완료' % (return_save[0,0], return_save[0,2]))

            rental.remove(user.g_user_info_list[0], return_save[0,1])
            print('%s 번의  "%s"  도서 대여목록 삭제 완료' % (return_save[0,0], return_save[0,2]) )

            book_return()  