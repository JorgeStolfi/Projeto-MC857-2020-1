import usuario
import compra
import trecho
import assento
import html_paragrafo


def gera(trco):
  id_trecho = trecho.obtem_identificador(trco)  
  usr = trecho.obtem_cliente(trco)
  id_usr = usuario.obtem_identificador(usr)
  atrs_trecho = trecho.obtem_atributos(trco)
  ids_assentos = assento.busca_por_trecho(trco)
  num_itens = len(ids_assentos)

  estilo_parag = "width: 600px; margin-top: 10px; margin-bottom: 2px; text-indent: 0px;  line-height: 75%;"
  ht_trco = html_paragrafo.gera(estilo_parag, id_trecho)
  ht_usr = html_paragrafo.gera(estilo_parag, id_usr)
  ht_num_itens = html_paragrafo.gera(estilo_parag, str(num_itens))

  ht_bloco = ht_trco + ht_usr + ht_num_itens
  return ht_bloco