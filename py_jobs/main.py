import db_actions

host = 'localhost'
port = '5432'
database = 'postgres'
user = 'postgres'
password = 'pg_admin#123'

connection = db_actions.get_connection(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
print("conneted")
cursor = connection.cursor()
cursor.execute("select * from postgres.public.sampletable")
print("executed")

for row in cursor:
    print(row)


connection.close()