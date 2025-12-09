from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# URL do seu site local
URL = "http://localhost:8000/"

# IDs utilizados pela sua calculadora
ID_INPUT = "salarioBruto"
ID_INSS = "resultadoInss"
ID_IRRF = "resultadoIrrf"
ID_LIQ = "salarioLiquido"
ID_MSG_ERRO = "mensagemErro"


# -------------------------------
# Funções de cálculo internas
# -------------------------------

def calcINSS_py(salario):
    limites = [1100.00, 2203.48, 3305.22, 6433.57]
    aliquotas = [0.075, 0.09, 0.12, 0.14]

    total = 0.0
    prev = 0.0
    for i in range(len(limites)):
        faixaMax = limites[i]
        aliquota = aliquotas[i]
        if salario > prev:
            valorFaixa = min(salario, faixaMax) - prev
            total += valorFaixa * aliquota
        prev = faixaMax
        if salario <= faixaMax:
            break
    return round(total, 2)


def calcIRRF_py(base):
    if base <= 1903.98:
        return 0.00
    elif base <= 2826.65:
        aliq, ded = 0.075, 142.80
    elif base <= 3751.05:
        aliq, ded = 0.15, 354.80
    elif base <= 4664.68:
        aliq, ded = 0.225, 636.13
    else:
        aliq, ded = 0.275, 869.36

    imposto = base * aliq - ded
    return max(0, round(imposto, 2))


# -------------------------------
# Função de teste geral
# -------------------------------

def testar(nome, valor):
    print(f"\n===== Executando {nome} =====")
    print(f"Salário Bruto Original: {valor}")

    # CONFIGURAÇÃO CERTA do Selenium + ChromeDriver
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)
    time.sleep(1)

    campo = driver.find_element(By.ID, ID_INPUT)
    campo.clear()
    campo.send_keys(str(valor))

    driver.find_element(By.ID, "calcular").click()
    time.sleep(1)

    # Caso inválido (CT-04)
    if isinstance(valor, str):
        msg = driver.find_element(By.ID, ID_MSG_ERRO).text
        print("Mensagem exibida:", msg)
        driver.save_screenshot(f"../evidencias/{nome}.png")
        driver.quit()
        return

    # Ler valores da tela
    inss_text = driver.find_element(By.ID, ID_INSS).text.replace("R$", "").strip()
    irrf_text = driver.find_element(By.ID, ID_IRRF).text.replace("R$", "").strip()
    liquido_text = driver.find_element(By.ID, ID_LIQ).text.replace("R$", "").strip()

    inss_exib = float(inss_text.replace(",", "."))
    irrf_exib = float(irrf_text.replace(",", "."))
    liquido_exib = float(liquido_text.replace(",", "."))

    # Calcular esperado
    inss_exp = calcINSS_py(float(valor))
    irrf_exp = calcIRRF_py(float(valor) - inss_exp)
    liquido_exp = round(float(valor) - inss_exp - irrf_exp, 2)

    print("INSS exibido:", inss_exib, " | esperado:", inss_exp)
    print("IRRF exibido:", irrf_exib, " | esperado:", irrf_exp)
    print("Líquido exibido:", liquido_exib, " | esperado:", liquido_exp)

    status = "PASSOU" if (
        inss_exib == inss_exp and
        irrf_exib == irrf_exp and
        liquido_exib == liquido_exp
    ) else "FALHOU"

    print("STATUS:", status)

    driver.save_screenshot(f"../evidencias/{nome}.png")
    driver.quit()


# -------------------------------
# Testes da atividade
# -------------------------------

if __name__ == "__main__":
    testar("CT01", 2000)
    testar("CT02", 4500)
    testar("CT03", 7500)
    testar("CT04", "abc")
