# Proyecto # 1
# Base de datos distribuida simple k,v (SDBKV)

En este Folder se encuentra el codigo de la realizacion del Proyecto #1. ademas se indican los requisitos para su correcto funcionamiento
y los comandos para la correcta ejecucion de este. 

## Requisitos

Los requisitos para este Proyecto son los siguientes:

- Python 3.9.6
- Docker 20.10.12
- Docker-compose 1.29.2
- Cassandra 4.0.3

## Ejecucion

Para la correcta ejecucion de este codigo se debe de realizar de la siguiente manera: 

Primero que todo se debe de ejecurtar el **Docker-compose.yml** con el siguiente comando:

```
$ docker-compose up 
```

**Actualmente solo se crean 2 nodes, si se desea crear mas nodos tener en cuenta la memoria asignada par este proceso**
 
Despues de ejecutar este archivo hay dos maneras de realizar las operaciones en Cassandra una es a traves de CQLSH dentro del contenedor de Docker
y la segunda es ejecutando el archivo de python adjunto.

**Para realizar las operaciones a traves de CQLSH en una nueva terminal se ejecuntan los siguientes comandos**

```
$ docker ps                                  //Con este comando se mostraran la informacion de los contenedores
$ docker exec -it [CONTAINER NAME] cqlsh     // de esta manera se ingresa al contenedor donde se encuentra la imagen de Cassandra
```

**Para realizar las operaciones a traves del archivo de python se realizan los siguiente comandos**
En una terminal nueva ser ejecuta 
```
Python client.py
```


``` py 
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
```

**Integrantes**
 - Santiago Aguirre Delgado
 - Ricardo Gottheil Florez
 - Juan Diego Restrepo 
 