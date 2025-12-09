Calculadora de Salário Líquido

Projeto de Recuperação – Verificação e Validação de Software
Automação de Testes usando Selenium + Página Web (HTML/CSS/JS)

📌 Sobre o Projeto

Uma calculadora web que recebe o salário bruto e calcula:

INSS (tabela progressiva)

IRRF (calculado após desconto do INSS)

Salário Líquido

A automação valida 4 cenários obrigatórios do trabalho.

🗂 Estrutura
Calculadora-de-Salario/
│
├── site/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── tests/
│   └── test_calculadora.py
│
├── evidencias/
│   ├── CT01.png
│   ├── CT02.png
│   ├── CT03.png
│   └── CT04.png
│
├── Relatorio_Teste_Calculadora.docx
└── README.md

🌐 Como abrir a calculadora

Na pasta site, execute:

python -m http.server 8000


Acesse no navegador:
👉 http://localhost:8000/

🤖 Rodar os testes automatizados

Instalar dependências:

pip install selenium webdriver-manager


Executar:

cd tests
python test_calculadora.py


Os prints ficarão na pasta /evidencias.

✔ Resultados dos Testes
Teste	Salário	INSS	IRRF	Líquido	Status
CT01	2000	163,50	0,00	1836,50	✔
CT02	4500	481,29	268,08	3750,63	✔
CT03	7500	751,99	986,34	5761,67	✔
CT04	“abc”	—	—	Erro exibido	✔
🎨 Layout

Tema roxo bebê, design clean e centralizado.
CSS separado no arquivo style.css.

📝 Relatório
O relatório final está incluído em .docx, contendo:
cenário de testes
execução
prints
tabelas de INSS/IRRF
conclusões

👤 Autor

Adryan Albuquerque
