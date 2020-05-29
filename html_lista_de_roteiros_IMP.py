import html_resumo_de_roteiro
import html_tabela

def gera(ses, rots):
  linhas = [].copy()
  for rot in rots:
    ver_rot = True
    res_campos = html_resumo_de_roteiro.gera(ses, rot, ver)
    linhas.append(res_campos)
    
  res = html_tabela(linhas)
  return res
