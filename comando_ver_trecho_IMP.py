# Implementação do módulo {comando_solicitar_pag_minhas_trechos}.

#import html_lista_de_potronas
import html_pag_generica
#import html_resumo_de_trecho
import html_erro
import html_pag_ver_trecho
import sessao
#import usuario
import trecho
#import poltrona

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
    admin = sessao.eh_administrador(ses)
    comprar_pols = (ses != None) and not admin
    alterar_trc = admin
    pag = html_pag_ver_trecho.gera(ses, trc, comprar_pols, alterar_trc, None)
  return pag
