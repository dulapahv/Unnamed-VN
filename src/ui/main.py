import logging
from typing import Callable

# from PySide6.QtCore import QCoreApplication, QSize, Qt, Slot
# from PySide6.QtGui import (QCursor, QDragEnterEvent, QDragMoveEvent,
#                            QDropEvent, QFont, QKeyEvent)
# from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea,
#                                QApplication, QFrame, QLabel, QListWidget,
#                                QListWidgetItem, QMainWindow, QPushButton,
#                                QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from db import Database
from kanbaru_objects import Board, Card, List
from ui.app_settings import AppSettings
from ui.board_settings import BoardSettings
from ui.card_description import CardDescription
from ui.ui_main import Ui_MainWindow
from utils import setupFontDB
import datetime

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)

        parent.ui.btn_app_settings.clicked.connect(
            lambda: self.showAppSettings(parent))
        parent.ui.btn_board_settings.clicked.connect(
            lambda: self.showBoardSettings(parent))
        parent.ui.btn_add_board.clicked.connect(
            lambda: self.addBoard(parent))

        parent.ui.btn_app_settings.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.showAppSettings(parent))
        parent.ui.btn_board_settings.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.showBoardSettings(parent))
        parent.ui.btn_add_board.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.addBoard(parent))

        logging.info(
            f"Loaded {len(Database.getInstance().boards)} board(s) from database")

        # Create a new name for the listWidget
        # Set the new name as an attribute of the parent UI
        # Set the new name as the object name of the listWidget
        # Delete the old name from the parent UI
        # Create a new name for the listWidget
        # Set the new name as an attribute of the parent UI
        # Set the new name as the object name of the listWidget
        # Delete the old name from the parent UI
        parent.ui.qpushbutton = QPushButton()
        new_name = f"{parent.ui.qpushbutton.__class__.__name__}_{id(parent.ui.qpushbutton)}"
        setattr(parent.ui, new_name, parent.ui.qpushbutton)
        pushButton = getattr(parent.ui, new_name)
        pushButton.setObjectName(new_name)
        delattr(parent.ui, "qpushbutton")
        pushButton = self.boardFactory(
            parent, Database.getInstance().boards[0], "TorusPro.ttf")
        pushButton.clicked.connect(lambda: self.changeBoard(
            parent, Database.getInstance().boards[0]))
        parent.ui.verticalLayout_4.addWidget(pushButton)
        for board in Database.getInstance().boards[1:]:
            parent.ui.qpushbutton = QPushButton()
            new_name = f"{parent.ui.qpushbutton.__class__.__name__}_{id(parent.ui.qpushbutton)}"
            setattr(parent.ui, new_name, parent.ui.qpushbutton)
            pushButton = getattr(parent.ui, new_name)
            pushButton.setObjectName(new_name)
            delattr(parent.ui, "qpushbutton")
            pushButton = self.boardFactory(
                parent, board, "TorusPro.ttf", False)
            pushButton.clicked.connect(lambda: self.changeBoard(parent, board))
            parent.ui.verticalLayout_4.addWidget(pushButton)

        parent.ui.vertSpacer_scrollAreaContent = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        parent.ui.verticalLayout_4.addItem(
            parent.ui.vertSpacer_scrollAreaContent)

        self.addListButton(
            parent, Database.getInstance().boards[0], "TorusPro.ttf")

        parent.ui.label_board.setText(
            Database.getInstance().boards[0].title[:40] + (Database.getInstance().boards[0].title[40:] and '...'))

        self.setupFont(parent, "TorusPro.ttf")

    def boardFactory(self, parent: Ui_MainWindow, board: Board, font: str, isConstructed: bool = True) -> QPushButton:
        """Creates a board widget
        - Add a push button widget to the parent UI with specified style
        - If the board is displayed, construct the list widgets and card widgets

        Parameters
        ----------
        parent : QMainWindow
            The parent window
        board : Board
            The board object
        font : str
            The font to use
        isLoaded : bool, optional
            Load the board if True, by default True
        Returns
        -------
        QPushButton
            The board widget
        """
        logging.info(
            f'Loaded {len(board.lists)} list(s) from board "{board.title}" [{isConstructed = }]')

        parent.ui.label_board.setText(
            board.title[:40] + (board.title[40:] and '...'))

        parent.ui.btn_board = QPushButton(
            parent.ui.scrollAreaContent_panel_left)
        parent.ui.btn_board.setObjectName(u"btn_board")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            parent.ui.btn_board.sizePolicy().hasHeightForWidth())
        parent.ui.btn_board.setSizePolicy(sizePolicy)
        parent.ui.btn_board.setMinimumSize(QSize(0, 40))
        parent.ui.btn_board.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_board.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_board.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
                                          "QPushButton:hover {background-color: #7e828c;}\n"
                                          "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.btn_board.setText(
            board.title[:12] + (board.title[12:] and '...'))
        fontDB = setupFontDB(font)[0]
        parent.ui.btn_board.setFont(QFont(fontDB, 12))

        if isConstructed:
            for list in board.lists:
                qwidget = self.listFactory(parent, list, font)
                parent.ui.horizontalLayout_5.addWidget(qwidget)
        return parent.ui.btn_board

    def listFactory(self, parent: Ui_MainWindow, list: List, font: str) -> QWidget:
        """Creates a list widget
        - Add a list widget to the parent UI with specified style
        - Create a new name for the list with its class name and id
        - Set the new name as an attribute of the parent UI and as the
          object name of the list
        - Delete the old name attribute from the parent UI
        - Set the list data attribute as the List class object

        Parameters
        ----------
        parent : QMainWindow
            The parent window
        list : List
            The list object
        font : str
            The font to use

        Returns
        -------
        QWidget
            The list widget
        """
        logging.info(
            f'Loaded {len(list.cards)} card(s) from list "{list.title}"')

        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        parent.ui.list = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.list.setObjectName(u"list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            parent.ui.list.sizePolicy().hasHeightForWidth())
        parent.ui.list.setSizePolicy(sizePolicy2)
        parent.ui.list.setMinimumSize(QSize(250, 0))
        parent.ui.list.setStyleSheet(u"")
        parent.ui.verticalLayout_1 = QVBoxLayout(parent.ui.list)
        parent.ui.verticalLayout_1.setSpacing(0)
        parent.ui.verticalLayout_1.setObjectName(u"verticalLayout_1")
        parent.ui.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        parent.ui.widget = QWidget(parent.ui.list)
        parent.ui.widget.setObjectName(u"widget_list_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            parent.ui.widget.sizePolicy().hasHeightForWidth())
        parent.ui.widget.setSizePolicy(sizePolicy3)
        parent.ui.widget.setStyleSheet(u"background-color: #ebecf0;\n"
                                       "border-radius: 10px;")
        parent.ui.verticalLayout_2 = QVBoxLayout(parent.ui.widget)
        parent.ui.verticalLayout_2.setObjectName(u"verticalLayout_11")
        parent.ui.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        parent.ui.label_list = QLabel(parent.ui.widget)
        parent.ui.label_list.setObjectName(u"label_list")
        sizePolicy1.setHeightForWidth(
            parent.ui.label_list.sizePolicy().hasHeightForWidth())
        parent.ui.label_list.setSizePolicy(sizePolicy1)
        parent.ui.label_list.setMinimumSize(QSize(0, 30))
        parent.ui.label_list.setStyleSheet(u"color: #282c33;\n"
                                           "background-color: #ebecf0;\n"
                                           "border-radius: 5px;\n"
                                           "padding: 5px 0px 0px 5px;")
        parent.ui.label_list.setMargin(0)

        parent.ui.verticalLayout_2.addWidget(parent.ui.label_list)

        parent.ui.listWidget = QListWidget(parent.ui.widget)

        parent.ui.listWidget.setObjectName(u"listWidget")
        sizePolicy2.setHeightForWidth(
            parent.ui.listWidget.sizePolicy().hasHeightForWidth())
        parent.ui.listWidget.setSizePolicy(sizePolicy2)
        parent.ui.listWidget.setMaximumSize(QSize(250, 16777215))
        parent.ui.listWidget.setFocusPolicy(Qt.TabFocus)
        parent.ui.listWidget.setAcceptDrops(True)
        parent.ui.listWidget.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
                                           "QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
                                           "QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
                                           "QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
                                           "QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                           "QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                                           ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                           "QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
                                           "QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        parent.ui.listWidget.setFrameShape(QFrame.NoFrame)
        parent.ui.listWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustIgnored)
        parent.ui.listWidget.setAutoScroll(True)
        parent.ui.listWidget.setDragEnabled(True)
        parent.ui.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        parent.ui.listWidget.setDefaultDropAction(Qt.MoveAction)
        parent.ui.listWidget.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        parent.ui.listWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget.setProperty("isWrapping", False)
        parent.ui.listWidget.setSpacing(5)
        parent.ui.listWidget.setUniformItemSizes(True)
        parent.ui.listWidget.setWordWrap(True)
        parent.ui.listWidget.setSelectionRectVisible(True)

        parent.ui.verticalLayout_2.addWidget(parent.ui.listWidget)

        parent.ui.widget_add_card = QWidget(parent.ui.widget)
        parent.ui.widget_add_card.setObjectName(u"widget_add_card")
        sizePolicy1.setHeightForWidth(
            parent.ui.widget_add_card.sizePolicy().hasHeightForWidth())
        parent.ui.widget_add_card.setSizePolicy(sizePolicy1)
        parent.ui.verticalLayout_3 = QVBoxLayout(parent.ui.widget_add_card)
        parent.ui.verticalLayout_3.setObjectName(u"verticalLayout_6")
        parent.ui.verticalLayout_3.setContentsMargins(6, 0, 6, 6)
        parent.ui.btn_add_card = QPushButton(parent.ui.widget_add_card)
        parent.ui.btn_add_card.setObjectName(u"btn_add_card_list_1")
        parent.ui.btn_add_card.setMinimumSize(QSize(0, 25))
        parent.ui.btn_add_card.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_card.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_card.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
                                             "QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
                                             "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.verticalLayout_3.addWidget(parent.ui.btn_add_card)

        parent.ui.verticalLayout_2.addWidget(parent.ui.widget_add_card)

        parent.ui.verticalLayout_1.addWidget(parent.ui.widget)

        parent.ui.listWidget.setSortingEnabled(False)

        fontDB = setupFontDB(font)
        parent.ui.label_list.setFont(QFont(fontDB[0], 12, QFont.Bold))
        parent.ui.btn_add_card.setFont(QFont(fontDB[0], 12))
        
        parent.ui.btn_add_card.clicked.connect(lambda: self.addCard(parent, list))

        new_name = f"{parent.ui.listWidget.__class__.__name__}_{id(parent.ui.listWidget)}"
        setattr(parent.ui, new_name, parent.ui.listWidget)
        listWidget = getattr(parent.ui, new_name)
        listWidget.setObjectName(new_name)
        delattr(parent.ui, "listWidget")
        setattr(listWidget, "data", list)
        listWidget.dragEnterEvent = self.dragEnterEvent
        listWidget.dragMoveEvent = self.dragMoveEvent
        listWidget.dropEvent = self.dropEvent
        for index, card in enumerate(list.cards):
            qlistwidgetitem = self.cardFactory(
                listWidget, parent, card, font, index)
            listWidget.addItem(qlistwidgetitem)
        listWidget.clicked.connect(
            lambda event: self.showCardDescription(event, listWidget))

        parent.ui.label_list.setText(
            QCoreApplication.translate("MainWindow", list.title[:25] + (list.title[25:] and '...'), None))
        parent.ui.btn_add_card.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a card", None))

        return parent.ui.list

    def cardFactory(self, qlistwidget: QListWidget, parent: Ui_MainWindow, card: Card, font: str, index: int) -> QListWidgetItem:
        """Create a card item at the given QListWidget index
        - Create a new name for the card with its class name and id
        - Set the new name as an attribute of the parent UI and as the
          object name of the card
        - Delete the old name attribute from the parent UI
        - Set the card flags
        - Set the card data as the Card class object

        Parameters
        ----------
        qlistwidget : QListWidget
            The QListWidget to add the card item to
        parent : Ui_MainWindow
            The parent UI
        card : Card
            The card to add to the list
        font : str
            The font to use
        index : int
            The index to add the card item to

        Returns
        -------
        QListWidgetItem
            The card item
        """
        parent.ui.qlistwidgetitem = QListWidgetItem(qlistwidget)
        new_name = f"{parent.ui.qlistwidgetitem.__class__.__name__}_{id(parent.ui.qlistwidgetitem)}"
        setattr(parent.ui, new_name, parent.ui.qlistwidgetitem)
        listWidgetItem = getattr(parent.ui, new_name)
        delattr(parent.ui, "qlistwidgetitem")
        listWidgetItem.setFlags(
            Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        listWidgetItem = qlistwidget.item(index)
        listWidgetItem.setData(Qt.UserRole, card)
        listWidgetItem.setText(
            QCoreApplication.translate("MainWindow", card.title[:24] + (card.title[24:] and '...'), None))
        fontDB = setupFontDB(font)[0]
        listWidgetItem.setFont(QFont(fontDB, 12))

        return listWidgetItem

    def addListButton(self, parent: Ui_MainWindow, board: Board, font: str) -> None:
        """Add a button to add a new list

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        font : str
            The font to use
        """
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        parent.ui.list_add = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.list_add.setObjectName(u"list_add")
        sizePolicy.setHeightForWidth(
            parent.ui.list_add.sizePolicy().hasHeightForWidth())
        parent.ui.list_add.setSizePolicy(sizePolicy)
        parent.ui.list_add.setMinimumSize(QSize(250, 0))
        parent.ui.verticalLayout_9 = QVBoxLayout(parent.ui.list_add)
        parent.ui.verticalLayout_9.setSpacing(0)
        parent.ui.verticalLayout_9.setObjectName(u"verticalLayout_9")
        parent.ui.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        parent.ui.btn_add_list = QPushButton(parent.ui.list_add)
        parent.ui.btn_add_list.setObjectName(u"btn_add_list")
        parent.ui.btn_add_list.setMinimumSize(QSize(0, 30))
        parent.ui.btn_add_list.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_list.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_list.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
                                             "QPushButton:hover {background-color: #7e828c;}\n"
                                             "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.verticalLayout_9.addWidget(parent.ui.btn_add_list)

        parent.ui.vertSpacer_list_add = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        parent.ui.verticalLayout_9.addItem(parent.ui.vertSpacer_list_add)
        parent.ui.btn_add_list.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a list", None))

        parent.ui.scrollAreaContent_panel_right.layout().addWidget(parent.ui.list_add)
        parent.ui.horzSpacer_panel_right = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        parent.ui.horizontalLayout_5.addItem(parent.ui.horzSpacer_panel_right)

        parent.ui.btn_add_list.clicked.connect(
            lambda: self.addList(parent, board))

        fontDB = setupFontDB(font)[0]
        parent.ui.btn_add_list.setFont(QFont(fontDB, 12))

    def showAppSettings(self, parent: Ui_MainWindow) -> None:
        """Show the application settings window

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        """
        self.appSettings = AppSettings(parent)
        self.appSettings.setWindowModality(Qt.ApplicationModal)
        self.appSettings.show()

    def showBoardSettings(self, parent: Ui_MainWindow) -> None:
        """Show the board settings window

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        """
        self.boardSettings = BoardSettings()
        self.boardSettings.setWindowModality(Qt.ApplicationModal)
        self.boardSettings.show()

    def showCardDescription(self, event, parent: QListWidget) -> None:
        """Show the card description window

        Parameters
        ----------
        event : QMouseEvent
            The mouse event
        parent : QListWidget
            The parent QListWidget
        """
        card = parent.item(event.row()).data(Qt.UserRole)
        self.cardDescription = CardDescription(card)
        self.cardDescription.setWindowModality(Qt.ApplicationModal)
        self.cardDescription.show()

    def addBoard(self, parent: Ui_MainWindow) -> None:
        """Add a new board"""
        ...

    def addList(self, parent: Ui_MainWindow, board: Board) -> None:
        """Add a new list

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        board : Board
            The board to add the list to
        """
        text, ok = QInputDialog().getText(
            parent, "New list", "Enter a title for the list")
        if ok and text != "":
            data = Database.getInstance().data
            for i in range(len(Database.getInstance().boards)):
                if Database.getInstance().boards[i].title == board.title:
                    data["_Database__data"][i]["_Board__lists"].append(
                        {"_List__title": text, "_List__cards": []})
                    Database.getInstance().data = data
                    Database.getInstance().write()
                    self.changeBoard(parent, Database.getInstance().boards[i])
            parent.ui.scrollArea_panel_right.horizontalScrollBar().setValue(
                parent.ui.scrollArea_panel_right.horizontalScrollBar().maximum())

    def addCard(self, parent: Ui_MainWindow, list: List) -> None:
        """Add a new card
        
        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        list : List
            The list to add the card to
        """
        text, ok = QInputDialog().getText(
            parent, "New card", "Enter a title for the card")
        if ok and text != "":
            data = Database.getInstance().data
            for i in range(len(Database.getInstance().boards)):
                for j in range(len(Database.getInstance().boards[i].lists)):
                    if Database.getInstance().boards[i].lists[j].title == list.title:
                        data["_Database__data"][i]["_Board__lists"][j]["_List__cards"].append(
                            {"_Card__title": text, "_Card__description": "", "_Card__date": datetime.date.today().strftime("%d-%m-%Y"), "_Card__time": datetime.datetime.now().strftime("%H:%M")})
                        Database.getInstance().data = data
                        Database.getInstance().write()
                        self.changeBoard(parent, Database.getInstance().boards[i])

    @Slot()
    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """Override the dragEnterEvent method to customize the drag enter event
        - Check if the clicked item has the qabstractitemmodeldatalist format
        - If it is, accept the event. If not, ignore the event

        Parameters
        ----------
        event : QDragEnterEvent
            The drag enter event
        """
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.accept()
        else:
            event.ignore()

    @Slot()
    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        """Override the dragMoveEvent method to customize the drag move event
        - Check if the dragged item has the qabstractitemmodeldatalist format
        - If it is, accept the event. If not, ignore the event

        Parameters
        ----------
        event : QDragMoveEvent
            The drag move event
        """
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.accept()
        else:
            event.ignore()

    @Slot()
    def dropEvent(self, event: QDropEvent) -> None:
        """Override the dropEvent method to customize the drop event
        - Check if the item to be dropped has the qabstractitemmodeldatalist format
        - Get the source widget
        - Get the current mouse position
        - Get the widget at the mouse position
        - Get the items that is being dragged
        - Remove those items from the source widget
        - Add those items to the destination widget

        Parameters
        ----------
        event : QDropEvent
            The drop event
        """
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            source_widget = event.source()
            mouse_position = QCursor().pos()
            dest_widget = QApplication.widgetAt(mouse_position).parent()
            items = source_widget.selectedItems()
            if source_widget == dest_widget:
                return None
                # TODO: Implement rearranging items within the same list (and other lists)
            else:
                for item in items:
                    source_widget.takeItem(source_widget.row(item))
                    dest_widget.addItem(item)
                    dest_widget.setCurrentItem(item)
                    self.changeCard(source_widget, dest_widget,
                                    item.data(Qt.UserRole))
            logging.info(
                f'Moved {len(items)} Card(s) ({list(map(lambda item: getattr(item, "data")(Qt.UserRole).title, items))}) from list "{getattr(source_widget, "data").title}" to list "{getattr(dest_widget, "data").title}"')
            Database.getInstance().write()
            event.accept()
        else:
            event.ignore()

    def changeBoard(self, parent: Ui_MainWindow, board: Board) -> None:
        """Change the board to the specified board
        - Remove all widgets from the layout
        - Create the new board
        - Remove the add list button and horizontal spacer then add list button again

        Parameters
        ----------
        parent : Ui_MainWindow
            The parent widget
        board : Board
            The board to change to
        """
        layout = parent.ui.scrollAreaContent_panel_right.layout()
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
        self.boardFactory(parent, board, "TorusPro.ttf")
        parent.ui.list_add.setParent(None)
        parent.ui.horizontalLayout_5.removeItem(
            parent.ui.horzSpacer_panel_right)
        self.addListButton(parent, board, "TorusPro.ttf")

    def changeCard(self, source: List, destination: List, card: Card) -> None:
        """Change the card in a list to another list
        - Get the data from the database
        - Find the source list and the specified card
        - Find the destination list and add the card
        - Remove the card from the source list
        - Update the database

        Parameters
        ----------
        source : List
            The source list
        destination : List
            The destination list
        card : Card
            The card to move
        """
        data = Database.getInstance().data
        for i in range(len(data["_Database__data"][0]["_Board__lists"])):
            if data["_Database__data"][0]["_Board__lists"][i]["_List__title"] == getattr(source, "data").title:
                source_list = data["_Database__data"][0]["_Board__lists"][i]
                for j in range(len(source_list["_List__cards"])):
                    if source_list["_List__cards"][j]["_Card__title"] == card.title:
                        card_to_move = source_list["_List__cards"].pop(j)
                        break
        for i in range(len(data["_Database__data"][0]["_Board__lists"])):
            if data["_Database__data"][0]["_Board__lists"][i]["_List__title"] == getattr(destination, "data").title:
                dest_list = data["_Database__data"][0]["_Board__lists"][i]
                dest_list["_List__cards"].append(card_to_move)
                break
        Database.getInstance().data = data

    def setupFont(self, parent: Ui_MainWindow, font: str | list[str]) -> None:
        toruspro = setupFontDB(font)[0]
        parent.ui.label_logo.setFont(QFont(toruspro, 36))
        parent.ui.label_board.setFont(QFont(toruspro, 28))
        parent.ui.btn_add_board.setFont(QFont(toruspro, 12))
        parent.ui.btn_board_settings.setFont(QFont(toruspro, 12))
        parent.ui.btn_app_settings.setFont(QFont(toruspro, 12))

    def keyPressEvent(self, event: QKeyEvent, parent: Ui_MainWindow = None, function: Callable = None) -> None | Callable:
        """This function is used to call a function when the enter key is pressed

        Parameters
        ----------
        event : QKeyEvent
            The key event
        function : Callable
            The function to call
        parent : Ui_MainWindow, optional
            The parent window, by default None
        """
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if not function:
                return None
            if not parent:
                return function()
            return function(parent)
