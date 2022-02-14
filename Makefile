.DEFAULT_GOAL := help
ARGS := $(filter-out $(KNOWN_TARGETS),$(MAKECMDGOALS))
HOST_USER = $(id -u)

##@ Help
help: ## Show this screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo ""


##@ Server commands
build: ## Build all containers
	@docker-compose build

setup: ## First time setup
	cp --no-clobber ./env.sample .env

runserver: ## Runs the server [flags]
	 @USER=$(HOST_USER) docker-compose up $(flags)

down: ## Take down server [flags]
	@docker-compose down $(flags)

logs: ## Follow container logs [flags] <container>
	@docker-compose logs $(flags) $(container) | grcat ./config/grc-confs/conf.docker-compose-logs

rebuild: ## Rebuilds contianer [[docker-compose] flags]
	make down && make runserver $(flags)

generate_requirements_file: ## Required for digitalocean deploy
	poetry export -f requirements.txt --output requirements.txt --without-hashes


##@ Django comamnds
makemigrations: ## Make migrations [app] [flags]
	@USER=$(HOST_USER) docker-compose exec web python manage.py makemigrations $(app) $(flags)

checkmigrations: ## Check migrations [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py makemigrations --check --dry-run $(app)

showmigrations: ## Show migrations [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py showmigrations $(app)

migrate: ## Migrate [app] [number]
	@USER=$(HOST_USER) docker-compose exec web python manage.py migrate $(app) $(number) | grcat ./config/grc-confs/conf.sql

run_command: ## Run a management command [command]
	@USER=$(HOST_USER) docker-compose exec web python manage.py $(command) | grcat ./config/grc-confs/conf.sql


##@ Testing
pytest: ## Run pytest [path]
	@USER=$(HOST_USER) docker-compose exec web poetry run pytest $(path)


##@ Tooling
mypy: ## Run mypy
	@poetry run mypy config src

black: ## Run black check
	@poetry run black --check config src

black_format: ## Run black format
	@poetry run black config src

flake8: ## Run flake8
	@poetry run flake8 config src

isort: ## Run isort check
	@poetry run isort --jobs 4 --check config src

isort_format: ## Run isort format
	@poetry run isort --jobs 4 config src

check_all: ## Run all checks
	make -k mypy black isort flake8

format_all: ## Run all formatters
	@make isort_format black_format
