from PyQt6.QtWidgets import QApplication , QMainWindow , QFileDialog , QMessageBox , QFontDialog , QColorDialog
from PyQt6.QtPrintSupport import QPrinter , QPrintDialog , QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo , Qt
from PyQt6.QtGui import QFont
from ui import Ui_MainWindow
import sys

class notep(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.actionsave.triggered.connect(self.saver)
        self.actionnew.triggered.connect(self.newf)
        self.actionopen.triggered.connect(self.opener)
        self.actionprint.triggered.connect(self.printer)
        self.actionprint_previe.triggered.connect(self.pre)
        self.actionexport_PDF.triggered.connect(self.pdfer)
        self.actionQuite.triggered.connect(self.closer)
        self.actionredo.triggered.connect(self.textEdit.redo)
        self.actionundo.triggered.connect(self.textEdit.undo)
        self.actioncopy.triggered.connect(self.textEdit.copy)
        self.actionpaste.triggered.connect(self.textEdit.paste)
        self.actioncut.triggered.connect(self.textEdit.cut)
        self.actionBold.triggered.connect(self.bolder)
        self.actionItallic.triggered.connect(self.italer)
        self.actionUnderline.triggered.connect(self.under)
        self.actionLeft.triggered.connect(self.left)
        self.actionRight.triggered.connect(self.right)
        self.actioncenter.triggered.connect(self.center)
        self.actionJustify.triggered.connect(self.just)
        self.actionFont.triggered.connect(self.fonter)
        self.actionColor.triggered.connect(self.color)
        
        
        
    def saver(self):
        filename = QFileDialog.getSaveFileName(self , "save File")
        if filename[0]:
            with open(filename[0]  , "w") as file :
                text =  self.textEdit.toPlainText()
                file.write(text)
                QMessageBox.about(self , "save file" , "file have been saved")
    
    def maysave(self):
        if not self.textEdit.document().isModified():
            return True
        else :
            res =  QMessageBox.warning(self , "notepade" ,  "do you want save new changes? " , QMessageBox.StandardButton.Save | QMessageBox.StandardButton.No |QMessageBox.StandardButton.Cancel)
            if res == QMessageBox.StandardButton.Save  :
                self.saver()
                return True
            elif res == QMessageBox.StandardButton.No:
                return True
            else :
                return False
            
    def newf(self):
        if self.maysave():
            self.textEdit.clear()
    
    def opener(self):
        if not self.maysave():
            return False
        namef = QFileDialog.getOpenFileName(self,"open file" , )
        if namef[0] :
            with open(namef[0] , "r") as file :
                self.textEdit.setText(file.read())
        
    def printer(self):
        printerr = QPrinter(QPrinter.PrinterMode.HighResolution)
        dia = QPrintDialog(printerr)
        if dia.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printerr)
            
    def pre(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dia = QPrintPreviewDialog(printer , self)
        
        dia.paintRequested.connect(self.pref)
        dia.exec()
        
    def pref(self , printer):
        self.textEdit.print(printer)
        
        
    def pdfer(self):
        fn , _ = QFileDialog.getSaveFileName(self , "Export PDF" , "new.pdf")
        if fn :
            if QFileInfo(fn).suffix() == "": fn = f"{fn}.pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)
            
    def closer(self):
        self.close()   
        
    def bolder(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)      
        
    def italer(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)  
        
    def under(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)     
            
    def left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)
    def center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def just(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)
                   
    def fonter(self):
        font , ok  = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
        
        
    def color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)   
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = notep()
    sys.exit(app.exec())