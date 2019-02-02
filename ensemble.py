# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ensemble.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
# from modeller import SnapShot1,DenseNet_169,SnapShot2,EnsembleModel
import sys
import time
from scipy import misc
import numpy as np
import pandas as pd
from sklearn.decomposition import  PCA
from sklearn.neighbors import KNeighborsClassifier
from keras.models import load_model

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
    def transform(self):
        vectors = pd.read_csv('./featureVector/featureWithresult.csv', header=None) # feature vektor
        vectorsTest = pd.read_csv('./featureVector/featureWithresultTest.csv', header=None) # feature Vektor result
        ##### Split label tag train data #############
        SVMx_train = vectors.iloc[:, 2:-1]  # ilk 2 sutun bos indis
        SVMy_train = vectors.iloc[:, -1] # son sutunda sonuclar var
        pca = PCA(n_components=45) # testlete gore ideal transform 45
        x_tr = pca.fit_transform(SVMx_train, SVMy_train)
        self.transFormM = pca

        ###################### KNN ################################
        self.knn = KNeighborsClassifier(n_neighbors=10, metric='euclidean')

        self.knn.fit(x_tr, SVMy_train) # fit knn

    def buidModel(self):
        self.dnsnet169 = load_model('./ALL/dnsNt169.h5') # load denseNet 169
        print('denseNet169')
        self.snpsht140 = load_model('./ALL/snpsht140-DenseNet121.h5') # snapshot140 - DenseNet-121
        print('snap1')
        self.snpsht2 = load_model('./ALL/snpsht2-DenseNet121.h5') # snapshot-2 DenseNet Ensemble
        print('snap2')
        self.allModel = load_model('./ALL/lastEnsemble.h5') # ensemble model with feature vectors
        print('allmodel')

    def setupUi(self, Form):
        self.buidModel() # build model
        self.transform() # transform PCA
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(622, 452)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 551, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(16, 200, 590, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(132, 42, 15)"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color:rgb(132, 42, 15)"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(132, 42, 15)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(132, 42, 15)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_4.addWidget(self.label_13)
        self.R_ensemble = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.R_ensemble.setFont(font)
        self.R_ensemble.setStyleSheet(_fromUtf8("color:rgb(132,42,15)"))
        self.R_ensemble.setAlignment(QtCore.Qt.AlignCenter)
        self.R_ensemble.setObjectName(_fromUtf8("R_ensemble"))
        self.horizontalLayout_4.addWidget(self.R_ensemble)
        self.R_densenet169 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.R_densenet169.setFont(font)
        self.R_densenet169.setStyleSheet(_fromUtf8("color:rgb(132,42,15)"))
        self.R_densenet169.setAlignment(QtCore.Qt.AlignCenter)
        self.R_densenet169.setObjectName(_fromUtf8("R_densenet169"))
        self.horizontalLayout_4.addWidget(self.R_densenet169)
        self.R_snapShot1 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.R_snapShot1.setFont(font)
        self.R_snapShot1.setStyleSheet(_fromUtf8("color:rgb(132,42,15)"))
        self.R_snapShot1.setAlignment(QtCore.Qt.AlignCenter)
        self.R_snapShot1.setObjectName(_fromUtf8("R_snapShot1"))
        self.horizontalLayout_4.addWidget(self.R_snapShot1)
        self.R_snaphot2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.R_snaphot2.setFont(font)
        self.R_snaphot2.setStyleSheet(_fromUtf8("color:rgb(132,42,15)"))
        self.R_snaphot2.setAlignment(QtCore.Qt.AlignCenter)
        self.R_snaphot2.setObjectName(_fromUtf8("R_snaphot2"))
        self.horizontalLayout_4.addWidget(self.R_snaphot2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color:rgb(0, 76, 230)\n"
                                              ""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.S_e = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_e.sizePolicy().hasHeightForWidth())
        self.S_e.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_e.setFont(font)
        self.S_e.setStyleSheet(_fromUtf8("color:rgb(145,42,12)\n"
                                         ""))
        self.S_e.setObjectName(_fromUtf8("S_e"))
        self.horizontalLayout_2.addWidget(self.S_e)
        self.S_sanp1 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_sanp1.sizePolicy().hasHeightForWidth())
        self.S_sanp1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_sanp1.setFont(font)
        self.S_sanp1.setStyleSheet(_fromUtf8("color:rgb(145,42,12)\n"
                                             ""))
        self.S_sanp1.setObjectName(_fromUtf8("S_sanp1"))
        self.horizontalLayout_2.addWidget(self.S_sanp1)
        self.S_sanp2 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_sanp2.sizePolicy().hasHeightForWidth())
        self.S_sanp2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_sanp2.setFont(font)
        self.S_sanp2.setStyleSheet(_fromUtf8("color:rgb(145,42,12)\n"
                                             ""))
        self.S_sanp2.setObjectName(_fromUtf8("S_sanp2"))
        self.horizontalLayout_2.addWidget(self.S_sanp2)
        self.S_snap3 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_snap3.sizePolicy().hasHeightForWidth())
        self.S_snap3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_snap3.setFont(font)
        self.S_snap3.setStyleSheet(_fromUtf8("color:rgb(145,42,12)\n"
                                             ""))
        self.S_snap3.setObjectName(_fromUtf8("S_snap3"))
        self.horizontalLayout_2.addWidget(self.S_snap3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(230, 150, 281, 251))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        Form.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.predict)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mapping(self,k):  # map digital to string result
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

    def predict(self):
        self.img = QtGui.QFileDialog.getOpenFileName() # read file
        resim = misc.imread(self.img)
        den = []
        den.append(resim)
        den = np.array(den) # image convert to numpy array
        sec1 = time.time()  # birinci sure testpiti
        res = self.allModel.predict(den) # create feature vektor
        res = self.transFormM.transform(res)
        ensembleR = self.knn.predict(res)
        sec2 = time.time()  # ikinci sure tespiti
        print(abs(sec2 - sec1))
        self.S_e.setText(str(round(abs(sec2 - sec1), 2)))  # ensemble time
        self.R_ensemble.setText(self.mapping(ensembleR))  # ensemble prediction

        ########################## DENSENET-169 ##################################
        sec1 = time.time()  # birinci sure testpiti
        DENSENET169 = self.dnsnet169.predict(den)  # densenet 169
        sec2 = time.time()  # ikinci sure tespiti
        self.S_sanp1.setText(str(round(abs(sec2 - sec1), 2)))
        self.R_densenet169.setText(self.mapping(np.argmax(DENSENET169))+str(" - ")+str(np.max(DENSENET169).round(2)))
        ################################  SNAPSHOT1  #############################
        sec1 = time.time()  # birinci sure testpiti
        SNAPSHOT_1 = self.snpsht140.predict(den) # snapshot1 - 140
        sec2 = time.time()
        self.S_sanp2.setText(str(round(abs(sec2 - sec1), 2)))
        self.R_snapShot1.setText(self.mapping(np.argmax(SNAPSHOT_1))+str(" - ")+str(np.max(SNAPSHOT_1).round(2)))
        ################################# SNAPSHOT 2 #############################
        sec1 = time.time()  # birinci sure testpiti
        SNAPSHOT_2 = self.snpsht2.predict(den)  # snapshot1 - 140
        sec2 = time.time()
        self.S_snap3.setText(str(round(abs(sec2 - sec1), 2)))
        self.R_snaphot2.setText(self.mapping(np.argmax(SNAPSHOT_2))+str(" - ")+str(np.max(SNAPSHOT_2).round(2)))



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "ENSEMBLE LEARNING ", None))
        self.label_2.setText(_translate("Form", "Tahmin Edilecek Görüntüyü seçin: ", None))

        self.pushButton.setText(_translate("Form", "Görüntü Seç", None))

        self.label_12.setStyleSheet(_translate("Form", "color:rgb(0, 76, 230)\n"
                                                       "", None))
        self.label_12.setText(_translate("Form", "Modeller:", None))

        self.label_6.setText(_translate("Form", "Ensemle Result", None))

        self.label_5.setText(_translate("Form", "DenseNet-169", None))

        self.label_4.setText(_translate("Form", "DenseNet-121", None))

        self.label_3.setText(_translate("Form", "DenseNet-121", None))

        self.label_13.setStyleSheet(_translate("Form", "color:rgb(0, 76, 230)\n"
                                                       "", None))
        self.label_13.setText(_translate("Form", "Sonuçlar:", None))
        self.R_ensemble.setText(_translate("Form", " " , None))
        self.R_densenet169.setText(_translate("Form", " ", None))
        self.R_snapShot1.setText(_translate("Form", " ", None))
        self.R_snaphot2.setText(_translate("Form", " ", None))
        self.label_11.setText(_translate("Form", "Süre:            ", None))
        self.S_e.setText(_translate("Form", " ", None))
        self.S_sanp1.setText(_translate("Form", " ", None))
        self.S_sanp2.setText(_translate("Form", " ", None))
        self.S_snap3.setText(_translate("Form", " ", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    win = Ui_Form()
    win.setupUi(form)
    form.show()
    app.exec_()
