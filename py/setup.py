from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')

#Mydata_files = [('images', ['C:/Users/Jibestream/Xcelerator/bin/excel.ico'])]

setup(options = {"py2exe": {"includes": ["Tkinter", "openpyxl", "xlrd", "tkFileDialog"]}}, windows = [{'script': "xcelerator.py", "icon_resources": [(1, "../bin/excel.ico")]}])
