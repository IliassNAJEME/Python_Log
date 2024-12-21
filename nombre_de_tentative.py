from database import con

""" cette fonction te permet d'obtenir le nombre de fois qu'une adresse IP 
apparaît dans ta table, ce qui est utile pour analyser les accès enregistrés """

def progress()->list[tuple[int,str]]:
    query="select COUNT(*),ip from t_ip GROUP BY ip;"
    cursor=con.cursor()
    cursor.execute(query)
    #print(cursor.fetchall())
    return cursor.fetchall()
#progress()

def filter(date_1,date_2)->list[tuple[int,str]]:
    query="select COUNT(*),ip from T_ip where date>='" + str(date_1) +"' AND date<='" + str(date_2) + "' GROUP BY ip;"
    cursor=con.cursor()
    cursor.execute(query)
    #print(cursor.fetchall())
    return cursor.fetchall()
#filter("2024-02-27 21:40:13","2024-02-28 23:59:00")