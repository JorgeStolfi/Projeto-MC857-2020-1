# Implementação do módulo {comando_fechar_sessao}.

import html_pag_ver_sessao
import html_pag_mensagem_de_erro
import html_pag_principal
import sessao

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    # Isto nunca deveria acontecer, mas em todo caso:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa entrar como administrador antes de fechar a sessão de outro usuário")
  else:
    # Busca sessão mandada nos argumentos da url e a fecha
    sessao_a_fechar = sessao.busca_por_identificador(args['id_sessao'])
    
    if ses == sessao_a_fechar:
      # se a sessao que está sendo fechada for a sessao corrente, fazer como em comando_fazer_logout (retorna pra homepage).
      pag = html_pag_principal.gera(None, None)
    else:
      # Redireciona para a mesma página, agora com dados atualizados
      pag = html_pag_ver_sessao.gera(ses, sessao_a_fechar, None)
    
    sessao.fecha(sessao_a_fechar)
  return pag