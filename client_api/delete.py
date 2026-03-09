import requests

id =input("entrez l'identifiant du produit a supprimer:")
endpoint = f"http://127.0.0.1:8000/product/{id}/delete/"
response =requests.delete(endpoint)
print(response.status_code,response.status_code==204)
# response.status_code==204: renvoies vrai ou faux