
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS_OK := \
   \
  utils_testes \
   \
  base_sql \
  identificador \
  tabela_generica \
  objeto \
  conversao_sql \
   \
  html_elemento_span \
  html_bloco_texto \
   \
  html_elemento_label \
  html_elemento_input \
  html_estilo_de_botao \
  html_botao_simples \
  html_botao_submit \
   \
  html_cabecalho \
  html_menu_geral \
  html_rodape \
   \

MODULOS := \
  usuario \
  compra \
  sessao \
  tabelas \
   \
  
MODULOS_A_CONVERTER := \
   \
  gera_html_elem \
   \
  gera_html_form \
  gera_html_pag \
   \
  processa_comando_http \
   \
  comando_alterar_qtd_de_produto \
  comando_buscar_compras \
  comando_buscar_produtos \
  comando_comprar_produto \
  comando_definir_dados_de_produto \
  comando_definir_dados_de_usuario \
  comando_definir_endereco \
  comando_definir_meio_de_pagamento \
  comando_excluir_item_de_compra \
  comando_fazer_login \
  comando_fazer_logout \
  comando_finalizar_compra \
  comando_solicitar_form_de_endereco \
  comando_solicitar_form_de_dados_de_produto \
  comando_solicitar_form_de_dados_de_usuario \
  comando_solicitar_form_de_meio_de_pagamento \
  comando_solicitar_form_de_login \
  comando_trocar_carrinho \
  comando_ver_compra \
  comando_ver_carrinho \
  comando_ver_ofertas \
  comando_ver_produto

# O que "make" deve fazer:
all: todos_os_testes
# all: teste_unico
# all: roda_servidor

# Roda todos os módulos de teste:
todos_os_testes:
	for modulo in ${MODULOS} ; do \
	  { ./testa.sh $${modulo} ; echo "" ; } ; \
        done

# MODULO := identificador
# MODULO := conversao_sql
# MODULO := base_sql
# MODULO := tabela_generica
# MODULO := usuario
# MODULO := produto
# MODULO := sessao 
# MODULO := compra
# MODULO := gera_html_elem

teste_unico:
	./testa.sh ${MODULO}

roda_servidor:
	./cria_base_de_teste.py
	( ./servidor.py & sleep 1000 )
