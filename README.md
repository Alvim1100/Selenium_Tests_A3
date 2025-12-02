# 🚀 Automação de Testes E2E - SauceDemo

Projeto robusto de automação de testes End-to-End para o e-commerce **SauceDemo**, desenvolvido em **Python** com **Selenium**.

O projeto utiliza o padrão de projeto **Page Object Model (POM)** (adaptado) para modularização e fácil manutenção, além de contar com execução em modo **Headless** (invisível) e relatórios coloridos no terminal.

## ✨ Funcionalidades e Diferenciais

* **Cobertura Completa:** 20 Casos de Teste Positivos (Happy Path) e 20 Casos de Teste Negativos (Edge Cases/Erros).
* **Modo Headless (Fantasma):** Opção para rodar os testes em segundo plano (sem abrir a janela do navegador) para maior velocidade.
* **Relatórios Visuais:** Uso da biblioteca `colorama` para feedback visual claro (Verde/Vermelho) no terminal.
* **Blindagem de Segurança:** Configurações avançadas do Chrome Options para bloquear pop-ups de "Vazamento de Senha" e detecção de automação.
* **Tratamento de Exceções:** Lógica robusta para lidar com falhas de carregamento, elementos não encontrados e *timeouts*.

## 🛠️ Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/)
* [Selenium WebDriver](https://www.selenium.dev/)
* [Colorama](https://pypi.org/project/colorama/) (Para estilização do terminal)
* Google Chrome Browser

## 📋 Pré-requisitos

Certifique-se de ter o Python e o Google Chrome instalados em sua máquina.

## 🔧 Instalação

1. **Clone este repositório** ou baixe os arquivos.
2. **Abra o terminal** na pasta do projeto.
3. **Instale as dependências** necessárias executando o comando abaixo:

```bash
pip install selenium colorama
````

## ▶️ Como Rodar

Execute o arquivo principal através do terminal:

```bash
python main.py
```

### 🖥️ Menu de Opções

Ao iniciar, você verá um menu interativo:

  * **Opções 1 a 3 (Modo Visual):** Abrem o navegador Chrome e você pode assistir aos testes sendo executados em tempo real. Ideal para *debug*.
  * **Opções 4 a 6 (Modo Rápido/Headless):** Executam os testes em segundo plano, sem interface gráfica. Ideal para execução rápida ou integração contínua.

## 📂 Estrutura do Projeto

  * `main.py`: Ponto de entrada. Gerencia o menu interativo e a orquestração das baterias de teste.
  * `base.py`: O "coração" do framework. Contém a classe `SauceBase` com configurações do Driver, métodos auxiliares (login, screenshots, waits) e tratamento de alertas.
  * `positivos.py`: Contém a classe `TestesPositivos` com 20 cenários de sucesso (Compra, Filtros, Carrinho, etc.).
  * `negativos.py`: Contém a classe `TestesNegativos` com 20 cenários de erro (Login inválido, SQL Injection, URLs restritas, etc.).

## 🧪 Exemplos de Testes Cobertos

### ✅ Positivos

  * Fluxo completo de compra (do login ao "Thank you").
  * Adição e remoção de itens do carrinho.
  * Ordenação de produtos (Preço/Nome).
  * Reset de estado da aplicação.

### ❌ Negativos

  * Tentativas de Login (Senha errada, usuário bloqueado, performance glitch).
  * Validação de campos obrigatórios no Checkout.
  * Tentativa de acesso direto a URLs restritas (Bypass de Login).
  * Tentativa de remoção de itens inexistentes.
  * Tratamento de páginas 404.

-----

**Autor:** Eric Weber Alvim

```
```
