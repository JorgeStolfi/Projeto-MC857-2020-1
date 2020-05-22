import html_roteiro

def gera(ses, rots, detalhe):
  res = ""
  for rot in rots:
    res = res + html_roteiro.gera(ses, rot, detalhe)
  return res
