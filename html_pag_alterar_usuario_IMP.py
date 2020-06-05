import sessao
import usuario
import html_form_dados_de_usuario
import html_pag_generica

from utils_testes import erro_prog

def gera(ses, id_usuario, atrs, admin, erros):
  # Constrói formulário com dados:
  conteudo = html_form_dados_de_usuario.gera(id_usuario, atrs, admin, "Confirmar", "alterar_usuario")
  # Monta a página:
  pagina = html_pag_generica.gera(ses, conteudo, erros)
  return pagina
