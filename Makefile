N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

help:
	@echo ""
	@echo "${B}COMANDOS DISPONIBLES"
	@echo " iniciar"
	@echo " notebook"
	@echo ""

install:
	@pipenv install

install_verbose:
	@pipenv install --verbose

notebook:
	@pipenv run jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password=''

lab:
	@pipenv run jupyter lab --no-browser --NotebookApp.token='' --NotebookApp.password=''

deploy:
	git push dokku main:master -f

deploy_enjambre:
	git push enjambre main:master -f