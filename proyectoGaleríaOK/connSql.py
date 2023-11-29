import sqlite3

class Galeria:
    '''

        Clase que gestiona una colección de obras de arte, artistas, exposiciones y 
    contactos telefónicos.

        Esta clase proporciona diferentes métodos para operar con diferentes tipos de 
    datos de una galería de arte, como crear, insertar, borrar, seleccionar un objeto 
    específico, listar todos los elementos, actualizar un campo y actualizar todos los 
    campos. También incluye un método para listar las obras vendidas de una exposición 
    y otro para borrar artistas que no tienen obras asociadas. 
     
    '''

    # Tabla Exposicion
    def crear_tabla_exposicion(self):
        '''
            Este método es el encargado de la construcción de la tabla Exposición en la base de datos Galería.db.
        '''
        conexBase = sqlite3.connect("Galería.db") 
        cursor = conexBase.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Exposición(Título_expo TEXT UNIQUE PRIMARY KEY,
                                                                Fecha_inauguración DATE, 
                                                                Fecha_clausura DATE, 
                                                                Descripción TEXT)''')
        conexBase.commit()
        conexBase.close()

    def insertar_exposicion(self, titulo, fecha_ing, fecha_cl, descripcion):
        '''
            Este método es el encargado de insertar los registros de una exposición en la base de datos Galería.db
        dado su título.
        
        Atributos:
            titulo(TEXT): proporciona el titulo de la exposición.
            fecha_ing(DATE): proporciona la fecha de inicio de la exposición.
            fecha_cl(DATE): proporciona la fecha de cierre de la exposición.
            descripcion(TEXT): proporciona una breve descripción de la exposición.
        '''

        existe = self.existeExposicion(titulo)
        self.crear_tabla_exposicion()
        if existe == False:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            lista_expo = [
                (titulo, fecha_ing, fecha_cl, descripcion)
                ]               
            cursor.executemany("INSERT INTO Exposición(Título_expo, Fecha_inauguración, Fecha_clausura, Descripción) VALUES(?, ?, ?, ?)", lista_expo)
            conexBase.commit()
            conexBase.close()
        else:
            return f"Ya existen registros para {titulo}."
        
    def seleccionar_exposicion(self, t_expo):
        '''
            Este método selecciona una exposición dada y devuelve la información  que contiene.

        Atributos:
           t_expo(TEXT): proporciona el nombre de la exposición a seleccionar.

        Retorna:
            tuple: exposición, una tupla con la  información de la exposición que 
        contiene dicha exposición en caso de que exista dicha exposición.
            str: f"No existen registros para {t_expo}.", en caso de que no exista 
        esta exposición en la tabla.
        '''
        existe = self.existeExposicion(t_expo)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
        
            cursor.execute("SELECT * FROM Exposición WHERE Título_expo = ?", (t_expo,))
            lista_exp = cursor.fetchall()
            conexBase.commit()
            conexBase.close()
            for e in lista_exp:
                exposicion = e
            return exposicion
        else:
            return f"No existen registros para {t_expo}."

    def listarExposicion(self):
        '''
            Este método lista toda la información, en forma de tupla de todas las exposiciones registradas en la tabla Exposición.

        Retorna: 

            list: lista_resultado, es una lista con las  tuplas que proporcionan la información
        de cada exposición generada en la lista.
        '''
        try:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Exposición")
            lista_resultado = cursor.fetchall()
            conexBase.close()
            return lista_resultado
        except sqlite3.Error as e:
            return f"Ha ocurrido un error: ", e

    def actualizar_exposicion(self, t_expo, campo, nuevo_valor):
        '''
            Este método actualiza un campo específico de una exposción dado su título.

        Atributos:

            t_expo(TEXT): proporciona el nombre de la exposición que se desa actualizar.
            campo(TEXT): proporciona el nombre del campo que se desa actualizar de la tabla  estos valores. 
            Fecha_clausura, Descripción).
            nuevo_valor(TEXT o DATE): proporciona el nuevo valor que va a tomar dicho campo en la tabla.

        Retorna:

            str: f"Nombre del campo incorrecto. Los valores a llenar son(Título_expo, Fecha_inauguración, 
            Fecha_clausura, Descripción)", si el valor del campo proporcionado no coincide con ningún nombre
            de los campos de la tabla Exposición.
            str: f"No existen registros para {t_expo}.", en caso de que el para título de la exposición dada 
            no exista en la tabla.  
        '''
        existe = self.existeExposicion(t_expo)
        if existe == True:
            if campo  == "Título_expo" or campo == "Fecha_inauguración" or campo == "Fecha_clausura"  or campo == "Descripción":
                conexBase = sqlite3.connect("Galería.db") 
                cursor = conexBase.cursor()

                sql = f"UPDATE Exposición SET {campo} = ? WHERE Título_expo = ?"
                parametros = (nuevo_valor, t_expo)
                cursor.execute(sql, parametros)
                conexBase.commit()
                conexBase.close()
            else:
                return f"Nombre del campo incorrecto. Los valores a llenar son(Título_expo, Fecha_inauguración, Fecha_clausura, Descripción)"
        else:
            return f"No existen registros para {t_expo}."

    def existeExposicion(self, titulo):
        '''
            Esta función busca la existencia de registros de una exposición en la tabla Exposición dado su título.

        Atributos:
            titulo(TEXT): proporciona el nombre de la exposición que se desea conocer su existencia.

        Retorna:
            TRUE: En caso de exista dicha exposición en la tabla.
            FALSE: En caso de no haber ocorrencia de la misma en la tabla.
        '''
        try:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Exposición WHERE Título_expo = ? LIMIT 1", (titulo,))
            resultado = cursor.fetchone()
            conn.close()
            return resultado is not None  # True si se encontró al menos un registro, False si no se encontró
        except sqlite3.Error as e:
            return f"Ha ocurrido un error en la conexión:", e

    def actualizar_toda_exposicion(self, titulo, fecha_inauguracion,fecha_clausura, descripcion):
        '''
            Este método actualiza todos los campos de una exposición en la tabla Exposición de la base de datos Galería.db
        dado su título.

        Atributos:
            titulo(TEXT): proporciona el titulo de la exposición que se desea actualizar.
            fecha_ing(DATE): proporciona la fecha de inicio actualizad de dicha exposición.
            fecha_cl(DATE): proporciona la fecha de cierre actualizada de dicha exposición.
            descripcion(TEXT): proporciona una breve descripción actualizada de dicha exposición.

        Retorna:           

            str: f"No existen registros para {titulo}.", si dicha exposición aún no ha sido creada.  
        '''
        existe = self.existeExposicion(titulo)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            self.borrar_exposicion(titulo)
            self.insertar_exposicion(titulo,fecha_inauguracion,fecha_clausura, descripcion)
            conexBase.commit()
            conexBase.close()
        else:
            return f"No existen registros para {titulo}."

    def borrar_exposicion(self, titulo):
        '''
            Este método es el encargado de borrar de la tabla Exposición en la base de datos Galeía.db la exposición 
        dado su título.
        
        Atributos:
            titulo(TEXT): proporciona el título de la exposición que se desea borrar.

        '''
        try:    
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Exposición WHERE  Título_expo = ?", (titulo,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            conn.close()
            return f"Ha ocurrido un error: ", e

    # Tabla Obra
    def crear_tabla_obra(self):
        '''
            Este método es el encargado de construir la tabla Obra en la base de datos Galería.db.
        '''
        conexBase = sqlite3.connect("Galería.db") 
        cursor = conexBase.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Obra(Id_registro INTEGER PRIMARY KEY, 
                                                      Título_obra TEXT, 
                                                      Estilo TEXT, 
                                                      Precio_salida REAL,
                                                      Título_Exposición TEXT, 
                                                      Ci_artista INTEGER, 
                                                      Vendido TEXT,
                                                      Precio_mejor_oferta REAL)''')

        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_obra_exposicion ON Obra(Título_Exposición)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_obra_artista ON Obra(Ci_artista)")
        conexBase.commit()
        conexBase.close()

    def insertar_obra(self, id_registro, titulo_obra, estilo, precio_salida, tituloExposicion, ci_artista, vendido, precio_mejor_oferta=0.0):
        '''
            Este método es el encargado de insertar  datos de una obra en la tabla Obra de la base de datos Galería.db.

        Atributos:
            id_registro(INTEGER): es el código que hace diferente a cada obra.
            titulo_obra(TEXT): proporciona el nombre dado por el artista a la obra creada. 
            estilo(TEXT): proporciona el estilo de la obra. Puede ser barroco, contemporáneo entre otros. 
            precio_salida(REAL): proporciona el precio atribuído a la obra.
            tituloExposicion(TEXT): proporciona una de las llaves foráneas de la tabla Obra. Nombre de la exposición
            a la que pertenece. 
            ci_artista(INTEGER): Es el número de identificación del artista a la que pertenece la obra. 
            vendido(TEXT): puede ser de valor si o no en dependencia de si la obra fue vendida o no. 
            precio_mejor_oferta(REAL): este campo puede quedar vacío si la obra aún no ha sido vendida.

        Retorna:

            str: f"Ya existen registros para {id_registro}.", si la obra está en la tabla.  
        '''
        existe = self.existeObra(id_registro)
        self.crear_tabla_obra()
        if existe == False:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()

            lista_obra = [
                (id_registro, titulo_obra, estilo, precio_salida, tituloExposicion, ci_artista, vendido, precio_mejor_oferta)
                ]

            cursor.executemany("INSERT INTO Obra(Id_registro, Título_obra , Estilo, Precio_salida, Título_Exposición, Ci_artista, Vendido, Precio_mejor_oferta) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", lista_obra)
            conexBase.commit()
            conexBase.close()
        else:
            return f"Ya existen registros para {id_registro}."
            
    def seleccionar_obra(self, id_registro):
        '''
            Este método selecciona una obra dado su id y  de la misma muestra su información registrada.

        Atrinutos:
            id_registro(INTEGER): es el código que hace diferente a cada obra. 

        Retorna:
            tuple: si hay registros de la obra en la tabla
            str: f"No existen registros para {id_registro}.", en caso de que no se haya creado ninguna
            instancia para ese id de obra.   
        '''
        existe = self.existeObra(id_registro)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Obra WHERE Id_registro=?",(id_registro,))
            listaObra = cursor.fetchall()
            conexBase.commit()
            conexBase.close()
            for o in listaObra:
                obra = o
            return obra
        else:
            return f"No existen registros para {id_registro}."

    def listarObra_vendida(self, nombre_expo):
        '''
            Este metodo muestra una lista con todas las obras que hayan sido vendidas dada una
        exposición.

        Atributos
            nombre_expo(TEXT): proporciona el nombre de la exposición que se desea conocer sus
            obras vendidas.

        Retorna:
           list: devuelve la lista_vendido.
        '''
        try:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Obra WHERE Título_Exposición=?",(nombre_expo,))
            lista_obra = cursor.fetchall()
            vendido = "si"
            lista_vendido = []
            count = 0
            for obra in lista_obra:
                if obra[6] == vendido:
                    lista_vendido.append(obra)
                    count += 1 
            if count != 0:
                return lista_vendido
            else:
                return f"De la exposición {nombre_expo} no se han vendido obras."
            
        except sqlite3.Error as e:
            return f"Ha ocurrido un error ", e

    def listarObra(self):
        '''
            Este método devuelve una lista con todas las obras que han sido registradas en la base de datos Galeía.db.

        Retorna:
            list: devuelve lista_resultado con todas las obras registradas.
        '''
        try:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Obra")
            lista_resultado = cursor.fetchall()
            conexBase.close()
            return lista_resultado
        except sqlite3.Error as e:
            return "Ha ocurrido un error: ", e

    def actualizar_obra(self, idR, campo, nuevo_valor):
        '''
            Este método actualiza un campo de una obra determinada atribuyendole un nuevo valor, pasado como parametro.

        Atributos:
            idR(INTEGER): es el número que identifica la obra a actualizar.
            campo(TEXT): es el nombre del campo a actualizar.
            nuevo_valor(INTEGER, REAL, TEXT): es el nuevo valor que se le deesea atribuir al campo seleccionado.

        Retorna:
            str: "Nombre del campo incorrecto. Los valores a llenar son: (Id_registro, Título_obra , Estilo, Precio_salida, 
            Título_Exposición, Ci_artista, Vendido, Precio_mejor_oferta) ", si el nombre del campo insertado no es correcto.
            str: f"No existen registros para {idR}", si para el título de la exposición dada no existen valores registrados en la tabla Exposición 
        '''
        existe = self.existeObra(idR)
        if existe == True:
            if campo == "Id_registro" or campo == "Título_obra" or campo == "Estilo" or campo == "Precio_salida" or campo == "Título_Exposición" or campo == "Ci_artista" or campo == "Vendido" or campo == "Precio_mejor_oferta":
                conexBase = sqlite3.connect("Galería.db") 
                cursor = conexBase.cursor()

                sqlO = f"UPDATE Obra SET {campo} = ? WHERE Id_registro = ?"
                parametros = (nuevo_valor, idR)
                cursor.execute(sqlO, parametros)
                conexBase.commit()
                conexBase.close()
            else:
                return "Nombre del campo incorrecto. Los valores a llenar son: (Id_registro, Título_obra , Estilo, Precio_salida, Título_Exposición, Ci_artista, Vendido, Precio_mejor_oferta) "
        else:
            return f"No existen registros para {idR}"

    def existeObra(self, id_registro):
        '''
        Este método comprueba la existencia de una obra dada en la base de datos Galería.db.

        Atributos:
            id_registro(INTEGER): proporciona el id de la obra que se desea comprobar su existencia.
        
        Retorna:
            TRUE: si se encontró la obra.
            False: si no no se encontró.
        '''
        try:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM Obra WHERE Id_registro = ? LIMIT 1", (id_registro,))
            resultado = cursor.fetchone()

            conn.close()

            return resultado is not None  # True si se encontró al menos un registro, False si no se encontró
        except sqlite3.Error as e:
            return f"Ha ocurrido un error:", e

    def actualizar_toda_obra(self, id_registro, titulo_obra, estilo, precio_salida, tituloExposicion, ci_artista, vendido, precio_mejor_oferta=0.0):
        '''
            Este método actualiza todos los campos de una obra dada en la tabla Obra de la  base de datos Galería.db.
                
            Atributos:
                id_registro(INTEGER): el id de la obra que se desea actualizar. 
                titulo_obra(TEXT): el nuevo nombre de la obra actualizado. 
                estilo: estilo que trabajó el artista en la obra actualizado.  
                precio_salida(REAL): el precio que toma la obra actualizado. 
                tituloExposicion(TEXT): referencia a la exposición que pertenece.
                ci_artista(TEXET): id que identifica al artista. Es único  
                vendido(TeEXT): puede ser si o no en dependencia si la obra fue vendida o no. 
                precio_mejor_oferta(REAL): este campo puede quedar vacío en caso de no haber sido vendida la obra.

            Retorna:
               
                str: f"No existen registros {id_registro}.", en caso que la obra no se encuentre en la tabla. 
        '''
        existe = self.existeObra(id_registro)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            self.borrar_obra(id_registro)
            self.insertar_obra(id_registro, titulo_obra, estilo, precio_salida, tituloExposicion, ci_artista, vendido, precio_mejor_oferta)
            conexBase.commit()
            conexBase.close()
        else:
            return f"No existen registros {id_registro}."

    def borrar_obra(self, id_Registro):
        '''
            Este método borra cualquier ocurrencia de una obra dado su id.
            
            Atributos:
                id_Registro(TEXT): id que identifica la obra que se desea borrar.
        '''
        try: 
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()

            cursor.execute("DELETE FROM Obra WHERE Id_registro = ?", (id_Registro,))
            conexBase.commit()
            conexBase.close()
        except sqlite3.Error as e:
            return f"Ha ocurrido un error:", e
   
    # Tabla Artista
    def crear_tabla_artista(self):
        '''
            Función que crea la tabla Artista abriendo una conexión a la base de datos Galería.db.
        '''

        conexBase = sqlite3.connect("Galería.db") 
        cursor = conexBase.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Artista(Ci INTEGER PRIMARY KEY,
                                                        Calle TEXT,
                                                        No VARCHAR,
                                                        Provincia TEXT,
                                                        Nacionalidad TEXT)''')
        conexBase.commit()
        conexBase.close()

    def insertar_artista(self, ciArtista, calle, no_vivienda, provincia, nacionalidad):
        '''
            Función encargada de insertar valores a la tabla Artista en la base de datos Galería.db.

            Atributos:
                ciArtista(INTEGER): atributo que identifica a cada artista.
                calle(TEXT): proporciona el nombre de la calle de residencia del artista.
                no_vivienda(VARCHAR): proporciona el número de vivienda donde reside el artista.
                provincia(TEXT): proporciona el nombre de la provincia a la que pertenece el artista.
                nacionalidad(TEXT): proporciona el nombre del país al que pertenece el artista.

            Retorna:
                str: f"Ya existen registros para {ciArtista}.", si existen registros para el artista en la tabla.    
        '''
        existe = self.existeArtista(ciArtista)
        self.crear_tabla_artista()
        if existe == False:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()

            lista_artista = [
                        (ciArtista, calle, no_vivienda, provincia, nacionalidad)
                ]    

            cursor.executemany("INSERT INTO Artista(Ci, Calle, No, Provincia, Nacionalidad) VALUES(?, ?, ?, ?, ?)", lista_artista)
            conexBase.commit()
            conexBase.close()
        else:
            return f"Ya existen registros para {ciArtista}."

    def seleccionar_artista(self, ci):
        '''
            Método encargado de seleccionar un artista dado su carnet de identidad y mostrar su información.

            Atributos:
                ci(INTEGER): id del artista que se desea conocer su información.

            Retorna:
                str: f"No existen registros para {ci}.", en caso de que para dicho id no hayan valores registrados. 
        '''
        existe = self.existeArtista(ci)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Artista WHERE Ci = ?", (ci,))
            lista_art = cursor.fetchall()
            conexBase.commit()
            conexBase.close()
            for a in lista_art:
                artista = a
            return artista
        else:
            return f"No existen registros para {ci}."

    def listarArtista(self):
        '''
            Función encargada de mostrar una lista con la información de todos los artistas registrados en forma de tuplas.
        '''
        try:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Artista")
            lista_resultado = cursor.fetchall()
            conexBase.close()
            return lista_resultado
        except sqlite3.Error as e:
            return f"Ha ocurrido un error: ", e

    def actualizar_artista(self, ci, campo, nuevo_valor):
        '''
            Funcion que se encarga de actualizar un campo determinado por el usuario dado un id.

            Atributos:
                ci(INTEGER): referencia al carnet del artista que se desea actualizar.
                campo(TEXT): es el nombre del campo que se desea actualizar.
                nuevo_valor(TEXT, INTEGER, VARCHAR): es el nuevo valor que toma el campo a actualizar.

            Retorna:
                str: "Nombre del campo incorrecto. Los valores a rellenar son: (Ci, Calle, No, Provincia, Nacionalidad)", en 
                caso de que el campo entrado como parámetro no coinsida con los nombres de los campos de la tabla.
                str: f"No existen registros para {ci}.", en caso de que no existan registros del artista en la tabla.  
        '''
        existe = self.existeArtista(ci)
        if existe == True:
            if  campo == "Ci" or campo == "Calle" or campo == "No" or campo == "Provincia" or campo == "Nacionalidad": 
                conexBase = sqlite3.connect("Galería.db") 
                cursor = conexBase.cursor()

                sql = f"UPDATE Artista SET {campo} = ? WHERE Ci = ?"
                parametros = (nuevo_valor, ci)
                cursor.execute(sql, parametros)
                conexBase.commit()
                conexBase.close()
            else:
                return "Nombre del campo incorrecto. Los valores a rellenar son: (Ci, Calle, No, Provincia, Nacionalidad)"
        else:
            return f"No existen registros para {ci}."

    def existeArtista(self, ci):
        '''
            Función encargada de buscar registros de un id específico en la tabla Artista de la base de datos Galería.db.
            
            Atributos:
                ci(INTEGER): atributo que identifica al artista que se desea comprobar su existencia en la tabla.

            Retorna:
                TRUE: en caso de que el ci del artista haya sido encontrado.
                FALSE: si el artista no se encuentra en la tabla
        '''
        try:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Artista WHERE Ci = ? LIMIT 1", (ci,))
            resultado = cursor.fetchone()
            conn.close()
            return resultado is not None  # True si se encontró al menos un registro, False si no se encontró
        except sqlite3.Error as e:
            return f"Ha ocurrido un error en la conexión:", e

    def actualizar_todo_artista(self, ciArtista, calle, no_vivienda, provincia, nacionalidad):
        '''
            Función encargada de actualizar todos los registros de un artista dado su id.

            Atributos:
                ciArtista(INTEGER): id que identifica al artista que se desa actualizar
                calle(TEXT): nuevo valor entrado para remplazar el campo Calle en la tabla
                no_vivienda(TEXT): nuevo valor entrados para rempazar el campo No en la tabla 
                provincia(TEXT): nuevo valor entrado para remplazar el campo Provincia en la tabla
                nacionalidad(TEXT): nuevo valor entrado para remplazar el campo Nacionalidad en la tabla.

            Retorna:
                str: f"No existen registros para {ciArtista}.", en caso de que no hayan registros para el id
                que se desea su actualización.   
        '''
        existe = self.existeArtista(ciArtista)
        if existe == True:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            self.borrar_ocurrencia(ciArtista)
            self.insertar_artista(ciArtista, calle, no_vivienda, provincia, nacionalidad)
            conn.commit()
            conn.close()
        else:
            return f"No existen registros para {ciArtista}."

    def borrar_ocurrencia(self, ci):
        '''
            Función encargada dado un id de borrar cualquier ocurrencia de un atrista que no tenga obras asociadas y 
        en caso de que sí tenga impide su eliminación.

            Atributos:
                ci(INTEGER): id que identifica al artista que se desea eliminar de la tabla.

            Retorna:
                str: f"El artista {ci} tiene {obras_count} obras asociadas. No se puede eliminar de la tabla.", si 
                el artista tiene obras asociadas
                str: f"No existen registros para {ci}", si el artista no está registrado en la tabla.
        '''
        existe = self.existeArtista(ci)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            # verificar si el artista tiene obras asociadas
            obras_count = cursor.execute("SELECT COUNT(*) FROM Obra WHERE Ci_artista = ?", (ci,)).fetchone()[0]
            if obras_count == 0:
                cursor.execute("DELETE FROM Artista WHERE Ci = ?", (ci,))
                self.borrar_telefono(ci)
                conexBase.commit()
            else:
                return f"El artista {ci} tiene {obras_count} obras asociadas. No se puede eliminar de la tabla."
        
            conexBase.close()
        else:
            return f"No existen registros para {ci}"

 # Tabla Teléfono
    def crear_tabla_teléfono(self):
        '''
            Función encargada de crear la tabla Teléfono abriendo una conexión a la base de datos Galería.db.
        '''
        conexBase = sqlite3.connect("Galería.db") 
        cursor = conexBase.cursor()        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Teléfono(Ci_artista INTEGER, 
                                                              TeléfonoA INTEGER,
                                                              PRIMARY KEY(Ci_artista, TeléfonoA))''')

        conexBase.commit()
        conexBase.close()

    def insertar_telefono(self, ci_artista, telefono):
        '''
            Función que se encarga de insertar los registros telefónicos de un artista en la tabla Teléfono.
        de la base de datos Galería.db.

            Atributos:
                ci_artista(INTEGER): id que identifica a el artista que pertenece el teléfono.
                telefono(INTEGER): contacto telefónigo del artista. Es único

            Retorna:
                str: f"Ya existen registros para {telefono}.", en caso de que se quiera registrar el mismo número
                telefónico varias veces.  

        '''
        existe = self.existetelefono(telefono)
        self.crear_tabla_teléfono()
        if existe == False:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()

            lista_teléfono = [
                (ci_artista, telefono)
                ]

            cursor.executemany('INSERT INTO Teléfono(Ci_artista, TeléfonoA) VALUES(?, ?)', lista_teléfono)
            conexBase.commit()
            conexBase.close()
        else:
            return f"Ya existen registros para {telefono}."

    def seleccionar_telefono(self, ci_artista):
        '''
            Función encargada de selecionar un registro teléfonico de un artista dado su id.

            Atributos:
               ci_artista(INTEGER): id que identifica al artista que se desea conocer su registro telefónico.

            Retorna:
                list: devuelve una lista, lista_t con todos los registros de dicho artista, en caso de que dicho
                artista tenga algún registro en la tabla Teléfono.
                str: f"No existen registros para {ci_artista}.", en caso de que no existan registros telefónicos
                para dicho artista.  
        '''
        existe = self.tienetelefono(ci_artista)
        if existe == True:
            conexBase = sqlite3.connect("Galería.db") 
            cursor = conexBase.cursor()
            lista_t = cursor.execute("SELECT * FROM Teléfono WHERE Ci_artista = ?", (ci_artista,)).fetchall()
            conexBase.commit()
            conexBase.close()
            return lista_t
        else:
            return f"No existen registros para {ci_artista}."

    def listartelefono(self):
        '''
            Función encargada de devolver una lista con todos los registros telefónicos de la tabla Teléfono en la 
        base de datos Galería.db

            Retorna:
                list: devuelve una lista_resultado, con todos los registros teléfonicos que existen en la tabla.
        '''
        try:
            conexBase = sqlite3.connect("Galería.db")
            cursor = conexBase.cursor()
            cursor.execute("SELECT * FROM Teléfono")
            lista_resultado = cursor.fetchall()
            conexBase.close()
            return lista_resultado
        except sqlite3.Error as e:
            return f"Ha ocurrido un error: ", e

    def actualizar_telefono(self, ci_artista, campo, nuevo_valor):
        '''
            Función encargada de actualizar un campo de la tabla Teléfono de la base de datos Galería.db
        dado su id.

            Atributos:
                ci_artista(INTEGER): es el número de id que identifica el artista que se desea su actualización.
                campo(TEXT): responde al nombre del campo de la tabla Teléfono que se desee actualizar.
                nuevo_valor(INTEGER): es el nuevo valor que va a tomar dicho campo.

            Retorna:
                str: "Nombre de campo incorrecto. Los valores a llenar son: (Ci_artista, TeléfonoA)", en caso de que 
                el nomrbe del campo entrado no coincida con ninguno de la tabla Teléfono.
                str: f"No existen registros para {ci_artista}.", si el artista no tiene registros telefónicos en la tabla.
        '''
        existe = self.tienetelefono(ci_artista)
        if existe == True:
            if campo == "Ci_artista" or campo == "TeléfonoA":
                conexBase = sqlite3.connect("Galería.db") 
                cursor = conexBase.cursor()
                sql = f"UPDATE Teléfono SET {campo} = ? WHERE Ci_artista = ?"
                parametros = (nuevo_valor, ci_artista)
                cursor.execute(sql, parametros)
                conexBase.commit()
                conexBase.close()
            else:
                return "Nombre de campo incorrecto. Los valores a llenar son: (Ci_artista, TeléfonoA)"
        else:
            return f"No existen registros para {ci_artista}."

    def existetelefono(self, telefono):
        '''
            Función encargada de comprobar la existencia de registros telefónicos en la tabla Teléfono de la base de datos Galería.db
        de un artista dado su id.

            Atributos:
               telefono(INTEGER): número que identifica al teléfono que se desea comprobar la existencia de sus registros telefónicos 
               en la base de datos.

            Retorna:
                TRUE: en caso de que dicho artista tenga registros telefónicos.
                FALSE: si para el id del artista no existe ningún registro en la tabla. 
        '''
        try:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM Teléfono WHERE TeléfonoA = ? LIMIT 1", (telefono,))
            resultado = cursor.fetchone()

            conn.close()

            return resultado is not None  # True si se encontró al menos un registro, False si no se encontró
        except sqlite3.Error as e:
            return f"Ha ocurrido un error: ", e

    def tienetelefono(self, ci_artista):
        '''
            Función encargada de comprobar la existencia de registros telefónicos en la tabla Teléfono de la base de datos Galería.db
        de un artista dado su id.

            Atributos:
               ci_artista(INTEGER): id que identifica al artista que se desea comprobar la existencia de sus registros telefónicos en la 
               base de datos.

            Retorna:
                TRUE: en caso de que dicho artista tenga registros telefónicos.
                FALSE: si para el id del artista no existe ningún registro en la tabla. 
        '''
        try:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM Teléfono WHERE Ci_artista = ? LIMIT 1", (ci_artista,))
            resultado = cursor.fetchone()

            conn.close()

            return resultado is not None  # True si se encontró al menos un registro, False si no se encontró
        except sqlite3.Error as e:
            return f"Ha ocurrido un error: ", e

    def actualizar_todo_telefono(self, ci_artista, telefono):
        '''
            Función que se encarga de actualizar todos los campos de la tabla Télefono en la base de datos Galería.db dado  el id
        de un artista.

            Atributos:
                ci_artista(INTEGER): id que identifica al artista que se desee actualizar sus registros telefónicos.
                telefono
                telefono(INTEGER): referencia al nuevo valor que va a tomar este campo en la tabla Teléfono.

            Retorna:
                str: f"No existen registros para {ci_artista}.", indica que no existen valores para este artista en la tabla Teléfono.

        '''
        existe = self.tienetelefono(ci_artista)
        if existe == True:
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            self.borrar_telefono(ci_artista)
            self.insertar_telefono(ci_artista, telefono)
            conn.commit()
            conn.close()
        else:
            return f"No existen registros para {ci_artista}."

    def borrar_telefono(self, ci_artista):
        '''
            Función encargada de borrar cualquier ocurrencia que exista de un artista en la tabla Teléfono dado su id.

            Atributos:
                ci_artista(INTEGER): es el id que identifica al artista que se desea eliminar de la tabla Teléfono en la base de datos.
        '''
        try:    
            conn = sqlite3.connect("Galería.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Teléfono WHERE  Ci_artista = ?", (ci_artista,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            conn.close()
            return f"Ha ocurrido un error: ", e
        
    
    
    def mostrar_tabla(self, nombre_tabla):
        conn = sqlite3.connect("Galería.db")
        cursor = conn.cursor()

        try:
            # Obtener los datos de la tabla correspondiente al nombre proporcionado
            cursor.execute(f'SELECT * FROM {nombre_tabla}')
            data = cursor.fetchall()

            # Obtener los encabezados de las columnas
            cursor.execute(f'PRAGMA table_info({nombre_tabla})')
            encabezado = [column[1] for column in cursor.fetchall()]

            # Cerrar la conexión a la base de datos
            conn.close()

            return encabezado, data


        except sqlite3.Error as e:
            print(f"Error al mostrar la tabla {nombre_tabla}: {e}")
            conn.close()

          