from PyQt5.QtWidgets import QApplication, QDialog, QComboBox,  QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QDate
from PyQt5.uic import loadUi
from  proyectoGaleríaOK.connSql import Galeria
import sys


class VentanaAgregar(QDialog):
    def __init__(self):
        super(VentanaAgregar, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz_agregar.ui', self)
        self.setWindowTitle('Agregar')
        # pagina que se muestra por defecto
        self.stackedWidget.setCurrentIndex(0)
        self.bd = Galeria()
        self.cargar_combobox()
        self.dateEdit_fecha_inauguracion.setDate(QDate.currentDate())
        self.dateEdit_fecha_clausura.setDate(QDate.currentDate())

        # Deshabilitar el botón de ayuda en la barra de título
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Conecta la señal activated de tu QComboBox a la ranura (slot) mostrar_pagina
        self.cb_tablas.activated.connect(self.mostrar_pagina)
        items = ["Exposición", "Obra", "Artista", "Teléfono"]
        self.cb_tablas.addItems(items)

        # botones aceptar y cancelar 
        # telefono 
        self.bt_aceptar_telefono.clicked.connect(self.agregar_telefono)
        self.bt_cancelar_telefono.clicked.connect(lambda: self.close())
        # exposicion
        self.bt_aceptar_exposicion.clicked.connect(self.agregar_exposicion)
        self.bt_cancelar_exposicion.clicked.connect(lambda: self.close())
        # artista
        self.bt_aceptar_artista.clicked.connect(self.agregar_artista)
        self.bt_cancelar_artista.clicked.connect(lambda: self.close())
        # obra
        self.bt_aceptar_obra.clicked.connect(self.agregar_obra)
        self.bt_cancelar_obra.clicked.connect(lambda: self.close())

    def mostrar_pagina(self, index):
        # Encuentra el índice de la página que deseas mostrar
        index_page = self.cb_tablas.findText(self.cb_tablas.currentText())
        
        self.stackedWidget.setCurrentIndex(index_page)
        
    
    def agregar_telefono(self):
        ci = self.lineEdit_ci_artista.text()
        telefono = self.lineEdit_no_telefono.text()
        if ci == "" or telefono == "":
            r = "Rellene los campos vacíos"
            QMessageBox.critical(None, "Error", r)
        elif not ci.isdigit() or not telefono.isdigit():
            r = "ci y teléfono deben ser números enteros"
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existetelefono(telefono):
            r = "Teléfono de {} ya existen".format(telefono)
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existeArtista(ci):
            self.bd.insertar_telefono(ci, telefono)
            self.mensaje = QMessageBox.information(None, "Éxito", "El número de teléfono del artista {} se agregó con éxito.".format(ci))
            self.lineEdit_ci_artista.clear()
            self.lineEdit_no_telefono.clear()
        else:
            QMessageBox.critical(None, "Error", "El artista no existe en la base de datos.")

            
    def agregar_exposicion(self):
        titulo  = self.lineEdit_titulo_exposicion.text()
        f_inauguracion = self.dateEdit_fecha_inauguracion.text()
        f_clausura = self.dateEdit_fecha_clausura.text()
        descripcion = self.textEdit_descripcion.toPlainText()
        if type(titulo) != str:
            r = "El título es una cadena"
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existeExposicion(titulo):
            r = "La exposición ya existe"
            QMessageBox.critical(None, "Error", r)
        elif titulo != "" and f_inauguracion != "" and f_clausura != "" and descripcion != "":
            self.bd.insertar_exposicion(titulo, f_inauguracion, f_clausura, descripcion)
            self.mensaje = QMessageBox.information(None, "Éxito", "La exposición {} se agregó con éxito.".format(titulo))
            self.lineEdit_titulo_exposicion.clear()
            self.textEdit_descripcion.clear()
        else:
            QMessageBox.critical(None, "Error", "Rellene los campos vacíos")

    def agregar_artista(self):
        ci  = self.lineEdit_ci_Artista.text()
        calle = self.lineEdit_calle.text()
        no = self.lineEdit_no.text()
        provincia = self.lineEdit_provincia.text()
        nacionalidad = self.lineEdit_nacionalidad.text()
        print(type(provincia), type(nacionalidad))


        if ci != "" and calle != "" and no != "" and provincia != "":
            if not ci.isdigit()  or not no.isdigit():
                r = "ci y no deben ser números enteros"
                QMessageBox.critical(None, "Error", r)
            elif type(provincia) != str and type(nacionalidad) != str:
                r = "La provincia y la nacionalidad  son de tipo string"
                QMessageBox.critical(None, "Error", r)
            elif self.bd.existeArtista(ci):
                r = "El artista ya existe"
                QMessageBox.critical(None, "Error", r)
            else:
                self.bd.insertar_artista(ci, calle, no, provincia, nacionalidad)
                self.mensaje = QMessageBox.information(None, "Éxito", "El artista {} se agregó con éxito.".format(ci))
                self.lineEdit_ci_Artista.clear()
                self.lineEdit_calle.clear()
                self.lineEdit_no.clear()
                self.lineEdit_provincia.clear()
                self.lineEdit_nacionalidad.clear()
        else:
            QMessageBox.critical(None, "Error", "Rellene los campos vacíos")

    def agregar_obra(self):
        id = self.lineEdit_registro.text()
        titulo = self.lineEdit_titulo_obra.text()
        estilo = self.lineEdit_Estilo.text()
        exposicion = self.comboBox_titulo_exposicion.currentText()
        precio = self.lineEdit_presio_salida.text()
        ci_artista = self.lineEdit_ci_artist.text()
        mejor_oferta = self.lineEdit_precio_mejor.text()

        # checkbuttom 
        vendido = self.check_si.isChecked() # devuelve true o false
        if vendido:
            self.valor = "si"
        else: 
           self.valor = "no"
        
        if id != "" and titulo != "" and estilo != "" and precio != "" and ci_artista != "" and mejor_oferta != "":

            if not id.isdigit() or not precio.isdigit() or not ci_artista.isdigit() or not mejor_oferta.isdigit():
                r = "id, precio, ci artista, mejor oferta deben ser números enteros"
                QMessageBox.critical(None, "Error", r)
            elif type(titulo) != str:
                r = "El título debe ser una cadena (string)"
                QMessageBox.critical(None, "Error", r)
            elif int(precio) <= 0 or int(mejor_oferta) <= 0:
                r = "El precio de venta y el precio de la mejor oferta deben ser mayores que cero"
                QMessageBox.critical(None, "Error", r)
            elif self.bd.existeArtista(ci_artista):
                self.bd.insertar_obra(id, titulo, estilo,precio , exposicion, ci_artista, self.valor, mejor_oferta)
                self.mensaje = QMessageBox.information(None, "Éxito", "La obra {} se agregó con éxito.".format(id))

                # Limpiar campos después de agregar la obra
                self.lineEdit_registro.clear()
                self.lineEdit_titulo_obra.clear()
                self.lineEdit_Estilo.clear()
                self.lineEdit_presio_salida.clear()
                self.lineEdit_ci_artist.clear()
                self.comboBox_titulo_exposicion.setCurrentIndex(-1)
                self.check_si.setChecked(False)
                self.lineEdit_precio_mejor.clear()
        else:
            QMessageBox.critical(None, "Error", "Rellene los campos vacíos")


    def cargar_combobox(self):
        datos_exposicion = self.bd.mostrar_tabla("Exposición")
        indice_titulo_exposicion = datos_exposicion[0].index("Título_expo")
        exposicion = [item[indice_titulo_exposicion] for item in datos_exposicion[1]]
        print(indice_titulo_exposicion)

        # Limpiar elementos previos en el ComboBox antes de volver a cargar
        self.comboBox_titulo_exposicion.clear()

        # Agregar datos al ComboBox
        self.comboBox_titulo_exposicion.addItem('')
        self.comboBox_titulo_exposicion.addItems(exposicion)
    

    


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaAgregar()
    ventana.show()
    sys.exit(app.exec_())

