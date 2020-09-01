
import pika
import random

#criando conexao
conexao = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexao.channel ()

#criando fila
#channel.queue_declare (queue = 'testerenan')

#exchange é o nome da troca
#routing key nome da fila
i=0

while i <10:
    a = random.randrange(0,2)
    if a == 1:
        a='{"ras_mon_hospedeiro":"5697","ras_cli_desc":"Velomarques Transportes","ras_cli_id":"149267","ras_eal_id":"0","ras_eat_descricao":"","ras_eve_comb_analogico":{},"ras_eve_combustivel":{},"ras_eve_data_enviado":"02/04/2020 12:03:43","ras_eve_data_gps":"02/04/2020 12:03:43","ras_eve_data_servidor":"02/04/2020 12:03:43","ras_eve_id_evento_sintetico":"0","ras_eve_id_indice":"9350","ras_eve_ignicao":"0","ras_eve_latitude":"-23.2755089","ras_eve_longitude":"-45.9674711","ras_eve_satelites":"6","ras_eve_temp_analogico":{},"ras_eve_temperatura":{},"ras_eve_validade":"0","ras_eve_velocidade":"0","ras_mot_nome":"PADRAO","ras_prd_cat":"0","ras_prd_id":"155","ras_ras_data_ult_comunicacao":"02/04/2020 12:03:43","ras_ras_id":"318940","ras_ras_id_aparelho":"358735074820894","ras_vei_horimetro":"0","ras_vei_id":"376320","ras_vei_odometro":"283996000","ras_vei_placa":"DPB 9716","ras_vei_tag_identificacao":"DPB - 9716 ","ras_vei_tipo":"3","ras_vei_veiculo":"Caminhão Ford","ras_vei_velocidade_limite":"90","status_acoes":[]}'
        channel.basic_publish (exchange = 'renan',
                              routing_key = 'testerenan',
                              body = a)

    else:
        a ='{"ras_mon_hospedeiro":"5680","ras_cli_desc":"JBS FOODS","ras_cli_id":"15240","ras_eal_id":"0","ras_eat_descricao":"","ras_eve_comb_analogico":{},"ras_eve_combustivel":{},"ras_eve_data_enviado":"02/04/2020 12:00:58","ras_eve_data_gps":"02/04/2020 12:00:58","ras_eve_data_servidor":"02/04/2020 12:03:45","ras_eve_id_evento_sintetico":"0","ras_eve_id_indice":"3333","ras_eve_ignicao":"1","ras_eve_latitude":"-23.558338","ras_eve_longitude":"-47.809726","ras_eve_satelites":"12","ras_eve_temp_analogico":{},"ras_eve_temperatura":{},"ras_eve_validade":"1","ras_eve_velocidade":"49","ras_mot_nome":"PADRAO","ras_prd_cat":"0","ras_prd_id":"28","ras_ras_data_ult_comunicacao":"02/04/2020 12:03:45","ras_ras_id":"79484","ras_ras_id_aparelho":"1831155754","ras_vei_horimetro":"0","ras_vei_id":"69349","ras_vei_odometro":"0","ras_vei_placa":"AZZ-7268","ras_vei_tag_identificacao":"AZZ-7268","ras_vei_tipo":"3","ras_vei_veiculo":"J.MARIANO","ras_vei_velocidade_limite":"140","status_acoes":[]}'
        channel.basic_publish(exchange='renan',
                              routing_key='testerenan',
                              body=a)
    print ( "[x] Enviado ",a )
    i += 1

conexao.close ()