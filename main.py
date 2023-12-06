from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import icons_rc
import sys
from  proyectoGaleríaOK.connSql import Galeria
from secundaria import VentanaAgregar
from secundaria_2 import VentanaEliminar

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz.ui', self)
        # pagina que se muestra por defecto
        self.stackedWidget.setCurrentIndex(0)
        self.bd = Galeria()
        self.cargar_combobox()
        #self.setEnabled(True)
     
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

        self.bt_actualizar.clicked.connect(self.actualizar_tabla)

        # botones del menu 
        self.bt_exposicion.clicked.connect(lambda: self.visualizar_tabla("Exposición"))
        self.bt_obra.clicked.connect(lambda: self.visualizar_tabla("Obra"))
        self.bt_artista.clicked.connect(lambda: self.visualizar_tabla("Artista"))
        self.bt_telefono.clicked.connect(lambda: self.visualizar_tabla("Teléfono"))
        self.bt_tablas.clicked.connect(self.pag_tablas)
        self.bt_obra_vendida.clicked.connect(self.pag_tb_obras_vendidas)
        self.bt_acerca_de.clicked.connect(self.pag_acerca_de)

        # botones crud
        self.bt_agregar.clicked.connect(lambda: VentanaAgregar().show())
        self.bt_eliminar.clicked.connect(lambda: VentanaEliminar().exec_())

        # mover ventana
        self.fr_superior.mouseMoveEvent=self.mover_ventana

        self.lb_nombre_tb.text()

        

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
    
    
    def pag_tablas(self):
        self.stackedWidget.setCurrentIndex(0)

    def pag_tb_obras_vendidas(self):
        self.stackedWidget.setCurrentIndex(2)

    def pag_acerca_de(self):
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
        self.tb_main.setSelectionBehavior(QAbstractItemView.SelectRows) # selcciona una fila 

        # Llenar la tabla con los datos
        contador = 0
        for i in datos:
            for j in range(len(i)):
                self.tb_main.setItem(contador, j, QtWidgets.QTableWidgetItem(str(i[j]))) 
            contador += 1
        self.tb_main.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.deshabilitar_edicion(self.tb_main)

    def actualizar_tabla(self):
        nombre_tb_actual = self.lb_nombre_tb.text()
        self.visualizar_tabla(nombre_tb_actual)


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

    def visusalizar_obra_vendida(self):
        """
        Primero debo pasarle al combobox un listado de las exposiciones
        y al seleccionar una exposicion me muestre en la tabla las obras vendidas de dicha exposicion
        """
        titulo_exposicion = self.cb_exposicion.currentText()
        encabezados, datos = self.bd.mostrar_tabla("Obra")
        obras = self.bd.listarObra_vendida(titulo_exposicion)

        
        # Configurar la tabla
        self.tb_vendido.clear()
        #self.tb_vendido.setRowCount(len(obras))
        self.tb_vendido.setColumnCount(len(encabezados))
        self.tb_vendido.setHorizontalHeaderLabels(encabezados)
        self.tb_vendido.setSelectionBehavior(QAbstractItemView.SelectRows) # selcciona una fila 

        # Llenar la tabla con los datos
        if obras is None:
            r = "{} no tiene obras vendidas".format(titulo_exposicion)
            QMessageBox.critical(None, "Error", r)
        else:
            self.tb_vendido.setRowCount(len(obras))
            contador = 0
            for i in obras:
                if i != None:
                    for j in range(len(i)):
                        self.tb_vendido.setItem(contador, j, QtWidgets.QTableWidgetItem(str(i[j]))) 
                    contador += 1
        self.tb_vendido.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.deshabilitar_edicion(self.tb_vendido)



    def cargar_combobox(self):
        datos_exposicion = self.bd.mostrar_tabla("Exposición")
        indice_titulo_exposicion = datos_exposicion[0].index("Título_expo")
        exposicion = [item[indice_titulo_exposicion] for item in datos_exposicion[1]]

        # Limpiar elementos previos en el ComboBox antes de volver a cargar
        self.cb_exposicion.clear()

        # Agregar datos al ComboBox
        self.cb_exposicion.addItem('')
        self.cb_exposicion.addItems(exposicion)
        self.cb_exposicion.currentIndexChanged.connect(self.visusalizar_obra_vendida)



        
    def editar_item(self):
        pass
    
    



if __name__ == '__main__':
    app = QApplication([])
    ventana = Principal()
    ventana.show()
    sys.exit(app.exec_())

