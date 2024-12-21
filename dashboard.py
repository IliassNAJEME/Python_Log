from matplotlib import pyplot as pl
from nombre_de_tentative import progress, filter
import numpy as np

# Récupération des données
nb_f = progress()
nb_f_d = filter("2024-02-27 21:40:13", "2024-02-28 23:59:00")

# Création de la figure
pl.figure(figsize=(10, 6))

# Graphique 1 : Nombre d'échecs par IP
pl.subplot(221)
pl.title('Nombre d\'échecs par IP')
x = [str(ip) for nb, ip in nb_f]
y = [nb for nb, ip in nb_f]
pl.xlabel("IP")
pl.ylabel("Nombre d'échecs")
pl.bar(x, y)
pl.xticks(rotation=45)  # Rotation des étiquettes de l'axe X
pl.legend(loc='upper left', labels=['Échecs par IP'])

# Graphique 2 : Nombre d'échecs par IP dans une période donnée
pl.subplot(222)
pl.title('Nombre d\'échecs par IP (dates spécifiques)')
a = [str(ip) for nb, ip in nb_f_d]
b = [nb for nb, ip in nb_f_d]
pl.xlabel("IP")
pl.ylabel("Nombre d'échecs")
pl.bar(a, b)
pl.xticks(rotation=45)  # Rotation des étiquettes de l'axe X
pl.legend(loc='upper left', labels=['Échecs par IP (dates spécifiques)'])

# Affichage des graphiques
pl.tight_layout()  # Ajuste le layout pour éviter le chevauchement
pl.show()
