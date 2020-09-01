import pika
import json
from conexoes import socket_obj
import threading
from conexoes import funcoes


def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    threading.Lock()

    # Obrigatoriamente deve existir (ras_eve_id_indice,ras_mon_hospedeiro) mesmo que não aja valor se não codigo ira dar erro
    # VERIFICAR JSON DO RABBIT E ALTERAR ras_eve_id_indice
    if mensagem["ras_eve_id_indice"] in socket_obj.objConnectedUsers:
        funcoes.enviar(socket_obj.objConnectedUsers[mensagem["ras_eve_id_indice"]],body)


    # ras_mon_hospedeiro, perguntar se é so um hospedeiro ou uma lista de hospedeiro
    # esse codigo so funcionara se for 1 hospedeiro
    if mensagem["ras_mon_hospedeiro"] in socket_obj.objConnectedUsers:
        funcoes.enviar(socket_obj.objConnectedUsers[mensagem["ras_mon_hospedeiro"]], body)
    threading.RLock()


def procurar():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_consume(queue='testerenan', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

