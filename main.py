import sys

from view import PyCalcUi
from controller import PyCalcCtrl
from model import evaluateExpression

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

def main():
    calc = QApplication(sys.argv)
    view = PyCalcUi()   
    view.show()         
    model = evaluateExpression          
    PyCalcCtrl(model=model, view=view)  
    sys.exit(calc.exec_())    
    
if __name__ == "__main__":
    main()