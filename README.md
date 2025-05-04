# MCP-Server para gerar ideias de conteúdos

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como instalar no Claude Desktop](#como-instalar-no-claude-desktop)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

Este projeto `mcp_content` cria uma ferramenta simples para ajudar na organização de ideias para posts e vídeos. Ele gera uma lista estruturada com um tema principal, cinco subtemas e três microtemas para cada subtema, facilitando a criação de conteúdos variados. Além disso, o programa lê um arquivo de exemplo que mostra essa estrutura na prática.

## Estrutura do projeto

Este projeto leva em consideração as explicações do professor Sandeco Macedo, da UFG (Universidade Federal de Goiás), sobre MCPs por meio do livro [MCP e A2A para Leigos
](https://physia.com.br/mcp/). É um MCP-Server simples que utiliza somente o pacote FastMCP, seguindo também as orientações do repositório oficial do [Model Context Protol](https://github.com/modelcontextprotocol/python-sdk), da Anthropic.

Como referência para a ideia deste MCP-server, está este prompt que fiz: [Matriz de Conteúdo](https://github.com/marioluciofjr/prompts/blob/main/matriz_de_conteudo.md)

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/c0604008-f730-413f-9c4e-9b06c0912692" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/18c95cc3-d8bc-486c-b0cf-b5d128980176" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/0324b2d2-c9f4-4c2e-ba62-703a7f346de6" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/abafaea5-eb57-4965-9130-7816280a8d84" />&nbsp;&nbsp;&nbsp; 
</div>

## Requisitos

* Python instalado (versão 3.10 ou superior);
* Pacote `uv` instalado;
* Claude Desktop instalado.

## Como instalar no Claude Desktop

Agora vou detalhar como foi o meu passo a passo no Windows 11, utilizando o terminal (atalho `CTRL` + `SHIFT` + `'`) no VSCode: 

1. Instalei a [versão mais atualizada do Python](https://www.python.org/downloads/)
2. Já no VSCode, eu utizei o terminal para verificiar a versão do python com o comando
   ```powershell
   python --version
   ```
3. Depois eu instalei o `uv` com o comando
   ```powershell
   pip install uv
   ```
4. Para conferir se estava tudo certo, eu utilizei o comando
   ```powershell
   uv
   ```
5. Para criar a pasta do projeto, eu utilizei este comando
   ```powershell
   mkdir “C:\Users\meu_usuario\OneDrive\area_de_trabalho\MCPs\mcp_content”
   ```

  > [!IMPORTANT]
  > Não necessariamente quer dizer que você utilizará o mesmo caminho, pode ser que você queira utilizar outro caminho, como este abaixo
  > ```powershell
  >   mkdir "C:\Users\seu_usuario\mcp_content"
  >   ```
  >   Ou você pode simplesmente fazer o download do zip desse projeto para a sua máquina pelo caminho `Code` > `Download ZIP` aqui mesmo no GitHub

6. Chamei a pasta que eu tinha acabado de criar
   ```powershell
   cd “C:\Users\meu_usuario\OneDrive\area_de_trabalho\MCPs\mcp_content”
   ```
7. Utilizei o comando abaixo para abrir outra janela do VSCode e continuar com os demais comandos direto na pasta
   ```
   code .
   ```

  > [!IMPORTANT]
  > Se não quiser criar a pasta via terminal, você pode criar uma nova pasta na sua área de trabalho ou outro local que se lembre facilmente, a fim de utilizar o atalho no VSCode
  > `CTRL` + `O`
  > Depois é só procurar a pasta que acabou de criar, clicar nela e abrir no VSCode. Ou somente importar a pasta completa desse repositório no seu VSCode.

8. Voltando ao terminal, utilizei o comando abaixo para inicializar um novo projeto Python, criando arquivos de configuração e dependências automaticamente
   ```powershell
   uv init
   ```
9. Utilizei em seguida o comando abaixo para criar um ambiente virtual Python isolado para instalar dependências do projeto
    ```powershell
    uv venv
    ```
10. Para ativar o .venv, utilizei o comando abaixo
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
11. Adicionei a dependência MCP, necessária para o projeto
    ```powershell
    uv add mcp[cli]
    ```
12. Verifiquei se estava tudo ok, com o comando abaixo
    ```powershell
    uv run mcp
    ```

> [!IMPORTANT]
> Se aparecer esta informação abaixo no seu terminal é porque está tudo certo
> 
> ![Image](https://github.com/user-attachments/assets/7c692a88-929e-4b8c-84df-b8ce0f004139)

13. Para criar o arquivo `server.py`, eu utilizei esse comando
    ```powershell
    uv init --script server.py
    ```

> [!TIP]
> Como você pode já ter baixado a pasta desse repositório, então o arquivo `server.py`já estará lá no seu VSCode nessa altura do campeonato.

14. Instalei o json abaixo do MCP-Server diretamente no arquivo `claude_desktop_config.json`
    ```json
    "ideias_de_posts": {
      "command": "uv",
      "args": [
        "--directory",
        "C://Users//meu_usuario//OneDrive//area_de_trabalho//MCPs//mcp_content",
        "run",
        "server.py"
      ]
    }
    ```

> [!IMPORTANT]
> Se você já instalou o Claude Desktop corretamente, siga o caminho para acessar o arquivo `claude_desktop_config.json` no seu computador\
> 14a. Com o Claude Desktop aberto, utilize o atalho `CTRL` + `,`\
> 14b. Clique na aba `Desenvolvedor` e depois em `Editar configuração`\
> 14c. Procure o arquivo `claude_desktop_config.json` e edite no VSCode corretamente\
> 14d. Salve o arquivo com `CTRL` + `S`\
> 14e. Feche o Claude Desktop e abra novamente depois de alguns segundos\
> 14f. Confira no ícone de configuração se a ferramenta do MCP "mcp_content" está instalada corretamente
>
> ![Image](https://github.com/user-attachments/assets/6553bcd2-1f3c-4963-9d6a-15b0dc614edd)
>
> A ferramenta foi nomeada como `subtemas`.

## Links úteis

* [Documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/introduction) - Você saberá todos os detalhes dessa inovação da Anthropic
* [Site oficial da Anthropic](https://www.anthropic.com/) - Para ficar por dentro das novidaddes e estudos dos modelos Claude
* [Como baixar o Claude Desktop](https://claude.ai/download) - Link direto para download
* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia
* [Não é difícil encontrar ideias de conteúdo.](https://www.linkedin.com/posts/victorwendt_n%C3%A3o-%C3%A9-dif%C3%ADcil-encontrar-ideias-de-conte%C3%BAdo-activity-7254824064052060161-rDq7?utm_source=share&utm_medium=member_desktop&rcm=ACoAACHvXJYBKyTyP1ggw536I9ZWCnCwD7LTax0) - post do Victor Wendt sobre o processo de geração de novas ideias que ele utiliza

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/mcp_content/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 

