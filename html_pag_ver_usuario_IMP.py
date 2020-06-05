import usuario
import html_form_dados_de_usuario
import html_pag_generica

def gera(ses, usr1, erros):
  id = usuario.obtem_identificador(usr1)
  atrs = usuario.obtem_atributos(usr1)
  # !!! Deveria confirmar que o dono da sessão {ses} é administrador. !!!
  admin = True
  ht_dados = html_form_dados_de_usuario.gera(id, atrs, admin, "Confirmar", "alterar_usuario")
  return html_pag_generica.gera(ses, ht_dados, erros)
