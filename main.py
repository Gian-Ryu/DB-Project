import mysql.connector

def get_database_connection():
  connection = mysql.connector.connect(user='gianr4',
                                      password='233157387',
                                      host='10.8.37.226',
                                      database='gianr4_db')
  return connection

def execute_statement(connection, statement):
  cursor = connection.cursor()
  cursor.execute(statement)
  results = []

  for row in cursor:
    results.append(row)

  cursor.close()
  connection.close()

  return results

def get_student_schedule(student_id):
  statement = "CALL get_class_info(" + student_id + ")"
  return execute_statement(get_database_connection(), statement)

student_id = input("Choose a student id: ")
results = get_student_schedule(student_id)

for result in results:
   print()
   period = result[0]
   course = result[1]
   room = result[2]
   teacher = result[3]
   print("Period:", period)
   print("Course:", course)
   print("Room:", room)
   print("Teacher:", teacher)
