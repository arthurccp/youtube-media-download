import os
import shutil

def mover_arquivos_e_remover_subpastas(diretorio):
    # Verifica se existem pastas dentro do diretório
    if not os.path.exists(diretorio) or not any(os.path.isdir(os.path.join(diretorio, f)) for f in os.listdir(diretorio)):
        print(f"Nenhuma pasta encontrada em {diretorio}")
        return

    # Percorre os elementos dentro do diretório
    for elemento in os.listdir(diretorio):
        caminho_elemento = os.path.join(diretorio, elemento)

        # Verifica se o elemento é um diretório
        if os.path.isdir(caminho_elemento):
            # Move os arquivos dentro do diretório para o diretório pai
            for pasta_raiz, _, arquivos in os.walk(caminho_elemento):
                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                    destino_arquivo = os.path.join(diretorio, arquivo)
                    if not os.path.exists(destino_arquivo):
                        try:
                            shutil.move(caminho_arquivo, destino_arquivo)
                            print(f"Arquivo '{arquivo}' movido para '{diretorio}'")
                        except Exception as e:
                            print(f"Erro ao mover '{arquivo}': {str(e)}")
            
            # Remove a pasta vazia se estiver vazia após a movimentação de arquivos
            if not os.listdir(caminho_elemento):
                try:
                    os.rmdir(caminho_elemento)
                    print(f"Pasta '{elemento}' removida.")
                except Exception as e:
                    print(f"Erro ao remover '{elemento}': {str(e)}")
