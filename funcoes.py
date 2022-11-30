import os
import webbrowser

tipos_de_arquivos = {

     ".jpg": "imagens",
     ".png": "imagens",
     ".ico": "imagens",
     ".gif": "imagens",
     ".svg": "imagens",
     ".sql": "sql",
     ".exe": "programas",
     ".msi": "programas",
     ".pdf": "pdf",
     ".xlsx": "excel",
     ".xls": "excel",
     ".csv": "excel",
     ".rar": "arquivo",
     ".zip": "arquivo",
     ".gz": "arquivo",
     ".tar": "arquivo",
     ".docx": "palavra",
     ".torrent": "torrent",
     ".txt": "texto",
     ".ipynb": "python",
     ".py": "python",
     ".pptx": "powerpoint",
     ".ppt": "powerpoint",
     ".mp3": "audio",
     ".wav": "áudio",
     ".mid": "áudio",
     ".mp4": "vídeo",
     ".m3u8": "vídeo",
     ".webm": "vídeo",
     ".avi": "vídeo",
     ".mpg": "vídeo",
     ".wmv": "vídeo",
     ".mov": "vídeo",
     ".ts": "vídeo",
     ".json": "json",
     ".css": "web",
     ".js": "web",
     ".html": "web",
     ".apk": "apk",
     ".sqlite3": "sqlite3",
}


def abrir_meu_github():
    meu_site = "https://github.com/Kalebe16"
    webbrowser.open(meu_site)


def organizar_pasta(diretorio):

    # Lista as extensões encontradas no diretorio
    extensoes_encontradas = []
    for arquivo in os.listdir(diretorio):
        nome, extensao = os.path.splitext(arquivo)
        if extensao != "":
            extensoes_encontradas.append(extensao)
            lista_unica_extensoes_encontradas = list(set(extensoes_encontradas)) #removendo itens duplicados
        

    # Cria as pastas correspondentes a cada extensão encontrada no diretorio
    for item in lista_unica_extensoes_encontradas:
        if item in tipos_de_arquivos.keys():
            tipo_de_arquivo = tipos_de_arquivos.get(item)
            print('Encontramos a extensão: ' + item + ' do tipo: ' + tipo_de_arquivo)
        
        if not os.path.exists(diretorio + "/" + tipo_de_arquivo):
            os.mkdir(diretorio + "/" + tipo_de_arquivo)

            

    # Adiciona arquivos em suas respectivas pastas
    for arquivo in os.listdir(diretorio):
        nome, extensao = os.path.splitext(arquivo)
        if extensao == "":
            None
        elif extensao in tipos_de_arquivos.keys():
            try:
                os.rename(f"{diretorio}/{arquivo}", f"{diretorio}/{tipos_de_arquivos.get(extensao)}/{arquivo}")
            except FileExistsError:
                caminho_completo_arquivo = f"{diretorio}/{arquivo}"
                os.remove(caminho_completo_arquivo)
                continue
