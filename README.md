# Simple Website — DevOps Final Project

A minimal Flask site to demonstrate DevOps fundamentals: tests, CI builds, container image publishing, release artifacts, and optional CD to a local k3d/K3s cluster using Kustomize.

## Features
- **Flask app** with `/health` and `/version` endpoints + simple homepage
- **Tests** with `pytest`
- **Docker** + `docker-compose` for local dev
- **CI** with GitHub Actions: test → build → push image to GHCR
- **Release** workflow: zip artifact on tag (e.g., `v0.1.0`)
- **IaC**: k3d cluster config, K8s manifests via Kustomize, Ansible deploy playbook

## Quickstart

### Local (no Kubernetes)
```bash
cp .env.example .env
make run
# open http://localhost:8080
```

### Run tests
```bash
make test
```

### Build & Push container (requires GHCR auth)
```bash
echo 0.1.0 > VERSION
make build push
```

### Release (creates tag & GH Release via GitHub Action)
```bash
make release
# pushes tag v0.1.0; release.yml uploads dist zip
```

### (Optional) Deploy to local k3d/K3s
```bash
# requires k3d, kubectl, kustomize
make deploy
# visit http://localhost:8080 (Ingress forwards 80→8080 on host)
```

## Configuration
- Update image name in `Makefile` and `k8s/kustomization.yaml`: `ghcr.io/<OWNER>/simple-website`
- Change `SITE_NAME` in `.env` or K8s env vars

## Troubleshooting
- **Image pull error**: Ensure GHCR visibility/permissions and `docker login ghcr.io`
- **Ingress not reachable**: Check that the k3d load balancer port mapping exists (`infra/k3d-cluster.yaml`) and Traefik ingress class matches your cluster
- **CI cannot push**: PAT must have `write:packages` scope; set `GHCR_USERNAME` and `GHCR_TOKEN` in repo secrets
- **Kustomize apply fails**: Ensure kubecontext points to your k3d cluster (`kubectl config get-contexts`)

## Tech Stack
- Python/Flask, Pytest
- Docker, Docker‑Compose
- GitHub Actions (CI, Release)
- k3d/K3s, Kubectl, Kustomize, Ansible

## License
MIT
