import sqlite3

connection = sqlite3.connect('organizationdb.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS counts')
cursor.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

filename = 'mbox.txt'
data = open(filename)

dbPackage = dict()

for line in data:
    if not line.startswith('From') or line.count(' ') != 1:
        continue
    organization = line.split()[1].split('@')
    print(organization[1])
    dbPackage[organization[1]] = dbPackage.get(organization[1], 0) + 1

for organization, count in dbPackage.items():
    cursor.execute('INSERT INTO Counts(org, count) VALUES(?, ?)', (organization, count))
    print('Inserted', organization, 'with count of', count, 'into database')

connection.commit()
print('The changes have been commited to the database')