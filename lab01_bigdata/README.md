# LAB 01


## Prerrequisitos

 -   Tener el cluster corriendo en EMR, así como tambien una conexión ssh desde una terminal al master.
    
-   Clonar el repositorio con los datos a copiar dentro de la instancia del master. https://github.com/st0263eafit/st0263_20212.git
    
 

## GUIA


Procederemos, desde nuestra instancia, a escribir el comando para poder crear una carpeta

```
user@master$ hdfs dfs -mkdir /user/<username>/datasets

```

Una vez creada la carpeta, usaremos el comando para copiar los datos desde la carpeta datasets del repositorio clonado, hasta nuestra cuenta en hadoop previamente creada.

    user@master$ hdfs dfs -copyFromLocal /datasets/* /user/<username>/datasets/
    



![image](https://user-images.githubusercontent.com/35736499/143804349-a4d9c995-6693-405c-b044-f6d1d34e846b.png)


   
   

