import html_relatorio_de_trafego_IMP

def gera(dados):
  """Formata um relatório {dados} de tráfego por aeroporto.
  
  A entrada é uma lista cujos elementos são tuplas {(codigo, rel_chegada, rel_saida)},
  onde {codigo} é um código de aeroporto ("VCP", "SDU", etc.), {rel_chegada}
  é o resumo do tráfego de chegada nesse aeroporto, e {rel_saida} é o
  resumo do tráfego de saída nesse aeroporto.  Cada um destes resumos 
  deve  ter sido gerado por {trecho.resumo_de_trafego}.
  
  O resultado deve ser esses dados formatados como um <table>...</table> HTML.
  As colunas devem ter cabeçalhos no estilo padrão."""
  return html_relatorio_de_trafego_IMP.gera(dados)
