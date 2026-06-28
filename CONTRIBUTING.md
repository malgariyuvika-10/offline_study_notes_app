# Contributing Guide

Thank you for your interest in contributing to the **Offline Study Notes Structuring App**.

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

## Getting Started

1. Fork this repository.
2. Clone your fork locally.

```bash
git clone https://gitlab.com/your-username/offline-study-notes-ai.git
```

3. Create a new branch.

```bash
git checkout -b feature/feature-name
```

---

## Development Setup

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Coding Standards

* Follow PEP 8
* Write modular code
* Add comments where necessary
* Keep functions small and reusable
* Use descriptive variable names

---

## Commit Message Format

Use semantic commits.

Examples:

```text
feat: add PDF extraction module

fix: resolve OCR parsing issue

docs: update README

test: add unit tests for pipeline

refactor: simplify preprocessing module
```

---

## Pull Request Process

Before submitting a merge request:

* Run all tests
* Verify formatting
* Update documentation if required
* Ensure the application works offline
* Ensure CPU-only inference

---

## Code of Conduct

Please be respectful and collaborative.

We aim to create an inclusive and welcoming open-source community.

---

## Reporting Issues

When creating an issue, include:

* Operating System
* Python Version
* Error Logs
* Steps to Reproduce
* Expected Behaviour
* Actual Behaviour

---

## Project Goals

This project follows the CPU-First Hackathon principles:

* Offline First
* CPU Optimized
* Open Source
* Privacy Focused
* No Cloud APIs

Thank you for contributing!
