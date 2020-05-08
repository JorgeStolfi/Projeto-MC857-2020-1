
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS_OK := \
   \
  utils_testes \
  valida_campo \
 \
  base_sql \
  identificador \
  tabela_generica \
  conversao_sql \
 \
  html_span \
  html_div \
  html_bloco_texto \
  html_paragrafo \
  html_input \
  html_label \
 \
  html_estilo_de_botao \
  html_botao_simples \
  html_botao_submit \
 \
  html_cabecalho \
  html_menu_geral \
  html_rodape \
 \
  processa_comando_http \
 \
  comando_alterar_usuario \
  comando_cadastrar_usuario \

MODULOS := \
  html_tabela \
 \
  objeto \
 \
  html_form \
  html_form_tabela_de_campos \
  html_form_entrar \
 \
  html_bloco_erro \
 \
  usuario \
  compra \
  sessao \
  tabelas \
 \
  html_bloco_lista_de_usuarios \
  html_bloco_usuario \
  html_form_alterar_usuario \
  html_form_cadastrar_usuario \
  html_form_dados_de_usuario \
 \
  html_pag_alterar_usuario \
  html_pag_cadastrar_usuario \
  html_pag_entrar \
  html_pag_generica \
  html_pag_mensagem_de_erro \
  html_pag_principal \
 \
  comando_fazer_login \
  comando_fazer_logout \
  comando_solicitar_pag_login \

MODULOS_A_CONVERTER := \
  comando_buscar_compras \
  comando_definir_dados_de_usuario \
  comando_definir_endereco \
  comando_definir_meio_de_pagamento \
  comando_excluir_item_de_compra \
  comando_finalizar_compra \
  comando_solicitar_pag_dados_de_usuario \
  comando_solicitar_pag_meio_de_pagamento \
  comando_trocar_carrinho \
  comando_ver_compra \
  comando_ver_carrinho \
  comando_ver_ofertas \

# O que "make" deve fazer:
all: todos_os_testes
# all: teste_unico
# all: roda_servidor

# Roda todos os módulos de teste:
todos_os_testes:
	-rm -fv testes/saida/*.html
	for modulo in ${MODULOS} ; do \
	  { ./testa.sh $${modulo} ; echo "" ; } ; \
        done

# MODULO := identificador
# MODULO := conversao_sql
# MODULO := base_sql
# MODULO := tabela_generica
# MODULO := usuario
# MODULO := sessao 
# MODULO := compra
MODULO := html_pag_cadastrar_usuario

teste_unico:
	./testa.sh ${MODULO}

roda_servidor:
	./cria_base_de_teste.py
	( ./servidor.py & sleep 1000 )
