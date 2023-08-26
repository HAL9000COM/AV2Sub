# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen_Source_Licenses = QAction(MainWindow)
        self.actionOpen_Source_Licenses.setObjectName(u"actionOpen_Source_Licenses")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_main = QWidget()
        self.tab_main.setObjectName(u"tab_main")
        self.verticalLayout_5 = QVBoxLayout(self.tab_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.tab_main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_av = QLineEdit(self.groupBox_3)
        self.lineEdit_av.setObjectName(u"lineEdit_av")

        self.horizontalLayout_4.addWidget(self.lineEdit_av)

        self.pushButton_av_browse = QPushButton(self.groupBox_3)
        self.pushButton_av_browse.setObjectName(u"pushButton_av_browse")

        self.horizontalLayout_4.addWidget(self.pushButton_av_browse)

        self.checkBox_batch = QCheckBox(self.groupBox_3)
        self.checkBox_batch.setObjectName(u"checkBox_batch")

        self.horizontalLayout_4.addWidget(self.checkBox_batch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_output = QLineEdit(self.groupBox_3)
        self.lineEdit_output.setObjectName(u"lineEdit_output")

        self.horizontalLayout_5.addWidget(self.lineEdit_output)

        self.pushButton_out_browse = QPushButton(self.groupBox_3)
        self.pushButton_out_browse.setObjectName(u"pushButton_out_browse")

        self.horizontalLayout_5.addWidget(self.pushButton_out_browse)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.tab_main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_target_lang = QComboBox(self.groupBox_2)
        self.comboBox_target_lang.setObjectName(u"comboBox_target_lang")

        self.horizontalLayout_3.addWidget(self.comboBox_target_lang)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_bilingual = QComboBox(self.groupBox_2)
        self.comboBox_bilingual.addItem("")
        self.comboBox_bilingual.addItem("")
        self.comboBox_bilingual.addItem("")
        self.comboBox_bilingual.setObjectName(u"comboBox_bilingual")

        self.horizontalLayout_2.addWidget(self.comboBox_bilingual)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_save_original = QCheckBox(self.groupBox_2)
        self.checkBox_save_original.setObjectName(u"checkBox_save_original")

        self.horizontalLayout_8.addWidget(self.checkBox_save_original)

        self.checkBox_clear_cache = QCheckBox(self.groupBox_2)
        self.checkBox_clear_cache.setObjectName(u"checkBox_clear_cache")

        self.horizontalLayout_8.addWidget(self.checkBox_clear_cache)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.pushButton_process = QPushButton(self.tab_main)
        self.pushButton_process.setObjectName(u"pushButton_process")

        self.verticalLayout_5.addWidget(self.pushButton_process)

        self.tabWidget.addTab(self.tab_main, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.comboBox_transcribe = QComboBox(self.groupBox)
        self.comboBox_transcribe.addItem("")
        self.comboBox_transcribe.setObjectName(u"comboBox_transcribe")

        self.horizontalLayout_6.addWidget(self.comboBox_transcribe)

        self.lineEdit_transcribe_key = QLineEdit(self.groupBox)
        self.lineEdit_transcribe_key.setObjectName(u"lineEdit_transcribe_key")

        self.horizontalLayout_6.addWidget(self.lineEdit_transcribe_key)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.comboBox_translate = QComboBox(self.groupBox)
        self.comboBox_translate.addItem("")
        self.comboBox_translate.addItem("")
        self.comboBox_translate.setObjectName(u"comboBox_translate")

        self.horizontalLayout_7.addWidget(self.comboBox_translate)

        self.lineEdit_translate_key = QLineEdit(self.groupBox)
        self.lineEdit_translate_key.setObjectName(u"lineEdit_translate_key")

        self.horizontalLayout_7.addWidget(self.lineEdit_translate_key)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.spinBox_max_lines = QSpinBox(self.tab_2)
        self.spinBox_max_lines.setObjectName(u"spinBox_max_lines")
        self.spinBox_max_lines.setMaximum(200)
        self.spinBox_max_lines.setValue(20)

        self.horizontalLayout_9.addWidget(self.spinBox_max_lines)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionOpen_Source_Licenses)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AV2Sub", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen_Source_Licenses.setText(QCoreApplication.translate("MainWindow", u"Open Source Licenses", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Audio/Video Path", None))
        self.pushButton_av_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.checkBox_batch.setText(QCoreApplication.translate("MainWindow", u"batch", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.pushButton_out_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Subtitle settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Target Language", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bilingual subtitles", None))
        self.comboBox_bilingual.setItemText(0, QCoreApplication.translate("MainWindow", u"Translated at top", None))
        self.comboBox_bilingual.setItemText(1, QCoreApplication.translate("MainWindow", u"Translated at bottom", None))
        self.comboBox_bilingual.setItemText(2, QCoreApplication.translate("MainWindow", u"None", None))

        self.checkBox_save_original.setText(QCoreApplication.translate("MainWindow", u"Save Original subtitle", None))
        self.checkBox_clear_cache.setText(QCoreApplication.translate("MainWindow", u"Clear Cache", None))
        self.pushButton_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), QCoreApplication.translate("MainWindow", u"main", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"API key", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Transcribe API", None))
        self.comboBox_transcribe.setItemText(0, QCoreApplication.translate("MainWindow", u"OpenAI", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Translate API:", None))
        self.comboBox_translate.setItemText(0, QCoreApplication.translate("MainWindow", u"DeepL", None))
        self.comboBox_translate.setItemText(1, QCoreApplication.translate("MainWindow", u"Deepl Pro", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Max lines in one translate request:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

