import sessao
import usuario
import html_form_alterar_usuario
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, id_usuario, atrs, erros):
  # Quem está cadastrando é administrador?
  if ses == None:
    # Não deveria acontecer:
    erro_prog("usuário deveria estar logado")

  usr_ses = sessao.obtem_usuario(ses)
  atrs_ses = usuario.obtem_atributos(usr_ses)
  admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)

  # Constrói formulário com dados:
  conteudo = html_form_alterar_usuario.gera(id_usuario, atrs, admin)
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
