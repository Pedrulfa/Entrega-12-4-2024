def crear_Estructura(names,goles,golesE,assist,dic):
    for i in range(len(goles)):
        estadisticas = [goles[i],golesE[i],assist[i]]
        dic[names[i]] = estadisticas

def conocer_Jugador(nombre,dic):
    nombre = nombre.strip().upper()
    print("Jugador:",nombre,"Goles:",dic[nombre][0])

def jugador_mas_influyente(dic):
    prom = [(nombre,float (((estadisticas[0]*1.5) + (estadisticas[1]*1.25) + estadisticas[2])/3)) for nombre,estadisticas in dic.items()]
    max_value= max(prom,key= lambda x: x[1])
    return max_value[0]

def promedio_goles_equipo(dic):
    prom= sum(estadisticas[0] for estadisticas in dic.values())
    return prom/25

def  promedio_goles_jugador(nombre,dic):
    nombre = nombre.strip().upper()
    return dic[nombre][0]/25
