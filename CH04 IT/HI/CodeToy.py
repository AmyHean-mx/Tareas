#ejercicio 1 Code a Toy
print("Escribe lo que se te pide y pulsa ENTER cuando hayas terminado de escribir")
nombre=input('Ingresa un nombre-- ')                                  #se nombran las variables
puesto=input('Escoge un puesto-- ')                                   #y se pide al usuario que
ad1=input('Elige un adjetivo-- ')                                     #acomplete lo solicitado
ad2=input('Elige un segundo adjetivo-- ')                             
ad3=input('Elige un tercer adjetivo-- ')                              
comida1=input('Escoge un tipo de comida-- ')
comida2=input('Escoge un segundo tipo de comida-- ')
sentimiento=input('¿Qué sentimiento escogerias?-- ')

print("\nEl ejercicio queda así.\n")                                    #se muestra el resultado
print(nombre +' ha comenzado hoy su primer curso de Generation.\n'+
      'Se está formando como '+puesto+'.'+
      '\nA sus compañeros les pareció muy '+ad1+','+
      '\npero su profesor era '+ad2+', cuando menos '+ad3+'.'+
      '\nPara comer comen '+comida1+ ' y '+comida2+ ' mientras repasan sus notas.\n'
      'Sienten '+sentimiento+ ' pero están decididos a completar el curso.\n')

espera=input('Pulsa ENTER para finalizar')                             #espera que el usuario de ENTER para finalizar