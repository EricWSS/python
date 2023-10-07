##################################### Tela gráfica para capturar cotação de moédas
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

""" modelo2 = [
    [sg.Text('Pegar cotação da moeda')],
    [sg.InputOptionMenu(['BTC', 'USD', 'EUR'], size=(20,2), key='opcao')],
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
    [sg.Multiline('', False,s=(15,8)), sg.Column([[sg.Button('teste1')], [sg.Button('teste2')]])]
] """

""" 
layout2 = [
    [sg.Text('Teste')],
    [sg.InputOptionMenu(['ex1','ex2'], size=(20,1)), sg.Button('Bt1')],
    [sg.Multiline('', s=(15,8))],
    [sg.Multiline('',s=(15,8)), sg.Column([[sg.Button('Bt2')],[sg.Button('Bt3')]])]
]

layout1 = [
    [sg.Text()],
    [sg.InputOptionMenu(), sg.Button()],
    [sg.Multiline()],
    [sg.Multiline(), sg.Column([[sg.Button()],[sg.Button()]])]
] """


""" layout3 = [
    [sg.Text('Pegar cotação da moeda')],
    [sg.InputOptionMenu(['BTC', 'USD', 'EUR'], size=(20,2), key='opcao')],
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
    [sg.Multiline('', False,s=(15,8)), sg.Column([[sg.Button('teste1')], [sg.Button('teste2')]])]
] """
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

