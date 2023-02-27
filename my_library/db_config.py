import sqlite3
import login

try:
    #DB 생성 (오토 커밋)
    conn = sqlite3.connect('my_library\my_library.db', isolation_level = None, timeout = 10)

    #쿼리문 실행 후 출력
    #conn.set_trace_callback(print)  

    #커서 획득
    cursor = conn.cursor() 

    #제약 조건 체크 활성화
    cursor.execute('PRAGMA primary_keys = ON') 
    cursor.execute('PRAGMA foreign_ke2ys = ON') 
except:
     print('DBconnect 에러발생')
     exit()


def main():
    login.action_chk()

if __name__ == '__main__':
    main()