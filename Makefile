
.PHONY: todos_os_testes teste_unico

# Módulos na ordem a testar:
MODULOS_NAO_TESTAR := ${shell gawk '/^[N]/{ print $$2; }' modulos.txt}

MODULOS_OK := ${shell gawk '/^[A]/{ print $$2; }' modulos.txt}

MODULOS_BUG := ${shell gawk '/^[*]/{ print $$2; }' modulos.txt} \

# O que "make" deve fazer:
MODULOS := ${MODULOS_OK} ${MODULOS_BUG}
# MODULOS := ${MODULOS_BUG}

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
	( ./servidor.py & sleep 1000 )
