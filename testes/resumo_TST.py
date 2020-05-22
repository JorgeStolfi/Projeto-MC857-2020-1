#! /usr/bin/python3

import sys
import identificador
from utils_testes import erro_prog, mostra

ok_global = True  # Vira {False} se houver erro.

erro_prog("A implementar")

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
