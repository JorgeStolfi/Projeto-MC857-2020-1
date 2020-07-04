import html_form_dados_de_usuario
import html_pag_generica
import html_botao_simples


def gera(ses, id_usuario, atrs, admin, erros):
  # Constrói formulário com dados:
  formulario = html_form_dados_de_usuario.gera(id_usuario, atrs, admin, "Confirmar", "alterar_usuario")

  # Constroi botões de ações adicionais na página
  ht_botao_sessoes = ""
  ht_botao_compras = ""
  ht_botao_poltronas = ""

  if admin:
    ht_botao_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes", {'id': id_usuario}, '#eeee55')
  else:
    ht_botao_compras = html_botao_simples.gera("Ver compras", "ver_minhas_compras", {'id': id_usuario}, '#eeee55')
    ht_botao_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas", {'id': id_usuario}, '#eeee55')

  # Gera conteudo
  conteudo = formulario + "<br />" + \
             ("   " + ht_botao_sessoes + "    " + ht_botao_compras + "    " + ht_botao_poltronas)

  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)

  return pagina
