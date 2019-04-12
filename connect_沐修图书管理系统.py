import sqlite3


# 初始化数据库##############################

# U_A_P_cmd = 'CREATE TABLE IF NOT EXISTS u_a_p' \
#             '(id INTEGER PRIMARY KEY,username TEXT NOT NULL, password TEXT NOT NULL)'
# BOOKS_cmd = 'CREATE TABLE IF NOT EXISTS books' \
#             '(id INTEGER PRIMARY KEY,sm TEXT,jg REAL,zz TEXT,fl TEXT,cbs TEXT,jc INTEGER)'
# # sm书名,jg价格,zz作者,fl分类,cbs出版社,jc借出与否
# cu.execute(U_A_P_cmd)  # 创建用户表
# cu.execute(BOOKS_cmd)  # 创建书表
# cu.execute('INSERT  INTO  books(id,sm,jg,zz,fl,cbs,jc)VALUES(NULL,"python从入门到精通",160,"袁可庆","科技类","人民教育出版社",0)')


class Conn(object):
    """数据库工具箱"""

    def __init__(self, fl):
        self.conn = sqlite3.connect(fl)  # 创建一个在硬盘上的数据库（如果此数据库不存在）
        self.cu = self.conn.cursor()  # 创建一个游标对象

        # U_A_P_cmd = 'CREATE TABLE IF NOT EXISTS u_a_p' \
        #             '(id INTEGER PRIMARY KEY,username TEXT NOT NULL, password TEXT NOT NULL)'
        # BOOKS_cmd = 'CREATE TABLE IF NOT EXISTS books' \
        #             '(id INTEGER PRIMARY KEY,sm TEXT,jg REAL,zz TEXT,fl TEXT,cbs TEXT,jc INTEGER)'
        # # sm书名,jg价格,zz作者,fl分类,cbs出版社,jc借出与否
        # self.cu.execute(U_A_P_cmd)  # 创建用户表
        # self.cu.execute(BOOKS_cmd)  # 创建书表
        # self.cu.execute('INSERT  INTO  books(id,sm,jg,zz,fl,cbs,jc)' +
        #                 'VALUES(NULL,"python从入门到精通",160,"袁可庆","科技类","人民教育出版社",0)')

    def register(self, um, pw):
        """用户注册到数据库"""
        self.cu.execute('INSERT  INTO  u_a_p(id,username,password)VALUES(NULL,"%s","%s")' % (um, pw))
        self.conn.commit()

    def register_check(self, um):
        """用户名是否被注册"""
        if self.cu.execute('SELECT * FROM u_a_p WHERE username="%s"' % um).fetchall():
            return True
        else:
            return False

    def log_in(self, um, pw):
        """是否登录成功"""
        log_um = self.cu.execute('SELECT * FROM u_a_p WHERE username="%s"' % um).fetchall()
        if log_um and pw == log_um[0][2]:
            return log_um[0][0]  # 注册成功返回用户id
        else:
            return False

    def view(self, search=[]):
        """将搜索条件显示出来"""
        if not search:
            return self.cu.execute('SELECT * FROM books').fetchall()
        else:
            return self.cu.execute('SELECT * FROM books WHERE %s' % search).fetchall()

    def bor_pay(self, id_, jc):
        self.cu.execute('UPDATE books SET jc=%s WHERE id = %s' % (jc, id_))
        self.conn.commit()

    def add(self, sm, jg, zz, fl, cbs):
        self.cu.execute('INSERT  INTO  books VALUES(NULL,"%s",%s,"%s","%s","%s",0)' % (sm, jg, zz, fl, cbs))
        self.conn.commit()

    def del_(self, id_):
        self.cu.execute('DELETE FROM books WHERE id = %s' % id_)
        self.conn.commit()

    def upd_(self, id_, update):
        self.cu.execute('UPDATE books SET %s WHERE id = %s' % (update, id_))
        self.conn.commit()

    def is_in(self, id_):
        return self.cu.execute('SELECT * FROM books WHERE id = %s' % id_).fetchall()