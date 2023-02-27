import sys
import pu_function 
import pu_class
import main

user = pu_class.Global_var()

login_menu_info = {"회원가입":1, "로그인":2, "책 반납하기":3, "종료하기":4  }

def action_chk():
    pu_function.line_divide()
    print("%50s" % '광산구 도서관 도서관리프로그램')

    for key, value in login_menu_info.items():
        print(str(value) + ".", key)

    print('\n무엇을 하시겠습니까?')
    action = sys.stdin.readline().strip().replace(" ","")  

    if action == "1":
        new_login()
    elif action == "2":
        login()
    elif action == "3":
        if len(user.g_user_info_list) <= 0:
            print('로그인 먼저 해주십시요.')    
            action_chk()       
        else:
            main.book_return()
    elif action == "4":
        print('프로그램을 종료합니다.')           
        exit()
    else:
        print('다시 선택해주세요.')
        action_chk()

def login():
    user = pu_class.user_info()

    pu_function.line_divide()   

    print("%50s" % '로그인 화면')  

    print('\n아이디를 입력해주세요.(나가기: Q)')     
    user.id = sys.stdin.readline().strip().replace(" ","")    

    if  user.id.upper() == 'Q':
        print('\n로그인 화면을 나갑니다.') 
        action_chk()

    while user.id_chk() <= 0:
        print('\n존재하지 않는 아이디입니다. 다시 입력해주세요.(나가기: Q)') 
        user.id = sys.stdin.readline().strip().replace(" ","")   
        if  user.id.upper() == 'Q':
            print('\n로그인 화면을 나갑니다.') 
            action_chk()

    print('\n암호를 입력해주세요.')  
    user.password = sys.stdin.readline().strip().replace(" ","") 

    while user.pwd_chk() != True:
        print('\n일치하지 않는 암호입니다. 다시 입력해주세요.(나가기: Q)') 
        user.password = sys.stdin.readline().strip().replace(" ","")     
        if  user.password.upper() == 'Q':
            print('\n로그인 화면을 나갑니다.') 
            action_chk()


    print('\n로그인 완료')  

    user.set_info()
    main.action_chk()

def new_login():
    user = pu_class.user_info()
    save_yn = ''

    pu_function.line_divide()

    print("%50s" % '회원가입 화면')
    

    print('\n아이디를 입력해주세요.(나가기: Q)')   
    user.id = sys.stdin.readline().strip().replace(" ","")  
    if  user.id.upper() == 'Q':
        print('\n회원가입 화면을 나갑니다.') 
        action_chk()

    while len(user.id.replace(" ","")) <= 0:
        print('\n아이디는 필수 입력 사항입니다. 다시 입력해주세요.(나가기: Q)')      
        user.id = sys.stdin.readline().strip().replace(" ","")    
        if  user.id.upper() == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()

    while (user.id_chk() >= 1) or (user.id == ''):
        print('\n중복된 아이디입니다. 다시 입력해주세요.(나가기: Q)') 
        user.id = sys.stdin.readline().strip().replace(" ","")         
        if  user.id.upper() == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()  

    print('\n암호를 입력해주세요.(나가기: Q)')   
    user.password = sys.stdin.readline().strip().replace(" ","")  

    while len(user.password.replace(" ","")) <= 0:
        print('\n암호는 필수 입력 사항입니다. 다시 입력해주세요.(나가기: Q)')   
        user.password = sys.stdin.readline().strip().replace(" ","")   
        if  user.password.upper() == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()  

    print('\n이름을 입력해주세요.(나가기: Q)')   
    user.name = sys.stdin.readline().strip().replace(" ","")  

    while len(user.name.replace(" ","")) <= 0:
        print('\n이름은 필수 입력 사항입니다. 다시 입력해주세요.(나가기: Q)')       
        user.name = sys.stdin.readline().strip().replace(" ","")    
        if  user.name.upper() == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()  

    # print('\n전화번호을 입력해주세요.')   
    # user.phone_num = sys.stdin.readline().strip().replace(" ","")  

    # print('\n생년월일을 입력해주세요.')     
    # user.birth_date = sys.stdin.readline().strip().replace(" ","")  

    print('\n성별을 입력해주세요.(나가기: Q) 0.남, 1.여')     
    user.gender = sys.stdin.readline().strip().replace(" ","")  
    if  user.gender.upper() == 'Q':
        print('\n회원가입 화면을 나갑니다.') 
        action_chk()  

    while user.gender != '0' and  user.gender != '1':
        print('\n다시 성별을 입력해주세요.(나가기: Q) 0.남, 1.여')     
        user.gender = sys.stdin.readline().strip().replace(" ","")    
        if  user.gender.upper() == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()  
    # print('\n이메일을 입력해주세요.')     
    # user.email = sys.stdin.readline().strip().replace(" ","")  

    # print('\n주소를 입력해주세요.')     
    # user.address = sys.stdin.readline().strip().replace(" ","")  

    if int(user.gender) == 0:
        gender = '남자'
    else:
        gender = '여자'       
    
    pu_function.line_divide()
    print('\n아이디: %s, 암호: %s, 이름: %s, 전화번호: %s, \
           \n생년월일: %s, 성별: %s, 이메일: %s, 주소: %s' 
          % (user.id, user.password, user.name, user.phone_num, 
          user.birth_date, gender, user.email, user.address) )    
    
    print('\n입력하신 정보는 위와 같으며 생성하시겠습니까?(나가기: Q) Y.네, N.아니오')  
    save_yn = sys.stdin.readline().strip().replace(" ","")  
    save_yn = save_yn.upper()
    if  save_yn == 'Q':
        print('\n회원가입 화면을 나갑니다.') 
        action_chk()  

    while (save_yn != 'Y') and (save_yn != 'N'):
        print('\n다시 입력해주세요.(나가기: Q) Y.네, N.아니오')     
        save_yn = sys.stdin.readline().strip().replace(" ","")      
        save_yn = save_yn.upper()
        if  save_yn == 'Q':
            print('\n회원가입 화면을 나갑니다.') 
            action_chk()          

    if save_yn == 'Y':
        
        user.add()

        print('\n회원가입 완료')
        action_chk()
    else:
        action_chk()  