# Implementação do módulo {comando_buscar_trechos}.

import trecho
import sessao
import html_lista_de_trechos
import html_pag_generica
import html_pag_buscar_trechos
import sys

from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    # Por via das dúvidas:
    if args == None: args = {}.copy()
    
    erros = [].copy()

    # Obtem os campos sem defaults:
    origem = args['origem'] if 'origem' in args else None
    dia_partida = args['dia_partida'] if 'dia_partida' in args else None
    destino = args['destino'] if 'destino' in args else None
    dia_chegada = args['dia_chegada'] if 'dia_chegada' in args else None
    
    # Verifica campos obrigatórios:
    if origem == None and destino == None:
      erros.append("um dos campos 'origem' e 'destino' deve ser especificado")
    if dia_partida == None: erros.append("o campo 'dia_partida' deve ser especificado")
    if dia_chegada == None: erros.append("o campo 'dia_chegada' deve ser especificado")
    
    # Obtem horas e providencia defaults:
    hora_partida = args['hora_partida'] if 'hora_partida' in args else "00:00"
    hora_chegada = args['hora_chegada'] if 'hora_chegada' in args else "00:00"

    if len(erros) > 0: raise ErroAtrib(erros)

    # Monta datas completas:
    data_min = dia_partida + " " + hora_partida + " UTC"
    data_max = dia_chegada + " " + hora_chegada + " UTC"

    # Busca trechos:
    trcs_ids = trecho.busca_por_origem_e_destino(origem, destino, data_min, data_max)
    trcs = map(lambda id_trecho: trecho.busca_por_identificador(id_trecho), trcs_ids)
    alterar_trcs = sessao.eh_administrador(ses)
    bloco = html_lista_de_trechos.gera(trcs, alterar_trcs)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagens de erro:
    admin = sessao.eh_administrador(ses)
    pag = html_pag_buscar_trechos.gera(ses, args, admin, erros)
    return pag
