import html_pag_acrescentar_trecho
import html_pag_generica
import sys
from valida_campo import ErroAtrib
import sessao

def processa(ses, args):
  # !!! Deveria verificar se a sessão {ses} está aberta e o dono é administrador !!!
  try:
    if (sessao.eh_administrador):
      pag = html_pag_acrescentar_trecho.gera(ses, args, None)
    else:
      raise ErroAtrib("Voce precisa ser administrador para fazer isso.\"")
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de acrescentar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_generica.gera(ses, "", erros)
  return pag
