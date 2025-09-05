independance_stages = ["Inicio", "Organizacion", "Resistencia" , "Consolidacion"] #craemos una lista
print(independance_stages[0:]) #imprimimos la lista pero desde el primer elemento hasta el final " : " eso significa rango
print(len(independance_stages)) #imprimimos la longitud de la lista

#List methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
# leaders.extend(independance_stages) #mix the two lists

leaders.insert(1, "Jose Maria Morelos") #insertar en la posicion 1
#leaders.remove("Vicente Guerrero") #remover un elemento el primero que se encuentre en la lista

forth_leader = input("type the forth leader: ") #pedimos un input
leaders.append(forth_leader) #agregamos el input en la lista

# leaders.pop(0) #remueve posiciones especificas de la lista
print(leaders.index("Miguel Hidalgo")) 
print(leaders.count("Vicente Guerrero")) #cuenta cuantas veces aparece el elemento en la lista

print(leaders.sort(leaders)) #ordena alfabeticamente la lista
print(leaders.reverse()) #invierte el orden de la lista

print(leaders)