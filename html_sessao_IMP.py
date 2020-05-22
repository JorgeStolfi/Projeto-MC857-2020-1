import usuario
import sessao
import compra
import html_paragrafo

def gera(ses):
  id_ses = sessao.obtem_identificador(ses)
  usr = sessao.obtem_usuario(ses)
  id_usr = usuario.obtem_identificador(usr)
  carr = sessao.obtem_carrinho(ses)
  id_cpr = compra.obtem_identificador(carr)
  abrt = sessao.aberta(ses)

  #estilo_parag = "width: 600px; margin-top: 10px; margin-bottom: 2px; text-indent: 0px;  line-height: 75%;"
  #ht_ses = html_paragrafo.gera(estilo_parag, id_ses)
  #ht_usr = html_paragrafo.gera(estilo_parag, id_usr)
  #ht_carr = html_paragrafo.gera(estilo_parag, id_cpr)
  #ht_abrt = html_paragrafo.gera(estilo_parag, str(abrt))
  #ht_bloco = ht_ses + ht_usr + ht_carr + ht_abrt
  #return ht_bloco

  #Formata um linha em html que exibe todos os atributos da sessao. Esta linha pode ser concatenada com outras linhas do mesmo tipo sem perder forma
  linha_formatada = '<hr/><p><b>ID sessao:</b> {0} | <b>ID usuario:</b> {1} | <b>ID compra:</b> {2} | <b>Status sessao:</b> <font color="{3}">{4}</font><p>'.format(id_ses, id_usr, id_cpr, "green" if abrt else "red", "Aberta" if abrt else "Fechada")
  linha_formatada += linha_formatada
  linha_formatada += linha_formatada
  linha_formatada += linha_formatada
  linha_formatada += linha_formatada

  return linha_formatada
