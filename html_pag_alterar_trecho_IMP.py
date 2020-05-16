import sessao
import usuario
import trecho
import html_form_alterar_trecho
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, id_usuario, id_trecho, atrs, erros):
  # Quem está alterando é administrador?
  if ses == None:
    # Não deveria acontecer:
    erro_prog("usuário deveria estar logado")

  usr_ses = sessao.obtem_usuario(ses)
  atrs_ses = usuario.obtem_atributos(usr_ses)
  admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)

  # Constrói formulário com dados:
  conteudo = html_form_alterar_trecho.gera(id_trecho, atrs, admin)
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
