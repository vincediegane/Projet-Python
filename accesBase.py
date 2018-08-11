#   Acces à une base de données :
import sqlite3
cnx = sqlite3.connect("E:\maBD.sql")
curseur = cnx.cursor()
req = str('CREATE TABLE PERSONNE (nom TEXT,prenom TEXT)')
#enreg = curseur.execute(req)
#for tuple in enreg:
#    print("NOM : ",tuple[1]," PRENOM : ",tuple[2]," AGE : ",tuple[3],"\n")
#curseur.execute("INSERT INTO PERSONNE (nom,prenom) VALUES('FAYE','VINCENT')")
cnx.commit()
cnx.close()
