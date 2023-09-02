build:
	docker-compose build --parallel
up:
	docker-compose up -d
logs:
	docker-compose logs
down:
	docker-compose down --remove-orphans
clean:
	docker image prune -a

BACKEND_DIR := backend
TARGET := $(MAKECMDGOALS)

include $(BACKEND_DIR)/Makefile

.PHONY: $(TARGET)
$(TARGET):
	cd $(BACKEND_DIR) && $(MAKE) $(TARGET)
	@true