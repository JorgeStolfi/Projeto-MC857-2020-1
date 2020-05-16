import assento
import html_bloco_texto
import html_botao_submit
import html_tabela



def gera(ses, cpr, tre, ids, detalhe):
  linhas = [].copy()
  cmdverProduto = "ver_produto"
  for id_assento in ids:
    ass = assento.busca_por_identificador(id_assento)
    atrs_assento = assento.obtem_atributos(ass)
    id_trecho = atrs_assento['id_trecho']
    id_compra = atrs_assento['id_compra']
    numero = atrs_assento['numero']
    ht_trecho = html_bloco_texto.gera(id_trecho, None, None, None, None, None, None, None, None)
    ht_compra = html_bloco_texto.gera(id_compra, None, None, None, None, None, None, None, None)
    ht_numero = html_bloco_texto.gera(numero, None, None, None, None, None, None, None, None)
    ht_exlcuir = html_botao_submit.gera("Excluir", "excluir_assento", None, '#bca360')
    ht_ver = html_botao_submit.gera("Ver", 'ver_assento', None, '#60a3bc')
    linhas.append(( ht_trecho, ht_compra, ht_numero, ht_exlcuir, ht_ver ))
  ht_itens = html_tabela.gera(linhas)
  return ht_itens
