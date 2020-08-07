import html_pag_principal
import html_pag_trecho
import trecho
import sessao
import poltrona
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def processa(ses, args):

  admin = False if ses == None else sessao.eh_administrador(ses)
  assert admin # Paranóia (cliente comum e deslogado não deeveria ter acesso a este cmd)
  
  # Obtem o trecho a clonar e seus atributos:
  id_trc = args['id_trecho'] if 'id_trecho' in args else None
  assert id_trc != None # Paranóia (formulário/botão deveria especificar).
  del args['id_trecho']
  trc = trecho.busca_por_identificador(id_trc)
  assert id_trc != None # Paranóia.
  
  # Obtem os atributos correntes do trecho:
  atrs_clone = trecho.obtem_atributos(trc)
  
  # Elimina atributos que não podem ser mantidos:
  del atrs_clone['dia_partida']
  del atrs_clone['hora_partida']
  del atrs_clone['dia_chegada']
  del atrs_clone['hora_chegada']
  
  # Acrescenta especificação de poltronas:
  ids_pols = poltrona.busca_por_trecho(trc)
  nums_precos = poltrona.obtem_numeros_e_precos(ids_pols)
  esp_poltronas = resume_numeros_e_precos(nums_precos)
  atrs_clone['poltronas'] = esp_poltronas
    
  # Mostra página de novo trecho com esses atributos:
  pag = html_pag_trecho.gera(ses, None, atrs_clone, None)
  return pag
