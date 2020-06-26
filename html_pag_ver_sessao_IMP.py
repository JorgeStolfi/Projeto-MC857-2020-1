import html_sessao
import html_pag_generica
import html_botao_simples
import html_form_dados_de_sessao
import sessao

def gera(ses, ses1, erros):
  ht_bloco_ses = html_sessao.gera(ses1)
  ht_bloco_ses_form = html_form_dados_de_sessao.gera(ses1)

  ht_bloco_ses += ht_bloco_ses_form

  # Somente gera botão caso o usuário da sessao atual seja administrador e a sessão selecionada esteja aberta
  if (sessao.eh_administrador(ses) and sessao.aberta(ses1)):
    args = {}
    args['id_sessao'] = sessao.obtem_identificador(ses1)

    # TODO: escolher cores melhores para os botões
    fecha_btn = html_botao_simples.gera('Fechar sessão', 'fechar_sessao', args, 'green')
    ht_bloco_ses += fecha_btn

  pag = html_pag_generica.gera(ses, ht_bloco_ses, erros)
  return pag
