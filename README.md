
[README.md](https://github.com/user-attachments/files/24065446/README.md)

## Calculadora de Salário Líquido📌 Sobre o Projeto

Uma calculadora web que recebe o salário bruto e calcula automaticamente:

📉 INSS — tabela progressiva

📉 IRRF — aplicado após o INSS

💰 Salário Líquido

❌ Identificação de valores inválidos

Inclui automação completa com Selenium, prints das execuções e relatório final.

🗂 Estrutura do Projeto
site/
  index.html
  style.css
  app.js

tests/
  test_calculadora.py

evidencias/
  CT01.png
  CT02.png
  CT03.png
  CT04.png

  As evidências são geradas em /evidencias.

  | Teste | Entrada | Resultado        |
| ----- | ------- | ---------------- |
| CT01  | 2000    | Cálculo correto  |
| CT02  | 4500    | Cálculo correto  |
| CT03  | 7500    | Cálculo correto  |
| CT04  | “abc”   | Mensagem de erro |


  🚀 Como executar a calculadora

Dentro da pasta site:

python -m http.server 8000

Relatorio_Teste_Calculadora.docx

🌐 Como executar a calculadora
cd site
python -m http.server 8000


Acesse em → http://localhost:8000

🤖 Executar os testes automatizados

Instale os requisitos:

pip install selenium webdriver-manager


Execute:

cd tests
python test_calculadora.py

🎨 Layout

Interface simples e limpa, com tema roxo claro, centralizada e estilizada com style.css.

👤 Autor

Adryan Albuquerque


As evidências serão salvas na pasta /evidencias.
