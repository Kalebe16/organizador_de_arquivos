import PySimpleGUI as sg

from funcoes import abrir_meu_github, organizar_pasta

# Adicionando tema de cores.
sg.theme("LightGreen8")


# Definindo layout da Janela
menu_def = [
    ["Opções", ["Desenvolvedor", "Sobre"]],
]


layout = [  
            [sg.Menu(menu_def, font=('Courier 12 bold italic'))],
            [sg.Text(" "*15), sg.Text('Organizador de arquivos', font=('Courier 30 underline'))],
            [sg.Text(" "*26), sg.Image(filename='imgs/icone_arquivos.png')],
            [sg.Text("Escolha o diretório: "), sg.Input("", key="_diretorio_"), sg.FolderBrowse("Procurar")],
            [sg.Button('Organizar'), sg.Button('Sair')]]


# Criando Janela
janela = sg.Window('Organizador de Arquivos', layout, font="Courier 15 bold italic", finalize=True, icon="imgs/icone_principal.ico", return_keyboard_events=True)


while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Sair' or event == "Escape:27": 
        break
    if event == 'Organizar':
        diretorio = (values['_diretorio_']).strip()
        try:
            organizar_pasta(diretorio)
        except NameError:
            sg.Popup("{Calma lá campeão}", 'O diretório "' + diretorio + '" já está super hiper mega power organizado!', font="Courier 13 bold italic", icon="imgs/icone_popup.ico")  
        except FileNotFoundError:
            sg.Popup("{Ops}", 'Parece que este diretório não existe.', font="Courier 13 bold italic", icon="imgs/icone_popup.ico")  
    if event == 'Desenvolvedor':
        abrir_meu_github()
    if event == "Sobre":
        sg.Popup("{Como usar?}", "Selecione uma pasta que esteja bagunçada, clique em 'Organizar', relaxe e deixe que façamos o trabalho duro por você.", font="Courier 13 bold italic", icon="imgs/icone_popup.ico")
        

janela.close()