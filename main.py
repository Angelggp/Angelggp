from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
import icons_rc
import sys
from  proyectoGaleríaOK.connSql import Galeria
from secundaria import Secundaria

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz.ui', self)
        # pagina que se muestra por defecto
        self.stackedWidget.setCurrentIndex(1)
        self.bd = Galeria()
     
     # eliminar la barra de titulo que viene por defecto en Qt
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # determinar el tamaño del QSizeGrip
        self.size = 15
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.size, self.size)

        # botones de la barra de titulo
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.bt_minimizar.clicked.connect(self.minimizar)
        self.bt_maximizar.clicked.connect(self.maximizar)

        # botones del menu 
        self.bt_exposicion.clicked.connect(lambda: self.visualizar_tabla("Exposición"))
        self.bt_obra.clicked.connect(lambda: self.visualizar_tabla("Obra"))
        self.bt_artista.clicked.connect(lambda: self.visualizar_tabla("Artista"))
        self.bt_telefono.clicked.connect(lambda: self.visualizar_tabla("Teléfono"))
        self.bt_acerca_de.clicked.connect(self.pag_acerca_de)
        self.bt_tablas.clicked.connect(self.pag_tablas)

        # botones crud
        self.bt_agregar.clicked.connect(lambda: Secundaria().show())

        # mover ventana
        self.fr_superior.mouseMoveEvent=self.mover_ventana

    def minimizar(self):
        self.showMinimized()

    def maximizar(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    # ubica el la opcion de redimensionar a la derecha y abajo
    def resizeEvent(self, event):
        self.grip.move(self.rect().right() - self.size, self.rect().bottom() - self.size) 
        

    
    # Capturar clic del mouse para recordar la posición al arrastrar
    def mousePressEvent(self, event):
        self.position = event.globalPos()
    
    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.position)
                self.position = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            self.showMaximized()
        else:
            self.showNormal()
        
    # Cambiar a la página Acerca de al hacer clic en el botón
    def pag_acerca_de(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def pag_tablas(self):
        self.stackedWidget.setCurrentIndex(1)


    def visualizar_tabla(self, nombre_tabla):
        self.lb_nombre_tb.setText(nombre_tabla)
        result = self.bd.mostrar_tabla(nombre_tabla)
        #print(result)
        
        if result is None:
            # Manejar el caso en que mostrar_tabla devuelve None
            raise ValueError(f"Error al obtener datos de la tabla {nombre_tabla}")

        encabezados, datos = result

        # Configurar la tabla
        self.tb_main.clear()
        self.tb_main.setRowCount(len(datos))
        self.tb_main.setColumnCount(len(encabezados))
        self.tb_main.setHorizontalHeaderLabels(encabezados)

        # Llenar la tabla con los datos
        contador = 0
        for i in datos:
            for j in range(len(i)):
                self.tb_main.setItem(contador, j, QtWidgets.QTableWidgetItem(str(i[j]))) 
            contador += 1
        self.tb_main.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.deshabilitar_edicion(self.tb_main)



    def deshabilitar_edicion(self, tabla):
        # Verificar si el argumento es una instancia de QTableWidget
        if not isinstance(tabla, QtWidgets.QTableWidget):
            raise TypeError("El argumento debe ser un objeto QTableWidget")

        # Definir la bandera que desactiva la edición
        flags = QtCore.Qt.ItemFlags(~QtCore.Qt.ItemIsEditable)

        # Iterar sobre todas las celdas de la tabla
        for row in range(tabla.rowCount()):
            for colum in range(tabla.columnCount()):
                # Obtener el objeto QTableWidgetItem en la celda actual
                item = tabla.item(row, colum)

                # Verificar si la celda contiene un objeto QTableWidgetItem
                if item is not None:
                    # Establecer las flags para desactivar la edición
                    item.setFlags(flags)


    
    def editar_item(self):
        pass

    def eliminar_item(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    ventana = Principal()
    ventana.show()
    sys.exit(app.exec_())

