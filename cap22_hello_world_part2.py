#Pregunta por el nombre
name = input("Cual es tu nombre?:")

#Pregunta por la edad
age = input("Cual es la edad?:")

#Pregunta cual es la ciudad
city = input("Cual es la ciudad?:")

#Pregunta que es lo que le gusta hacer
love = input("Que te gusta hacer?:")

#Create output text
string = "Tu nombre es {} y tienes {} anios. Tu vives en {} y te gusta {}"
output = string.format(name, age, city, love)

#Print output to screen
print(output)

