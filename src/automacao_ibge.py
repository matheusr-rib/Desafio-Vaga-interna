from playwright.sync_api import sync_playwright
import time
import os

## adicionei pausa para melhorar visualização ao vivo 
def pausa(segundos=0.5):
    time.sleep(segundos)

def executar_automacao():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        contexto = navegador.new_context(accept_downloads=True)
        pagina = contexto.new_page()

        # abre site 
        print("Acessando o site")
        pagina.goto("https://sidra.ibge.gov.br/")
        pagina.wait_for_load_state("networkidle")
        pausa(2.5)

       # abre campo de busca
        print("Abrindo o campo de busca...")
        pagina.wait_for_selector('a[title="Pesquisa Tabela"]', timeout=10000)
        pagina.click('a[title="Pesquisa Tabela"]')
        pausa(1.8)

        # confirma que campo de pesquisa existe
        pagina.wait_for_selector('#sidra-pesquisa-lg input[type="text"]', timeout=10000)
        print("Campo de pesquisa apareceu")

        # preenche input
        pagina.fill('#sidra-pesquisa-lg input[type="text"]', "1209")
        pausa(1.2)
        # Aperta enter
        pagina.keyboard.press("Enter")
        # confirma que pagina foi carregada na tabela correta
        pagina.wait_for_selector('h4:has-text("Tabela 1209")', timeout=30000)

        print("Página foi carregada")
        pausa(2)
        # faz filtros do relatorio
        
        pagina.click('span:has-text("60 a 69")',timeout=30000)
        pausa(1)
        pagina.click('span:has-text("70 anos")',timeout=30000)
        pausa(1.5)
        pagina.click('div.sidra-check:has(span:has-text("Brasil")) button.sidra-toggle') 
        pausa(1)
        pagina.click('div.sidra-check:has(span:has-text("Unidade da Federação")) button.sidra-toggle')
        pausa(2)
        # clicando para fazer download
        pagina.click('button[title="Downloads"]',timeout=30000)
        print("Clicou em download")

        # confirma que aba de seleçao de downloads apareceu
        pagina.wait_for_selector('span:has-text("81 valores na seleção")',timeout=30000)
        print("abriu aba de download")
        
        pausa(1.8)
        #preenche com o nome do arquivo desejado e seleciona opçao csv
        pagina.fill('#modal-downloads input[name="nome-arquivo"]', 'populacao_60mais_1209')
        pausa(1.8)
        pagina.select_option('#modal-downloads[style*="display: block"] select[name="formato-arquivo"]', value='br.csv')
        
        # faz download do arquivo
        pausa(1.8)
        with pagina.expect_download() as download_info:
            pagina.click('strong:has-text("Download")')

        download = download_info.value

        # pega o nome real do arquivo baixado automaticamente
        nome_final = download.suggested_filename
        print(f"Nome do arquivo detectado: {nome_final}")

        # manda arquivo baixado para pasta dados
        os.makedirs("dados", exist_ok=True)
        caminho_final = os.path.join("dados", nome_final)
        download.save_as(caminho_final)
        pausa(2.5)

        print(f"Download concluído e salvo em: {caminho_final}")
        
        
        print("Código finalizado")
        pausa(1.5)
        navegador.close()
        

if __name__ == "__main__":
    executar_automacao()
