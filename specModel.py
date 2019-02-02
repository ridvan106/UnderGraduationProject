# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specific.ui'
# take a result specific model
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
from PyQt4 import QtCore, QtGui
import sys
from keras.models import load_model
from scipy import misc
import numpy as np
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

        ####################  load models #############################
        self.vgg16 = load_model('./ALL/vgg16.h5')
        print("vgg16")
        self.vgg19 = load_model('./ALL/vgg19.h5')
        print("vgg19")
        self.ResNet50 = load_model('./ALL/resNet50.h5')
        print("resNet50")
        self.denseNet = load_model('./ALL/DenseNet121.h5')
        print("DenseNet50")
        self.inception = load_model('./ALL/InceptionNet.h5')
        print("InceptionNet")

        ######################################################################################


        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(561, 456)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 80, 331, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:rgb(134, 55, 29)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 111, 111))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 180, 341, 35))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.models = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.models.setObjectName(_fromUtf8("models"))
        self.horizontalLayout.addWidget(self.models)
        self.predict = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.predict.setObjectName(_fromUtf8("predict"))
        self.horizontalLayout.addWidget(self.predict)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 270, 481, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.model = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.model.setFont(font)
        self.model.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName(_fromUtf8("model"))
        self.horizontalLayout_3.addWidget(self.model)
        self.result = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName(_fromUtf8("result"))
        self.horizontalLayout_3.addWidget(self.result)
        self.confidence = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confidence.setFont(font)
        self.confidence.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.confidence.setAlignment(QtCore.Qt.AlignCenter)
        self.confidence.setObjectName(_fromUtf8("confidence"))
        self.horizontalLayout_3.addWidget(self.confidence)
        self.time = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.models.setFixedHeight(25)
        self.predict.setFixedHeight(25)
        self.time.setFont(font)
        self.time.setStyleSheet(_fromUtf8("color:rgb(127, 46, 8)"))
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName(_fromUtf8("time"))
        self.horizontalLayout_3.addWidget(self.time)
        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.models.addItems(["VGG16","VGG19","ResNet50","DenseNet","InceptionNet"])

        Form.connect(self.predict, QtCore.SIGNAL("pressed()"), self.calc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def calc(self): # calculation according to selected model
        self.img = QtGui.QFileDialog.getOpenFileName()
        resim = misc.imread(self.img)
        den = []
        den.append(resim)
        den = np.array(den)
        indis = self.models.currentIndex();
        if indis == 0: # VGG16
            self.model.setText(str(self.models.currentText()))
            sec1 = time.time()  # birinci sure testpiti
            res = self.vgg16.predict(den)
            sec2 = time.time()
            self.result.setText(self.mapping(np.argmax(res)))
            self.confidence.setText(str(np.max(res).round(2)))
            self.time.setText(str(round(abs(sec2-sec1),2)))

        elif indis == 1: ## vgg 19
            self.model.setText(str(self.models.currentText()))
            sec1 = time.time()  # birinci sure testpiti
            res = self.vgg19.predict(den)
            sec2 = time.time()
            self.result.setText(self.mapping(np.argmax(res)))
            self.confidence.setText(str(np.max(res).round(2)))
            self.time.setText(str(round(abs(sec2 - sec1), 2)))
        elif indis == 2: # ResNet-50
            self.model.setText(str(self.models.currentText()))
            sec1 = time.time()  # birinci sure testpiti
            res = self.ResNet50.predict(den)
            sec2 = time.time()
            self.result.setText(self.mapping(np.argmax(res)))
            self.confidence.setText(str(np.max(res).round(2)))
            self.time.setText(str(round(abs(sec2 - sec1), 2)))
        elif indis == 3: # DenseNEt
            self.model.setText(str(self.models.currentText()))
            sec1 = time.time()  # birinci sure testpiti
            res = self.denseNet.predict(den)
            sec2 = time.time()
            self.result.setText(self.mapping(np.argmax(res)))
            self.confidence.setText(str(np.max(res).round(2)))
            self.time.setText(str(round(abs(sec2 - sec1), 2)))
        elif indis == 4: # inceptionNet
            self.model.setText(str(self.models.currentText()))
            sec1 = time.time()  # birinci sure testpiti
            res = self.inception.predict(den)
            sec2 = time.time()
            self.result.setText(self.mapping(np.argmax(res)))
            self.confidence.setText(str(np.max(res).round(2)))
            self.time.setText(str(round(abs(sec2 - sec1), 2)))


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "BELİRLİ MODELDEN SONUÇ ALMA", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\":./images/recycling.png\"/></p></body></html>", None))
        self.predict.setText(_translate("Form", "Tahmin", None))
        self.label_3.setText(_translate("Form", "Model", None))
        self.label_4.setText(_translate("Form", "Sonuç", None))
        self.label_5.setText(_translate("Form", "Güvenilirlik", None))
        self.label_6.setText(_translate("Form", "Süre", None))
        self.model.setText(_translate("Form", "Seçilen Model", None))
        self.result.setText(_translate("Form", "Model Sonucu", None))
        self.confidence.setText(_translate("Form", "yüzde", None))
        self.time.setText(_translate("Form", "saniye", None))

    def mapping(self,k): # convert int to String result
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
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    win = Ui_Form()
    win.setupUi(form)
    form.show()
    app.exec_()

