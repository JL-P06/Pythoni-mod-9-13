import mariadb
conn = mariadb.connect(
    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user='root',
    password='pavell',
    autocommit=True
)
cursor = conn.cursor()