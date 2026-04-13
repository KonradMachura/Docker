# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A minimal Docker learning exercise demonstrating container parameterization using Alpine Linux. The same image is reused with different runtime environment variables to produce different behavior across multiple containers.

## Commands

**Build the image:**
```bash
docker build -t hello-container .
```

**Run all 5 containers (builds first, then runs sequentially):**
```bash
./run.sh
```

**Run a single container with a specific number:**
```bash
docker run --rm -e CONTAINER_NUMBER=3 hello-container
```

**Build with a baked-in number (build-time arg):**
```bash
docker build --build-arg CONTAINER_NUMBER=3 -t hello-container .
docker run --rm hello-container
```

## Architecture

- `Dockerfile` — Alpine 3.19 base; accepts `CONTAINER_NUMBER` as both a build arg (baked into the image via `ENV`) and a runtime env var override. The `CMD` echoes the value.
- `run.sh` — Builds the image once, then runs 5 containers sequentially, passing `CONTAINER_NUMBER` via `-e` (the `--build-arg` in the run loop has no effect on already-built images — only the `-e` flag matters at runtime).

**Key distinction:** `ARG` is build-time only; `ENV` persists into the container. The Dockerfile uses `ENV CONTAINER_NUMBER=${CONTAINER_NUMBER}` to promote the build arg into a runtime variable, but runtime `-e` always overrides it.
