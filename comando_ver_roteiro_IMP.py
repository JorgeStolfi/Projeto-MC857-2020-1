# Implementação do módulo {comando_solicitar_pag_minhas_roteiros}.

import html_lista_de_trechos
import html_pag_generica
import html_resumo_de_roteiro
import html_pag_mensagem_de_erro
import sessao
import usuario
import roteiro
import trecho

def processa(ses, args):
  assert 'ids_trechos' in args # Deveria acontecer
  
  # Monta página:
  ids_trechos = args['ids_trechos']
  # !!! CONSERTAR !!!
  rot = [ trecho.busca_por_identificador("T-00000003"), trecho.busca_por_identificador("T-00000002") ]
  if rot == None or len(rot) == 0:
    erros = ["roteiro é vazio"]
    pag = hrml_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_ver_roteiro.gera(ses, rot)
  return pag
