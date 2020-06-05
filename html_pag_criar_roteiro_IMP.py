import html_form_criar_roteiro
import html_pag_generica
import sessao
import usuario


def gera(ses, erros):
  if ses is None:
    return html_pag_generica.gera(ses, "", ["Precisa estar logado para acessar a página."])

  usr_ses = sessao.obtem_usuario(ses)
  atrs_ses = usuario.obtem_atributos(usr_ses)
  admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)

  if not admin:
    return html_pag_generica.gera(ses, "", ["Precisa ser administrador para acessar a página."])

  conteudo = html_form_criar_roteiro.gera()
  pag = html_pag_generica.gera(ses, conteudo, erros)
  return pag
