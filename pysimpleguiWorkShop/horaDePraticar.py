import requests
import PySimpleGUI as sg

from numba import jit



@jit
def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        return "Código de Moeda Inválido"

layout =[
    [sg.Text('Cotações das moedas Hoje!')],
    [sg.InputOptionMenu(['BTC','USD','EUR'], size= (20,2), key='opcao'),sg.Button('Pesquisar')],
    [sg.Text('',key='saida')]
]

janela = sg.Window("buscar cotações", layout)

while True:
    evento , valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Pesquisar':
        cotacao = valores['opcao']
        moeda = pegar_cotacoes(cotacao)
        janela['saida'].update(moeda)
        while True
            while True

        

janela.close() #Fecha a janela

