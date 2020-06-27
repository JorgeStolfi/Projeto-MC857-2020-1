import compra
import usuario
import poltrona
import trecho
import html_form
import html_table
import html_label
import html_input
import html_botao_submit
import html_div
import html_input

def gera(cpr, editavel, texto_bt, comando_bt):

  # Obtem atributos a mostrar:
  
  valores = {}.copy()
  id_cpr = compra.obtem_identificador(cpr)
  atrs_cpr = compra.obtem_atributos(cpr)
  
  # Atributos da compra em si
  valores['id_cpr'] = id_cpr
  valores['status'] = atrs_cpr['status']
  valores['nome_pass'] = atrs_cpr['nome_pass']
  valores['doc_pass'] = atrs_cpr['doc_pass']
  valores['preco_tot'] = ("%.2f" % compra.calcula_preco(cpr))
  # valores['pagamento'] = atrs_cpr['pagamento']

  # Cliente que está montando ou montou a compra:
  usr = compra.obtem_cliente(cpr)
  valores['id_usr'] = usuario.obtem_identificador(usr)
  atrs_usr = usuario.obtem_atributos(usr)
  valores['nome_usr'] = atrs_usr['nome']

  # Bilhetes da compra:
  ids_pols = compra.obtem_poltronas(cpr)
  num_trechos = len(ids_pols)
  valores['n_trechos'] = str(num_trechos)
  
  if (num_trechos >= 1):
    # Obtém origem, data, e hora de partida do primeiro trecho:
    pol_ini = poltrona.busca_por_identificador(ids_pols[0])
    id_trc_ini = poltrona.obtem_atributo(pol_ini, 'id_trecho')
    trc_ini = trecho.busca_por_identificador(id_trc_ini)
    origem = trecho.obtem_atributo(trc_ini, 'origem')
    dh_partida = trecho.obtem_dia_e_hora_de_partida(trc_ini)
    valores['partida'] = origem + " " + dh_partida

    # Obtém destino, data, e hora de chegada do último trecho:
    pol_fin = poltrona.busca_por_identificador(ids_pols[-1])
    id_trc_fin = poltrona.obtem_atributo(pol_fin, 'id_trecho')
    trc_fin = trecho.busca_por_identificador(id_trc_fin)
    destino = trecho.obtem_atributo(trc_fin, 'destino')
    dh_chegada = trecho.obtem_dia_e_hora_de_chegada(trc_fin)
    valores['chegada'] = destino + " " + dh_chegada
    
  # Linhas para {html_table.gera}:
  linhas = (
    html_cpr_campo("Compra",                  'id_cpr',    valores, 'text', None,              False),
    html_cpr_campo("Cliente",                 'id_usr',    valores, 'text', None,              False),
    html_cpr_campo("Nome do cliente",         'nome_usr',  valores, 'text', None,              False),
    html_cpr_campo("Nome do passageiro",      'nome_pass', valores, 'text', "Fulano da Silva", editavel),
    html_cpr_campo("Documento do passageiro", 'doc_pass',  valores, 'text', "123.456.789-10", editavel),
    html_cpr_campo("Número de trechos",       'n_trechos', valores, 'text', None,              False),
    html_cpr_campo("Preço total",             'preco_tot', valores, 'text', None,              False),
    html_cpr_campo("Estado",                  'status',    valores, 'text', None,              False),
    html_cpr_campo("Partida",                 'partida',   valores, 'text', None,              False),
    html_cpr_campo("Chegada",                 'chegada',   valores, 'text', None,              False),
  )
  ht_campos = html_table.gera(linhas);

  # Botões: 
  if editavel:
    args_submit = { 'id_compra': id_cpr } # Argumentos adicionais para submissão.
    ht_submit = html_botao_submit.gera(texto_bt, comando_bt, args_submit, "#44ff44")
    ht_campos += "<br/>" + ht_submit

  return html_form.gera(ht_campos)

def html_cpr_campo(rotulo, nome, valores, tipo, dica, editavel):
  """Função auxiliar para formatar a tabela de campos.

  Devolve um par {(ht_lab, ht_val)} onde {ht_lab} é um elemento <label>...</label>,
  e {ht_val} é um elemento <input ... /> ou um <div>...</div> com o formato apropriado.  
  
  O string {rotulo} é o nome do campo visível para o usuário, como
  "Nome do passageiro". Será o conteúdo do {ht_lab}.
  
  O string {nome} é o nome interno do atributo da compra, como 'id_usuario',
  'preco_tot', 'saida', 'chegada', etc.
  
  O parâmetro {valores} é um dicionário Python que pode definir ou não um
  valor {val} para a chave {nome}.  Se não definir, o valor {val} será tomado como {None}.
  Se o {tipo} for "number", o dicionário pode também definir um valor {vmin}
  para a chave "{nome}_min"; caso contrário {vmin} será tomado como {None}.
  
  Se o parâmetro {tipo} for {None}, o resultado {ht_val} será o valor
  {val} formatado como um <div>...</div> de estilo adequado.
  
  Se o parâmetro {tipo} não for {None}, deve ser um string que especifica
  um tipo de elemento <input.../> que será devolvido em {ht_val},
  Por exemplo "text", "number", "readonly". Nesse caso {ht_val} será 
  
    "<input type='{tipo}' name='{nome}' value='{val}'
    min='{vmin}' placeholder='{dica}'/>"
  
  O parâmetro {dica} só é usado se {tipo} não for {None} mas {val} for {None};
  será a dica de preenchimento do camo. Por exemplo, para
  um campo de data, a dica pode ser "AAAA-MM-DD"."""
  ht_lab = html_label.gera(rotulo, ": ")
  val = (valores[nome] if nome in valores else None)
  if tipo == None:
    estilo = "font-family:Courier;font-size:18"
    ht_val = html_div.gera(estilo, val)
  else:
    nmin = nome + "_min"
    vmin = (valores[nmin] if nmin in valores else None)
    if val != None: dica = None
    ht_val = html_input.gera(None, tipo, nome, val, vmin, editavel, dica, None)
    
  return (ht_lab, ht_val)
  
