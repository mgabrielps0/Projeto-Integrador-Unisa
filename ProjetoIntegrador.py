# Código do Back-End///////////////////////////////////////////
def fgts(salario):
    return round(salario * 0.08, 2)

def calcular_deducao_salarial(salario, faltas):
    return round((salario / 30) * faltas, 2)

def inss(salario):
    if salario <= 1212:
        return round(salario * 0.075, 2)
    elif salario <= 2427.35:
        return round(salario * 0.09, 2)
    elif salario <= 3641.03:
        return round(salario * 0.12, 2)
    elif salario <= 7507.49:
        return round(salario * 0.14, 2)
    else:
        return 1051.05

def irrf(salario):
    if salario <= 1903.98:
        return 0
    elif salario <= 2826.65:
        return round((salario * 0.075) - 142.80, 2)
    elif salario <= 3751.05:
        return round((salario * 0.15) - 354.80, 2)
    elif salario <= 4664.68:
        return round((salario * 0.225) - 636.13, 2)
    else:
        return round((salario * 0.275) - 869.36, 2)

def valeTransporte(salario):
    return round(salario * 0.06, 2)

def adiantamentoSalarial(salario):
    return round(salario * 0.4, 2)

def salarioLiquido(salario, falta_value, inss_value, irrf_value, valeTransporte_value, adiantamentoSalarial_value):
    return round(salario - falta_value - inss_value - irrf_value - valeTransporte_value - adiantamentoSalarial_value, 2)

# Interface Streamlit///////////////////////////////////////////
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='titulo'>Calcular Descontos</h1>", unsafe_allow_html=True)
st.markdown("<h5 class='subtitulo'>Informe seu salário e receba os descontos</h5>", unsafe_allow_html=True)

name = st.text_input("Digite o seu nome:")
salario = st.number_input("Digite o valor do salário:", min_value=0)
faltas = st.number_input("Digite a quantidade de faltas", min_value=0)

st.write("Informações adicionais")
transporte = st.checkbox("Recebo vale-transporte")
adiantamento = st.checkbox("Recebo adiantamento salarial")

fgts_value = fgts(salario)
falta_value = calcular_deducao_salarial(salario, faltas)
inss_value = inss(salario)
irrf_value = irrf(salario)

valeTransporte_value = 0
if transporte:
    valeTransporte_value = valeTransporte(salario)

adiantamentoSalarial_value = 0
if adiantamento:
    adiantamentoSalarial_value = adiantamentoSalarial(salario)

salarioLiquido_value = salarioLiquido(salario, falta_value, inss_value, irrf_value, valeTransporte_value, adiantamentoSalarial_value)

st.write("Olá", name + ", Esses são os seus descontos:")
st.write("Valor do FGTS:", fgts_value)
st.write("Valor do INSS:", inss_value)
st.write("Faltas:", "-", falta_value)
if transporte:
    st.write("Vale Transporte:", valeTransporte_value)
if adiantamento:
    st.write("Adiantamento Salarial:", adiantamentoSalarial_value)
st.write("Valor do IRRF:", irrf_value)
st.write("Salário Líquido:", salarioLiquido_value)