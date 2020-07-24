import compra
import usuario
import poltrona
import trecho
import sessao

import html_form_dados_de_usuario
import html_pag_generica
import html_botao_simples

def gera(ses, usr, erros):
  usr_sessao = sessao.obtem_usuario(ses)
  usr_sessao_admin = usuario.obtem_atributo(usr_sessao, "administrador") == 1

  assert usr != None and type(usr) is usuario.Objeto_Usuario
  id_usr = usuario.obtem_identificador(usr)
  atrs = usuario.obtem_atributos(usr)

  total = 0
  
  formulario = html_form_dados_de_usuario.gera(id_usr, atrs, usr_sessao_admin, "Confirmar", "alterar_usuario")

  ht_botao_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes", {'id': id_usr}, '#eeee55')
  ht_botao_compras = html_botao_simples.gera("Ver compras", "ver_compras_de_usuario", {'id': id_usr}, '#eeee55')
  ht_botao_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas", {'id': id_usr}, '#eeee55')

  # Pega a lista de compra do cliente
  ids_compras = compra.busca_por_cliente(id_usr)
  num_poltronas = 0
  for id_cpr in ids_compras:
    cpr = compra.busca_por_identificador(id_cpr)
    # Pega o id das poltronas de cada uma dessas compras
    ids_poltronas = compra.obtem_poltronas(cpr)
    for id_pol in ids_poltronas:
      # Para cada um desses ids pega o objeto da poltrona
      pol = poltrona.busca_por_identificador(id_pol)
      # e verifica se o trecho esta aberto
      id_trc = poltrona.obtem_atributo(pol, 'id_trecho')
      trc = trecho.busca_por_identificador(id_trc)
      if trecho.obtem_atributo(trc, 'aberto'):
        # Caso sim adicionamos uma poltrona ao contador
        num_poltronas += 1


  compraStr = "O usuário possui %d poltronas reservadas" % num_poltronas
  
  conteudo = formulario + "<br />" + \
            "<p>" + compraStr + "</p>" + \
             ("   " + ht_botao_sessoes + "    " +  ht_botao_compras + "    " + ht_botao_poltronas )

  conteudo = "<span>O usuário tem " + \
             str(len(usuario.sessoes_abertas(usr))) + \
             " sessões abertas</span><br />" + \
             conteudo

  return html_pag_generica.gera(ses, conteudo, erros)
