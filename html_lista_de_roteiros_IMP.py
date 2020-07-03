import html_resumo_de_roteiro
import html_table

def gera(rots):
  cabecalho = ["!!!coluna1", "!!!coluna2", "!!!coluna3"]
  linhas = [].copy()
  for rot in rots:
    ver_rot = True
    res_campos = html_resumo_de_roteiro.gera(rot, ver_rot)
    linhas.append(res_campos)
    
  res = html_table.gera(linhas, cabecalho)
  return res
