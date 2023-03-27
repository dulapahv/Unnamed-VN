# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_description.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_CardWindow(object):
    def setupUi(self, CardWindow):
        if not CardWindow.objectName():
            CardWindow.setObjectName(u"CardWindow")
        CardWindow.resize(620, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        CardWindow.setWindowIcon(icon)
        CardWindow.setStyleSheet(u"background-color: #454c5a;")
        CardWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(CardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_card_desc = QLabel(self.centralwidget)
        self.label_card_desc.setObjectName(u"label_card_desc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_card_desc.sizePolicy().hasHeightForWidth())
        self.label_card_desc.setSizePolicy(sizePolicy)
        self.label_card_desc.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(28)
        self.label_card_desc.setFont(font)
        self.label_card_desc.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #ffffff;\n"
"padding: 0px 0px 0px 10px;")
        self.label_card_desc.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_card_desc)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background-color: #f4f5f7;\n"
"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_title = QLabel(self.widget1)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: #282c33;")
        self.label_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_title)

        self.lineEdit_title = QLineEdit(self.widget1)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(12)
        self.lineEdit_title.setFont(font2)
        self.lineEdit_title.setStyleSheet(u"QLineEdit {background-color: #ebecf0; color: #282c33; border-radius: 5px; padding: 0px 8px 0px 8px}\n"
"QLineEdit:focus {background-color: #ffffff; border-color: #6badee; border-width: 1.5px; border-style: solid;; padding: 0px 6px 0px 6px}")
        self.lineEdit_title.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit_title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_date = QLabel(self.widget1)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font1)
        self.label_date.setStyleSheet(u"color: #282c33;")
        self.label_date.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_date)

        self.calendarWidget = QCalendarWidget(self.widget1)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setFont(font2)
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setFocusPolicy(Qt.TabFocus)
        self.calendarWidget.setStyleSheet(u"background-color: rgb(107, 173, 238);")
        self.calendarWidget.setGridVisible(False)

        self.verticalLayout_4.addWidget(self.calendarWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_time = QLabel(self.widget1)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font1)
        self.label_time.setStyleSheet(u"color: #282c33;")
        self.label_time.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_time)

        self.timeEdit = QTimeEdit(self.widget1)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans"])
        font3.setPointSize(16)
        self.timeEdit.setFont(font3)
        self.timeEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.timeEdit.setStyleSheet(u"QTimeEdit {background-color: #6badee; color: #ffffff; border-radius: 5px; padding: 0px 5px 0px 5px;}\n"
"QTimeEdit:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")
        self.timeEdit.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_2.addWidget(self.timeEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_description = QLabel(self.widget1)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: #282c33;")
        self.label_description.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_description)

        self.textEdit_description = QTextEdit(self.widget1)
        self.textEdit_description.setObjectName(u"textEdit_description")
        font4 = QFont()
        font4.setFamilies([u"Noto Sans"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.textEdit_description.setFont(font4)
        self.textEdit_description.setStyleSheet(u"QTextEdit {background-color: #ebecf0; color: #282c33; border-radius: 5px; padding: 4px 8px 4px 8px}\n"
"QTextEdit:focus {background-color: #ffffff; border-color: #6badee; border-width: 1.5px; border-style: solid;}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.textEdit_description.setFrameShape(QFrame.NoFrame)
        self.textEdit_description.setAutoFormatting(QTextEdit.AutoAll)
        self.textEdit_description.setTabChangesFocus(True)
        self.textEdit_description.setTabStopDistance(20.000000000000000)
        self.textEdit_description.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.textEdit_description)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_delete = QPushButton(self.widget1)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy1)
        self.btn_delete.setMinimumSize(QSize(140, 30))
        font5 = QFont()
        font5.setFamilies([u"Torus Pro"])
        font5.setPointSize(12)
        self.btn_delete.setFont(font5)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setFocusPolicy(Qt.TabFocus)
        self.btn_delete.setStyleSheet(u"QPushButton {background-color: #d63a3e; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #9e2a2a;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
        self.btn_cancel.setMinimumSize(QSize(100, 30))
        self.btn_cancel.setFont(font5)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancel.setFocusPolicy(Qt.TabFocus)
        self.btn_cancel.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(self.widget1)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(100, 30))
        self.btn_save.setFont(font5)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setFocusPolicy(Qt.TabFocus)
        self.btn_save.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.widget1)


        self.verticalLayout_3.addWidget(self.widget)

        CardWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_title, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.timeEdit)
        QWidget.setTabOrder(self.timeEdit, self.textEdit_description)
        QWidget.setTabOrder(self.textEdit_description, self.btn_delete)
        QWidget.setTabOrder(self.btn_delete, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_save)

        self.retranslateUi(CardWindow)

        QMetaObject.connectSlotsByName(CardWindow)
    # setupUi

    def retranslateUi(self, CardWindow):
        CardWindow.setWindowTitle(QCoreApplication.translate("CardWindow", u"Card Description", None))
        self.label_card_desc.setText(QCoreApplication.translate("CardWindow", u"Card Description", None))
        self.label_title.setText(QCoreApplication.translate("CardWindow", u"Title", None))
        self.lineEdit_title.setText("")
        self.lineEdit_title.setPlaceholderText(QCoreApplication.translate("CardWindow", u"Add a card title...", None))
        self.label_date.setText(QCoreApplication.translate("CardWindow", u"Date", None))
        self.label_time.setText(QCoreApplication.translate("CardWindow", u"Time", None))
        self.label_description.setText(QCoreApplication.translate("CardWindow", u"Description", None))
        self.textEdit_description.setHtml(QCoreApplication.translate("CardWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Torus Pro';\"><br /></p></body></html>", None))
        self.textEdit_description.setPlaceholderText(QCoreApplication.translate("CardWindow", u"Add a more detailed description...", None))
        self.btn_delete.setText(QCoreApplication.translate("CardWindow", u"Delete Card", None))
        self.btn_cancel.setText(QCoreApplication.translate("CardWindow", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("CardWindow", u"Save", None))
    # retranslateUi

