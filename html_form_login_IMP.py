import html_label
import html_input
import html_tabela
import html_botao_submit
import html_form

def gera():
  linhas = [].copy()
  
  ht_rotulo = html_label.gera("E-mail", ": ")
  ht_campo = html_input.gera(None, "text", "email", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))
  
  ht_rotulo = html_label.gera("Senha", ": ")
  ht_campo = html_input.gera(None, "password", "senha", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_tabela = html_tabela.gera(linhas)

  ht_bt_login = html_botao_submit.gera("Entrar", 'fazer_login', None, '#55ee55')

  ht_campos = \
    ht_tabela + \
    ht_bt_login

  ht = html_form.gera(ht_campos)
  return ht
  
