# Implementação do módulo {comando_comprar_roteiro}

import compra
import roteiro
import trecho
import poltrona
import sessao
import usuario
import comando_ver_carrinho
import comando_comprar_poltrona
import html_pag_mensagem_de_erro
import utils_testes

import math

def processa(ses, args):

  # Usuário deve estar logado para iniciar um pedido de compra
  if ses == None:
    pag = html_pag_mensagem_de_erro.gera(ses, ["Voce deve estar logado para comprar um roteiro!"])
    return pag

  cpr = sessao.obtem_carrinho(ses)
  if cpr == None:
    # Novo carrinho associada ao usuario
    compra.cria(ses.cliente, ses.cliente.nome_pass, ses.cliente.doc_pass)

  # Recupera os objetos trechos para verificar poltronas
  ids_trechos = args['ids_trechos']
  obj_trechos = []
  for id in ids_trechos:
    obj_trechos.append(trecho.busca_por_identificador(id))

  # Verifica e inclui poltronas na compra
  for trc in obj_trechos:
    # Verifica se o trecho possui pelo menos uma poltrona livre
    if trecho.numero_de_poltronas_livres(trc) < 1:
      pag = html_pag_mensagem_de_erro.gera(ses, ["Nao tem mais poltronas livres no trecho {} :(".format(trecho.obtem_atributo(trc, "codigo"))])
      return pag

    # Obtem lista de poltronas livres para comparacao do melhor preco
    id_pol_livres = poltrona.lista_livres(trc)
    melhor_preco = math.inf
    id_melhor_preco = None

    for id_pol in id_pol_livres:

      pol = poltrona.busca_por_identificador(id_pol)
      preco_pol = poltrona.obtem_atributo(pol, "preco")

      # Atualiza melhor preco, assim como seu id
      if preco_pol < melhor_preco:
        melhor_preco = preco_pol
        id_melhor_preco = id_pol

    # Adiciona a poltrona ao carrinho
    comando_comprar_poltrona.processa(ses, {'id_poltrona': id_melhor_preco})

  pag = comando_ver_carrinho.processa(ses, None)
  return pag
