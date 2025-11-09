# Import required modules
import csv
import sqlite3
import sys
import zipfile
import os

class DatabaseManager:
	# creating DatabaseManager object
	def __init__(self,argv, database_file):
		self.argv=argv
		self.database_file = database_file
	
	#connect to database or create if doesn't exist
	def create_database(self):
		with sqlite3.connect(self.database_file) as conn:

			# interact with database
			cursor = conn.cursor()
			
			# open zipfile
			with zipfile.ZipFile('world.zip', 'r') as z:
				
				# selects command line parameters (0th is script name)
				for index in range(1, len(self.argv)):
					file_name = self.argv[index]
					# separates table name from extension
					table_name = file_name.split(".")[0]
					
					# check if table exists
					cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
					if cursor.fetchone():
						print(f"Table {table_name} already exists. Skipping creation.", file=sys.stderr)
						continue
					
					# extraxts file from zip (will be deleted later - temporary file)
					z.extract(file_name)
					with open(file_name, "r") as csvfile:
						# values are separated with ; instead of ,
						contents = csv.reader(csvfile, delimiter=";")
						
						# reads table header
						fields = next(contents)
						# Field1 TEXT, Field2 TEXT, ...
						fields_defs = ", ".join([f'"{f}" TEXT' for f in fields])
						# build SQL query to create table
						create_table = f'CREATE TABLE "{table_name}" ({fields_defs})'
		
						# creates table
						cursor.execute(create_table)
						
						# Field1, Field2, Field3, ...
						fields_comma_separated = ", ".join([field for field in fields])
						# ?, ?, ?, ... (? will be replaced with real value)
						questionmarks_comma_separated = ", ".join('?' for _ in fields)
						# builds SQL query to insert values into database
						insert_records = f'INSERT INTO "{table_name}" ({fields_comma_separated}) VALUES({questionmarks_comma_separated})'

						# inserts values into table
						cursor.executemany(insert_records, contents)
					
					# delete extracted file
					os.remove(file_name)

	# find all spanish speaking countries
	def find_spanish_speaking_countries(self):
		# connect to database
		with sqlite3.connect(self.database_file) as conn:
			# creating a cursor object to execute SQL queries on a database table
			cursor = conn.cursor()
			# creates query
			query = '''
				SELECT country.Name 
				FROM country, countrylanguage 
				WHERE country.Code = countrylanguage.CountryCode
				AND countrylanguage.Language = 'Spanish'
				ORDER BY country.Name
				'''
			cursor.execute(query)
			results = cursor.fetchall()
			# prints question and results
			print("In what countries is used the Spanish language? Provide their full names, sorted alphabetically.")
			for result in results:
				print(result[0])
	
if __name__ == "__main__":
	dm = DatabaseManager(sys.argv, "db.sqlite")
	dm.create_database()
	dm.find_spanish_speaking_countries()