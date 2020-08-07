import html_span
import html_paragrafo
import html_botao_simples
import re

def gera(erros):
  if type(erros) is list or type(erros) is tuple:
    erros = "\n".join(erros)

  # Processa quebras de linha em {erros}:
  erros = re.sub(r'\n', r'<br/>Erro: \n', erros)

  # Formata as mensagens:
  estilo_erro = \
    "font-family:Courier;" + \
    "font-size:20px;" + \
    "font-weight:bold;" + \
    "padding: 2px;" + \
    "text-align:left;" + \
    "color: #880000;"
  ht_erros = html_span.gera(estilo_erro, erros)

  # Formata como parágrafo:
  estilo_parag = \
    "margin-top:2px;" + \
    "margin-bottom:2px;" + \
    "text-indent:0px;"
  ht_res = html_paragrafo.gera(estilo_parag, ht_erros)

  return ht_res
