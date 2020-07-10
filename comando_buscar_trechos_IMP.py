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
    campos = ['origem', 'destino', 'dia_partida', 'dia_chegada', 'hora_partida', 'hora_chegada']
    if not verifica_pelo_menos_um_campo(campos, args):
      raise ErroAtrib("Pelo menos um dos campos da busca precisa estar preenchido")

    for campo in campos:
      if campo not in args:
        args[campo] = None

    data_min = args['dia_partida']

    if data_min is not None:
      if args['hora_partida'] is None:
        data_min = data_min + " 00:00"
      else:
        data_min = data_min + " " + args['hora_partida']

    data_max = args['dia_chegada']

    if data_max is not None:
      if args['hora_chegada'] is None:
        data_max = data_max + " 23:59"
      else:
        data_max = data_max + " " + args['hora_chegada']

    if args['origem'] == args['destino'] == None:
      raise ErroAtrib("Pelo menos a origem ou destino precisam estar definidos")

    trcs_ids = trecho.busca_por_origem_e_destino(args['origem'], args['destino'], data_min, data_max)
    trcs = map(lambda id_trecho: trecho.busca_por_identificador(id_trecho), trcs_ids)
    alterar_trcs = sessao.eh_administrador(ses)
    bloco = html_lista_de_trechos.gera(trcs, alterar_trcs)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    admin = sessao.eh_administrador(ses)
    pag = html_pag_buscar_trechos.gera(ses, args, admin, erros)
    return pag
