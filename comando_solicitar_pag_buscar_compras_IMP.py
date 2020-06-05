import html_pag_buscar_compras
import sessao
import usuario
import html_pag_mensagem_de_erro


def processa(ses, args):
  if ses == None:
    return html_pag_mesnagem_de_erro.gera(ses, "Precisa estar logado para usar este comando.")
  else:
    usr_ses = sessao.obtem_usuario(ses)
    admin = usuario.obtem_atributo(usr_ses, 'administrador')
    if not admin:
       return html_pag_mensagem_de_erro.gera(ses, "Precisa ser administrador para usar este comando.")
  pag = html_pag_buscar_compras.gera(ses, {}, admin, None)
  return pag
