import html_form_contato
import utils_testes

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_contato
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

atrs = { 
            'nome': "valor nome",
            'email': "valor email",
            'telefone': "valor telefone",
            'assunto': "valor assunto" 
        }

# Teste com valores iniciais
admin = True
testa("Valores_Admin", atrs, admin)

admin = False
testa("Valores_Comum", atrs, admin)

atrs = { }

# Teste sem valores iniciais
admin = True
testa("Sem_Valores_Admin", atrs, admin)

admin = False
testa("Sem_Valores_Comum", atrs, admin)