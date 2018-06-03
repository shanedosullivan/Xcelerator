import Tkinter
import tkFileDialog
from Tkinter import *
from filenameGenerator import FilenameGenerator
from converter import Converter

class ConverterApp:



    def __init__(self, master):
        global globalMaster
        globalMaster = master
        global errorLabel
        errorLabel = Label (globalMaster, text="")
        global label
        global label1
        global label2
        label = Label (globalMaster, text="")
        label1 = Label (globalMaster, text="")
        label2 = Label (globalMaster, text="")



        master.iconbitmap('../../bin/excel.ico')
        master.title("Xcelerator")
        master.resizable(width=False, height=False)
        master.minsize(width=400, height=100)
        fileToConvertButton = Button(master, text="Select a file...", command = self.open_file_dialog)
        fileToConvertButton.place(x=20, y=30)

    def open_file_dialog(self):
        try:
            fileName = tkFileDialog.askopenfilename(initialdir = "C:/", title='File to convert', filetypes=(("Excel Files", "*.xlsx"),))
            if fileName != None:
                filenameGenerator = FilenameGenerator()
                converter = Converter()
                hash = filenameGenerator.generate_name()
                converter.convert_and_save_excel("../../excel/results/transformed-excel_"+hash+".xlsx", fileName)

                errorLabel.place_forget()
                label.configure(text="File converted successfully.")
                label1.configure(text="Check it out at excel/results/transformed-excel_"+hash+".xlsx")
                label2.configure(text="in the Xcelerator directory.")
                label.place(x=20, y =60)
                label1.place(x=20, y =80)
                label2.place(x=20, y =100)
        except:
                errorLabel.configure(text="Oops, something went wrong. Is the file format correct?")
                errorLabel.place(x=20, y =60)
                label.place_forget()
                label1.place_forget()
                label2.place_forget()



top = Tkinter.Tk()
app = ConverterApp(top)
top.mainloop()
