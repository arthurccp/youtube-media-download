from pytube import YouTube
import os
from formatter_1 import mover_arquivos_e_remover_subpastas  

diretory_music_downloads = r'C:\Users\arthu\OneDrive\Desktop\srcriptDownload\Musicas'
diretory_videos_downloads = r'C:\Users\arthu\OneDrive\Desktop\srcriptDownload\Videos'

def baixar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        if video is not None:
            filename = yt.title + ".mp4"
            output_path = os.path.join(r"C:\Users\arthu\OneDrive\Desktop\srcriptDownload\Videos", filename+"archive")
            video.download(output_path=output_path, filename=filename)
            mover_arquivos_e_remover_subpastas(diretory_videos_downloads)
            print(f"O vídeo foi baixado com sucesso ")
            print("______________________________")

            
        else:
            print(f"Não foi possível obter o vídeo do URL '{url}'.")
    except Exception as e:
        print(f"Ocorreu um erro durante o download do vídeo do URL '{url}': {str(e)}")

def baixar_musica(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_audio_only()

        if video is not None:
            filename = yt.title + ".mp3"
            output_path = os.path.join(r"C:\Users\arthu\OneDrive\Desktop\srcriptDownload\Musicas", filename+"archive")
            video.download(output_path=output_path, filename=filename)
            mover_arquivos_e_remover_subpastas(diretory_music_downloads)
            print(f"A música foi baixada com sucesso")
        else:
            print(f"Não foi possível obter a música do URL '{url}'.")
    except Exception as e:
        print(f"Ocorreu um erro durante o download da música do URL '{url}': {str(e)}")

while True:
    # Menu de escolha
    print("Escolha uma opção:")
    print("1. Baixar Vídeo")
    print("2. Baixar Música")
    print("_________________________________")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        baixar_funcao = baixar_video
    elif opcao == "2":
        baixar_funcao = baixar_musica
    else:
        print("Opção inválida.")
        continue 

    urls = input("Informe os URLs dos conteúdos do YouTube separados por vírgula: ").split(",")

    for url in urls:
        baixar_funcao(url)
print("____`PROCESS__FINISH_____.")

print("_________________________.")
