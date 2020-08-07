import sessao
import trecho
import compra
import usuario
import poltrona
import html_pag_generica
import html_form_dados_de_poltrona
import html_botao_submit
import html_botao_simples

def gera(ses, pol, atrs, erros):
  # Obtem dados da sessão e seu usuário:
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)
  admin = sessao.eh_administrador(ses)
  carr = None if (ses == None) or admin else sessao.obtem_carrinho(ses)
  
  # Obtem dados correntes da poltrona:
  assert pol != None, "poltrona deve ser especificada"
  assert type(pol) is poltrona.Objeto_Poltrona
  id_pol = poltrona.obtem_identificador(pol)
  assert id_pol != None # Paranóia.

  # Completa {atrs} com atributos correntes de {pol}:
  if atrs == None: atrs = {}.copy() # Por via das dúvidas.
  atrs_pol = poltrona.obtem_atributos(pol)
  assert atrs_pol != None # Paranóia
  for ch, val in atrs_pol.items():
    if not ch in atrs: atrs[ch] = val

  # Obtem compra {cpr} da poltrona, se houver:
  id_cpr = poltrona.obtem_atributo(pol, 'id_compra')
  cpr = None if id_cpr == None else compra.busca_por_identificador(id_cpr)
  cpr_aberta = False if cpr == None else compra.obtem_status(cpr) == 'comprando'
  usr_cpr = None if cpr == None else compra.obtem_cliente(cpr)
  
  # Obtem trecho {trc} da poltrona:
  id_trc = poltrona.obtem_atributo(pol, 'id_trecho')
  assert id_trc != None # Paranóia.
  trc = trecho.busca_por_identificador(id_trc)
  assert trc != None # Paranóia.
  encerrado = trecho.obtem_atributo(trc, 'encerrado')
  
  # Gera botões da página:
  ht_submit = ""
  # Tem botão "Alterar" para alterar dados?
  if admin:
    ht_submit += html_botao_submit.gera("Alterar", "alterar_poltrona", None, "#ff0000")
  
  # Tem botão "Excluir" para excluir a poltrona de {cpr}?
  if poltrona.pode_excluir(usr_ses, pol): 
    ht_submit += html_botao_simples.gera("Excluir", "excluir_poltrona", {'id_poltrona': id_pol}, "#ff4400")

  # Tem botão "Comprar" para comprar a poltrona?
  if poltrona.pode_comprar(usr_ses, pol, carr): 
    ht_submit += html_botao_simples.gera("Comprar", "comprar_poltrona", {'id_poltrona': id_pol}, "#ff4400")
  
  # Tem botão "Trocar" para trocar a poltrona?
  if poltrona.pode_trocar(usr_ses, pol): 
    ht_submit += html_botao_simples.gera("Trocar", "trocar_poltrona", {'id_poltrona': id_pol}, "#ff4400")
  
  # Botão de cancelar alteração:
  if admin:
    ht_submit += html_botao_simples.gera("Cancelar", "principal", None, "#00ff00")
    
  ht_conteudo = html_form_dados_de_poltrona.gera(id_pol, atrs, admin, ht_submit)
  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
