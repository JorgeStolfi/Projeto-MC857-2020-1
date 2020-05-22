import sessao
import usuario
import html_pag_generica

def gera(ses):
  if ses is None:
    return html_pag_generica.gera(ses, "", ["Precisa estar logado para acessar a página."])

  usr_ses = sessao.obtem_usuario(ses)
  atrs_ses = usuario.obtem_atributos(usr_ses)
  admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)

  if not admin:
    return html_pag_generica.gera(ses, "", ["Precisa ser administrador para acessar a página."])

  return html_pag_generica.gera(ses, "", ["Implementar formulario para buscar usuario"])
