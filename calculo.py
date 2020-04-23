#Obtener diferentes incgnitas de la tasa de la prueba del acido
# Tasa = (activo - inventario) / pasivo

def getTasa(activo, inventario, pasivo):
    return ( activo - inventario ) / pasivo

def getActivo(inventario, pasivo, tasa):
    return ( tasa * pasivo ) + inventario

def getPasivo(activo, inventario, tasa):
    return ( activo - inventario ) / tasa

def getInventario(activo, pasivo, tasa):
    return  activo - ( tasa * pasivo )
