import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QCalendarWidget, QTableWidget, QTableWidgetItem, QPushButton, QTextEdit, QCheckBox, QLineEdit, QTableView
from PyQt5.QtCore import QDate, QAbstractTableModel, Qt
from PyQt5 import QtGui, QtWidgets
from campsite import Campsite
from pandasModel import pandasModel

camp = Campsite("Charleston Lake")
camp_df = camp.get_park_availability_test('2023-08-23')

class CampSiteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.day_mode = True
        width = 800
        self.window_height = 600
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setWindowTitle('Campsite Availability Checker')
        self.setWindowIcon(QtGui.QIcon('./img/icon.png'))        
            
        self.setStyleSheet(self.getStyleSheet(self.day_mode))

        self.modeButton = QPushButton('Switch to Night Mode' if self.day_mode else 'Switch to Day Mode')
        self.modeButton.clicked.connect(self.switchMode)
        
        self.emailNotificationBox = QCheckBox('Email notifications')
        self.soundAlertBox = QCheckBox('Sound alert on new availability')
        self.emailInputBox = QLineEdit()
        self.emailInputBox.setPlaceholderText('Enter your email')

        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.addWidget(self.modeButton)
        self.topLayout.addWidget(self.emailNotificationBox)
        self.topLayout.addWidget(self.soundAlertBox)
        self.topLayout.addWidget(self.emailInputBox)

        self.parkSelection = QComboBox()
        self.parkSelection.addItems(['Park 1', 'Park 2', 'Park 3', 'Park 4', 'Park 5'])

        self.datePicker = QCalendarWidget()

        self.grid = QTableWidget()
        self.grid.setColumnCount(7)
        self.grid.setHorizontalHeaderLabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
        self.grid.setRowCount(5)

        for i in range(5):
            self.grid.setVerticalHeaderItem(i, QTableWidgetItem(f'Site {i + 1}'))
            for j in range(7):
                date = QDate.currentDate().addDays(j)
                self.grid.setItem(i, j, QTableWidgetItem(f'Available on {date.toString()}'))

        self.logContainer = QTextEdit()
        self.logContainer.setReadOnly(True)
        self.logContainer.append("Last refreshed at: N/A")


        self.layout.addLayout(self.topLayout)
        self.layout.addWidget(QLabel('Select a Park'))
        self.layout.addWidget(self.parkSelection)
        self.layout.addWidget(QLabel('Select a Date'))
        self.layout.addWidget(self.datePicker)
        self.layout.addWidget(QLabel('Availability Grid'))
        self.layout.addWidget(self.grid)
        self.layout.addWidget(QLabel('Refresh Log'))
        self.layout.addWidget(self.logContainer)

        self.setLayout(self.layout)

    def switchMode(self):
        self.day_mode = not self.day_mode
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.initUI()
    
    def df_to_table(self, table, df):
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(df.columns)
        table.setVerticalHeaderLabels(df.index.map(str))
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))

    def getStyleSheet(self, day_mode=True):
        if day_mode:
            return """
                QWidget {
                    background-color: #F0F0F0;
                    color: #383838;
                    font-family: 'Arial';
                }
                QLabel {
                    font-size: 20px;
                    font-weight: bold;
                }
                QComboBox, QTableWidget, QPushButton, QTextEdit, QLineEdit {
                    font-size: 16px;
                    background-color: white;
                    border: 1px solid #B0B0B0;
                    border-radius: 5px;    /* Rounded corners */
                    padding: 10px;         /* Padding for comfort */
                }
                QCheckBox {
                    padding: 10px;
                    spacing: 20px;
                }
                QPushButton {
                    background-color: #008CBA;  /* A light blue color */
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #007B9A;  /* A darker blue on hover */
                }
                QCheckBox::indicator {
                    width: 13px;
                    height: 13px;
                }
                QCheckBox::indicator:unchecked {
                    image: url(/path/to/your/unchecked-box-icon.png);
                }
                QCheckBox::indicator:checked {
                    image: url(/path/to/your/checked-box-icon.png);
                }
            """
        else:
            return """
                QWidget {
                    background-color: #282C34;
                    color: #ABB2BF;
                    font-family: 'Arial';
                }
                QLabel {
                    font-size: 20px;
                    font-weight: bold;
                }
                QComboBox, QTableWidget, QPushButton, QTextEdit, QLineEdit {
                    font-size: 16px;
                    background-color: #3C4048;
                    border: 1px solid #282C34;
                    border-radius: 5px;    /* Rounded corners */
                    padding: 10px;         /* Padding for comfort */
                }
                QCheckBox {
                    padding: 10px;
                    spacing: 20px;
                }
                QPushButton {
                    background-color: #3C8CBA;  /* A light blue color */
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #3C7B9A;  /* A darker blue on hover */
                }
                QCheckBox::indicator {
                    width: 13px;
                    height: 13px;
                }
                QCheckBox::indicator:unchecked {
                    image: url(/path/to/your/unchecked-box-icon-dark.png);
                }
                QCheckBox::indicator:checked {
                    image: url(/path/to/your/checked-box-icon-dark.png);
                }
            """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CampSiteApp()
    window.show()
    window.setGeometry(300, 200, 600, 600)

    sys.exit(app.exec_())