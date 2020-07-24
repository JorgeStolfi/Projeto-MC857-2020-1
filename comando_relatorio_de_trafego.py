import comando_relatorio_de_trafego_IMP

def processa(ses, args):
  """Esta função é acionada quando o usuário (que deve ser um administrador)
  quer um relatório de tráfego nos aeroportos. 
  
  Por enquanto, ignora o {args} e lista todos os aeroportos no sistema e
  todos os voos, passados ou futuros.
  
  Usa {trecho.resumo_de_trafego} para resumir os dados dos voos de chegada
  ou partida em cada aeroporto.  Usa {html_relatorio_de_trafego.gera} para
  formatar esses resumos."""
  return comando_relatorio_de_trafego_IMP.processa(ses, args)
