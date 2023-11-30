from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView,  QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from  proyectoGaleríaOK.connSql import Galeria




import sys


class Secundaria(QMainWindow):
    def __init__(self):
        super(Secundaria, self).__init__()

        # Cargar el archivo .ui
        loadUi('interfaz_secundaria.ui', self)
        # pagina que se muestra por defecto
        self.stacked_widget.setCurrentIndex(0)
        self.bd = Galeria()

        self.actionExposicion.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.actionArtista.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.actionObra.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.actionTelefono.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.bt_aceptar_telefono.clicked.connect(self.agregar_telefono)
        self.bt_cancelar_telefono.clicked.connect(lambda: self.close())

    
    def agregar_telefono(self):
        ci = self.lineEdit_ci_artista.text()
        telefono = self.lineEdit_no_telefono.text()
        if not ci.isdigit() or not telefono.isdigit():
            r = "ci y teléfono deben ser números enteros"
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existeArtista(ci) and self.bd.existetelefono(telefono):
            r = "ci y teléfono ya existen"
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existeArtista(ci):
            r = "ci existe"
            QMessageBox.critical(None, "Error", r)
        elif self.bd.existetelefono(telefono):
            r = "teléfono ya existe"
            QMessageBox.critical(None, "Error", r)
        elif ci != "" and telefono != "":
            self.bd.insertar_telefono(ci, telefono)
            self.mensaje = QMessageBox.information(None, "Éxito", "El número de teléfono del artista {} se agregó con éxito.".format(ci))
            self.lineEdit_ci_artista.clear()
            self.lineEdit_no_telefono.clear()
        else:
            QMessageBox.critical(None, "Error", "Rellene los campos vacíos")

            

    


if __name__ == '__main__':
    app = QApplication([])
    ventana = Secundaria()
    ventana.show()
    sys.exit(app.exec_())