import sessao
import usuario
import html_pag_generica
import html_bloco_texto
from utils_testes import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
import re, sys

def gera(ses, erros):
  if ses !=None:
    usr = sessao.obtem_usuario(ses)
    atrs = usuario.obtem_atributos(usr)
    nome = atrs['nome']
    texto1 = "Olá <b>"+nome+"</b>!"
  else:
    texto1 = None
  texto2 = "Bem vindo(a) ao nosso site de viagens!"
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto3 = "<hr/><i>DATA CORRENTE </i><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  cor_texto = "#000488"
  cor_fundo = "#eeeeee"
  bloco_texto1 =  html_bloco_texto.gera(texto1, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  bloco_texto2 =  html_bloco_texto.gera(texto2, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  bloco_texto3 =  html_bloco_texto.gera(texto3, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  conteudo = bloco_texto1 + bloco_texto2 + bloco_texto3
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
