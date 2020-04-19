# -*- coding: utf-8 -*-

import sys
sys.path.append(r'.\real_url')
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_UI import Ui_MainWindow
import re
import douyu
import huya

class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.setupUi(self)
        self.getUrlButton.clicked.connect(self.getUrl)
        self.roomID.textChanged.connect(self.ridStatusChange)

    def getUrl(self):
        platform = self.comboBox.currentText()
        rid = self.roomID.text()
        if platform == '斗鱼':
            realUrl = douyu.get_real_url(rid)
        elif platform == '虎牙':
            realUrl = huya.get_real_url(rid)
        #elif platform == 'Bilibili':

        #elif platform == '触手':

        #elif platform == '抖音':

        #elif platform == '企鹅电竞':

        #elif platform == '花椒':

        #elif platform == '火猫':

        #elif platform == '爱奇艺':

        #elif platform == '快手':

        #elif platform == '酷狗':

        #elif platform == '龙珠':

        #elif platform == 'NOW':

        #elif platform == 'pps':

        #elif platform == '六间房':

        #elif platform == '网易CC':

        #elif platform == '西瓜':

        #elif platform == '映客':

        #elif platform == '一直播':

        #elif platform == 'YY':

        #elif platform == '战旗':


        zh = "".join(re.compile('[^\u4e00-\u9fa5]').split(realUrl)).strip()
        
        if zh != realUrl:
            clipboard = QApplication.clipboard()
            clipboard.setText(realUrl)
            QMessageBox.information(self, '完成', '直播地址已复制')
        else:
            QMessageBox.information(self, '完成', '获取地址错误')

    def ridStatusChange(self):
        if len(self.roomID.text()) == 0:
            self.getUrlButton.setEnabled(False)
        else:
            self.getUrlButton.setEnabled(True)

    #def updataSelectList(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)

    real_url_GUI = Interface()
    real_url_GUI.show()

    sys.exit(app.exec_())
