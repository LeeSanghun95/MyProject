import db_config
import pu_function


class Global_var(object):
        g_user_info_list = [] #현재 접속자 정보
        g_cur_library = ''  #도서관 테이블명
        g_cur_library_nm = '' #도서관 이름
        g_cur_book_join_list = [] #조회한 책 리스트
        g_cur_cart_join_list = [] #장바구니 리스트
        g_cur_rental_join_list = [] #대여내역 리스트
        g_cur_return_join_list = [] #반납내역 리스트
class book_list:
    def __init__(self):
        self.book_in = ''
        self.book_no = 0
        self.library = ''
        self.library_nm = ''
        self.info_nm = ''
        self.book_nm = ''
        self.author_nm = ''
        self.publisher = ''
        self.publisher_date = ''
        self.claim_sign = ''
        self.standard_date = ''

    #도서명 검색
    def book_join(self):
        # db_config.cursor.execute("select ROW_NUMBER() OVER (ORDER BY (select null)) as no, \
        #                                 book_id, library_nm, info_nm,  \
        #                                 substr(book_nm,1,30) as book_nm, substr(author_nm,1,30) as author_nm  \
        #                             from '%s' \
        #                                 where book_nm like '%s'   or author_nm like '%s'  \
        #                                      order by book_no limit 5  " 
        #                                                                         % ('jangdeok_list', '%'+self.book_nm+'%', '%'+self.author_nm+'%') )
        
        sql =  '''
                                    select ROW_NUMBER() OVER (ORDER BY (select null)) as no 
                                    , D.*   
                                        FROM (   
                                                select  A.*  
                                                from (      
                                                        select 
                                                        book_id, library_nm, info_nm,   
                                                        substr(book_nm,1,30) as book_nm,   
                                                        substr(author_nm,1,30) as author_nm 
                                                        from jangdeok_list  
                                                        where (book_nm like '{0}' or author_nm like '{1}')  
                                                        ORDER BY book_no LIMIT 5   
                                                    ) A   
                                            union  
                                                select  B.*   
                                                from (
                                                        select 
                                                        book_id, library_nm, info_nm, 
                                                        substr(book_nm,1,30) as book_nm, 
                                                        substr(author_nm,1,30) as author_nm
                                                        from cheomdan_list 
                                                        where (book_nm like '{0}' or author_nm like '{1}') 
                                                        ORDER BY book_no LIMIT 5  
                                                    ) B  
                                            union                       
                                                    select  C.*  
                                                    from (   
                                                        select 
                                                        book_id, library_nm, info_nm, 
                                                        substr(book_nm,1,30) as book_nm, 
                                                        substr(author_nm,1,30) as author_nm
                                                        from singa_list 
                                                        where (book_nm like '{0}' or author_nm like '{1}') 
                                                        ORDER BY book_no LIMIT 5			
                                                    ) C  
                                                        )D       

        '''

        db_config.cursor.execute( sql.format('%'+self.book_nm+'%', '%'+self.author_nm+'%') )
                
                                                       

        result = db_config.cursor.fetchall() 
    
        Global_var.g_cur_book_join_list = result

        strFormat = '%-10s%-20s%-20s%-10s%-10s\n'

        strOut = strFormat % ( pu_function.fmt('순번',0,'l'), pu_function.fmt('책이름',60,'l'), pu_function.fmt('저자',50,'l'), 
                               pu_function.fmt('도서관',0,'l'), pu_function.fmt('위치',0,'l') )
       
        for row_data in result:
            strOut += strFormat % ( pu_function.fmt(row_data[0],0,'l'), pu_function.fmt(row_data[4],60,'l'), pu_function.fmt(row_data[5],50,'l'), 
                                    pu_function.fmt(row_data[2],0,'l'), pu_function.fmt(row_data[3],0,'l') )
        
        pu_function.line_divide()
        print("%80s" % '전체 도서관 검색결과')
        pu_function.line_divide()
              
        return print(strOut)  
    
