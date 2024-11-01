# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com

import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

with open("Main.txt", "r", encoding="utf-8") as file:

    matris = list()
    boyut = int(file.readline().replace("\n",""))

    for i in range(boyut):  # dosyadaki bilgiler adim adim matrise aliniyor
        liste = file.readline().replace("\n", "").split(",")
        matris.append(liste)

alfabe = "ABCDEFGHIJKLMNOPRSTUVYZ"


def gorsel_yazdir(son_liste): # Graphs yapisini gorsel olarak yazdirmaktadir.

    edges = list()
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] != "0":
                edges.append((alfabe[i], alfabe[j]))

    G = nx.DiGraph()
    G.add_edges_from(edges)
    nx.draw_circular(G, with_labels=True)
    plt.savefig("Baslangic_Graphs_yapisi.png")    # python dosyasinin buludugu dizine graphs yapisini "Baslangic_Graphs_yapisi.png" ismiyle yazdirmaktadir.
    plt.show()


    edges = list()
    for i in son_liste:
        edges.append((i[0], i[1]))
    G = nx.DiGraph()
    G.add_edges_from(edges)
    nx.draw_circular(G, with_labels=True)
    plt.savefig("Kruskal_Graphs_yapisi.png")    # python dosyasinin buludugu dizine graphs yapisini "Kruskal_Graphs_yapisi.png" ismiyle yazdirmaktadir.
    plt.show()


def kruskal_algoritmasi():
    kenarlar = list()
    son_liste = list()

    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] != "0":
                liste = list()
                liste.append(alfabe[i])
                liste.append(alfabe[j])
                liste.append(int(matris[i][j]))
                kenarlar.append(liste)


    temp = list()
    for i in range(len(kenarlar)):
        for j in range(0,len(kenarlar)-i-1):
            if kenarlar[j][2] > kenarlar[j+1][2]:
                temp = kenarlar[j]
                kenarlar[j] = kenarlar[j+1]
                kenarlar[j+1] = temp

    kontrol1 = list()
    kontrol2 = list()
    for i in kenarlar:
        temp = 0
        kontrol1 = list()
        kontrol2 = list()
        kontrol1.append(i[1])
        while True:
            for j in son_liste:
                if i[1] == j[1]:
                    temp = 1
                    break
                if j[0] in kontrol1:
                    kontrol2.append(j[1])
            if (i[0] in kontrol2) or (temp == 1):
                break
            if (len(kontrol2) == 0):
                son_liste.append(i)
                break
            kontrol1 = kontrol2.copy()
            kontrol2 = list()

    print("Tum Kenarlar: ",kenarlar)
    print("Kruskal Kenarlar: ",son_liste)

    kenarlar_agirlik = 0
    for i in kenarlar:
        kenarlar_agirlik += i[2]


    kruskal_agirlik = 0
    for i in son_liste:
        kruskal_agirlik += i[2]

    print("Tum Kenarlar Agirlik: ", kenarlar_agirlik)
    print("Kruskal Kenarlar Agirlik: ", kruskal_agirlik)

    gorsel_yazdir(son_liste)
    print("\n***Python Dosyasinin Buludugu Dizine Graphs Yapilari Gorsel olarak Yazdirilmstir.***\n")




print("--------------------------------------------------------------------------------------------------------------")
print("\n***Bilgilendirme: 'txt' Dosyasinda Bulunan '0' Simgesi 'Kenar Yok' Olarak Dergerlendirilecektir***\n")

kruskal_algoritmasi()
