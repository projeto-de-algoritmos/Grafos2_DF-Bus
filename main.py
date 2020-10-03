from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtlet import L, MapWidget, leaflet
from graph import Graph
import sys
import requests

class Ui_MainWindow(object):
    tableWidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mapLayout = QtWidgets.QVBoxLayout()
        self.mapLayout.setObjectName("mapLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mapLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.mapLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.source_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.source_ComboBox.setFont(font)
        self.source_ComboBox.setObjectName("source_ComboBox")
        self.source_ComboBox.currentTextChanged.connect(self.enable_DestinyComboBox)
        self.source_ComboBox.currentTextChanged.connect(self.enable_SearchButton)
        self.verticalLayout.addWidget(self.source_ComboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.destiny_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.destiny_ComboBox.setFont(font)
        self.destiny_ComboBox.setObjectName("destiny_ComboBox")
        self.destiny_ComboBox.currentTextChanged.connect(self.enable_SearchButton)
        self.destiny_ComboBox.setEnabled(False)
        self.verticalLayout.addWidget(self.destiny_ComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tableLayout = QtWidgets.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.verticalLayout.addLayout(self.tableLayout)
        self.totalLayout = QtWidgets.QHBoxLayout()
        self.totalLayout.setObjectName("totalLayout")
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_label.setFont(font)
        self.total_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_label.setObjectName("total_label")
        self.totalLayout.addWidget(self.total_label)
        self.value_fare = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.value_fare.setFont(font)
        self.value_fare.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.value_fare.setObjectName("value_fare")
        self.totalLayout.addWidget(self.value_fare)
        self.verticalLayout.addLayout(self.totalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.add_map()
        self.total_label.setHidden(True)
        self.value_fare.setHidden(True)
        self.graph = Graph()
        self.loadComboBox(self.source_ComboBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ônibus do Distrito Federal"))
        self.label.setText(_translate("MainWindow", "Origem"))
        self.label_2.setText(_translate("MainWindow", "Destino"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.total_label.setText(_translate("MainWindow", "Total:"))
        self.value_fare.setText(_translate("MainWindow", "xx"))

    def loadComboBox(self, comboBox, removed_city=None):
        comboBox.addItem(None)
        for city in self.graph.adjacency_list.keys():
            if city != removed_city:
                comboBox.addItem(city)

    def enable_DestinyComboBox(self):
        if len(self.source_ComboBox.currentText()) != 0:
            self.destiny_ComboBox.setEnabled(True)
            self.destiny_ComboBox.clear()
            self.loadComboBox(self.destiny_ComboBox, self.source_ComboBox.currentText())
        else:
            self.destiny_ComboBox.setEnabled(False)

    def enable_SearchButton(self):
        if len(self.source_ComboBox.currentText()) != 0 and len(self.destiny_ComboBox.currentText()) != 0:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
            

    def get_lat_long(self, path):
        list_lat_long = []

        url = 'https://nominatim.openstreetmap.org/search?format=json&limit=3&q={}, Federal District'

        for city in path:
            if city == 'Plano Piloto':
                list_lat_long.append([-15.79398797, -47.88279533])
            elif city == 'Sudoeste':
                list_lat_long.append([-15.80030603, -47.92438030])
            else:
                r = requests.get(url.format(city))
                list_lat_long.append([float(r.json()[0]['lat']), float(r.json()[0]['lon'])])

        return list_lat_long

    def add_marker(self, lat_long, city):
        marker = L.marker(lat_long)
        marker.bindPopup(city)
        self.map.addLayer(marker)

    def add_map(self):
        self.mapWidget = MapWidget()
        self.mapLayout.addWidget(self.mapWidget)

        self.map = L.map(self.mapWidget)
        self.map.setView([-15.84972874, -47.93128967], 11)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)

    def search(self):
        path, trip_fare = self.graph.get_path(self.source_ComboBox.currentText(), self.destiny_ComboBox.currentText())

        list_lat_long = self.get_lat_long(path)
        for i in range(3):
            for layer in self.map.layers:
                if leaflet.layer.tile.tilelayer.TileLayer != type(layer):
                    self.map.removeLayer(layer)

        for i in range(len(path)):
            self.add_marker(list_lat_long[i], path[i])

        # L.polyline(list_lat_long).addTo(self.map)

        self.total_label.setHidden(False)
        self.value_fare.setHidden(False)
        self.create_table(trip_fare)

    def create_table(self, trip_fare):
        tableWidget = QtWidgets.QTableWidget()
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)     

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tableWidget.sizePolicy().hasHeightForWidth())

        tableWidget.setSizePolicy(sizePolicy)
        tableWidget.setRowCount(len(trip_fare.keys()))
        tableWidget.setColumnCount(3)
        tableWidget.setBaseSize(QtCore.QSize(0, 350))

        header = tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Origem'))
        tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Destino'))
        tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Valor da passagem'))

        total = 0

        for i,city in enumerate(trip_fare.keys()):
            tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(list(trip_fare)[i]))
            tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(trip_fare[city][0]))

            total = total + trip_fare[city][1]
            item = QtWidgets.QTableWidgetItem('R$ {:.2f}'.format(trip_fare[city][1]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            tableWidget.setItem(i, 2, item)

        self.value_fare.setText('R$ {:.2f}'.format(total))

        if self.tableWidget is None:
            self.tableLayout.addWidget(tableWidget)
        else:
            self.tableLayout.replaceWidget(self.tableWidget, tableWidget)
        self.tableWidget = tableWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
