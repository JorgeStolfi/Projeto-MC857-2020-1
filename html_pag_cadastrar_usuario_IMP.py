import sessao
import usuario
import html_form_cadastrar_usuario
import html_pag_generica

def cadastrar_usuario(ses, atrs, erros):
  # Quem está cadastrando é administrador?
  if ses != None:
    usr_ses = sessao.obtem_usuario(ses)
    atrs_ses = usuario.obtem_atributos(usr_ses)
    admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)
  else:
    admin = False
  # Constrói formulário com dados:
  html_dados = html_form_cadastrar_usuario.gera(atrs, admin)
  conteudo = html_dados
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
