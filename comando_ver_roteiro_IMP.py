# Implementação do módulo {comando_solicitar_pag_minhas_roteiros}.

import html_pag_ver_roteiro
import html_pag_mensagem_de_erro
import sessao
import usuario
import roteiro
import trecho

def processa(ses, args):

  # Obtem os identificadores dos trechos do roteiro a mostrar:
  ids_trcs_str = args['ids_trechos'] if 'ids_trechos' in args else None
  assert ids_trcs_str != None and type(ids_trcs_str) is str # Paranóia (formulário deveria fornecer).
  ids_trcs = ids_trcs_str.split(",")
  
  # Obtem o roteiro (lista de trechos):
  rot = [].copy()
  for id_trc in ids_trcs:
    trc = trecho.busca_por_identificador(id_trc)
    rot.append(trc)

  if len(rot) == 0:
    erros = ["Roteiro vazio!"]
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_roteiro.gera(ses, rot, None)
  return pag
