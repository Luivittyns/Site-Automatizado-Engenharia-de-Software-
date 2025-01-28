# **Test Automation Exercise**

Este projeto foi criado para realizar testes automatizados no site [Automation Exercise](https://automationexercise.com/) utilizando a biblioteca **Selenium** e a estrutura de testes unitários do Python, **unittest**.

---

## **Tecnologias Utilizadas**

### **Python**
Linguagem de programação utilizada para escrever os testes. O código está estruturado no formato de classes e métodos para facilitar a organização dos casos de teste.

### **Selenium WebDriver**
Framework usado para automatizar interações com navegadores web. Neste projeto, o driver do Microsoft Edge foi utilizado para navegar e interagir com o site.

### **unittest**
Módulo padrão do Python para escrever e executar testes unitários. Permite a definição de casos de teste, configuração de ambiente (*“set up” e “teardown”*) e a verificação de resultados com asserções.

---

## **Lógica do Código**

### **Estrutura Geral**

O código é organizado em uma classe chamada `TestAutomationExercise`, que herda de `unittest.TestCase`. Esta classe contém os seguintes métodos:

- **`setUpClass`**: Configura o ambiente de teste inicial. Inicia o driver do Microsoft Edge e acessa o site alvo.
- **`tearDownClass`**: Encerra o navegador após a execução de todos os testes.

#### **Casos de Teste**
- **`test_site_accessibility`**: Verifica se o site está acessível confirmando a presença do texto **“Automation Exercise”** no título da página.
- **`test_add_product_to_cart`**: Testa a funcionalidade de adicionar um produto ao carrinho e verifica se ele foi incluído com sucesso.
- **`test_login_process`**: Realiza um teste do processo de login preenchendo o formulário com credenciais fictícias e verificando se a conta foi autenticada corretamente.

---

### **Fluxo de Cada Teste**

#### **`test_site_accessibility`**
1. Acessa o site.
2. Verifica se o título da página contém o texto esperado.

#### **`test_add_product_to_cart`**
1. Espera até que o produto esteja visível e clica nele.
2. Clica no botão **“Adicionar ao carrinho”**.
3. Acessa o carrinho de compras.
4. Verifica se o carrinho contém o produto adicionado.

#### **`test_login_process`**
1. Acessa a página de login.
2. Preenche o formulário de login com um e-mail e senha.
3. Clica no botão **“Login”**.
4. Verifica se o nome do usuário é exibido após o login.

---

### **Tratamento de Exceções**

- **TimeoutException**: Caso algum elemento demore mais do que o esperado para carregar, o teste é encerrado com falha e uma captura de tela (*“screenshot”*) é salva para auxiliar na depuração.

---

### **Configurações Específicas**

- **Driver**: O caminho para o driver do Edge deve ser especificado corretamente na variável `edge_driver_path`.
- **Tempo de Espera**: Foi definido um tempo de espera máximo de 30 segundos para o carregamento de elementos dinâmicos.

---

## **Como Executar os Testes**

1. Instale as dependências necessárias:
   ```bash
   pip install selenium
2. Baixe o driver do Microsoft Edge compatível com a sua versão do navegador e ajuste o caminho no código.

3. Execute o script no terminal:

   ```bash
   python nome_do_arquivo.py
## **Possíveis Melhorias**

- Implementar testes para outras funcionalidades do site.
- Adicionar suporte a outros navegadores, como Chrome e Firefox.
- Configurar um sistema de integração contínua (CI) para execução automática dos testes.
