import usuario
import sessao
import html_form_dados_de_usuario
import html_pag_generica

def gera(ses, usr1, erros):
  id = usuario.obtem_identificador(usr1)
  atrs = usuario.obtem_atributos(usr1)
  usr2 = sessao.obtem_usuario(ses) # Usuario {usr2} é o dono da sessao {ses}
  admin = usuario.obtem_atributo(usr2, "administrador") == 1 # {True} se {usr2} for administrador, {False} caso contrário
  ht_dados = html_form_dados_de_usuario.gera(id, atrs, admin, "Confirmar", "alterar_usuario")
  return html_pag_generica.gera(ses, ht_dados, erros)
