#
# Makefile
#

help:
	@echo "Usage: make [target]"
.PHONY: help

run:
	pipenv run python bin/main.py
.PHONY: run

prepare:
	./scripts/prepare.sh
.PHONY: prepare
