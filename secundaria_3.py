from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.uic import loadUi
import icons_rc
from  proyectoGaleríaOK.connSql import Galeria
from secundaria import VentanaAgregar
import sys

class VentanaEditar(QDialog):
    def __init__(self):
        super(VentanaEditar, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz_editar.ui', self)
        # conectar base de datos
        self.bd = Galeria()

        self.setWindowTitle('Editar')

        # Deshabilitar el botón de ayuda en la barra de título
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.cargarCombobox = VentanaAgregar().cargar_combobox()

        # fecha actual por defecto
        self.dateEdit_fecha_inauguracion.setDate(QDate.currentDate())
        self.dateEdit_fecha_clausura.setDate(QDate.currentDate())

        # botones buscar, aceptar y cancelar
        # telefono
        self.bt_buscar_telefono.clicked.connect(self.buscar_telefono)
        self.bt_aceptar_telefono.clicked.connect(self.editar_telefono)
        self.bt_cancelar_telefono.clicked.connect(lambda: self.close())
        # exposicion
        self.bt_buscar_exposicion.clicked.connect(self.buscar_exposicion)
        self.bt_aceptar_exposicion.clicked.connect(self.editar_exposicion)
        self.bt_cancelar_exposicion.clicked.connect(lambda: self.close())
        # artista
        self.bt_buscar_artista.clicked.connect(self.buscar_artista)
        self.bt_aceptar_artista.clicked.connect(self.editar_artista)
        self.bt_cancelar_artista.clicked.connect(lambda: self.close())
        # obra
        self.bt_buscar_obra.clicked.connect(self.buscar_obra)
        self.bt_aceptar_obra.clicked.connect(self.editar_obra)
        self.bt_cancelar_obra.clicked.connect(lambda: self.close())

    # Conecta la señal activated de tu QComboBox a la ranura (slot) mostrar_pagina
        self.cb_tablas.activated.connect(self.mostrar_pagina)
        items = ["Exposición", "Obra", "Artista", "Teléfono"]
        self.cb_tablas.addItems(items)

    def mostrar_pagina(self, index):
        # Encuentra el índice de la página que deseas mostrar
        index_page = self.cb_tablas.findText(self.cb_tablas.currentText())
        
        self.stackedWidget.setCurrentIndex(index_page)


    def buscar_telefono(self):
        
        self.lineEdit_no_telefono.clear()
        self.telefono = self.bd.seleccionar_telefono(self.lineEdit_ci_artista.text())
        if self.lineEdit_ci_artista.text() == "":
            r = "Debe entrar un dato para poder buscar"
            QMessageBox.critical(None, "Error", r)
        elif len(self.telefono) != 0:
            try:
                self.lineEdit_no_telefono.insert(str(self.telefono[0][1]))
                self.ci = self.lineEdit_ci_artista.text()
            except:
                r = "No se encuentra número de teléfono de {} ".format(self.lineEdit_ci_artista.text())
                QMessageBox.critical(None, "Error", r)
                self.lineEdit_ci_artista.clear()

    
    
    def editar_telefono(self):

        ci = self.lineEdit_ci_artista.text()
        telefono = self.lineEdit_no_telefono.text()
        
        if ci != "" and telefono != "":
            self.bd.actualizar_todo_telefono(ci, telefono)
            self.lineEdit_ci_artista.clear()
            self.lineEdit_no_telefono.clear()
            r = "El teléfono {} ha sido actualizado".format(ci)
            QMessageBox.information(None, "Éxito", r)
        else:
            r = "No pueden quedar campos vacíos"
            QMessageBox.critical(None, "Error", r)

    def buscar_exposicion(self):
        titulo_exposicion = self.lineEdit_titulo_exposicion.text()
        self.textEdit_descripcion.clear()
        exposicion = self.bd.seleccionar_exposicion(titulo_exposicion)
        if len(exposicion) != 0:
            self.dateEdit_fecha_inauguracion.setDate(QDate.fromString(exposicion[1], "dd/MM/yyyy"))
            self.dateEdit_fecha_clausura.setDate(QDate.fromString(exposicion[2], "dd/MM/yyyy"))
            self.textEdit_descripcion.setPlainText(str(exposicion[3]))
            self.lineEdit_titulo_exposicion.text()


            

    def editar_exposicion(self):
        
        titulo = self.lineEdit_titulo_exposicion.text()
        f_inauguracion = self.dateEdit_fecha_inauguracion.text()
        f_clausura = self.dateEdit_fecha_clausura.text()
        descripcion = self.textEdit_descripcion.toPlainText()
        
        if titulo != "" and f_inauguracion != "" and f_clausura != "" and descripcion != "":

            self.bd.actualizar_toda_exposicion(titulo, f_inauguracion, f_clausura, descripcion)
            self.lineEdit_titulo_exposicion.clear()
            self.dateEdit_fecha_inauguracion.setDate(QDate.currentDate())
            self.dateEdit_fecha_clausura.setDate(QDate.currentDate())
            self.textEdit_descripcion.clear()
            r = "La exposición {} ha sido actualizada".format(titulo)
            QMessageBox.information(None, "Éxito", r)
        else:
            r = "No pueden quedar campos vacíos"
            QMessageBox.critical(None, "Error", r)

    
    def buscar_artista(self):
        id = self.lineEdit_ci_Artista.text()
        self.lineEdit_calle.clear()
        self.lineEdit_no.clear()
        self.lineEdit_provincia.clear()
        self.lineEdit_nacionalidad.clear()
        artista = self.bd.seleccionar_artista(id)
        if len(artista) != 0:
            self.lineEdit_calle.insert(artista[1])
            self.lineEdit_no.insert(artista[2])
            self.lineEdit_provincia.insert(artista[3])
            self.lineEdit_nacionalidad.insert(artista[4])
            self.lineEdit_ci_Artista.text()

    def editar_artista(self):
        
        id = self.lineEdit_ci_Artista.text()
        calle = self.lineEdit_calle.text()
        no = self.lineEdit_no.text()
        provincia = self.lineEdit_provincia.text()
        nacionalidad = self.lineEdit_nacionalidad.text()
        if id != "" and calle != "" and no != "" and provincia != "" and nacionalidad != "":
            self.bd.actualizar_todo_artista(id, calle, no, provincia, nacionalidad)
            self.lineEdit_calle.clear()
            self.lineEdit_no.clear()
            self.lineEdit_provincia.clear()
            self.lineEdit_nacionalidad.clear()
            self.lineEdit_ci_Artista.clear()
            r = "El Artista {} ha sido actualizado".format(id)
            QMessageBox.information(None, "Éxito", r)
        else:
            r = "No pueden quedar campos vacíos"
            QMessageBox.critical(None, "Error", r)

    def buscar_obra(self):
        id = self.lineEdit_registro.text()
        self.lineEdit_titulo_obra.clear()
        self.lineEdit_Estilo.clear()
        self.lineEdit_presio_salida.clear()
        self.comboBox_titulo_exposicion.setCurrentIndex(-1)
        self.lineEdit_ci_artist.clear()
        self.check_si.setChecked(False)
        self.lineEdit_precio_mejor.clear()
        obra = self.bd.seleccionar_obra(id)
        if len(obra) != 0:
            self.lineEdit_titulo_obra.insert(obra[1])
            self.lineEdit_Estilo.insert(obra[2])
            self.lineEdit_presio_salida.insert(str(obra[3]))
            self.comboBox_titulo_exposicion.setCurrentText(obra[4])
            #self.check_sisetChecked()
            self.lineEdit_precio_mejor.insert(str(obra[6]))
            self.lineEdit_registro.text()


    def editar_obra(self):
        pass


'''if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaEditar()
    ventana.show()
    sys.exit(app.exec_())'''