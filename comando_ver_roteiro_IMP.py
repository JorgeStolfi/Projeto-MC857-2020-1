# Implementação do módulo {comando_solicitar_pag_minhas_roteiros}.

import html_lista_de_trechos
import html_pag_ver_roteiro
import html_pag_mensagem_de_erro
import sessao
import usuario
import roteiro
import trecho

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    erros = ["Sessão não iniciada!"]
    return html_pag_mensagem_de_erro.gera(ses, erros)

  if args == None or 'ids_trechos' not in args or type(args['ids_trechos']) is not str:
    erros = ["Roteiro inválido!"]
    return html_pag_mensagem_de_erro.gera(ses, erros)
  
  # Monta página:
  ids_trechos = args['ids_trechos'].split(",")
  rot = []
  for id_trecho in ids_trechos:
    rot.append(trecho.busca_por_identificador(id_trecho))

  if rot == None or len(rot) == 0:
    erros = ["Roteiro vazio!"]
    return html_pag_mensagem_de_erro.gera(ses, erros)

  pag = html_pag_ver_roteiro.gera(ses, rot, None)
  return pag
