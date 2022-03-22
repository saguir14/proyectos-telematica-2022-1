from cassandra.cluster import Cluster

class cassandra_db:

    session = {}

    def create_connection(self):
        cluster = Cluster(['127.0.0.1'])
        self.session = cluster.connect('demo')
        print("Connection done...")
        
    def get_all_users(self):
        result = self.session.execute("SELECT * FROM users")
        print("List users: ")
        for i in result:
            print("User: " + i.lastname, i.age, i.city, i.email, i.firstname)
        
    def create_user(self, lastname, age, city, email, firstname):
        self.session.execute("INSERT INTO users (lastname, age, city, email, firstname) VALUES (%s,%s,%s,%s,%s)", [lastname, age, city, email, firstname])
        print("User: " + lastname +  " have been created...")

    def get_user(self, lastname):
        result = self.session.execute("SELECT * FROM users WHERE lastname = %s", [lastname]).one()
        print("User: " + result.lastname, result.age, result.city, result.email, result.firstname)
        
    def update_user(self, new_age, lastname):
        self.session.execute("UPDATE users SET age =%s WHERE lastname = %s", [new_age, lastname])
        print("User " + lastname + " have been updated..")
    
    def delete_user(self, lastname):
        self.session.execute("DELETE FROM users WHERE lastname = %s", [lastname])
        print("User " + lastname + " have been deleted..")
    
bd = cassandra_db()
bd.create_connection()
print("CREATING USER... ")
bd.create_user("Aguirre", 23, "Medellin", "Test1@test.com", "Santiago")
print("CREATING USER... ")
bd.create_user("Gothiel", 40, "Bogota", "Test2@test.com", "Ricardo")
print("GETTING ALL USERS... ")
bd.get_all_users()
print("GETTING SPECIFIC USER... ")
bd.get_user("Gothiel")
print("GETTING SPECIFIC USER AGAIN... ")
bd.get_user("Aguirre")
print("UPDATING USER... ")
bd.update_user(99, "Aguirre")
print("SEEING CHANGES... ")
bd.get_user("Aguirre")
print("DELETING USER... ")
bd.delete_user("Aguirre")
