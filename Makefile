
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS_NAO_TESTAR := \
   \
  processa_comando_http \
  servidor \

MODULOS_OK := \
   \
  utils_testes \
  valida_campo \
  conversao_sql \
 \
  base_sql \
  identificador \
  tabela_generica \
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
  html_bloco_erro \
 \
  objeto \
  usuario \
  compra \
  sessao \
 \
  html_form_login \
  html_form_dados_de_usuario \
  html_form_alterar_usuario \
  html_form_cadastrar_usuario \
 \
  html_pag_login \
  html_pag_generica \
  html_pag_mensagem_de_erro \
  html_pag_principal \
 \
  html_pag_cadastrar_usuario \
  html_pag_alterar_usuario \
 \
  comando_solicitar_pag_login \
  comando_solicitar_pag_alterar_usuario \
  comando_solicitar_pag_cadastrar_usuario \
 \
  comando_fazer_login \
  comando_fazer_logout \
  comando_cadastrar_usuario \
  comando_alterar_usuario \
  
# Módulos cujos testes não estão OK
MODULOS_TAREFAS := \
 \
  html_tabela \
  html_form \
  html_form_tabela_de_campos \
 \
  assento \
  tabelas \
 \
  html_bloco_lista_de_usuarios \
  html_bloco_usuario \

MODULOS_BUG := \
 \
  trecho \
 \
  comando_ver_objeto \

MODULOS_A_CONVERTER := \
  comando_buscar_compras \
  comando_ver_compra \
  comando_ver_carrinho \
  comando_ver_ofertas \

# O que "make" deve fazer:
# MODULOS := ${MODULOS_OK} ${MODULOS_BUG}
MODULOS := ${MODULOS_BUG}

# all: todos_os_testes
# all: teste_unico
all: roda_servidor

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
	( ./servidor.py & sleep 1000 )
