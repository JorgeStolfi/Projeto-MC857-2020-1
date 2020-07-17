import html_resumo_de_roteiro
import html_table
import html_cabecalho
import html_div

def gera(rots):

  ht_cabe = html_cabecalho.gera("Lista de Roteiros", False)

  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"

  cabecalho = ["Origem", "Data Partida", "Destino", "Data Chegada", "NE", "Preço Mínimo"]
  cabs_div = [].copy()
  for cb in cabecalho:
    cabs_div.append(html_div.gera(estilo_cab, cb))


  linhas = [].copy()
  for rot in rots:
    ver_rot = True
    res_campos = html_resumo_de_roteiro.gera(rot, ver_rot)
    linhas.append(res_campos)

  observacao = "</br><b>LEGENDA:</b></br><span>NE = Número de Escalas</span></br>"
    
  res = ht_cabe + html_table.gera(linhas, cabs_div) + observacao
  return res
