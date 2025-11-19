# Desafio Técnico – Automação RPA

**Autor:** Matheus Reis Ribeiro  
**Linguagem:** Python  
**Biblioteca utilizada:** Playwright  

---

## Objetivo

Desenvolver uma automação capaz de navegar pelo site [SIDRA/IBGE](https://sidra.ibge.gov.br/), localizar e configurar a **Tabela 1209 (População por grupos de idade)** e realizar o **download dos dados referentes à população com 60 anos ou mais**, filtrados por **Unidades da Federação (UF)**.

A automação deve simular o comportamento humano, navegando pela interface, aplicando filtros e salvando o arquivo gerado em formato `.csv`.

---

## Tecnologias e Ferramentas Utilizadas

| Tecnologia | Função |
|-------------|--------|
| **Python 3.9+** | Linguagem principal da automação |
| **Playwright (1.56.0)** | Biblioteca de automação de navegador |
| **time** | Pausas manuais para simular interação humana |
| **os** | Criação de diretórios e manipulação de arquivos |

---

## Estrutura do Projeto

Desafio-Vaga-interna/
├── src/
│ ├── automacao_ibge.py # Script principal da automação
│ ├── main.py # Executa a função principal
│ └── dados/
│ └── .gitkeep # Mantém a pasta no repositório
├── requirements.txt # Dependências do projeto
├── .gitignore
└── README.md # Documento de explicação e execução

---

## Lógica e Estratégia Adotada

A automação foi construída visando simular uma manipulação manual do DOM com a interação do usuário.  
Sendo assim, utilizei as seguintes funções visando simular o comportamento humano:

- **`click()`** – Realiza um clique.  
- **`fill()`** – Preenche texto em um campo de input textual.  
- **`keyboard.press()`** – Aperta uma tecla do teclado.  
- **`select_option()`** – Seleciona uma opção em um menu suspenso (`<select>`).

Para verificar e aguardar o carregamento de elementos após navegações no site, utilizei:  

- **`wait_for_load_state("networkidle")`** – Aguarda até que todas as requisições de rede estejam concluídas (ou seja, o site terminou de carregar completamente).  
- **`wait_for_selector()`** – Espera até que o elemento especificado pelo seletor esteja presente e visível na página.

---

### 1. Início e busca da tabela

- Acessa a página inicial do SIDRA.  
- Abre o campo de busca.  
- Digita “1209” e pressiona Enter.  
- Aguarda o carregamento da tabela.

### 2. Configuração da tabela

- Seleciona as faixas etárias “60 a 69” e “70 anos ou mais”.  
- Desmarca o nível territorial “Brasil”.  
- Marca “Unidades da Federação”.

### 3. Download dos dados

- Abre o modal de Downloads.  
- Define o nome do arquivo como `populacao_60mais_1209`.  
- Seleciona o formato CSV (BR).  
- Aguarda o evento de download e salva automaticamente em:

dados/populacao_60mais_1209.csv

### 4. Simulação humana

- Foram adicionadas pausas (`time.sleep`) entre ações para simular tempo de leitura, carregamento e interação humana realista.  
- Também foi usada a propriedade `headless=False` para visualização ao vivo durante a execução.

---

## Como Executar o Projeto

### 1. Clonar o repositório


git clone https://github.com/matheusr-rib/Desafio-Vaga-interna.git
cd Desafio-Vaga-interna/src
2. Criar e ativar ambiente virtual
python -m venv venv
Ativar no Windows:

venv\Scripts\activate
Ativar no Linux/macOS:


source venv/bin/activate
3. Instalar dependências

pip install -r requirements.txt
Instalar navegadores necessários:

playwright install
4. Executar a automação

python main.py
Após a execução, o arquivo será salvo automaticamente em:
src/dados/populacao_60mais_1209.csv
Dependências Utilizadas
Arquivo requirements.txt:

playwright==1.56.0

Principais Desafios Encontrados

O site possui elementos HTML idênticos	Foram utilizados seletores compostos com :has() e :has-text() para garantir que o elemento correto fosse acessado.
O site pode apresentar demoras no carregamento	Foram utilizadas funções de espera explícitas (wait_for_selector, wait_for_load_state) para garantir o carregamento dos elementos antes de avançar para o próximo passo.

Resultado Final

A automação acessa a tabela 1209
Filtra “60 anos ou mais” por UF

Baixa o arquivo CSV e o salva em:
dados/populacao_60mais_1209.csv
