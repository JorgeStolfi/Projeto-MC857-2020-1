import usuario
import compra
import assento
import html_paragrafo


def gera(cpr):
  id_cpr = compra.obtem_identificador(cpr)
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  atrs_compra = compra.obtem_atributos(cpr)
  ids_assentos = assento.busca_por_compra(cpr)
  num_itens = len(ids_assentos)

  estilo_parag = "width: 600px; margin-top: 10px; margin-bottom: 2px; text-indent: 0px;  line-height: 75%;"
  ht_cpr = html_paragrafo.gera(estilo_parag, id_cpr)
  ht_usr = html_paragrafo.gera(estilo_parag, id_usr)
  ht_num_itens = html_paragrafo.gera(estilo_parag, str(num_itens))

  ht_bloco = ht_cpr + ht_usr + ht_num_itens
  return ht_bloco
