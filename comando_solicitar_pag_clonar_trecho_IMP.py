import html_pag_principal
import html_pag_acrescentar_trecho
import trecho
import sessao
import poltrona
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):

  atrs_cmd = args.copy()
  
  # Salva o atributo 'id_trecho' e elimina dos {atrs_cmd}:
  assert 'id_trecho' in atrs_cmd
  id_trc = atrs_cmd['id_trecho']
  del atrs_cmd['id_trecho']
  
  # Salva especificação de poltronas, se houver, e elimina dos {atrs_cmd}:
  if 'poltronas' in atrs_cmd:
    esp_poltronas = atrs_cmd['poltronas']
    del atrs_cmd['poltronas']
  else:
    esp_poltronas = None
  
  # Obtem o trecho e seus atributos correntes:
  trc = trecho.busca_por_identificador(id_trc)
  atrs_trc = trecho.obtem_atributos(trc)
  
  # Substitui atributos correntes pelos atributos em {atrs_cmd}
  for ch, val in atrs_cmd.items():
    assert ch in atrs_trc
    atrs_trc[ch] = val
    
  # Acrescenta a espacificação de poltronas, se houve:
  atrs_trc['poltronas'] = esp_poltronas

  # Mostra os dados como página de acrescentar trecho:
  pag = html_pag_acrescentar_trecho.gera(ses, atrs_trc, None)
  return pag