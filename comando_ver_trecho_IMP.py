# Implementação do módulo {comando_solicitar_pag_minhas_trechos}.

#import html_lista_de_potronas
import html_pag_generica
import html_erro
import html_pag_trecho
import sessao
import usuario
import trecho
import poltrona

def processa(ses, args):

  # Validações, por via das dúvidas:
  assert 'id_trecho' in args # Deveria acontecer

  # Monta página:
  id_trecho = args['id_trecho']
  trc = trecho.busca_por_identificador(id_trecho)
  if trc == None:
    erros = ["trecho \"" + id_trecho + "\" não existe"]
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_trecho.gera(ses, trc, None, None)
  return pag
