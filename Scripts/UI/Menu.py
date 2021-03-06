from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class Menu(QtWidgets.QWidget):
    name = "Default"

    def __init__(self, parent):
        super(Menu, self).__init__(parent)
        self.parentMenu = parent

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        # super(Menu, self).__init__()

        # self.setStyleSheet("#MainWindow {background-image: url(Files/Images/Logo.png);}")

    def Update(self):
        pass

class DefaultButton(QtWidgets.QPushButton):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, text: str, func):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(x, y, w, h))
        self.setText(text)
        self.setObjectName(name)
        self.clicked.connect(func)
        self.setStyleSheet(StyleSheets.GenerateButtonStyleSheet(name, 20))


class DefaultParameter(QtWidgets.QWidget):
    def __init__(self, parent, name: str, x: int, y: int, w: int, h: int, text: str, offset: tuple = (10, 20), fontSize: int = 15, fontFamily: str = "Trench"):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(x, y, w, h))
        self.setObjectName(name)
        self.offset = offset

        self.label = QtWidgets.QLabel(self);
        self.label.setAttribute(QtCore.Qt.WA_StyledBackground, False)
        self.label.setStyleSheet(f"""
            color: rgb(255, 255, 255);
            background-color: rgba(255, 255, 128, 0);
            font-size: {fontSize}pt;
            font-family: {fontFamily};
        """)

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            #{self.objectName()} {{
                background-image: url(Files/Images/UI/Button_Empty.png);
                background-repeat: no-repeat;
            }}
        """)

    def SetText(self, text: str = "None"):
        self.label.clear()
        self.label.setText(text)
        self.label.adjustSize()
        self.label.move(self.offset[0], self.offset[1])


class Rect(QtWidgets.QWidget):
    def __init__(self, parent, x: int, y: int, w: int, h: int):
        super(Rect, self).__init__(parent)
        self.setGeometry(x, y, w, h);


class AnimationTextEdit(QtWidgets.QWidget):
    def __init__(self, parent, x: int, y: int, w: int, h: int, text: str, offset: tuple = (10, 6), pause: int = 50, speed: int = 2, fontSize: int = 15, fontFamily: str = "Trench"):
        super(AnimationTextEdit, self).__init__(parent)

        self.setGeometry(x, y, w, h);

        self.setObjectName("ScrollingText")

        self.rectLabel = Rect(self, 0 + offset[0], 0 + offset[1], w - offset[0] * 2, h - offset[1] * 2)

        self.label = QtWidgets.QLabel(self.rectLabel);
        self.label.setText(text)
        # self.label.adjustSize()

        self.label.setAttribute(QtCore.Qt.WA_StyledBackground, False)
        self.label.setStyleSheet(f"""
            color: rgb(255, 255, 255);
            background-color: rgba(255, 255, 128, 0);
            font-size: {fontSize}pt;
            font-family: {fontFamily};
        """)

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            #{self.objectName()} {{
                background-image: url(Files/Images/UI/InformationBar_5X1.png);
                background-repeat: no-repeat;
            }}
        """)

        self.pause, self.speed, self.offset = pause, speed, offset
        self.label.move(offset[0], offset[1])

        self.timer = QtCore.QTimer(self)
        self.timer.start(self.pause)
        self.timer.timeout.connect(lambda: self.Moving())

        self.SetText(text)

    def SetText(self, text: str = "None"):
        self.label.clear()
        self.label.setText(text)
        self.label.adjustSize()

    def Moving(self):
        if (self.label.x() >= 0 - self.label.width()):
            self.label.move(self.label.x() - self.speed, self.label.y())
        else: self.label.move(self.width(), self.label.y())


