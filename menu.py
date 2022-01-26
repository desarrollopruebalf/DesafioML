import re

def options ():

    option=input ("Ingrese un comando / F1 para conocer los comandos disponibles / exit para salir: ")    
    if option=="F1" or option=="f1" :
        print ("Para buscar palabra en archivo ingrese el comando: GET /search-in-doc/1?word=dev") 
        print ("Para buscar crear un archivo ingrese el comando: POST /file {“titulo”:”Pagos a prov”,“descripcion”:”Tengo que hacer un pago”}")
        comand="HELP"
        return option , comand
    elif "GET /search-in-doc/" in option :
                    comand= "GET"
                    #print (re.search('GET \/search-in-doc\/(.+?)\?word\=(.+)', option).group(1))
                    #print (re.search('GET \/search-in-doc\/(.+?)\?word\=(.+)', option).group(2))
                    return option, comand
    elif "POST /file" in option :
                    comand="POST"                    
                    #print (re.search('POST \/file \{\"titulo\"\:\"(.+)\"\,\"descripcion\"\:\"(.+)\"\}', option).group(1))
                    #print (re.search('POST \/file \{\"titulo\"\:\"(.+)\"\,\"descripcion\"\:\"(.+)\"\}', option).group(2))
                    return option, comand                  
    elif option == "EXIT" or option == "exit" :
                    print ("Hasta luego :)")
                    exit()
    else :
        print ("Ninguno de los comandos ingresados es valido.")
        comand="NONVALUE"
        return option , comand
       
"""     
if __name__ == '__main__':
    valor= (options())
    print (valor[1])
"""