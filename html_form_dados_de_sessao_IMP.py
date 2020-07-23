import usuario
import sessao
import compra
import html_paragrafo
import html_form_table

def gera(ses):
  id_ses = sessao.obtem_identificador(ses)
  usr = sessao.obtem_usuario(ses)
  admin = usuario.obtem_atributo(usr, 'administrador')
  id_usr = usuario.obtem_identificador(usr)
  carr = sessao.obtem_carrinho(ses)
  id_cpr = compra.obtem_identificador(carr)
  abrt = sessao.aberta(ses)
  data_login = sessao.obtem_data_login(ses)

  atrs = { 'id_ses': id_ses, 'data_login': data_login, 'id_usr': id_usr, 'id_cpr': id_cpr, 'abrt': "Sim" if abrt else "Não", }

  dados_linhas = \
    (
      ( "ID sessão", "text", "id_ses", None, False, ),
      ( "Criada em", "text", "data_login", None, False, ),
      ( "ID usuário", "text", "id_usr", None, False, ),
      ( "ID carrinho", "text", "id_cpr", None, False, ),
      ( "Status da sessão", "text", "abrt", None,  False, ),
    )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)

  return ht_table
