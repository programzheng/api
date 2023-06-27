COMPOSE=docker compose
ENV_ARG=--env-file .env.docker
SERVICES=app

build:
	$(COMPOSE) $(ENV_ARG) build $(SERVICES)

#重新編譯
dev:
	$(COMPOSE) $(ENV_ARG) build $(SERVICES)
	$(COMPOSE) $(ENV_ARG) up $(SERVICES)

#啟動服務
up:
	$(COMPOSE) $(ENV_ARG) up -d $(SERVICES)

ps:
	$(COMPOSE) $(ENV_ARG) ps