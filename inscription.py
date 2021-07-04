from numpy import quantile
import psycopg2
import psycopg2.extras
from face_shot import shot



# creation de DB si il n'existe pas
"""def create_db():
    infos = ["192.168.227.134","person","postgres","1256"]
    conn = psycopg2.connect(dbname=infos[1], user=infos[2], password=infos[3], host=infos[0])
    if conn:
        print("Creating Database...")
    cnx = conn.cursor()
    cnx.execute("CREATE TABLE Personne (id SERIAL PRIMARY KEY, firstName VARCHAR, lastName VARCHAR, age VARCHAR);")
    conn.commit()
    cnx.close()
    conn.close()"""


def con(fname,lname,age):
    infos = ["192.168.227.134","person","postgres","1256"]

    conn = psycopg2.connect(dbname=infos[1], user=infos[2], password=infos[3], host=infos[0])
    
    if conn:
        print("you're connected...")

    cnx = conn.cursor()
    #cnx.execute(f"INSERT INTO Personne (firstName,lastName, age) VALUES({fname},{lname},{age})")
    cnx.execute("SELECT firstName,lastName FROM Personne WHERE firstName=%s AND lastName=%s",(fname,lname))
    query = cnx.fetchall()
    if not query:
        print("insertion dans la table....")
        cnx.execute('INSERT INTO Personne (firstName, lastName, age) VALUES (%s, %s, %s)',(fname, lname, age))
    # Sauvegarde des enregistrements..
    conn.commit()
    # Fermer la connection
    cnx.close()
    conn.close()


    
