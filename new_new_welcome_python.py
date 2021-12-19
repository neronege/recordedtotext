# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/egemen/Desktop/recordtoText/new_new_welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(627, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(627, 450))
        MainWindow.setMaximumSize(QtCore.QSize(625, 450))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 10, 611, 401))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.Video_tr = QtWidgets.QPushButton(self.page)
        self.Video_tr.setGeometry(QtCore.QRect(20, 360, 89, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Video_tr.setFont(font)
        self.Video_tr.setStyleSheet("background-color: rgb(114, 159, 207);\n"
                                    "color: rgb(238, 238, 236);")
        self.Video_tr.setObjectName("Video_tr")
        self.video_en = QtWidgets.QPushButton(self.page)
        self.video_en.setGeometry(QtCore.QRect(480, 360, 89, 25))
        self.video_en.setStyleSheet("background-color: rgb(114, 159, 207);\n"
                                    "color: rgb(238, 238, 236);")
        self.video_en.setObjectName("video_en")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")


        self.soundBox = QtWidgets.QDialogButtonBox(self.page_2)
        self.soundBox.setGeometry(QtCore.QRect(520, 70, 80, 25))
        self.soundBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.soundBox.setStandardButtons(QtWidgets.QDialogButtonBox.Open)
        self.soundBox.setObjectName("soundBox")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 220, 501, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 180, 500, 30))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(500, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(80, 280, 391, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 70, 501, 25))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(10, 330, 150, 25))
        self.label.setMinimumSize(QtCore.QSize(200, 25))
        self.label.setMaximumSize(QtCore.QSize(200, 25))
        self.label.setObjectName("label")
        self.textButton = QtWidgets.QDialogButtonBox(self.page_2)
        self.textButton.setGeometry(QtCore.QRect(520, 220, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textButton.sizePolicy().hasHeightForWidth())
        self.textButton.setSizePolicy(sizePolicy)
        self.textButton.setMinimumSize(QtCore.QSize(50, 0))
        self.textButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.textButton.setStandardButtons(QtWidgets.QDialogButtonBox.Open)
        self.textButton.setObjectName("textButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 500, 30))
        self.textBrowser.setMaximumSize(QtCore.QSize(500, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")
        #self.menuWelcome = QtWidgets.QMenu(self.menubar)
        #self.menuWelcome.setObjectName("menuWelcome")
        #self.menuT_rk_e = QtWidgets.QMenu(self.menubar)
        #self.menuT_rk_e.setObjectName("menuT_rk_e")
        #self.menuEnglish = QtWidgets.QMenu(self.menubar)
        #self.menuEnglish.setMinimumSize(QtCore.QSize(0, 2))
        #self.menuEnglish.setMaximumSize(QtCore.QSize(16777215, 16777212))
        #self.menuEnglish.setObjectName("menuEnglish")
        #self.menuDeutsch = QtWidgets.QMenu(self.menubar)
        #self.menuDeutsch.setObjectName("menuDeutsch")
        #self.menuFran_ais = QtWidgets.QMenu(self.menubar)
        #self.menuFran_ais.setObjectName("menuFran_ais")

        #MainWindow.setMenuBar(self.menubar)
       # self.statusbar = QtWidgets.QStatusBar(MainWindow)
       # self.statusbar.setObjectName("statusbar")
       # MainWindow.setStatusBar(self.statusbar)
       # self.actionEnglish = QtWidgets.QAction(MainWindow)
       # self.actionEnglish.setObjectName("actionEnglish")
      #  self.actionFran_ais = QtWidgets.QAction(MainWindow)
      #  self.actionFran_ais.setObjectName("actionFran_ais")
      #  self.action_Deutsch = QtWidgets.QAction(MainWindow)
      #  self.action_Deutsch.setObjectName("action_Deutsch")
      #  self.menubar.addAction(self.menuWelcome.menuAction())
      #  self.menubar.addAction(self.menuT_rk_e.menuAction())
      #  self.menubar.addAction(self.menuEnglish.menuAction())
      #  self.menubar.addAction(self.menuDeutsch.menuAction())
      #  self.menubar.addAction(self.menuFran_ais.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RecordedtoText"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">English:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome. Please select language which you will use for start</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For help, you can push video button and arrive videos or send mail to admin@egemenozmen.net</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Françis:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bienvenue. Veuillez choisir la langue pour commencer </p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pour obtenir de l\'aide, Si besoin d'aide vous pouvez appuyer sur le video bouton Ou envoyer un mail à admin@egemenozmen.net</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Deutsch:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Willkommen. Bitte wählen Sie die Sprache aus, die Sie für den Start verwenden möchten</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Um Hilfe zu erhalten, können Sie die Videotaste drücken und Videos ankommen oder eine E-mail admin@egemenozmen.net senden</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Türkçe:</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hoş geldiniz. Lütfen başlangıç ​​için kullanacağınız dili seçin.</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yardım için , video düğmesine tıklayı videolara ulaşabilir veya admin@egemenozmen adresine mail gönderebilirsiniz</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Video_tr.setText(_translate("MainWindow", "Video(Tr)"))
        self.video_en.setText(_translate("MainWindow", "Video(En)"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oluşturacağınız yazı dosyasının yerini seçiniz</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Dönüştür"))
        self.label.setText(_translate("MainWindow", " Dönüştürülüyor... "))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dönüştürmek istediğiniz ses dosyasını giriniz</p></body></html>"))
     #   self.menuT_rk_e.setTitle(_translate("MainWindow", "Türkçe"))
     #   self.menuEnglish.setTitle(_translate("MainWindow", "English"))
     #   self.menuDeutsch.setTitle(_translate("MainWindow", "Deutsch"))
     #   self.menuFran_ais.setTitle(_translate("MainWindow", "Français"))
       # self.menuWelcome.setTitle(_translate("MainWindow", "Welcome"))
       # self.menuT_rk_e.setTitle(_translate("MainWindow", "Türkçe"))
       # self.actionEnglish.setText(_translate("MainWindow", "English"))
       # self.actionFran_ais.setText(_translate("MainWindow", "Français"))
       # self.action_Deutsch.setText(_translate("MainWindow", "Deutsch"))
