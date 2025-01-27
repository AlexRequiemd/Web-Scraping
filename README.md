# Web Scraping de Mercado Livre e OLX

Este projeto realiza a raspagem de dados de produtos do **Mercado Livre** e de **imóveis na OLX** utilizando **Python**, **Selenium** e **Pandas**. Os dados coletados são exportados para arquivos **CSV** para posterior análise.

## 🛠 Tecnologias Utilizadas

- **Python** - Linguagem de programação principal do projeto.
- **Selenium** - Utilizado para automação da coleta de dados nas páginas web.
- **Pandas** - Usado para manipulação e exportação dos dados em formato CSV.

## 🚀 Funcionalidades

### Mercado Livre
- Coleta as seguintes informações:
  - **Nome do Produto**
  - **Preço**

### OLX (Focado em Imóveis)
- Coleta as seguintes informações:
  - **Nome**
  - **Preço**
  - **Localidade**
  - **Link para a Página na loja**

## 📥 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶ Como Usar

1. Execute o script para coletar os dados:
   ```bash
   python scrap_mercadolivre.py
   ```
   OU
    ```bash
   python scrap_olx.py
   ```

3. Os arquivos CSV serão gerados automaticamente na pasta `output/`.

## ⚙ Configuração

- O script pode ser configurado para buscar dados de diferentes categorias ou localizações alterando os filtros diretamente no código.

## 🔮 Melhorias Futuras

- Implementação de rotação de user-agents para evitar bloqueios.
- Adição de delays dinâmicos entre requisições.
- Integração com banco de dados para armazenar os resultados.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📜 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
