import trecho
import html_botao_simples
import html_imagem
import html_span
import poltrona

def gera(trc, bt_ver, bt_alterar, bt_clonar, bt_fechar):
  id_trc = trecho.obtem_identificador(trc)
  atrs_trc = trecho.obtem_atributos(trc)
  # Pega/monta atributos a mostrar:
  
  map_poltronas_disponiveis = trecho.obtem_poltronas_livres(trc)
  if not map_poltronas_disponiveis:
    a_partir_de = "Esgotado"
  else:
    precos = [].copy()
    for id_poltrona in map_poltronas_disponiveis:
      pol = poltrona.busca_por_identificador(id_poltrona)
      atrs_pol = poltrona.obtem_atributos(pol)
      if(atrs_pol['id_compra'] is None):
        precos.append(atrs_pol['preco'])
    precos = list(map(float, precos))
    a_partir_de = str(min(precos))
  codigo = atrs_trc['codigo']
  empresa = codigo.split(" ")[0] # Sigla da empresa.
  origem = atrs_trc['origem']
  destino = atrs_trc['destino']
  dt_partida = atrs_trc['dia_partida'] + " " + atrs_trc['hora_partida']
  dt_chegada = atrs_trc['dia_chegada'] + " " + atrs_trc['hora_chegada']
  veiculo = atrs_trc['veiculo']
  num_poltronas_total = str(trecho.numero_de_poltronas(trc))
  num_poltronas_livres = str(trecho.numero_de_poltronas_livres(trc))
  # !!! Deveria mostrar também atributo 'aberto' !!!

  # Formata informações em HTML:
  ht_logo = html_imagem.gera("/" + empresa + ".png", "logo", 20)
  ht_codigo = formata_texto(codigo)
  ht_origem = formata_texto(origem)
  ht_destino = formata_texto(destino)
  ht_dt_partida = formata_texto(dt_partida)
  ht_dt_chegada = formata_texto(dt_chegada)
  ht_veiculo = formata_texto(veiculo)
  ht_num_poltronas_livres = formata_texto(num_poltronas_livres)
  ht_num_poltronas_total = formata_texto(num_poltronas_total)
  ht_a_partir_de = formata_texto(a_partir_de)

  ht_campos = [ 
    ht_logo, ht_codigo, 
    ht_origem, ht_dt_partida, 
    ht_destino, ht_dt_chegada, 
    ht_num_poltronas_livres, ht_num_poltronas_total,
    ht_a_partir_de 
  ]
  
  args_bt = {'id_trecho': id_trc} # Argumentos para os botões.
  cor_bt_normal = '#00FF00' # Cor para botões de uso geral.
  cor_bt_admin = '#FFA700' # Cor para botões de adminstrador.

  if bt_ver:
    ht_bt_ver = html_botao_simples.gera("Ver", 'ver_trecho', args_bt, cor_bt_normal)
    ht_campos.append(ht_bt_ver)

  if bt_alterar:
    ht_bt_alterar = html_botao_simples.gera("Alterar", 'solicitar_pag_alterar_trecho', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_alterar)

  if bt_clonar:
    ht_bt_clonar = html_botao_simples.gera("Clonar", 'solicitar_pag_clonar_trecho', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_clonar)

  if bt_fechar:
    ht_bt_fechar = html_botao_simples.gera("Encerrar", "encerrar_trecho", args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_fechar)

  return ht_campos

def formata_texto(txt):
  """Formata o texto {txt} com um estilo apropriado."""
  estilo = "font-weight:bold"
  return html_span.gera(estilo, txt)
