from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.files import FileNotUploadedError

directorio_credential = 'credentials_module.json'

# INICIA SESION EN DRIVE
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credential
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credential)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credential)
    credential = GoogleDrive(gauth)
    return credential



# CREAR ARCHIVOS
def create_file(file_name,description,id_folder):
    credential = login()
    file = credential.CreateFile({'title': file_name,\
                                       'description': description,\
                                       'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    file.Upload()
    print ("HTTP/1.1 200 OK")
    print('{\"id\": \"%s\" ,\"title\": \"%s\",  \"description\": \"%s\"}' % ( file['id'],file['title'],file['description']))    

#BUSCAR PALABRA EN ARCHIVO

def find_word (id_file,word):
    credential = login()
    file = credential.CreateFile({'id': id_file})
    file.GetContentFile ('Archivo para buscar palabra.txt')
    
    file = "Archivo para buscar palabra.txt"
    wout = "result.txt"
    findword = word
    w_line = []
    with open(file, "r") as file_read:
        n_line = 0
        existword="NO"
        for r_line in file_read:
            n_line += 1
            r_line = r_line.rstrip()
            split_out = r_line.split(" ")
            if findword in split_out:
                existword="SI"
                 
            
    with open(wout, "w") as file_out:
        for r_line in w_line:
            file_out.write(linea + "\n")
    if existword=="SI" :
        print ("HTTP/1.1 200 OK"," Su palabra se encuentra en el archivo")
    else :
        print ("HTTP/1.1 404 NO ENCONTRADO")