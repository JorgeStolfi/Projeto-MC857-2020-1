import html_pag_alterar_trecho
import html_pag_mensagem_de_erro
import sessao
import usuario
import trecho
from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    if ses == None or not sessao.aberta(ses):
      raise ErroAtrib("A sessão deveria estar aberta")
    elif not sessao.eh_administrador(ses):
      raise ErroAtrib("Este comando é reservado a administradores")
    elif (not 'id_trecho' in args) or args['id_trecho'] == None:
      raise ErroAtrib("Trecho não identificado")
    else:
      id_trecho = args['id_trecho']
      trc = trecho.busca_por_identificador(id_trc)
      if trc == None:
        raise ErroAtrib("Trecho \"" + str(id_trecho) + "\" não existe")
      atrs = trecho.obtem_atributos(trc)
      pag = html_pag_alterar_trecho.gera(ses, id_trc, atrs, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
    
