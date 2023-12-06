from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from  proyectoGaleríaOK.connSql import Galeria
import sys

class VentanaEliminar(QDialog):
    def __init__(self):
        super(VentanaEliminar, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz_eliminar.ui', self)
        # conectar base de datos
        self.bd = Galeria()

        self.setWindowTitle('Eliminar')

        # Deshabilitar el botón de ayuda en la barra de título
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # botones aceptar y cancelar
        self.bt_aceptar.clicked.connect(self.eliminar_elemento)
        self.bt_cancelar.clicked.connect(lambda: self.close())

    def eliminar_elemento(self):
         #  Obtener la lista de opciones directamente usando list comprehension
        opciones = [self.cb_tablas.itemText(i) for i in range(self.cb_tablas.count())]
        id = self.lineEdit_id.text()
        if self.cb_tablas.currentText() == "" or self.lineEdit_id.text() == "":
            r = "No pueden quedar campos vacíos"
            QMessageBox.critical(None, "Error", r)
        # eliminar una exposicion
        elif self.cb_tablas.currentText() == opciones[1]:
            print('Ha seleccionado la opcion {}'.format(opciones[1]))  
            # existe Exposicion
            if self.bd.existeExposicion(id):
                self.bd.borrar_exposicion(id)
                r = "La exposición {} ha sido eliminada".format(id)
                QMessageBox.information(None, "Éxito", r)
                self.cb_tablas.setCurrentIndex(-1)
                self.lineEdit_id.clear()
                print("La exposicion {} ha sido eliminada de la base de datos".format(id))
            else:
                r = "La exposición {} no existe en la base de datos".format(id)
                QMessageBox.critical(None, "Error", r)
        # eliminar un artista
        elif self.cb_tablas.currentText() == opciones[2]:  
            # existe Artista
            if self.bd.existeArtista(id):
                if self.bd.borrar_ocurrencia(id):
                    r = "El artista {} ha sido eliminado".format(id)
                    QMessageBox.information(None, "Éxito", r)
                    self.cb_tablas.setCurrentIndex(-1)
                    self.lineEdit_id.clear()
                else:
                    r = "El artista {} tiene obras asociadas. No se puede eliminar de la tabla.".format(id)
                    QMessageBox.critical(None, "Error", r)
                    self.cb_tablas.setCurrentIndex(-1)
                    self.lineEdit_id.clear()
            else:
                r = "El artista {} no existe en la base de datos".format(id)
                QMessageBox.critical(None, "Error", r)

        elif self.cb_tablas.currentText() == opciones[3]: 
            # existe orba
            if self.bd.existeObra(id):
                self.bd.borrar_obra(id)
                r = "La obra {} ha sido eliminada".format(id)
                QMessageBox.information(None, "Éxito", r)
                self.cb_tablas.setCurrentIndex(-1)
                self.lineEdit_id.clear()
            else:
                r = "La obra {} no existe en la base de datos".format(id)
                QMessageBox.critical(None, "Error", r)

        elif self.cb_tablas.currentText() == opciones[4]: 
            # existe telefono
            if self.bd.existeArtista(id) or self.bd.existetelefono(id):
                self.bd.borrar_telefono(id)
                r = "El teléfono {} ha sido eliminada".format(id)
                QMessageBox.information(None, "Éxito", r)
                self.cb_tablas.setCurrentIndex(-1)
                self.lineEdit_id.clear()
            else:
                r = "El teléfono {} no existe en la base de datos".format(id)
                QMessageBox.critical(None, "Error", r)
        


        

        


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaEliminar()
    ventana.show()
    sys.exit(app.exec_())