# Implementação do módulo {comando_buscar_trechos}.

import trecho
import sessao
import html_lista_de_trechos
import html_pag_generica
import html_pag_buscar_trechos
import sys

from valida_campo import ErroAtrib

def verifica_pelo_menos_um_campo(campos, dic):
  """ Garante que:
     - Todos os campos da busca são suportados pelo Objeto_Trecho.
     - Todos os campos da busca estão definidos com algo diferente de None.
     - Pelo menos um campo de busca está definido.
  """
  sys.stderr.write("dic = %s\n" % str(dic))
  for campo_busca in list(dic.keys()):
    if campo_busca not in campos:
      del dic[campo_busca]

  tem_campo = False
  for campo in campos:
    if campo in dic and dic[campo] is not None:
      if dic[campo] is None:
        del dic[campo]
      else:
        tem_campo = True
        break

  return tem_campo

def processa(ses, args):
  try:
    campos = ['codigo', 'destino', 'origem', 'dia_partida', 'hora_partida', 'dia_chegada', 'hora_chegada']
    if not verifica_pelo_menos_um_campo(campos, args):
      raise ErroAtrib("Pelo menos um dos campos da busca precisa estar preenchido")

    trechos = map(lambda id_trecho: trecho.busca_por_identificador(id_trecho), trecho.busca(args))
    alterar_trcs = sessao.eh_administrador(ses)
    bloco = html_lista_de_trechos.gera(trechos, alterar_trcs)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    admin = sessao.eh_administrador(ses)
    pag = html_pag_buscar_trechos.gera(ses, args, admin, erros)
    return pag
