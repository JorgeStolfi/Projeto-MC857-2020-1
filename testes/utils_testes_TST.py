
import utils_testes
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML
from utils_testes import erro_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.mostra}\n")
for p in range(10):
  utils_testes.mostra(2*p, ("indentado por %d" % (2*p)))
  
# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.formata_dict}\n")

d1 = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ], 'picas': { 'sim': 100, 'nao': 200, 'bah': 123 } }
fd1 = utils_testes.formata_dict(d1);
sys.stderr.write("d1 formatado\n%s\n" % fd1)

