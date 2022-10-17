import tkinter as tk
from  tkinter import *
import tkinter
import pymysql
from tkinter import messagebox
''''
先添加以下数据库
text
'''

class App:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            port=3306,
            db='text'
        )
        self.cursor = self.db.cursor()


        self.windos = tk.Tk()
        self.windos.title('功能选择')
        self.windos.geometry('600x500')

        self.lab = tk.Label(self.windos, text="欢迎使用！", font=("KaiTi", 40)).place(x=180, y=15)

        self.butt1 = tk.Button(self.windos, text='新建学生信息', font=('Arial,12'), width=20, height=2,
                               command=self.add_info).place(x=100, y=100)
        self.butt2 = tk.Button(self.windos, text='修改学生信息', font=('Arial,12'), width=20, height=2,
                               command=self.modify_info).place(x=100, y=160)
        self.butt3 = tk.Button(self.windos, text='查询学生信息', font=('Arial,12'), width=20, height=2,
                               command=self.var_info).place(x=320, y=100)
        self.butt4 = tk.Button(self.windos, text='删除学生信息', font=('Arial,12'), width=20, height=2,
                               command=self.del_info).place(x=320, y=160)

    def add_info(self):
        #关闭之前的窗口
        self.windos.destroy()

        self.root = tk.Toplevel()
        self.root = tk.Tk()
        self.root.title('添加信息')
        self.root.geometry('600x400')
        self.root.focus_force()#新窗口获得焦点
        # 控件
        self.lab1 = tk.Label(self.root, text="学号:", font=('Arial', 9)).place(x=80, y=60)
        self.lab2 = tk.Label(self.root, text="姓名:", font=('Arial', 9)).place(x=80, y=90)
        self.lab3 = tk.Label(self.root, text="年龄:", font=('Arial', 9)).place(x=80, y=120)
        self.lab4 = tk.Label(self.root, text="性别:", font=('Arial', 9)).place(x=80, y=150)
        #  # 定义一个文本框，用来存储
        #学号
        self.entry1 = tk.Entry(self.root, font=('Arial,9'), width=46)
        #姓名
        self.entry2 = tk.Entry(self.root, font=('Arial,9'), width=46)
        #年龄
        self.entry3 = tk.Entry(self.root, font=('Arial,9'), width=46)
        #性别
        self.entry4 = tk.Entry(self.root, font=('Arial,9'), width=46)
        # 布局
        self.entry1.pack()
        self.entry1.place(x=180, y=60, width=350)

        self.entry2.pack()
        self.entry2.place(x=180, y=90, width=350)

        self.entry3.pack()
        self.entry3.place(x=180, y=120, width=350)

        self.entry4.pack()
        self.entry4.place(x=180, y=150, width=350)


        self.butt2 = tk.Button(self.root, text="添加", bg='white', font=("Arial,9"), width=9, height=0,
                               command=self.add).place(
            x=400,
            y=360)
        self.butt3 = tk.Button(self.root, text="清空", bg='white', font=("Arial,9"), width=9, height=0,
                               command=self.clear).place(
            x=160,
            y=360)
        self.root.mainloop()

    def add(self):

        student_no=self.entry1.get()
        name=self.entry2.get()
        age=self.entry3.get()
        sex=self.entry4.get()
        self.sql = "INSERT INTO student(student_no, name,age,sex) values(%s, %s, %s, %s)"
        try:
            self.cursor.execute(self.sql, (student_no, name, age, sex))
            self.db.commit()
            print('插入成功')
            pass
        except:
            self.db.rollback()
            print('插入失败')
            self.db.close()
            pass
        messagebox.showinfo(title="信息", message="数据添加成功！")

    def clear(self):
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.entry3.delete(0, "end")
        self.entry4.delete(0, "end")

    def var_info(self):
        self.windos.destroy()

        self.root = tk.Toplevel()
        self.root = tk.Tk()
        self.root.title('查询信息')
        self.root.geometry('600x500')
        self.root.focus_force()  # 新窗口获得焦点

        # 文本
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack()
        self.entry.place(x=200, y=60)
        self.v1 = tk.Label(self.root, text='请输入查询信息:', font=("Arial", 9)).place(x=50, y=60)
        self.v2 = tk.Label(self.root, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)

        self.text1 = tk.Text(self.root, width=50, height=20)
        self.text1.pack()
        self.text1.place(x=150, y=120)
        self.butt5 = tk.Button(self.root, text='查询', bg='white', font=("Arial,12"), width=9, height=0,
                               command=self.select_one).place(x=450,
                                                              y=60)

    def select_one(self):
        name = self.entry.get()
        print(name)
        # self.text1.delete(1.0, 'end')
        sql = "select * from student where name=%s"
        try:
            self.cursor.execute(sql,(name))
            result = self.cursor.fetchall()
            self.db.commit()
            print(f'查询成功数据为:{result}')
        except:
            self.db.rollback()
            self.db.close()
            pass
        # self.text1.insert(chars="{}".format(data), index="insert")
        self.text1.insert(END,result)

    def modify_info(self):
        # 关闭之前的窗口
        self.windos.destroy()
        self.root = tk.Toplevel()
        self.root = tk.Tk()
        self.root.title('修改信息')
        self.root.geometry('600x400')
        self.root.focus_force()  # 新窗口获得焦点

        # 文本
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack()
        self.entry.place(x=200, y=60)
        self.v1 = tk.Label(self.root, text='请输入查询信息:', font=("Arial", 9)).place(x=50, y=60)
        # 控件
        self.lab1 = tk.Label(self.root, text="学号:", font=('Arial', 9)).place(x=80, y=100)
        self.lab2 = tk.Label(self.root, text="姓名:", font=('Arial', 9)).place(x=80, y=130)
        self.lab3 = tk.Label(self.root, text="年龄:", font=('Arial', 9)).place(x=80, y=160)
        self.lab4 = tk.Label(self.root, text="性别:", font=('Arial', 9)).place(x=80, y=190)

        self.butt5 = tk.Button(self.root, text='查询', bg='white', font=("Arial,12"), width=9, height=0,
                               command=self.select_info).place(x=450,
                                                         y=55)
        self.butt6 = tk.Button(self.root, text='修改', bg='white', font=("Arial,12"), width=9, height=0,
                               command=self. update_info).place(x=260,
                                                               y=370)

        self.t1= tk.Text(self.root,width=50,height=1)
        self.t2=tk.Text(self.root,width=50,height=1)
        self.t3 = tk.Text(self.root, width=50, height=1)
        self.t4 = tk.Text(self.root, width=50, height=1)

        self.t1.pack()
        self.t2.pack()
        self.t3.pack()
        self.t4.pack()

        self.t1.place(x=150,y=100)
        self.t2.place(x=150, y=130)
        self.t3.place(x=150, y=160)
        self.t4.place(x=150, y=190)



    def select_info(self):
        name = self.entry.get()
        print(name)
        sql = "select * from student where name=%s"
        try:
            self.cursor.execute(sql, (name))
            result = self.cursor.fetchall()
            self.db.commit()
            print(f'查询成功数据为:{result}')
        except:
            self.db.rollback()
            self.db.close()
        for i in result:
            pass
            # print(i[0])

            self.t1.insert(chars="{}".format(i[0]), index="insert")
            self.t2.insert(chars="{}".format(i[1]), index="insert")
            self.t3.insert(chars="{}".format(i[2]), index="insert")
            self.t4.insert(chars="{}".format(i[3]), index="insert")


    def update_info(self):
        name = self.entry.get()
        # print(name)

        student_no = self.t1.get("1.0", "end")
        print(student_no)
        # name = self.t2.get("1.0", "end")
        age = self.t3.get("1.0", "end")
        sex = self.t4.get("1.0", "end")

        sql = "update student set student_no=%s,age=%s where name=%s"
        try:
            self.cursor.execute(sql, (student_no,age,name))
            self.db.commit()
            print(f'修改成功')
            pass
        except:
            self.db.rollback()
            print('修改失败')
            self.db.close()





    def del_info(self):
        self.windos.destroy()

        self.root = tk.Toplevel()
        self.root = tk.Tk()
        self.root.title('删除信息')
        self.root.geometry('600x500')
        self.root.focus_force()  # 新窗口获得焦点
        # 文本
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack()
        self.entry.place(x=200, y=80)

        self.v1 = tk.Label(self.root, text='请输入查询学生的姓名:', font=("Arial", 9)).place(x=50, y=80)
        self.v2 = tk.Label(self.root, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)

        self.text1 = tk.Text(self.root, width=50, height=20)
        self.text1.pack()
        self.text1.place(x=150, y=120)
        self.butt5 = tk.Button(self.root, text='查询', bg='white', font=("Arial,12"), width=9, height=0,
                               command=self.selet).place(x=450,
                                                              y=75)
        self.butt6 = tk.Button(self.root, text='删除', bg='white', font=("Arial,12"), width=9, height=0,
                               command=self.del_Re).place(x=280,
                                                         y=400)

    def selet(self):
        name = self.entry.get()
        print(name)
        # self.text1.delete(1.0, 'end')
        sql = "select * from student where name=%s"
        try:
            self.cursor.execute(sql, (name))
            result = self.cursor.fetchall()
            self.db.commit()
            print(f'查询成功数据为:{result}')
        except:
            self.db.rollback()
            self.db.close()
            pass
        self.text1.insert(END, result)


    def del_Re(self):
        name = self.entry.get()
        print(name)
        sql = "delete from student where name =%s"
        try:
            self.cursor.execute(sql,(name))
            result = self.cursor.fetchall()
            self.db.commit()
            print(f'删除成功:{result}')
        except:
            self.db.rollback()
            print('删除失败')
            self.db.close()
        messagebox.showinfo(title="信息", message="信息已删除！")


t= App()
tk.mainloop()



