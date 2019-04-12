import tkinter
import tkinter.messagebox
from tkinter import ttk

F_ = "微软雅黑"


class Wind(object):
    def __init__(self, user_id, admin_):

        self.username = user_id  # 传入用户对象
        self.user_id = self.username
        self.admin = admin_
        self.root = tkinter.Tk()
        self.root.title('沐修图书管理系统v3.0')
        self.root.register(0, 0)
        self.root.geometry('960x540')

        self.logInDesk = None
        self.registerDesk = None
        self.userSystemDesk = None
        self.adminSystemDesk = None
        self.log_in_desk()

    def top_back_refresh(self, aou=None):
        self.top.destroy()
        if aou:
            self.adminSystemDesk.destroy()
            self.admin_system_desk()
        else:
            self.userSystemDesk.destroy()
            self.user_system_desk()

    def top_back(self):
        self.top.destroy()

    def log_in_desk(self):
        self.logInDesk = tkinter.Frame(self.root)
        self.logInDesk.pack()
        um_l = tkinter.Label(self.logInDesk, text='用户名', font=(F_, 12))
        pw_l = tkinter.Label(self.logInDesk, text='密码', font=(F_, 12))
        um_entry = tkinter.Entry(self.logInDesk, show=None, font=(F_, 14))
        pw_entry = tkinter.Entry(self.logInDesk, show='*', font=(F_, 14))
        um_l.grid(column=0, row=0, sticky='w')
        um_entry.grid(column=1, row=0)
        pw_l.grid(column=0, row=1, sticky='w')
        pw_entry.grid(column=1, row=1)

        def admin_log_in():
            r = self.admin.log_in(um_entry.get(), pw_entry.get())
            if r == 6:
                um_entry.delete(0, len(um_entry.get()))
                pw_entry.delete(0, len(pw_entry.get()))
                tkinter.messagebox.showinfo(message='无效操作')
            elif r == 5:
                self.logInDesk.destroy()
                self.admin_system_desk()
                self.user_id = self.admin

        def log_in():
            r = self.user_id.log_in(um_entry.get(), pw_entry.get())
            if r == 0:
                tkinter.messagebox.showinfo(message='账号密码不能为空')
            elif r == 2:
                um_entry.delete(0, len(um_entry.get()))
                pw_entry.delete(0, len(pw_entry.get()))
                tkinter.messagebox.showinfo(message='用户名不存在或密码错误')
            elif r == 1:  # 普通用户登陆成功
                self.logInDesk.destroy()
                self.user_system_desk()
                self.user_id = self.username

        def register():
            self.logInDesk.destroy()
            self.register_desk()

        log_b = tkinter.Button(self.logInDesk, text='登录', command=log_in)
        reg_b = tkinter.Button(self.logInDesk, text='注册', command=register)
        admin_b = tkinter.Button(self.logInDesk, text='管理员登录', command=admin_log_in)
        log_b.grid(column=1, row=2, sticky='e')
        reg_b.grid(column=0, row=2, sticky='w')
        admin_b.grid(column=1, row=3, sticky='e')

    def register_desk(self):
        self.registerDesk = tkinter.Frame(self.root)
        self.registerDesk.pack()
        um_entry = tkinter.Entry(self.registerDesk, show=None, font=(F_, 14))
        pw_entry1 = tkinter.Entry(self.registerDesk, show='*', font=(F_, 14))
        pw_entry2 = tkinter.Entry(self.registerDesk, show='*', font=(F_, 14))
        um_l = tkinter.Label(self.registerDesk, text='用户名', font=(F_, 12))
        pw_l1 = tkinter.Label(self.registerDesk, text='密码', font=(F_, 12))
        pw_l2 = tkinter.Label(self.registerDesk, text='再次输入密码', font=(F_, 12))
        um_l.grid(column=0, row=0, sticky='w')
        um_entry.grid(column=1, row=0, sticky='w')
        pw_l1.grid(column=0, row=1, sticky='w')
        pw_entry1.grid(column=1, row=1, sticky='w')
        pw_l2.grid(column=0, row=2, sticky='w')
        pw_entry2.grid(column=1, row=2, sticky='w')

        def register():
            r = self.user_id.register(um_entry.get(), pw_entry1.get(), pw_entry2.get())
            if r == 0:
                tkinter.messagebox.showinfo(message='用户名已存在')
            elif r == 2:
                tkinter.messagebox.showinfo(message='两次输入的密码不同')
            elif r == 1:
                tkinter.messagebox.showinfo(message='注册成功')

        def back():
            self.registerDesk.destroy()
            self.log_in_desk()

        reg_b = tkinter.Button(self.registerDesk, text='确认注册', command=register)
        log_b = tkinter.Button(self.registerDesk, text='返回登录', command=back)
        reg_b.grid(column=0, row=3, sticky='w')
        log_b.grid(column=1, row=3, sticky='e')

    def user_system_desk(self):
        self.userSystemDesk = tkinter.Frame(self.root)
        self.userSystemDesk.pack()
        frame1 = tkinter.Frame(self.userSystemDesk)
        frame1.pack()
        frame3 = tkinter.Frame(self.userSystemDesk)
        frame3.pack()
        frame2 = tkinter.Frame(self.userSystemDesk)
        frame2.pack()

        s1 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s2 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s3 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s4 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s5 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s6 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s7 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        list_s = [s1, s2, s3, s4, s5, s6, s7]
        dict_s = {s1: 'sm', s2: 'jg', s3: 'zz', s4: 'fl', s5: 'id', s6: 'cbs', s7: 'jc'}
        dict_c = {'sm': '书名', 'jg': '价格', 'zz': '作者', 'fl': '分类', 'cbs': '出版社', 'jc': '是否借出', 'id': '编号'}
        c = 0
        for i_ in list_s:
            i_l = tkinter.Label(frame1, text='%s' % dict_c[dict_s[i_]], font=(F_, 12))
            i_l.grid(column=0, row=c, sticky='w')
            i_.grid(column=1, row=c, sticky='w')
            c += 1

        def search():
            for widget in frame2.winfo_children():
                widget.destroy()
            self.view(self.user_id.search([s1.get(), s2.get(), s3.get(), s4.get(),
                                           s5.get(), s6.get(), s7.get()]), frame2, dict_c)

        def logout():
            self.user_id.log_out()
            self.userSystemDesk.destroy()
            self.log_in_desk()

        def borrow():
            self.top = tkinter.Toplevel()
            self.top.wm_attributes("-topmost", 1)
            i_l2 = tkinter.Label(self.top, text='请输入要借入的编号', font=(F_, 12))
            b1 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            i_l2.grid(column=0, row=0, sticky='w')
            b1.grid(column=1, row=0, sticky='w')

            def bor_():
                a = self.user_id.borrow(b1.get())
                if a == 1:
                    tkinter.messagebox.showinfo(message='借入成功')
                    self.top_back_refresh()
                elif a == 0:
                    tkinter.messagebox.showinfo(message='该编号不存在')
                elif a == 2:
                    tkinter.messagebox.showinfo(message='该书已借出')
                elif a == 3:
                    tkinter.messagebox.showinfo(message='编号不能为空')

            bor_b_ = tkinter.Button(self.top, text='确定借入', command=bor_)
            bor_b_.grid(column=0, row=6, sticky='w')
            back_b_ = tkinter.Button(self.top, text='返回', command=self.top_back)
            back_b_.grid(column=1, row=6, sticky='e')

        def pay_back():
            self.top = tkinter.Toplevel()
            self.top.wm_attributes("-topmost", 1)
            i_l2 = tkinter.Label(self.top, text='请输入要归还的编号', font=(F_, 12))
            b1 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            i_l2.grid(column=0, row=0, sticky='w')
            b1.grid(column=1, row=0, sticky='w')

            def pay_():
                a = self.user_id.pay_back(b1.get())
                if a == 1:
                    tkinter.messagebox.showinfo(message='归还成功')
                    self.top_back_refresh()
                elif a == 0:
                    tkinter.messagebox.showinfo(message='该编号不存在')
                elif a == 2:
                    tkinter.messagebox.showinfo(message='未借入此书')
                elif a == 3:
                    tkinter.messagebox.showinfo(message='编号不能为空')

            pay_b_ = tkinter.Button(self.top, text='确定归还', command=pay_)
            pay_b_.grid(column=0, row=6, sticky='w')
            back_b_ = tkinter.Button(self.top, text='返回', command=self.top_back)
            back_b_.grid(column=1, row=6, sticky='e')

        bor_b = tkinter.Button(frame3, text='借书', command=borrow)
        bor_b.pack(side='left', padx=20)
        pb_b = tkinter.Button(frame3, text='还书', command=pay_back)
        pb_b.pack(side='left', padx=20)
        search_b = tkinter.Button(frame3, text='查找', command=search)
        search_b.pack(side='left', padx=20)
        lo_b = tkinter.Button(frame3, text='注销', command=logout)
        lo_b.pack(side='left', padx=20)
        self.view(self.user_id.search(['', '', '', '', '', '', '']), frame2, dict_c)

    def admin_system_desk(self):
        self.adminSystemDesk = tkinter.Frame(self.root)
        self.adminSystemDesk.pack()
        frame1 = tkinter.Frame(self.adminSystemDesk)
        frame1.pack()
        frame3 = tkinter.Frame(self.adminSystemDesk)
        frame3.pack()
        frame2 = tkinter.Frame(self.adminSystemDesk)
        frame2.pack()
        s1 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s2 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s3 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s4 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s5 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s6 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        s7 = tkinter.Entry(frame1, show=None, font=(F_, 12))
        list_s = [s1, s2, s3, s4, s5, s6, s7]
        dict_s = {s1: 'sm', s2: 'jg', s3: 'zz', s4: 'fl', s5: 'id', s6: 'cbs', s7: 'jc'}
        dict_c = {'sm': '书名', 'jg': '价格', 'zz': '作者', 'fl': '分类', 'cbs': '出版社', 'jc': '是否借出', 'id': '编号'}
        c = 0
        for i_ in list_s:
            i_l = tkinter.Label(frame1, text='%s' % dict_c[dict_s[i_]], font=(F_, 12))
            i_l.grid(column=0, row=c, sticky='w')
            i_.grid(column=1, row=c, sticky='w')
            c += 1

        def add_desk():
            self.top = tkinter.Toplevel()
            self.top.wm_attributes("-topmost", 1)
            a1 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            a2 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            a3 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            a4 = tkinter.Entry(self.top, show=None, font=(F_, 12))

            a6 = tkinter.Entry(self.top, show=None, font=(F_, 12))

            list_s1 = [a1, a2, a3, a4, a6]
            dict_s1 = {a1: 'sm', a2: 'jg', a3: 'zz', a4: 'fl', a6: 'cbs'}
            dict_c1 = {'sm': '书名', 'jg': '价格', 'zz': '作者', 'fl': '分类',
                       'cbs': '出版社', 'jc': '是否借出', 'id': '编号'}
            c1 = 0
            for i_1 in list_s1:
                i_l1 = tkinter.Label(self.top, text='%s' % dict_c1[dict_s1[i_1]], font=(F_, 12))
                i_l1.grid(column=0, row=c1, sticky='w')
                i_1.grid(column=1, row=c1, sticky='w')
                c1 += 1

            def add_():
                a = self.user_id.add_(a1.get(), a2.get(), a3.get(), a4.get(), a6.get())
                if a == 1:
                    tkinter.messagebox.showinfo(message='添加成功')
                    self.top_back_refresh(aou=1)
                if a == 0:
                    tkinter.messagebox.showinfo(message='数据不完整')

            add_b_ = tkinter.Button(self.top, text='确定添加', command=add_)
            add_b_.grid(column=0, row=6, sticky='w')
            back_b_ = tkinter.Button(self.top, text='返回', command=self.top_back)
            back_b_.grid(column=1, row=6, sticky='e')

        def del_desk():
            self.top = tkinter.Toplevel()
            self.top.wm_attributes("-topmost", 1)
            i_l2 = tkinter.Label(self.top, text='请输入要删除的编号', font=(F_, 12))
            b1 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            i_l2.grid(column=0, row=0, sticky='w')
            b1.grid(column=1, row=0, sticky='w')

            def del_():
                a = self.user_id.del_(b1.get())
                if a == 1:
                    tkinter.messagebox.showinfo(message='删除成功')
                    self.top_back_refresh(aou=1)
                elif a == 0:
                    tkinter.messagebox.showinfo(message='该编号不存在')

            del_b_ = tkinter.Button(self.top, text='确定删除', command=del_)
            del_b_.grid(column=0, row=6, sticky='w')
            back_b_ = tkinter.Button(self.top, text='返回', command=self.top_back)
            back_b_.grid(column=1, row=6, sticky='e')

        def upd_desk():
            self.top = tkinter.Toplevel()
            self.top.wm_attributes("-topmost", 1)
            i_l3 = tkinter.Label(self.top, text='请输入要修改的编号', font=(F_, 12))
            c0 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            i_l3.grid(column=0, row=0, sticky='w')
            c0.grid(column=1, row=0, sticky='w')
            c1 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            c2 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            c3 = tkinter.Entry(self.top, show=None, font=(F_, 12))
            c4 = tkinter.Entry(self.top, show=None, font=(F_, 12))

            c6 = tkinter.Entry(self.top, show=None, font=(F_, 12))

            list_s2 = [c1, c2, c3, c4, c6]
            dict_s2 = {c1: 'sm', c2: 'jg', c3: 'zz', c4: 'fl', c6: 'cbs'}
            dict_c2 = {'sm': '书名', 'jg': '价格', 'zz': '作者', 'fl': '分类', 'cbs': '出版社'}
            d3 = 2
            for i_3 in list_s2:
                i_l3 = tkinter.Label(self.top, text='%s' % dict_c2[dict_s2[i_3]], font=(F_, 12))
                i_l3.grid(column=0, row=d3, sticky='w')
                i_3.grid(column=1, row=d3, sticky='w')
                d3 += 1

            def upd_():
                update = []
                for i_3_ in list_s2:
                    if i_3_.get():
                        if dict_s2[i_3_] == 'jg':
                            update += [dict_s2[i_3_] + ' = ' + i_3_.get()]
                        else:
                            update += [dict_s2[i_3_] + ' = \"' + i_3_.get() + '\"']
                update_ = ' , '.join(update)
                a = self.user_id.upd_(c0.get(), update_)
                if a == 1:
                    tkinter.messagebox.showinfo(message='修改成功')
                    self.top_back_refresh(aou=1)
                elif a == 0:
                    tkinter.messagebox.showinfo(message='此编号不存在')
                elif a == 2:
                    tkinter.messagebox.showinfo(message='修改条目不可全为空')

            upd_b_ = tkinter.Button(self.top, text='确定修改', command=upd_)
            upd_b_.grid(column=0, row=1, sticky='w')
            back_b_ = tkinter.Button(self.top, text='返回', command=self.top_back)
            back_b_.grid(column=1, row=1, sticky='e')

        def search():
            for widget in frame2.winfo_children():
                widget.destroy()
            self.view(self.user_id.search([s1.get(), s2.get(), s3.get(), s4.get(),
                                           s5.get(), s6.get(), s7.get()]), frame2, dict_c)

        def logout():
            self.user_id.log_out()
            self.adminSystemDesk.destroy()
            self.log_in_desk()

        add_b = tkinter.Button(frame3, text='增加', command=add_desk)
        add_b.pack(side='left', padx=10)
        del_b = tkinter.Button(frame3, text='删除', command=del_desk)
        del_b.pack(side='left', padx=10)
        upd_b = tkinter.Button(frame3, text='修改', command=upd_desk)
        upd_b.pack(side='left', padx=10)
        search_b = tkinter.Button(frame3, text='查找', command=search)
        search_b.pack(side='left', padx=10)
        lo_b = tkinter.Button(frame3, text='注销', command=logout)
        lo_b.pack(side='left', padx=10)
        self.view(self.user_id.search(['', '', '', '', '', '', '']), frame2, dict_c)

    @staticmethod
    def view(list_, desk_, dict_c):  # 查找表
        if list_ is None:
            list_ = []
        list_c = ['id', 'sm', 'jg', 'zz', 'fl', 'cbs', 'jc']
        tree_ = ttk.Treeview(desk_, columns=list_c, show='headings')
        tree_.pack()
        for i_ in list_c:
            if i_ == 'sm':
                tree_.column(i_, width=200)
            else:
                tree_.column(i_, width=100)
            tree_.heading(i_, text=dict_c[i_])
        for i_ in list_:
            if i_[-1]:
                i_ = list(i_)[:-1] + ['是']
            else:
                i_ = list(i_)[:-1] + ['否']
            tree_.insert('', 'end', values=i_)
