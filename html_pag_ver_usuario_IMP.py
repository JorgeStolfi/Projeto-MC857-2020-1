import compra
import usuario
import sessao
import html_form_dados_de_usuario
import html_pag_generica
import html_botao_simples
import compra
import poltrona
import trecho

def gera(ses, usr1, erros):
  usr_sessao = sessao.obtem_usuario(ses)
  usr_sessao_admin = usuario.obtem_atributo(usr_sessao, "administrador") == 1

  id = usuario.obtem_identificador(usr1)
  atrs = usuario.obtem_atributos(usr1)

  total = 0
  
  formulario = html_form_dados_de_usuario.gera(id, atrs, usr_sessao_admin, "Confirmar", "alterar_usuario")

  ht_botao_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes", {'id': id}, '#eeee55')
  ht_botao_compras = html_botao_simples.gera("Ver compras", "ver_minhas_compras", {'id': id}, '#eeee55')
  ht_botao_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas_de_usuario", {'id': id}, '#eeee55')

  # Pega a lista de compra do cliente
  cprs = compra.busca_por_cliente(id)
  num_poltronas = 0
  for cpr in cprs:
    # Pega o id das poltronas de cada uma dessas compras
    id_poltronas = compra.obtem_poltronas(cpr)
    for id_p in id_poltronas:
      # Para cada um desses ids pega o objeto da poltrona
      polt = poltrona.busca_por_identificador(id_p)
      # e verifica se o trecho esta aberto
      trec = trecho.busca_por_identificador(polt.id_trecho)
      if trec.aberto :
        # Caso sim adicionamos uma poltrona ao contador
        num_poltronas += 1


  compraStr = "O usuário possui %d poltronas reservadas" % num_poltronas
  
  conteudo = formulario + "<br />" + \
            "<p>" + compraStr + "</p>" + \
             ("   " + ht_botao_sessoes + "    " +  ht_botao_compras + "    " + ht_botao_poltronas )

  conteudo = "<span>O usuário tem " + \
             str(len(usuario.sessoes_abertas(usr1))) + \
             " sessões abertas</span><br />" + \
             conteudo

  return html_pag_generica.gera(ses, conteudo, erros)
