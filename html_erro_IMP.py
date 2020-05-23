import html_texto
import html_paragrafo
import html_botao_simples
import re

def gera(msg):
  fam_fonte = "Courier"
  # Cabeçalho espalhafatoso:
  ht_tit = html_texto.gera("Não foi possível completar a operação", None, fam_fonte, "24px", "bold", "5px", "left", "#880000", None)
  
  if type(msg) is list or type(msg) is tuple:
    msg = "\n".join(msg)

  # Processa quebras de linha em {msg}:
  msg = re.sub(r'\n', r'<br/>Erro: \n', msg)

  # Formata a mensagem:
  ht_msg = html_texto.gera(msg, None, fam_fonte, "20px", "bold", "5px", "left", "#000000", None)

  # Junta as partes:
  ht_tudo = ht_tit + "<br/>" + ht_msg

  # Formata:
  estilo_parag = " width: 600px; margin-top: 2px;margin-bottom: 2px; text-indent: 0px; align: center;"
  bloco_final = html_paragrafo.gera(estilo_parag, ht_tudo)

  return bloco_final
