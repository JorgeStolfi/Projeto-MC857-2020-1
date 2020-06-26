
.PHONY: testes_de_modulos teste_unico

# Módulos que não devem ter programas de teste:
MODULOS_NAO_TESTAR := ${shell gawk '/^[N]/{ print $$2; }' modulos.txt}

# Módulos cujos testes estavam OK na última verificação:
MODULOS_OK := ${shell gawk '/^[A]/{ print $$2; }' modulos.txt}

# Módulos cujos testes estavam com problemas na última verificação:
MODULOS_BUG := ${shell gawk '/^[*]/{ print $$2; }' modulos.txt}

# Todos os módulos testáveis:
MODULOS_TODOS := ${shell gawk '/^[*A]/{ print $$2; }' modulos.txt}

# Módulos a testar em {testes_de_modulos}:
MODULOS := ${MODULOS_TODOS}
# MODULOS := ${MODULOS_BUG}

# O que "make" deve fazer:
# all: testes_de_modulos 00-LINKS.html
# all: teste_unico 00-LINKS.html
all: roda_servidor 00-LINKS.html

# Roda testes dos módulos em ${MODULOS}:
testes_de_modulos:
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

00-LINKS.html: 00-LINKS.txt ~/bin/convert_links_to_html.gawk
	~/bin/convert_links_to_html.gawk 00-LINKS.txt > 00-LINKS.html
