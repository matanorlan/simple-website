APP?=simple-website
IMAGE?=ghcr.io/OWNER/$(APP)
TAG?=$(shell cat VERSION 2>/dev/null || echo dev)
KUBECONFIG?=$(HOME)/.kube/config
COMPOSE ?= docker compose


.PHONY: run build push test release infra-up k8s-apply deploy

run:
	docker compose up --build
	$(COMPOSE) up --build
build:
	docker build -t $(IMAGE):$(TAG) .

push:
	docker push $(IMAGE):$(TAG)

test:
	pytest -q

release:
	git tag v$(TAG) && git push origin v$(TAG)

infra-up:
	k3d cluster create --config infra/k3d-cluster.yaml || true

k8s-apply:
	kubectl apply -k k8s

deploy: infra-up k8s-apply
	@echo "Deployed $(IMAGE):$(TAG)"
