from  connSql import Galeria

galeria = Galeria()

# print(galeria.insertar_exposicion("Exposicion6", "08/02/2023", "12/01/2023", "Exposicion de literatura contemporanea"))
# print(galeria.insertar_obra(6, "Obra5", "barroco", 22.36, "Exposicion1", 22, "si", 55.24))
print(galeria.insertar_artista(66, "C6", "1F", "P1", "N2"))
# print(galeria.insertar_telefono(22, 22222221))

# print(galeria.tienetelefono(11))
# print(galeria.existelefono(11111111))


# print(galeria.seleccionar_exposicion("Exposicion6"))
# print(galeria.seleccionar_obra(1))
# print(galeria.seleccionar_artista(11))
# print(galeria.seleccionar_telefono(11))

# galeria.actualizar_exposicion("Exposicion6", "Descripción", "Estilo de arte Barroco")
# galeria.actualizar_obra(6, "Precio_salida", 32.32)
# galeria.actualizar_artista(66, "Nacionalidad", "N3")
# galeria.actualizar_telefono(33, "TeléfonoA", 33333331)

# galeria.actualizar_toda_exposicion("Exposicion6", "02/02/2023", "05/02/2023", "Estilo de arte moderno")
# galeria.actualizar_toda_obra(3, "obra2", "contemporaneo", "45.5", "Exposicion2", 22, "no")
# galeria.actualizar_todo_artista(44, "C4", "1D", "P4", "N3")
# galeria.actualizar_todo_telefono(44, 44444444)

# print(galeria.listarExposicion())
# print(galeria.listarObra())
# print(galeria.listarArtista())
# print(galeria.listartelefono())

# print(galeria.borrar_exposicion("Exposicion1"))
# print(galeria.borrar_obra(1))
# print(galeria.borrar_ocurrencia(11))
# print(galeria.borrar_telefono(11))

# print(galeria.listarObra_vendida("Exposicion1"))

# print(galeria.borrar_ocurrencia(44))

print(galeria.mostrar_tabla("Exposición"))
print()
#print(galeria.mostrar_tabla("Obra"))