class cart_list:
    def __init__(self):
        self.id = ''
        self.book_id = ''
        self.book_nm = ''
        self.author_nm = ''
        self.library_nm = ''
        self.info_nm = ''
        self.cart_date = ''

    #장바구니 조회
    def join(self, id):
        sql =  '''
                select ROW_NUMBER() OVER (ORDER BY (select null)) as no,
                    book_id, book_nm, author_nm, library_nm, info_nm, cart_date
                         from cart_list
                            where id = '{}'
            '''
        db_config.cursor.execute( sql.format(id) )

        result = db_config.cursor.fetchall() 

        Global_var.g_cur_cart_join_list = result

        strFormat = '%-10s%-20s%-20s%-10s%-10s%-10s\n'

        strOut = strFormat % ( pu_function.fmt('순번',0,'l'), pu_function.fmt('책이름',60,'l'), pu_function.fmt('저자',50,'l'), 
                               pu_function.fmt('도서관',0,'l'), pu_function.fmt('위치',20,'l'), pu_function.fmt('장바구니 추가일자',0,'l') )
    
        for row_data in result:
            strOut += strFormat % ( pu_function.fmt(row_data[0],0,'l'), pu_function.fmt(row_data[2],60,'l'), pu_function.fmt(row_data[3],50,'l'), 
                                    pu_function.fmt(row_data[4],0,'l'), pu_function.fmt(row_data[5],20,'l'), pu_function.fmt(row_data[6],0,'l') )
        
        pu_function.line_divide()
        print("%80s" % '장바구니 검색결과')
        pu_function.line_divide()
              
        return print(strOut)  

    #장바구니에 담은 도서가 있는지 확인
    def is_cart_chk(self, id):
        db_config.cursor.execute("select count(*) from cart_list where id = '%s' " % (id) )
        result = db_config.cursor.fetchone()           
        return result[0]
    
    #장바구니 추가 
    def add(self, id, book_id, book_nm, author_nm, library_nm, info_nm, cart_date):
        db_config.cursor.execute("INSERT INTO cart_list(id, book_id, book_nm, author_nm, library_nm, info_nm, cart_date) \
                                    VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                    (id, book_id, book_nm, author_nm, library_nm, info_nm, cart_date) )     
        db_config.conn.commit()     

    #장바구니 중복 존재 확인
    def dup_chk(self, id, book_id):
        db_config.cursor.execute("select count(*) from cart_list where id = '%s' and book_id = '%s' " % (id, book_id) )
        result = db_config.cursor.fetchone()
        return result[0]
    
    #대여완료 후 장바구니 목록에서 해당 레코드 제거
    def remove(self, id, book_id):
        db_config.cursor.execute("DELETE FROM cart_list \
                                    where id = ? and book_id = ?", 
                                    (id, book_id) )     
        db_config.conn.commit()           
    
class rental_list:
    def __init__(self):
        self.id = ''
        self.book_id = ''
        self.book_nm = ''
        self.author_nm = ''
        self.library_nm = ''
        self.info_nm = ''       
        self.rental_sta_date = ''
        self.rental_end_date =''

    #대여내역 조회
    def join(self, id):
        sql =  '''
                select ROW_NUMBER() OVER (ORDER BY (select null)) as no,
                    book_id, book_nm, author_nm, library_nm, info_nm, rental_sta_date, rental_end_date
                         from rental_list
                            where id = '{}'
            '''
        db_config.cursor.execute( sql.format(id) )

        result = db_config.cursor.fetchall() 

        Global_var.g_cur_rental_join_list = result

        strFormat = '%-10s%-10s%-10s%-10s%-10s%-10s%-10s\n'

        strOut = strFormat % ( pu_function.fmt('순번',0,'l'), pu_function.fmt('책이름',60,'l'), pu_function.fmt('저자',50,'l'), 
                               pu_function.fmt('도서관',0,'l'), pu_function.fmt('위치',20,'l'), pu_function.fmt('대여일자',20,'l'), pu_function.fmt('반납예정일자',0,'l') )
    
        for row_data in result:
            strOut += strFormat % ( pu_function.fmt(row_data[0],0,'l'), pu_function.fmt(row_data[2],60,'l'), pu_function.fmt(row_data[3],50,'l'), 
                                    pu_function.fmt(row_data[4],0,'l'), pu_function.fmt(row_data[5],20,'l'), pu_function.fmt(row_data[6],20,'l'), pu_function.fmt(row_data[7],0,'l' )
                                  )
        
        pu_function.line_divide()
        print("%80s" % '대여내역 검색결과')
        pu_function.line_divide()
              
        return print(strOut)  

    #대여한 도서가 있는지 확인
    def is_rental_chk(self, id):
        db_config.cursor.execute("select count(*) from rental_list where id = '%s' " % (id) )
        result = db_config.cursor.fetchone()           
        return result[0]
    
    #한명이 대여할 수 있는 도서 권수 5권 제한
    def max_rental_cnt_chk(self, id):
        db_config.cursor.execute("select count(*) from rental_list where id = '%s' " % (id) )
        result = db_config.cursor.fetchone()
        return result[0]
        
    #현재 이용자 대여내역 중복 존재 확인
    def dup_chk(self, id, book_id):
        db_config.cursor.execute("select count(*) from rental_list where id = '%s' and book_id = '%s' " % (id, book_id) )
        result = db_config.cursor.fetchone()
        return result[0]
    
    #다른 이용자 대여내역 중복 존재 확인
    def dif_dup_chk(self, id, book_id):
        db_config.cursor.execute("select count(*) from rental_list where id <> '%s' and book_id = '%s' " % (id, book_id) )
        result = db_config.cursor.fetchone()
        return result[0]
       
    #대여내역 추가 
    def add(self, id, book_id, book_nm, author_nm, library_nm, info_nm, rental_sta_date, rental_end_date):
        db_config.cursor.execute("INSERT INTO rental_list(id, book_id, book_nm, author_nm, library_nm, info_nm, rental_sta_date, rental_end_date) \
                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
                                    (id, book_id, book_nm, author_nm, library_nm, info_nm, rental_sta_date, rental_end_date) )     
        db_config.conn.commit()     

    #반납완료 후 대여내역삭제
    def remove(self, id, book_id):
        db_config.cursor.execute("DELETE FROM rental_list \
                                    where id = ? and book_id = ?", 
                                    (id, book_id) )     
        db_config.conn.commit()                  
class return_list:
    def __init__(self):
        self.id = ''
        self.book_id = ''
        self.book_nm = ''
        self.author_nm = ''
        self.library_nm = ''
        self.info_nm = ''
        self.return_date = ''

    #반납내역 조회
    def join(self, id):
        sql =  '''
                select ROW_NUMBER() OVER (ORDER BY (select null)) as no,
                    book_id, book_nm, author_nm, library_nm, info_nm, return_date
                         from return_list
                            where id = '{}'
            '''
        db_config.cursor.execute( sql.format(id) )

        result = db_config.cursor.fetchall() 

        Global_var.g_cur_return_join_list = result

        strFormat = '%-10s%-10s%-10s%-10s%-10s%-10s\n'

        strOut = strFormat % ( pu_function.fmt('순번',0,'l'), pu_function.fmt('책이름',60,'l'), pu_function.fmt('저자',50,'l'), 
                               pu_function.fmt('도서관',0,'l'), pu_function.fmt('위치',20,'l'), pu_function.fmt('반납일자',20,'l'))
    
        for row_data in result:
            strOut += strFormat % ( pu_function.fmt(row_data[0],0,'l'), pu_function.fmt(row_data[2],60,'l'), pu_function.fmt(row_data[3],50,'l'), 
                                    pu_function.fmt(row_data[4],0,'l'), pu_function.fmt(row_data[5],20,'l'), pu_function.fmt(row_data[6],20,'l') 
                                  )
                                  
        
        pu_function.line_divide()
        print("%80s" % '반납내역 검색결과')
        pu_function.line_divide()
              
        return print(strOut)  

   #반납한 도서가 있는지 확인
    def is_return_chk(self, id, book_id):
        db_config.cursor.execute("select count(*) from return_list where id = '%s' and book_id = '%s' " % (id, book_id) )
        result = db_config.cursor.fetchone()           
        return result[0]
    
    #반납내역 추가 
    def add(self, id, book_id, book_nm, author_nm, library_nm, info_nm, return_date):
        db_config.cursor.execute("INSERT INTO return_list(id, book_id, book_nm, author_nm, library_nm, info_nm, return_date) \
                                    VALUES(?, ?, ?, ?, ?, ?, ?)", 
                                    (id, book_id, book_nm, author_nm, library_nm, info_nm, return_date) )     

    #반납내역 중복도서 삭제
    def remove(self, id, book_id):
        db_config.cursor.execute("DELETE FROM return_list \
                                    where id = ? and book_id = ?", 
                                    (id, book_id) )     
        db_config.conn.commit()               

class user_info:
    def __init__(self):
        self.id = ''
        self.password = ''
        self.name = ''
        self.phone_num = ''
        self.birth_date = ''
        self.gender = 0
        self.email = ''
        self.address =''
        self.grade_no = 1

    #아이디 추가 
    def add(self):
        db_config.cursor.execute("INSERT INTO user_info(id, password, name, gender) \
                                    VALUES(?, ?, ?, ?)", 
                                    (self.id, self.password, self.name, int(self.gender)) )     
        db_config.conn.commit()      
    
    #아이디 중복 존재 확인
    def id_chk(self):
        db_config.cursor.execute("select count(*) from user_info where id = '%s' " % self.id)
        result = db_config.cursor.fetchone()
        return result[0]
    
    #암호 일치여부 확인
    def pwd_chk(self):
        db_config.cursor.execute("select password from user_info where id = '%s' " % self.id)
        result = db_config.cursor.fetchone()
    
        if result[0] == self.password:
            return True
        else:
            return False
        
    #유저정보 갱신
    def set_info(self):
        db_config.cursor.execute("select * from user_info where id = '%s' " % self.id)
        result = db_config.cursor.fetchone()
        Global_var.g_user_info_list = result

