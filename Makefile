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
	@docker-compose logs $(flags) $(container) | grcat conf.docker-compose-logs


##@ Django comamnds
makemigrations: ## Make migrations [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py makemigrations $(app)

checkmigrations: ## Check migrations [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py makemigrations --check --dry-run $(app)

showmigrations: ## Show migrations [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py showmigrations $(app)

migrate: ## Migrate [app]
	@USER=$(HOST_USER) docker-compose exec web python manage.py migrate $(app)


##@ Testing
pytest: ## Run pytest
	@poetry run pytest


##@ Tooling
mypy: ## Run mypy
	@poetry run mypy config apps

black: ## Run black check
	@poetry run black --check config apps

black_format: ## Run black format
	@poetry run black config apps

flake8: ## Run flake8
	@poetry run flake8config apps

isort: ## Run isort check
	@poetry run isort --jobs 4 --check config apps

isort_format: ## Run isort format
	@poetry run isort --jobs 4 config apps

check_all: ## Run all checks
	@make mypy black flake8 isort

format_all: ## Run all formatters
	@make isort_format black_format
