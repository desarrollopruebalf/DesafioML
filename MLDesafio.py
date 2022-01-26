from __future__ import print_function
from GoogleDrive import find_word
from GoogleDrive import create_file
from menu import options
import os.path
import os
import re


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload



SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        os.remove('token.json')
        #creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API and shows the available files and folders
        results = service.files().list(
            pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        
        if not items:
            print('No se encontraron archivos.')
            return
        print('Listado de ID´s de archivo disponibles:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
            
                
        callmenu="SI"
        while callmenu=="SI" :
            selected=options() 
            if selected[1]=="GET" :             
                #Call find_word to find a word in a file            
                get=selected[0]
                try:
                #GET /search-in-doc/1BvbcmeYcBt_w1NB79KQEyc7G7-_ZpghXIrDk8QAQ5e0?word=python
                    id_file = (re.search('GET \/search-in-doc\/(.+?)\?word\=(.+)', get).group(1))
                    word = (re.search('GET \/search-in-doc\/(.+?)\?word\=(.+)', get).group(2))
                    print ("Usted a seleccionado la palabra \" "+word+ "\" a buscar en  el archivo \""+id_file + "\"")                    
                    resp_continue=input("Desea continuar? Ingrese \"S\" para continuar o \"N\" para volver al menu principal o \"exit\" para terminar:")
                    idexists="NO"
                    if resp_continue == "S" or resp_continue == "s" :
                        for item in items:
                            if id_file==(item['id']) :
                                idexists="SI"
                        if idexists=="SI":                        
                            find_word (id_file,word)
                            break
                        else : 
                            print ("El ID ingresado no existe en el DRIVE")
                    elif resp_continue == "N" or resp_continue == "n" :
                        callmenu="SI"
                    elif resp_continue == "EXIT" or resp_continue == "exit" :
                        exit()
                    else:
                        print ("Para continuar debe ingresar alguna de las opciones validas S , N o exit.")   
                except AttributeError:                    
                    print ("Los valores ingresados no son validos")
                    pass
            elif selected[1]=="POST" :       
                #Creates new files
                post=selected[0]
                try:
                #POST /file {"titulo":"Pagos a prov","descripcion":"Tengo que hacer un pago"}
                    print ("Ha seleccionado la opcion para crear un nuevo archivo")
                    resp_continue=input("Desea continuar? Ingrese \"S\" para continuar o \"N\" para volver al menu principal o \"exit\" para terminar:")
                    if resp_continue == "S" or resp_continue == "s" :
                        folder_id="1aYmhWXShvjHXE4zZ-qnjmwSVXktgwPCr"
                        title = (re.search('POST \/file \{\"titulo\"\:\"(.+)\"\,\"descripcion\"\:\"(.+)\"\}', post).group(1))
                        description = (re.search('POST \/file \{\"titulo\"\:\"(.+)\"\,\"descripcion\"\:\"(.+)\"\}', post).group(2))
                        create_file (title,description, folder_id)
                        break                    
                    elif resp_continue == "N" or resp_continue == "n" :
                        callmenu="SI"
                    elif resp_continue == "EXIT" or resp_continue == "exit" :
                        exit()
                    else:
                        print ("Para continuar debe ingresar alguna de las opciones validas S , N o exit.")   
                except AttributeError:
                    print ("Los valores ingresados no son validos")
                    pass
                
    except HttpError as error:
        # Handle errors from drive API.
        print(f'An error occurred: {error}')
        
    # The file token.json is deleted
    if os.path.exists('token.json'):
        os.remove('token.json')
    
    
if __name__ == '__main__':
    main()