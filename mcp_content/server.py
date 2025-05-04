# Importa a classe principal do FastMCP para criar o servidor
from mcp.server.fastmcp import FastMCP

# Cria uma instância do FastMCP com o nome especificado
mcp = FastMCP(name="ideias_de_posts")

@mcp.tool(name="subtemas")
def subtemas(tema_principal: str) -> str:
    """
    Gera uma matriz de conteúdo em Markdown para um tema principal.
    A matriz terá 5 níveis de subtema, cada um com 3 microtemas. A ideia
    é que sejam subtemas e microtemas ideais para conteúdos de blog, vídeos no YouTube, posts no LinkedIn etc.

    Args:
        tema_principal: O tema central para gerar a matriz, fornecido pela pessoa usuária.

    Returns:
        Uma string formatada em Markdown representando a matriz de conteúdo.
    """
    response = f"""

# Tema: "{tema_principal}"

## Subtemas
* Subtema 1
* Subtema 2
* Subtema 3
* Subtema 4
* Subtema 5

## Microtemas
### Subtema 1
1. Microtema 1.1
2. Microtema 1.2
3. Microtema 1.3

### Subtema 2
1. Microtema 2.1
2. Microtema 2.2
3. Microtema 2.3

### Subtema 3
1. Microtema 3.1
2. Microtema 3.2
3. Microtema 3.3

### Subtema 4
1. Microtema 4.1
2. Microtema 4.2
3. Microtema 4.3

### Subtema 5
1. Microtema 5.1
2. Microtema 5.2
3. Microtema 5.3
"""
    return response

# Define um resource que lê o conteúdo do arquivo matriz_exemplo.md
@mcp.resource("file://exemplos")
def exemplos() -> bytes:
    """Retorna o conteúdo do arquivo
    matriz_exemplo.md com um exemplo de
    matriz de conteúdo em Markdown.
    Assume que o arquivo está no mesmo diretório do script.
    """
    
    with open("exemplos.md", "rb") as f:
        return f.read()


# Ponto de entrada principal para executar o servidor MCP
if __name__ == "__main__":
    mcp.run(transport='stdio')