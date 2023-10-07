import PySimpleGUI as sg

################ Layout da janela
container = [
    [sg.Text("Olá, PySimpleGUI!")],
    [sg.Button("Ok")]
]

################ Criação da janela com base no layout definido no "container".
janela = sg.Window("Minha Janela", container) 

################ Loop infinito que mantém a janela aberta.
while True: 
    evento, valor = janela.read() #"Escutador" de eventos que retorna o evento e os valores
    if evento == sg.WIN_CLOSED: # Verifica se o botão foi fechado ao clicar no 'X' de fechar a janela
        break #Encerra o loop

janela.close() #Fecha a janela