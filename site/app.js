// app.js
// CUIDADO: estes valores são um exemplo funcional.
// Se precisar dos números oficiais de 2025, substitua as tabelas abaixo
// pelo PDF/tabela oficial e anexe no relatório.

const inss_brackets = [
  // [limite, aliquota] formato progressivo
  [1100.00, 0.075],
  [2203.48, 0.09],
  [3305.22, 0.12],
  [6433.57, 0.14] // até teto
];

const irrf_brackets = [
  // [salario_base_min_exclusive, aliquota, deducao]
  [0.00, 0.0, 0.0],          // até isento (placeholder)
  [1903.98, 0.075, 142.80],
  [2826.65, 0.15, 354.80],
  [3751.05, 0.225, 636.13],
  [4664.68, 0.275, 869.36]
];

function calcINSS(salario) {
  // cálculo simplificado e progressivo por faixa (exemplo funcional)
  let restante = salario;
  let total = 0;
  let limites = [1100.00, 2203.48, 3305.22, 6433.57];
  let aliquotas = [0.075, 0.09, 0.12, 0.14];

  let prev = 0;
  for (let i = 0; i < limites.length; i++) {
    const faixaMax = limites[i];
    const aliquota = aliquotas[i];
    if (salario > prev) {
      const valorFaixa = Math.min(salario, faixaMax) - prev;
      total += valorFaixa * aliquota;
    }
    prev = faixaMax;
    if (salario <= faixaMax) break;
  }

  // se salário > teto, usa contribuição máxima proporcional (já somada acima)
  return round2(total);
}

function calcIRRF(salarioBase) {
  // salarioBase = salario bruto - INSS
  // encontra a faixa correta
  let aliquota = 0, deducao = 0;
  if (salarioBase <= 1903.98) {
    return 0.00;
  } else if (salarioBase <= 2826.65) {
    aliquota = 0.075; deducao = 142.80;
  } else if (salarioBase <= 3751.05) {
    aliquota = 0.15; deducao = 354.80;
  } else if (salarioBase <= 4664.68) {
    aliquota = 0.225; deducao = 636.13;
  } else {
    aliquota = 0.275; deducao = 869.36;
  }
  const imposto = salarioBase * aliquota - deducao;
  return Math.max(0, round2(imposto));
}

function round2(v) {
  return Math.round(v * 100) / 100;
}

document.getElementById('calcular').addEventListener('click', function(){
  document.getElementById('mensagemErro').innerText = "";
  const raw = document.getElementById('salarioBruto').value.trim().replace(',', '.');
  const val = parseFloat(raw);
  if (!raw || isNaN(val)) {
    document.getElementById('mensagemErro').innerText = "Insira um valor numérico válido.";
    document.getElementById('resultadoInss').innerText = "-";
    document.getElementById('resultadoIrrf').innerText = "-";
    document.getElementById('salarioLiquido').innerText = "-";
    return;
  }

  const inss = calcINSS(val);
  const baseIrrf = val - inss;
  const irrf = calcIRRF(baseIrrf);
  const liquido = round2(val - inss - irrf);

  document.getElementById('resultadoInss').innerText = `R$ ${inss.toFixed(2)}`;
  document.getElementById('resultadoIrrf').innerText = `R$ ${irrf.toFixed(2)}`;
  document.getElementById('salarioLiquido').innerText = `R$ ${liquido.toFixed(2)}`;
});
