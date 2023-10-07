import PySimpleGUI as sg
import requests
##############
def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None
##############
modelo = [
    [sg.Text('Pegar cotação da moeda')],
    [sg.InputOptionMenu(['BTC', 'USD', 'EUR'], size=(20,2), key='opcao')],
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')]
]

janela = sg.Window('Sistema de cotações', modelo)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores['opcao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f"A cotação de {codigo_cotacao} é {cotacao}")
        


janela.close()