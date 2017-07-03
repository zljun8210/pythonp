#! encoding:utf-8
import  sys
import  logging
import  xlrd
import  traceback
try:
    from lxml import  etree
except ImportError:
    import xml.etree.cElementTree as etree
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

t1 = []
root = None

#设置logger配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./test.log',
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

class Converter():
    # root = tkinter.Tk()
    # root.title("Tkinter: 选择文件")
    # root.geometry("400x200+480+350")
    # entry = Entry(root,width=40)
    # entry.pack()
    path="./"
    def __init__(self,rt):
        if rt == None:
            self.t = tkinter.Tk()
        else:
            self.t = tkinter.Toplevel(rt)

        self.t.title("xls2xml转换器")
        self.t.geometry('300x200')

        self.lab_input = Label(self.t,text = " 源文件：  ")
        self.lab_input.place(x=20,y=40)
        self.ent = Entry(self.t,bd=1)
        self.ent.place(x=80, y=40)
        self.btn = Button(self.t,text = "   打开 ",command = self.callback)
        self.btn.place(x=240,y=40)

        # self.lab_output = Label(self.t, text = "    转换为： ")
        # self.lab_output.place(x=30,y=80)
        # self.ent2 = Entry(self.t,bd = 1)
        # self.ent2.place(x=100,y=80)
        # self.btb2 = Button(self.t,text = "浏览",command = self.openfilename)
        # self.btb2.place(x=300,y=80)


        self.btn_exe = Button(self.t,text = "        转换        ",command = self.tcConvert)
        self.btn_exe.place(x=100,y=80)

        # self.st = tkinter.Text(self.t)
        # self.st.place(x=5,y=110,width=400,height=200)
        self.labinfo = Label(self.t,text ="  Testlink软件之XLS转XML工具 \n  作者：曾良均 \n  Ver: 0.1(20170703) ")
        self.labinfo.place(x=60,y=150)

    #选取文件路径
    def callback(self):
        self.ent.delete(0, END)
        # 清空entry里面的内容
        # 调用filedialog模块的askdirectory()函数去打开文件夹
        # filepath = tkFileDialog.askdirectory()
        filepath = filedialog.askopenfilename()
        if filepath:
            self.ent.insert(0, filepath) #将选择好的路径加入到entry里面

    def openfilename(self):
         filename = filedialog.asksaveasfilename(filetypes=[("打开文件", "*.xls")])

         if filename:
            return open(filename, 'w')

    #转换函数
    def tcConvert(self):
        path = self.ent.get()
        print(self.ent.get())
        logging.debug('Select path ==' + path)
        if path == "":
            tkinter.messagebox.showinfo("Messages","请打开有效的xls文件！")

        f_in = xlrd.open_workbook(path)
        if f_in:
            logging.debug("t")


        sheet = f_in.sheet_by_index(0)
        # create XML
        testcases = etree.Element('testcases')

        print("row = %d" % sheet.nrows)
        def format_str(rawstr):
            rawstr = "<p>" + rawstr + "</p>"
            return rawstr

        for seq in range(1,sheet.nrows):
            print(seq)
            try:
                name_ = sheet.row_values(seq)[0]
                summary_ = sheet.row_values(seq)[1]
                pre_ = sheet.row_values(seq)[2]
                importance_ = sheet.row_values(seq)[3]
                step_ = sheet.row_values(seq)[4]
                expect_ = sheet.row_values(seq)[5]
                exe_type_ = sheet.row_values(seq)[6]

                test_case = etree.SubElement(testcases, 'testcase', name=name_)
                summary = etree.SubElement(test_case, 'summary')
                summary.text = format_str(summary_)
                print(summary.text)
                logging.debug('summary.text====' + summary.text)


                preconditions = etree.SubElement(test_case, 'preconditions')
                print(pre_)
                # preconditions.text = u'"{0}"'.format(pre_)
                pre_ = pre_.replace("\n", "</br>")
                print(pre_)
                preconditions.text = format_str(pre_)
                print(preconditions.text)

                # <importance><![CDATA[2]]></importance>
                importance_level = etree.SubElement(test_case, 'importance')
                importance_level.text = str(int(importance_))
                print(importance_level.text)

                steps = etree.SubElement(test_case, 'steps')
                step = etree.SubElement(steps, 'step')
                step_number = etree.SubElement(step, 'step_number')
                step_number.text = str(1)

                # Transform the steps
                actions = etree.SubElement(step, 'actions')
                # actions.text = u'"{0}"'.format(step_)
                step_ = step_.replace("\n", "</br>")
                print(step_)
                actions.text = format_str(step_)
                print(actions.text)
                expectedresults = etree.SubElement(step, 'expectedresults')

                # expectedresults.text = u'"{0}"'.format(expect_)
                expect_ = expect_.replace("\n", "</br>")
                print(expect_)
                expectedresults.text = format_str(expect_)
                print(expectedresults.text)

                execution_type = etree.SubElement(step, 'execution_type')
                execution_type.text = str(int(exe_type_))
                print(execution_type.text)

            except Exception as e:
                print("line:", seq)
                print(str(e))
                for item in sys.exc_info():
                    print(item())

        s = etree.tostring(testcases, pretty_print=True)
        # s = etree.tostring(testcases)
        pathlist = path.split("/")
        pathlist.pop()
        newpath = '/'.join(pathlist)
        f_out = open(newpath + "/my.xml", 'w')
        f_out.write(s.decode("utf-8"))
        tkinter.messagebox.showinfo("Messages", "Convert Successfully.\n Save file to my.xml .")



if __name__ == '__main__':
    root = None
    t1.append(Converter(root))
    root = t1[0].t
    root.mainloop()
