from Item import Item
class ControlInventario:
    @staticmethod
    def usaItem(inventario:list[Item],nombre):
        existeUbicacion = ControlInventario.ubicarPorNombre(inventario,nombre)
        if(existeUbicacion[0]):
            inventario[existeUbicacion[1]].UsarObjeto()

    @staticmethod
    def AñadeOSobreescribe(inventario:list[Item],nombre,poder,cantidad):
        existeUbicacion = ControlInventario.ubicarPorNombre(inventario,nombre)
        if(existeUbicacion[0]):
            inventario[existeUbicacion[1]] = Item(nombre,poder,cantidad)
        else:
            inventario.append(Item(nombre,poder,cantidad))
    @staticmethod
    def ubicarPorNombre(inventario:list[Item],nombre):
        arregloDeNombres = []
        for item in inventario:
            arregloDeNombres.append(item.name)
        existeNombre=False
        ubicacion=-1
        for indexNombre in range(len(arregloDeNombres)):
            if(arregloDeNombres[indexNombre]==nombre):
                existeNombre=True
                ubicacion=indexNombre
        return (existeNombre,ubicacion)
