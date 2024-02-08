from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gauth.SaveCredentialsFile('creds.txt')

print(f'creds.text File has been created. Check the file')
