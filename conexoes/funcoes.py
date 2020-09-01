from conexoes import socket_obj
import main


def verificar_novo(atual,obj):
    if atual in obj:
        return 1
    return 0

def montarObjetoControle(ind, cli, idsVei, idsVeicPro,endereco):
    return {
        "indice": ind,
        "cliente": cli,
        "veiculos": idsVei,
        "pveiculos": idsVeicPro,
        "endereco" : endereco
    }

#Funcao baseada nos requisitos do realtrack_json_16025
def enviar(socket_conectado,mensagem):

    if len(socket_conectado["cliente"]) == 0 and len(socket_conectado["veiculos"]) == 0 and len(socket_conectado["pveiculos"]) == 0:
        main.main_io_loop.add_callback(socket_obj.objConnectedUsers[socket_conectado["indice"]]["endereco"].write_message, mensagem)

    elif len(socket_conectado["cliente"]) > 0 and len(socket_conectado["veiculos"]) == 0 and len(socket_conectado["pveiculos"]) == 0:
        if (socket_conectado["cliente"] == mensagem["ras_cli_id"]):
            main.main_io_loop.add_callback(socket_obj.objConnectedUsers[socket_conectado["indice"]]["endereco"].write_message, mensagem)

    elif (len(socket_conectado["veiculos"]) > 0 and len(socket_conectado["pveiculos"]) == 0):
        if mensagem["ras_vei_id"] in socket_conectado["veiculos"]:
            main.main_io_loop.add_callback(socket_obj.objConnectedUsers[socket_conectado["indice"]]["endereco"].write_message, mensagem)

    elif (len(socket_conectado["veiculos"]) == 0 and len(socket_conectado["pveiculos"]) > 0):
        veiculo_proibido = False
        if mensagem["ras_vei_id"] in socket_conectado["pveiculos"]:
            veiculo_proibido = True
        if veiculo_proibido == False:
            main.main_io_loop.add_callback(socket_obj.objConnectedUsers[socket_conectado["indice"]]["endereco"].write_message, mensagem)



#vem mensagem para 2 clientes na msm mensagem ?