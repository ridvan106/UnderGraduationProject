# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matematichal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import numpy as np
from keras.models import load_model
from scipy import misc
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

    def setupUi(self, Form):
        self.cond = False
        self.VGG19 = load_model('./ALL/vgg19.h5') # load Vgg19
        print('VGG19')
        self.Inception = load_model('./ALL/InceptionNet.h5') # load inception
        print('InceptionNet')
        self.DenseNet = load_model('./ALL/DenseNet121.h5') # load denseNet
        print('DenseNet')
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(495, 388)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 50, 361, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(165, 59, 33);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.select = QtGui.QPushButton(Form)
        self.select.setGeometry(QtCore.QRect(200, 120, 85, 27))
        self.select.setObjectName(_fromUtf8("select"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 478, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color:rgb(159, 56, 25)"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Dnet = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Dnet.setFont(font)
        self.Dnet.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.Dnet.setAlignment(QtCore.Qt.AlignCenter)
        self.Dnet.setObjectName(_fromUtf8("Dnet"))
        self.horizontalLayout_2.addWidget(self.Dnet)
        self.Inet = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Inet.setFont(font)
        self.Inet.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.Inet.setAlignment(QtCore.Qt.AlignCenter)
        self.Inet.setObjectName(_fromUtf8("Inet"))
        self.horizontalLayout_2.addWidget(self.Inet)
        self.Vnet = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Vnet.setFont(font)
        self.Vnet.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.Vnet.setAlignment(QtCore.Qt.AlignCenter)
        self.Vnet.setObjectName(_fromUtf8("Vnet"))
        self.horizontalLayout_2.addWidget(self.Vnet)
        self.max = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.max.setFont(font)
        self.max.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.max.setAlignment(QtCore.Qt.AlignCenter)
        self.max.setObjectName(_fromUtf8("max"))
        self.horizontalLayout_2.addWidget(self.max)
        self.avg = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.avg.setFont(font)
        self.avg.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.avg.setAlignment(QtCore.Qt.AlignCenter)
        self.avg.setObjectName(_fromUtf8("avg"))
        self.horizontalLayout_2.addWidget(self.avg)
        self.add = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet(_fromUtf8("color:rgb(148, 61, 17)"))
        self.add.setAlignment(QtCore.Qt.AlignCenter)
        self.add.setObjectName(_fromUtf8("add"))
        self.horizontalLayout_2.addWidget(self.add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.connect(self.select, QtCore.SIGNAL("pressed()"), self.predict)

    def sonuc(self):
        QtCore.QCoreApplication.processEvents()
        print(self.img)
        img = misc.imread(self.img)

        den = []
        den.append(img)
        den = np.array(den)
        print("sonuc")
        self.pred1 = self.DenseNet.predict(den)  # prediction of denseNet model
        self.pred2 = self.Inception.predict(den)  # prediction of Inception model
        self.pred3 = self.VGG19.predict(den)  # prediction of VGG19


    def predict(self):

        self.img = QtGui.QFileDialog.getOpenFileName() # because of freezing
        self.sonuc()
        ########################################
        maxi = np.maximum(self.pred1,self.pred2,self.pred3)
        add = np.add(self.pred1,self.pred2,self.pred3)
        avg = add/3
        ########################################

        self.Dnet.setText(self.mapping(np.argmax(self.pred1)))
        self.Vnet.setText(self.mapping(np.argmax(self.pred3)))
        self.Inet.setText(self.mapping(np.argmax(self.pred2)))
        ########################################
        self.max.setText(self.mapping(np.argmax(maxi)))
        self.add.setText(self.mapping(np.argmax(add)))
        self.avg.setText(self.mapping(np.argmax(avg)))
        print(self.img)

    def mapping(self,k): # map integer to string result
        if k == 0:
            return "Karton"
        elif k == 1:
            return "Cam"
        elif k == 2:
            return "Metal"
        elif k == 3:
            return "Kağıt"
        elif k == 4:
            return "Plastik"
        elif k == 5:
            return "Evsel"

    def retranslateUi(self, Form): #GUI
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "MATEMATİKSEL İŞLEMLER İLE SONUÇ ALMA", None))
        self.select.setText(_translate("Form", "Görüntü Seç", None))
        self.label_5.setText(_translate("Form", "DenseNet", None))
        self.label_4.setText(_translate("Form", "Inception", None))
        self.label_3.setText(_translate("Form", "VGG19", None))
        self.label_6.setText(_translate("Form", "maksimum", None))
        self.label_2.setText(_translate("Form", "Ortalama", None))
        self.label_7.setText(_translate("Form", "Toplama", None))
        self.Dnet.setText(_translate("Form", " ", None))
        self.Inet.setText(_translate("Form", " ", None))
        self.Vnet.setText(_translate("Form", " ", None))
        self.max.setText(_translate("Form", " ", None))
        self.avg.setText(_translate("Form", " ", None))
        self.add.setText(_translate("Form", " ", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    win = Ui_Form()
    win.setupUi(form)
    form.show()
    app.exec_()
