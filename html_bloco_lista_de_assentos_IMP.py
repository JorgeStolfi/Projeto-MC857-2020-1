

def gera(ses, cpr, tre, ids, detalhe):
  linhas = [].copy()
  cmdverProduto = "ver_produto"
  for id_assento in ids:
    ass = assento.busca_por_identifiador(id_assento)
    atrs_assento = assento.obtem_atributos(ass)
    id_trecho = atrs_assento['id_trecho']
    id_compra = atrs_assento['id_compra']
    numero = atrs_assento['numero']
    ht_trecho = html_bloco_texto.gera(id_trecho, estilo_id)
    ht_compra = html_bloco_texto.gera(id_compra, estilo_id)
    ht_numero = html_bloco_texto.gera(numero, estilo_id)]
    ht_excl = html_botao_submit.gera("Excluir", "excluir_assento", None, '#bca360')
    ht_ver = html_botao_submit.gera("Ver", 'ver_assento', None, '#60a3bc')
    linhas.append(( ht_trecho, ht_compra, ht_numero, ht_excl, ht_ver ))
  ht_itens = tabela(linhas)
  return ht_itens
