import usuario
import sessao
import compra
import html_paragrafo

def gera(ses):
  id_ses = sessao.obtem_identificador(ses)
  usr = sessao.obtem_usuario(ses)
  id_usr = usuario.obtem_identificador(usr)
  carr = sessao.obtem_carrinho(ses)
  id_cpr = compra.obtem_identificador(carr)
  abrt = sessao.aberta(ses)

  dados_linhas = \
    (
      ( "ID sessão:", "text", "id_ses", None, False, ),
      ( "ID usuário:", "text", "id_usr", None, False, ),
      ( "ID compra:", "text", "id_cpr", None, False, ),
      ( "Status da sessão", "text", "abrt", None,  False, ),
    )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)

  return linha_formatada