class FileSystemWatching(QtWidgets.QWidget):
    def __init__(self, parent, x: int, y: int, w: int, h: int, func, rootPath=QtCore.QDir.currentPath()):
        super().__init__(parent)

        self.setGeometry(x, y, w, h);

        self.fileSystem = QtWidgets.QFileSystemModel(self)
        self.fileSystem.setRootPath(QtCore.QDir.currentPath())

        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.fileSystem)
        self.tree.setRootIndex(self.fileSystem.index(rootPath))
        self.tree.move(200, 0)
        self.tree.setAnimated(False)
        self.tree.setIndentation(5)
        self.tree.setSortingEnabled(True)
        self.tree.setHeaderHidden(True)
        self.tree.setStyleSheet("""
            color: white;
            background-color: black;
        """)

        self.windowLayout = QtWidgets.QVBoxLayout()
        self.windowLayout.addWidget(self.tree)
        self.setLayout(self.windowLayout)

        self.tree.doubleClicked.connect(func)


class StaticText(QtWidgets.QWidget):
    def __init__(self, parent, x: int, y: int, w: int, h: int, text: str, offset: tuple = (20, 14), fontSize: int = 15, fontFamily: str = "Trench"):
        super(StaticText, self).__init__(parent)

        self.setGeometry(x, y, w, h);

        self.setObjectName("StaticText")

        self.rectLabel = Rect(self, 0 + offset[0], 0 + offset[1], w - offset[0] * 2, h - offset[1] * 2)

        self.label = QtWidgets.QLabel(self);
        self.label.setText(text)
        self.label.adjustSize()

        self.label.setAttribute(QtCore.Qt.WA_StyledBackground, False)
        self.label.setStyleSheet(f"""
            color: rgb(255, 255, 255);
            background-color: rgba(255, 255, 128, 0);
            font-size: {fontSize}pt;
            font-family: {fontFamily};
        """)

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            #{self.objectName()} {{
                background-image: url(Files/Images/UI/InformationBar_5X1.png);
                background-repeat: no-repeat;
            }}
        """)

        self.offset = offset
        self.label.move(offset[0], offset[1])

    def SetText(self, text: str = "None"):
        self.label.clear()
        self.label.setText(text)
        self.label.adjustSize()
        self.label.move(self.offset[0], self.offset[1])

class ListWidget(QtWidgets.QWidget):
    def __init__(self, parent, name, x: int, y: int, w: int, h: int, func, fontSize: int = 15, fontFamily: str = "Trench"):
        super(ListWidget, self).__init__(parent)

        self.setGeometry(x, y, w, h);
        self.setObjectName(name)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.listView = QtWidgets.QListView(self)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.doubleClicked.connect(func)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.SetItems(["Empty"])

        self.listView.setStyleSheet(f"""
            color: rgb(255, 255, 255);
            background-color: rgba(255, 255, 128, 0);
            font-size: {fontSize}pt;
            font-family: {fontFamily};
        """)

        self.gridLayout.addWidget(self.listView, 1, 0, 1, 2)

    def SetItems(self, items):
        self.model.clear()

        for i in items:
            item = QtGui.QStandardItem(i)
            self.model.appendRow(item)


class TextEdit(QtWidgets.QWidget):
    def __init__(self, parent, x: int, y: int, w: int, h: int, placeHolderText: str, defaultText: str = "", offset: tuple = (5, 5), fontSize: int = 15, fontFamily: str = "Trench"):
        super(TextEdit, self).__init__(parent)

        self.setGeometry(x, y, w, h);

        self.setObjectName("TextEdit")

        self.rectLabel = Rect(self, 0 + offset[0], 0 + offset[1], w - offset[0] * 2, h - offset[1] * 2)

        self.label = QtWidgets.QLineEdit(self.rectLabel);
        self.label.setGeometry(0 + offset[0], 0 + offset[1], w - offset[0] * 2 - 10, h - offset[1] * 2 - 15)

        self.label.setPlaceholderText(placeHolderText)
        self.label.setText(defaultText)

        # self.label.setGeometry()

        self.label.setAttribute(QtCore.Qt.WA_StyledBackground, False)
        self.label.setStyleSheet(f"""
            color: rgb(255, 255, 255);
            background-color: rgba(255, 255, 128, 0);
            border: none;
            font-size: {fontSize}pt;
            font-family: {fontFamily};
        """)

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            #{self.objectName()} {{
                background-image: url(Files/Images/UI/InformationBar_5X1.png);
                background-repeat: no-repeat;
            }}
        """)

        self.offset = offset
        self.label.move(offset[0], offset[1])