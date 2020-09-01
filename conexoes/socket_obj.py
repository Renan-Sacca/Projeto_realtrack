import tornado.web
import tornado.websocket
import tornado.ioloop
import json
from conexoes import funcoes
 
objConnectedUsers = {} # Variavel para guardar os objetos
objIdSocket = {} # Variavel para guardar indice e id do objeto
# Qual compensa mais, usar uma variavel pra guardar e usar função in na hora de deletar ou usar um for
# para percorrer todos objetos na hora de excluir ?

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    
    def initialize(self):
        global objConnectedUsers
        global objIdSocket


    def open(self):
        print("Novo cliente conectado")



    def on_close(self):
        del objConnectedUsers[objIdSocket[self]]
        del objIdSocket[self]

        print("Cliente desconectado")


    def on_message(self, message):
        self.write_message(u"Conectado: ")


        #CASO O CLIENTE NUNCA MANDE MENSAGEM ALEM DA ENTRADA REMOVER IF E FUNÇÂO VERIFICAR

        existente = funcoes.verificar_novo(self, objIdSocket)
        if existente == 0:
            idCliente = ''
            idsVeiculos = []
            idsVeiculosProibidos = []
            dados = json.loads(message)

            if "cliente" in dados and dados["cliente"] != "":
                idCliente = dados["cliente"]

            if "veiculos" in dados and type(dados["veiculos"]) is list:
                idsVeiculos = dados["veiculos"]

            if "pveiculos" in dados and type(dados["pveiculos"]) is list:
                idsVeiculosProibidos = dados["pveiculos"]

            objConnectedUsers[dados["indice"]] = funcoes.montarObjetoControle(dados["indice"],idCliente,idsVeiculos, idsVeiculosProibidos,self)
            objIdSocket[self] = dados["indice"]

    def check_origin(self, origin):
        return True


    """
    "objSocket":{
      "indice":502117,
      
      OQUE FAZER COM ESSES HOSPEDES ? 
      "hospedes":[
         "502208",
         "502282",
         "502346",
         "502117"
      ]
   }    
    """
