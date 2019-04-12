from connect_沐修图书管理系统 import *
from windows_沐修图书管理系统 import *

# 常量定义

ADMIN = ['沐修', '888']


class Admin(object):
    def __init__(self, cursor):
        self.cu = cursor
        self.username = None
        self.user_id = None

    def log_in(self, username_, password_):
        if username_ == ADMIN[0] and password_ == ADMIN[1]:
            return 5
        else:
            self.username = ADMIN[0]
            return 6

    def search(self, input_):
        search = []
        list_s = ['sm', 'jg', 'zz', 'fl', 'id', 'cbs', 'jc']
        for i_ in range(7):
            if input_[i_]:
                if list_s[i_] == 'jc':
                    if input_[i_] == '否':
                        search += [list_s[i_] + ' = "0" ']
                    else:
                        search += [list_s[i_] + ' > "0" ']
                else:
                    search += [list_s[i_] + ' = \"' + input_[i_] + '\"']
        search_ = ' AND '.join(search)
        a = self.cu.view(search_)
        return a

    def log_out(self):
        self.username = None
        self.user_id = None

    def add_(self, sm, jg, zz, fl, cbs):
        if sm and jg and zz and fl and cbs:
            self.cu.add(sm, jg, zz, fl, cbs)
            return 1
        return 0

    def del_(self, id_):
        if self.cu.is_in(id_):
            self.cu.del_(id_)
            return 1
        else:
            return 0

    def upd_(self, id_, update_):
        if update_ and id_:
            if self.cu.is_in(id_):
                self.cu.upd_(id_, update_)
                return 1
            else:
                return 0
        return 2


class User(Admin):
    """用户类"""

    def __init__(self, cursor, admin_):
        super().__init__(cursor)
        self.admin_ = admin_
        self.root = Wind(self, self.admin_)
        self.user_id = None

    def log_in(self, username_, password_):  # 登录方法
        if username_ == '' or password_ == '':
            return 0
        elif cu.log_in(username_, password_):
            self.username = username_
            self.user_id = self.cu.log_in(username_, password_)
            return 1
        else:
            return 2

    def register(self, username_, password1_, password2_):  # 注册方法
        if cu.register_check(username_):
            return 0
        elif password1_ != password2_:
            return 2
        else:
            self.cu.register(username_, password1_)
            return 1

    def borrow(self, id_):
        if id_:
            if self.cu.is_in(id_):
                if self.cu.is_in(id_)[0][6] == 0:
                    self.cu.bor_pay(id_, self.user_id)
                    return 1
                else:
                    return 2
            else:
                return 0
        else:
            return 3

    def pay_back(self, id_):
        if id_:
            if self.cu.is_in(id_):
                if self.cu.is_in(id_)[0][6] == self.user_id:
                    self.cu.bor_pay(id_, 0)
                    return 1
                else:
                    return 2
            else:
                return 0
        else:
            return 3


if __name__ == '__main__':
    filename = './conn/conn.db'
    cu = Conn(filename)
    admin = Admin(cu)
    user = User(cu, admin)
    user.root.root.mainloop()
