import re
from database import con
from datetime import datetime

def extract(*urls):
    results = {}
    
    for url in urls:
        data = ''
        try:
            with open(url, 'r') as f:
                data = f.read()
        except Exception as e:
            print(f"Erreur lors de l'ouverture de {url}: {e}")
            continue  # Passe au fichier suivant en cas d'erreur

        # Expression régulière pour extraire les tentatives d'accès échouées
        matches = re.findall(r'(\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2})\sns\ssshd\[\d+\]: Failed password for root from (\d+\.\d+\.\d+\.\d+) port \d+ ssh2', data)
        
        """ L'objectif de ce code est de stocker toutes les tentatives de connexion échouées par adresse IP, 
        et pour chaque IP, on garde une liste des dates auxquelles ces tentatives ont eu lieu. """
        
        for match in matches:
            date = match[0]  # La date de la tentative
            ip_address = match[1]  # L'adresse IP de la tentative
            if ip_address in results:
                results[ip_address].append(date)
            else:
                results[ip_address] = [date]
    
    print(results)  # Affiche les résultats pour vérifier
    return results

# Appel de la fonction avec plusieurs fichiers
results = extract("C:/Users/lenovo/Python/tp_log/auth.log.1",
                  "C:/Users/lenovo/Python/tp_log/auth.log.2",
                  "C:/Users/lenovo/Python/tp_log/auth.log.3",
                  "C:/Users/lenovo/Python/tp_log/auth.log.4")
#print(extract)

""" le role du fonction transforms : Les données de dates dans tes logs sont dans 
un format comme Oct 06 00:04:18. Ce format peut poser des problèmes lors de 
l'insertion dans la base de données ou lors de l'analyse. """
from datetime import datetime

def transform(results):
    for cle, value in results.items():
        # On ajoute un espace entre l'année et le mois
        value_with_year = ["2023 " + t.replace('Oct', ' Oct') for t in value]  # Ajoute un espace avant 'Oct'
        
        datetime_objects = [datetime.strptime(t, "%Y %b %d %H:%M:%S") for t in value_with_year]
        
        formatted_dates = [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in datetime_objects]
        
        results[cle] = formatted_dates
    return results


    """ Avant la transformation : Tu as une date comme Oct 06 00:04:18.
        Après la transformation : La même date devient 2024-10-06 00:04:18. """

trans = transform(results)
#print(trans)

""" la fonction load(data) prend les données extraites de tes fichiers log et les 
insère dans la table T_ip de ta base de données db_ip. C'est une étape clé dans 
le processus d'extraction et de chargement des données, qui te permettra ensuite 
de créer des visualisations à partir des données stockées. """

def load(data):
    for cle,valeur in data.items():
        for t in valeur:
            query='INSERT INTO t_ip (ip,date) values(%s,%s)'
            cursor=con.cursor()
            cursor.execute(query,(cle,t))
            con.commit()
#load(trans)