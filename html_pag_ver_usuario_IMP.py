import usuario
import sessao
import html_form_dados_de_usuario
import html_pag_generica
import html_botao_simples

def gera(ses, usr1, erros):
  usr_sessao = sessao.obtem_usuario(ses)
  usr_sessao_admin = usuario.obtem_atributo(usr_sessao, "administrador") == 1

  id = usuario.obtem_identificador(usr1)
  atrs = usuario.obtem_atributos(usr1)

  formulario = html_form_dados_de_usuario.gera(id, atrs, usr_sessao_admin, "Confirmar", "alterar_usuario")

  ht_botao_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes", {'id': id}, '#eeee55')
  ht_botao_compras = html_botao_simples.gera("Ver compras", "ver_compras_de_usuario", {'id': id}, '#eeee55')
  ht_botao_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas", {'id': id}, '#eeee55')

  conteudo = formulario + "<br />" + \
             ("   " + ht_botao_sessoes + "    " +  ht_botao_compras + "    " + ht_botao_poltronas )

  return html_pag_generica.gera(ses, conteudo, erros)
