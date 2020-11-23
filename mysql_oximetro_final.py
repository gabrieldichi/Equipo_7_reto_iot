import mysql.connector
import random

nameList = [ "Octavio","Javier","Gabriel","Kevin","Luis","Lulu","Ian","Kirby","Tom","Mario"]
lastNameList = [ "Navarro","Dichi","Corona","Lopez","Vazques","Bros","Kohn","Yamamoto","Riddle"]

def RamdomData(cnx, cursor):
    letra = "A"
    for i in range(1, 11):
      num_matricula = random.randint(0, 10000000)
      result = str(num_matricula)
      Matricula = letra+result
      Name = random.choice(nameList)
      Last = random.choice(lastNameList)
      query_data = (Matricula, Name, Last)      
      query = ("insert into Alumno (Matricula,Nombre,Apellido) values(%s,%s,%s);")
      print(query)
      cursor.execute(query, query_data)
    '''for i in range(0, 1):
        n =random.randint(80,99)
        query_data = (Matricula, n)
        query = ("insert into Historial_oxigeno (Matricula, Nivel_oxigeno) values(%s,%s);")
        print(query)
        cursor.execute(query, query_data)''' 

    query = ("select Matricula from Alumno")
    cursor.execute(query) 
    Lista_Matriculas = [result[0] for result in cursor]

    for i in range(0, 5000):
        mes2 = "-09-2020"
        num_oxigenacion =random.randint(80,99)
        num_fecha =random.randint(1,30)
        date = str(num_fecha) + mes2
        Matricula = random.choice(Lista_Matriculas)
        query_data = (Matricula, num_oxigenacion, date)
        query = ("insert into Historial_oxigeno (Matricula, Nivel_oxigeno, Fecha) values(%s,%s,%s);")
        print(query)
        cursor.execute(query, query_data) 
    for i in range(0, 5000):
        mes = "-11-2020"
        num_cardiaco =random.randint(60,240)
        num_fecha =random.randint(1,30)
        date = str(num_fecha) + mes
        Matricula = random.choice(Lista_Matriculas)
        query_data = (Matricula, num_cardiaco, date)
        query = ("insert into Historial_cardiaco (Matricula, Ritmo_cardiaco, Fecha) values (%s,%s,%s);")
        print(query)
        cursor.execute(query, query_data) 
    

    cnx.commit()

try:
    cnx = mysql.connector.connect(user='root', password='JC181818', host='127.0.0.1', database='Oximetro')
    cursor = cnx.cursor()
    
    RamdomData(cnx, cursor)


except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    #print(query)
    
finally:
  if 'cnx' in locals() or 'cnx' in globals():
    cnx.close()


