from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi

uri = "mongodb+srv://espiritudeaire:123@cluster0.lg823yo.mongodb.net/conexionpy?retryWrites=true&w=majority&appName=Cluster0"

#client = MongoClient(uri, server_api=ServerApi('1'))

class Usuario:
    def __init__(self, uri = "mongodb+srv://espiritudeaire:123@cluster0.lg823yo.mongodb.net/conexionpy?retryWrites=true&w=majority&appName=Cluster0"):
        self.client = MongoClient(uri)
        self.db = self.client['conexionpy']
        self.usuarios = self.db['Users']
    
    def validar_usuario(self, username, passw):
        """Verificar usuario"""
        usuario = self.usuarios.find_one({"username": username, "pass": passw})
        print("holi", usuario, username, passw)
        return usuario is not None