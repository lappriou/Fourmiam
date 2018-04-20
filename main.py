import os
from graph_manager import *
import pants as p
import math as math
import random as r
import csv
import matplotlib.pyplot as mt
import networkx as network


#Attribution des constantes nécessaires
CATEGORY = 0
NAME = 1
TOWN = 4
TENANT = 6
ABOUTISSANT = 7
BI_MIN = 8
BP_MIN = 9
BI_MAX = 10
BP_MAX = 11
DATE_CREATE = 11
DATE_UPDATE = 12

PATHFILESMALL = "VOIES_NM2.csv"
PATHFILEBIG = "VOIES_NM.csv"
#Initialisation du graph
graph = network.Graph()

ANT_NUMBER_FITNESS = 10

#Import du fichier CSV contenant les données à étudier
with open(PATHFILESMALL) as csv_file:
	reader_file = csv.reader(csv_file)
	count = 0
	for line in reader_file:
		if count > 1:
            if(line[TENANT] != "" and line[ABOUTISSANT] != "")
                if (line[BI_MIN] == ""):
                    line[BI_MIN] = 1
                else:
                    line[BI_MIN] = int(line[BI_MIN])
                if (line[BP_MIN] == ""):
                    line[BP_MIN] = 2
                else:
                    line[BP_MIN] = int(line[BP_MIN])
                if (line[BI_MAX] == ""):
                    line[BI_MAX] = line[BI_MIN]
                else:
                    line[BI_MAX] = int(line[BI_MAX])
                if (line[BP_MAX] == ""):
                    line[BP_MAX] = line[BP_MIN]
                else:
                    line[BP_MAX] = int(line[BP_MAX])

            #Calcul du poids de chaque rue
            pods = max(((line[BI_MAX] - line[BI_MIN])/2)+1, ((line[BP_MAX] - line[BP_MIN])/2)+1)

            name_full = line[TOWN] + " " + line[NAME]

            #Ajout d'une arrête et des liens entre les noeuds
            graph.add_edge(line[TENANT], line[ABOUTISSANT], weight=pods, label=name_full, pheromone=0)


pos = network.spring_layout(graph)

#Permet de dessiner le graph
network.draw_networkx_edges(graph, pos)
network.draw_networkx_labels(graph, pos)
network.draw_networkx_nodes(graph, pos)
network.draw_networkx_edge_labels(graph, pos)

#Affiche le graph. (si des "draw_xxx" ont été réalisés)
mt.show()

#Initialisation des rues de départ et de livraisons
print("Indiquer une rue de départ")
street_start = input()
print("Indiquer le nombre de points de livraison")
number_street_delivery = input()

for i in range(int(number_street_delivery)):
	print("Indiquer une rue de livraison")
	streets_delivery[i] = input()


#Creation d'une fourmi
def create_ant(id_ant, street_start, streets_delivery):
	ant["numero"] = id_ant
	ant["rue_depart"] = street_start
	ant["rues_livraisons"] = streets_delivery
	ant["rues_empruntés"] = ""
	ant["distance"] = 0
	return ant

#Méthode de travail d'une fourmi
def walk(graph, ant):
	#Tant que on est pas passé par toutes les rues
	while(count(array_intersect(ant["rues_empruntés"], ant["rues_livraisons"])) != count(fourmi["rues_livraisons"])):
		#On considère que la rue de départ est une arrête

		#On prend un noeud aléatoire sur les deux noeuds existants
		node = graph.edges()[ant["rue_depart"]][r.randint(0,1)]
		
		#On va dans un nouvel rue / on récupère la données et ses propriétés
		#Ici, on prend un random, mais pour que les fourmis
		new_street = graph.nodes()[node["label"]][r.randint(0,(len(node["label"])-1))]

		#On ajout une marque à la rue
		graph.edges()[new_street[TENANT]][new_street[ABOUTISSANT]]["pheromone"] += 1

		ant["rues_empruntés"] += new_street
	
	return ant

#Toutes les X fourmis, le phéromone s'évapore/se dissipe
def fitness(graph, ant, i):
	if (i % ANT_NUMBER_FITNESS == 0):
		for u,v,d in graph.edges(data=True):
			d["pheromone"] - 1

	return graph

#Création des fourmis
print("Indiquer le nombre de fourmi voulu")
number_ant = r.randint(1,10)

for i in range(number_ant):
	ant = create_ant(i, street_start, streets_delivery)
	ant = go_work(graph, ant)
	graph = fitness(graph, ant, i)


network.draw_networkx_edge_labels(graph, pos)

os.system("pause")


