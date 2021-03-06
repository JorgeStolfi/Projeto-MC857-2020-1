import sessao
import usuario
import html_pag_generica
import html_span
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
  estilo = f"font-family: Courier; font-size: 16px; font-weight: normal; padding: "\
           f"5px; text-align: center; color: {cor_texto}; background-color: {cor_fundo}"

  bloco_texto1 = html_span.gera(estilo, texto1)
  bloco_texto2 = html_span.gera(estilo, texto2)
  bloco_texto3 = html_span.gera(estilo, texto3)
  conteudo = bloco_texto1 + bloco_texto2 + bloco_texto3
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
