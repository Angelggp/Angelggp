# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\angel\Desktop\Crud DB\GUI Crud Ok\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/*background-color: rgb(255, 255, 255);*/\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fr_contenedor = QtWidgets.QFrame(self.centralwidget)
        self.fr_contenedor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fr_contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_contenedor.setObjectName("fr_contenedor")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fr_contenedor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_superior = QtWidgets.QFrame(self.fr_contenedor)
        self.fr_superior.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_superior.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_superior.setStyleSheet("*{background-color:#DEC085 ;}   /*#f39c12*/\n"
"\n"
"/* Estilo para el botón de cerrar */\n"
"#bt_cerrar {\n"
"    padding: 10px;\n"
"    background-color: #e74c3c; /* Color rojo */\n"
"    border: 2px solid #c0392b; /* Borde rojo oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px;\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón de minimizar */\n"
"#bt_minimizar {\n"
"    padding: 10px;\n"
"    background-color: #3498db; /* Color azul */\n"
"    border: 2px solid #2980b9; /* Borde azul oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px;\n"
"    margin-right: 2.5px;\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón de maximizar */\n"
"#bt_maximizar {\n"
"    padding: 10px;\n"
"    background-color: #3498db; /* Color azul */\n"
"    border: 2px solid #2980b9; /* Borde azul oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px; /* Margen en la parte inferior */\n"
"    margin-right: 2.5px;\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Efecto hover para todos los botones */\n"
"#bt_cerrar:hover,\n"
"#bt_minimizar:hover,\n"
"#bt_maximizar:hover {\n"
"    background-color: #c0392b; /* Cambio de color de fondo al pasar el mouse para el botón de cerrar */\n"
"}\n"
"\n"
"#bt_minimizar:hover,\n"
"#bt_maximizar:hover {\n"
"    background-color: #2980b9; /* Cambio de color de fondo al pasar el mouse para los botones de minimizar y maximizar */\n"
"}\n"
"\n"
"\n"
"")
        self.fr_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_superior.setObjectName("fr_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_superior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.fr_superior)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_minimizar = QtWidgets.QPushButton(self.fr_superior)
        self.bt_minimizar.setMinimumSize(QtCore.QSize(40, 0))
        self.bt_minimizar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon)
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout_2.addWidget(self.bt_minimizar)
        self.bt_maximizar = QtWidgets.QPushButton(self.fr_superior)
        self.bt_maximizar.setMinimumSize(QtCore.QSize(40, 0))
        self.bt_maximizar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_maximizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_maximizar.setIcon(icon1)
        self.bt_maximizar.setObjectName("bt_maximizar")
        self.horizontalLayout_2.addWidget(self.bt_maximizar)
        self.bt_cerrar = QtWidgets.QPushButton(self.fr_superior)
        self.bt_cerrar.setMinimumSize(QtCore.QSize(40, 0))
        self.bt_cerrar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_cerrar.setStyleSheet("bt_cerrar {\n"
"    padding: 10px;\n"
"    background-color: #e74c3c; /* Color rojo */\n"
"    border: 2px solid #c0392b; /* Borde rojo oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px;\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}")
        self.bt_cerrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon2)
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout_2.addWidget(self.bt_cerrar)
        self.verticalLayout.addWidget(self.fr_superior)
        self.fr_main = QtWidgets.QFrame(self.fr_contenedor)
        self.fr_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_main.setObjectName("fr_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_main)
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_menu_titulo = QtWidgets.QFrame(self.fr_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.fr_menu_titulo.sizePolicy().hasHeightForWidth())
        self.fr_menu_titulo.setSizePolicy(sizePolicy)
        self.fr_menu_titulo.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_menu_titulo.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fr_menu_titulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_menu_titulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_menu_titulo.setObjectName("fr_menu_titulo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fr_menu_titulo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_menu = QtWidgets.QPushButton(self.fr_menu_titulo)
        self.bt_menu.setMinimumSize(QtCore.QSize(275, 40))
        self.bt_menu.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon3)
        self.bt_menu.setIconSize(QtCore.QSize(40, 40))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout_4.addWidget(self.bt_menu)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.fr_menu_titulo)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.fr_menu_titulo)
        self.frame_2 = QtWidgets.QFrame(self.fr_main)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fr_menu = QtWidgets.QFrame(self.frame_2)
        self.fr_menu.setMinimumSize(QtCore.QSize(300, 0))
        self.fr_menu.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fr_menu.setStyleSheet("QPushButton{\n"
"    padding: 10px;\n"
"    background-color: #DEC085;\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: white; /* Fondo gris claro cuando el mouse está sobre el botón */\n"
"    color: black; /* Texto en color negro cuando el mouse está sobre el botón */\n"
"}\n"
"\n"
"#fr_menu {\n"
"    background-color: ;\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 20px;\n"
"    margin-right: 5px;\n"
"}")
        self.fr_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_menu.setObjectName("fr_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_exposicion = QtWidgets.QPushButton(self.fr_menu)
        self.bt_exposicion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_exposicion.setCheckable(False)
        self.bt_exposicion.setAutoRepeat(False)
        self.bt_exposicion.setObjectName("bt_exposicion")
        self.verticalLayout_3.addWidget(self.bt_exposicion)
        self.bt_obra = QtWidgets.QPushButton(self.fr_menu)
        self.bt_obra.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_obra.setCheckable(False)
        self.bt_obra.setAutoRepeat(False)
        self.bt_obra.setObjectName("bt_obra")
        self.verticalLayout_3.addWidget(self.bt_obra)
        self.bt_artista = QtWidgets.QPushButton(self.fr_menu)
        self.bt_artista.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_artista.setCheckable(False)
        self.bt_artista.setAutoRepeat(False)
        self.bt_artista.setObjectName("bt_artista")
        self.verticalLayout_3.addWidget(self.bt_artista)
        self.bt_telefono = QtWidgets.QPushButton(self.fr_menu)
        self.bt_telefono.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_telefono.setCheckable(False)
        self.bt_telefono.setAutoRepeat(False)
        self.bt_telefono.setObjectName("bt_telefono")
        self.verticalLayout_3.addWidget(self.bt_telefono)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.bt_acerca_de = QtWidgets.QPushButton(self.fr_menu)
        self.bt_acerca_de.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_acerca_de.setCheckable(False)
        self.bt_acerca_de.setAutoRepeat(False)
        self.bt_acerca_de.setObjectName("bt_acerca_de")
        self.verticalLayout_3.addWidget(self.bt_acerca_de)
        self.horizontalLayout_3.addWidget(self.fr_menu)
        self.fr_tablas = QtWidgets.QFrame(self.frame_2)
        self.fr_tablas.setStyleSheet("#fr_tablas {\n"
"    background-color: ;\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 20px;\n"
"    margin-right: 5px;\n"
"}")
        self.fr_tablas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_tablas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_tablas.setObjectName("fr_tablas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fr_tablas)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.fr_tablas)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_acerca_de = QtWidgets.QWidget()
        self.page_acerca_de.setObjectName("page_acerca_de")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_acerca_de)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text_acerca_de = QtWidgets.QTextBrowser(self.page_acerca_de)
        self.text_acerca_de.setObjectName("text_acerca_de")
        self.verticalLayout_6.addWidget(self.text_acerca_de)
        self.stackedWidget.addWidget(self.page_acerca_de)
        self.page_tb = QtWidgets.QWidget()
        self.page_tb.setObjectName("page_tb")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_tb)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fr_nombre_tb = QtWidgets.QFrame(self.page_tb)
        self.fr_nombre_tb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_nombre_tb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_nombre_tb.setObjectName("fr_nombre_tb")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fr_nombre_tb)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_tabla = QtWidgets.QLabel(self.fr_nombre_tb)
        self.lb_tabla.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_tabla.setFont(font)
        self.lb_tabla.setObjectName("lb_tabla")
        self.horizontalLayout_5.addWidget(self.lb_tabla)
        self.lb_nombre_tb = QtWidgets.QLabel(self.fr_nombre_tb)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lb_nombre_tb.setFont(font)
        self.lb_nombre_tb.setText("")
        self.lb_nombre_tb.setObjectName("lb_nombre_tb")
        self.horizontalLayout_5.addWidget(self.lb_nombre_tb)
        self.verticalLayout_5.addWidget(self.fr_nombre_tb)
        self.tb_main = QtWidgets.QTableWidget(self.page_tb)
        self.tb_main.setObjectName("tb_main")
        self.tb_main.setColumnCount(6)
        self.tb_main.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_main.setHorizontalHeaderItem(5, item)
        self.verticalLayout_5.addWidget(self.tb_main)
        self.stackedWidget.addWidget(self.page_tb)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.fr_crud = QtWidgets.QFrame(self.fr_tablas)
        self.fr_crud.setMinimumSize(QtCore.QSize(0, 100))
        self.fr_crud.setMaximumSize(QtCore.QSize(16777215, 100))
        self.fr_crud.setStyleSheet("/* Estilo para el botón Agregar */\n"
"#bt_agregar {\n"
"    padding: 15px 30px;\n"
"    background-color: #2ecc71; /* Color verde */\n"
"    border: 2px solid #27ae60; /* Borde verde oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px; /* Margen en la parte inferior */\n"
"    margin-right: 5px; /* Margen en la parte derecha */\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Editar */\n"
"#bt_editar {\n"
"    padding: 15px 30px;\n"
"    background-color: #3498db; /* Color azul */\n"
"    border: 2px solid #2980b9; /* Borde azul oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px; /* Margen en la parte inferior */\n"
"    margin-right: 5px; /* Margen en la parte derecha */\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Eliminar */\n"
"#bt_eliminar {\n"
"    padding: 15px 30px;\n"
"    background-color: #e74c3c; /* Color rojo */\n"
"    border: 2px solid #c0392b; /* Borde rojo oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px; /* Margen en la parte inferior */\n"
"    margin-right: 10px; /* Margen en la parte derecha */\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Actualizar */\n"
"#bt_actualizar {\n"
"    padding: 15px 30px;\n"
"    background-color: #f39c12; /* Color naranja */\n"
"    border: 2px solid #27ae60; /* Borde verde oscuro */\n"
"    border-radius: 10px;\n"
"    margin-bottom: 10px; /* Margen en la parte inferior */\n"
"    margin-right: 10px; /* Margen en la parte derecha */\n"
"    color: #fff; /* Color del texto */\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s; /* Transición de color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"#bt_agregar {\n"
"    background-color: #2ecc71; /* Color verde */\n"
"}\n"
"\n"
"/* Efecto hover para el botón Agregar */\n"
"#bt_agregar:hover {\n"
"    background-color: #27ae60; /* Cambio de color de fondo al pasar el mouse */\n"
"    transform: scale(1.1); /* Escala del botón al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Editar */\n"
"#bt_editar {\n"
"    background-color: #3498db; /* Color azul */\n"
"}\n"
"\n"
"/* Efecto hover para el botón Editar */\n"
"#bt_editar:hover {\n"
"    background-color: #2980b9; /* Cambio de color de fondo al pasar el mouse */\n"
"    transform: scale(1.1); /* Escala del botón al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Eliminar */\n"
"#bt_eliminar {\n"
"    background-color: #e74c3c; /* Color rojo */\n"
"}\n"
"\n"
"/* Efecto hover para el botón Eliminar */\n"
"#bt_eliminar:hover {\n"
"    background-color: #c0392b; /* Cambio de color de fondo al pasar el mouse */\n"
"    transform: scale(1.1); /* Escala del botón al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilo para el botón Actualizar */\n"
"#bt_actualizar {\n"
"    background-color: #2ecc71; /* Color naranja */\n"
"}\n"
"\n"
"/* Efecto hover para el botón Actualizar */\n"
"#bt_actualizar:hover {\n"
"    background-color:#27ae60; /* Cambio de color de fondo al pasar el mouse */\n"
"    transform: scale(1.1); /* Escala del botón al pasar el mouse */\n"
"}\n"
"")
        self.fr_crud.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_crud.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_crud.setObjectName("fr_crud")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fr_crud)
        self.horizontalLayout_6.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_agregar = QtWidgets.QPushButton(self.fr_crud)
        self.bt_agregar.setObjectName("bt_agregar")
        self.horizontalLayout_6.addWidget(self.bt_agregar)
        self.bt_editar = QtWidgets.QPushButton(self.fr_crud)
        self.bt_editar.setObjectName("bt_editar")
        self.horizontalLayout_6.addWidget(self.bt_editar)
        self.bt_eliminar = QtWidgets.QPushButton(self.fr_crud)
        self.bt_eliminar.setObjectName("bt_eliminar")
        self.horizontalLayout_6.addWidget(self.bt_eliminar)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.bt_actualizar = QtWidgets.QPushButton(self.fr_crud)
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.horizontalLayout_6.addWidget(self.bt_actualizar)
        self.verticalLayout_4.addWidget(self.fr_crud)
        self.horizontalLayout_3.addWidget(self.fr_tablas)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.fr_main)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.fr_contenedor)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  Galería bd"))
        self.label_2.setText(_translate("MainWindow", "Base de Datos"))
        self.bt_exposicion.setText(_translate("MainWindow", "Exposicion"))
        self.bt_obra.setText(_translate("MainWindow", "Obra"))
        self.bt_artista.setText(_translate("MainWindow", "Artista"))
        self.bt_telefono.setText(_translate("MainWindow", "Telefono"))
        self.bt_acerca_de.setText(_translate("MainWindow", "Acerca de..."))
        self.text_acerca_de.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Acerca de la aplicación:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Desarrolladores: Angel Gabriel Garcia Plutin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                Javier Alexey Molina Cardoso</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Descripción:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sistema de información para galería de arte que proporciona acceso actualizado a exposiciones, incluyendo detalles como título, descripción, fechas de inauguración y clausura. La aplicación muestra obras de arte con información detallada como título, artista, estilo y precio de salida. Permite a los usuarios realizar ofertas por obras, y al finalizar la exposición, el propietario puede vender la obra al mejor postor. Desarrollado en Python con sqlite3 para gestionar la base de datos. Utiliza Visual Studio Code 1.81.0 como entorno de desarrollo y DB Browser SQLite 3.12.2 para explorar y administrar eficientemente la base de datos. Se basa en un Modelo Entidad Relación (MER) y un modelo relacional para implementar el sistema de información de la galería de arte.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Versión: 1.0</span></p></body></html>"))
        self.lb_tabla.setText(_translate("MainWindow", "Tabla:"))
        item = self.tb_main.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tb_main.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tb_main.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tb_main.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tb_main.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tb_main.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        self.bt_agregar.setText(_translate("MainWindow", "Agregar"))
        self.bt_editar.setText(_translate("MainWindow", "Editar"))
        self.bt_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.bt_actualizar.setText(_translate("MainWindow", "Actualizar"))
import icons_rc
