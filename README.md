# 🧪 Interneers Lab 2026 – Fullstack Python (Django)
## Inventory Management System (IMS)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-REST_Framework-green)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)
![Status](https://img.shields.io/badge/Project%20Status-In%20Progress-yellow)
![Tests](https://img.shields.io/badge/Tests-Passing-success)
![Coverage](https://img.shields.io/badge/Coverage-WIP-orange)
![PRs](https://img.shields.io/badge/PRs-Required-blueviolet)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

### 📌 Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Database:** MongoDB (MongoEngine)  
- **Frontend:** HTML, CSS, JavaScript, React + TypeScript  
- **Testing:** PyTest / Django Test Framework  
- **Tools:** GitHub, Docker (MongoDB), Postman

This repository tracks my progress through the **Interneers Lab 2026 – Fullstack Python Track**.  
The goal is to build a **small but production-style end-to-end Inventory Management System**, evolving week by week.

---

## 🗂️ Week-wise Goals & Progress

> Use this checklist to track completion.  
> `[ ]` = Pending | `[x]` = Completed

---

## ✅ Week 1 – Development Setup & Foundations

### Upskilling
- [x] Understand Git & GitHub workflow
- [x] Learn Python virtual environments & pip (`venv`)
- [x] Follow PEP8 and clean code practices `(using black formatter)`
- [x] Understand Hexagonal Architecture (Ports & Adapters)

### Implementation
- [x] Fork the Interneers Lab starter repository
- [x] Install and verify all required tools
- [x] Make recommended repo changes and verify locally
- [x] Build a **simple GET API** using hexagonal architecture
- [x] Test API using Postman
- [x] Push changes to GitHub

### Advanced (Optional)
- [ ] Document project layering based on hexagonal architecture
- [x] Improve README 

---

## ✅ Week 2 – Django & REST APIs (In-Memory)

### Upskilling
- [x] Learn Python fundamentals
- [x] Learn Django basics and project structure
- [x] Understand HTTP methods (GET, POST, PUT, DELETE)
- [x] Learn REST API best practices

### Implementation
- [x] Create `Product` model (name, description, category, price, brand, quantity)
- [x] Implement CRUD APIs for Product
- [x] Use **in-memory storage** (no database)
- [x] Add basic input validations
- [x] Test all APIs using HTTP client

### Advanced (Optional)
- [x] Add pagination to product list API
- [x] Return meaningful error messages

---

## ✅ Week 3 – Service Layer & Database Integration

### Upskilling
- [ ] Learn Controller–Service–Repository pattern
- [ ] Understand ORMs and persistence
- [ ] Learn MongoDB basics and MongoEngine
- [ ] Understand MVC in Django

### Implementation
- [ ] Refactor controllers to be thin
- [ ] Create `ProductService` for business logic
- [ ] Create repository layer for DB access
- [ ] Setup MongoDB (preferably using Docker)
- [ ] Migrate Product model to MongoEngine
- [ ] Persist data in MongoDB
- [ ] Inspect collections using MongoDB Compass

### Advanced (Optional)
- [ ] Add `created_at` and `updated_at` audit fields
- [ ] Use audit fields to improve API responses

---

## ✅ Week 4 – Relations, Validation & Advanced APIs

### Upskilling
- [ ] Understand relational modeling in NoSQL
- [ ] Learn filtering, sorting, pagination patterns
- [ ] Learn advanced validation & error handling

### Implementation
- [ ] Create `ProductCategory` model (title, description)
- [ ] Implement `ProductCategoryService`
- [ ] Add CRUD APIs for product categories
- [ ] Associate Products with Categories
- [ ] Fetch products by category
- [ ] Add/remove products from categories
- [ ] Enforce **brand as mandatory**
- [ ] Handle existing products without brand
- [ ] Implement bulk product creation via CSV upload

### Advanced (Optional)
- [ ] Write seed scripts for categories
- [ ] Add rich filters (multiple categories, price ranges)
- [ ] Write migration scripts for legacy products

---

## ✅ Week 5 – Testing & Collaboration Workflow

### Upskilling
- [ ] Learn unit testing & mocking
- [ ] Learn integration testing
- [ ] Understand test coverage
- [ ] Learn GitHub code review workflow

### Implementation
- [ ] Write unit tests for `ProductService`
- [ ] Write unit tests for `ProductCategoryService`
- [ ] Mock repository layer in unit tests
- [ ] Create seed data for testing
- [ ] Write integration tests with test MongoDB
- [ ] Stop direct merges to `main`
- [ ] Use Pull Requests for all changes
- [ ] Respond to mentor/peer review feedback

### Advanced (Optional)
- [ ] Add regression test scripts
- [ ] Write parameterized unit tests
- [ ] Review a peer’s PR

---

## ✅ Week 6 – Frontend Basics (HTML/CSS/JS)

### Upskilling
- [ ] Learn HTML structure & semantics
- [ ] Learn CSS basics & box model
- [ ] Learn JavaScript fundamentals
- [ ] Use browser developer tools

### Implementation
- [ ] Create HTML page to display Product tile
- [ ] Style Product tile using CSS
- [ ] Fetch products via API using vanilla JS
- [ ] Log and inspect API responses in browser
- [ ] Explore DOM using dev tools

### Advanced (Optional)
- [ ] Dynamically render product data
- [ ] Render full product list
- [ ] Add CSS animations

---

## ✅ Week 7 – React & TypeScript

### Upskilling
- [ ] Learn TypeScript basics
- [ ] Learn React fundamentals
- [ ] Understand component-based architecture
- [ ] Learn debugging React apps

### Implementation
- [ ] Setup React + TypeScript project
- [ ] Create Product component with dummy data
- [ ] Create ProductList component
- [ ] Add expand/collapse interaction for products

### Advanced (Optional)
- [ ] Add header and navigation bar
- [ ] Improve component reuse

---

## ✅ Week 8 – Frontend Integration & State

### Upskilling
- [ ] Learn state management in React
- [ ] Learn API consumption patterns
- [ ] Handle loading & error states
- [ ] Learn routing and navigation

### Implementation
- [ ] Create dedicated Product detail page
- [ ] Enable editing products from UI
- [ ] Move products across categories
- [ ] Display API errors gracefully
- [ ] (Optional) CRUD for categories via UI

### Advanced (Optional)
- [ ] Create category pages
- [ ] Add loading spinners
- [ ] Add deep navigation between products & categories

---

## 🚀 Week 9/10 – Optional Product Extensions

### Features
- [ ] Reporting: product count per category
- [ ] Reporting: low-stock products
- [ ] Price range–based reports
- [ ] CSV export of reports
- [ ] Navigation from reports to products

### Engineering
- [ ] Write approach/design note
- [ ] Add end-to-end Playwright test
- [ ] Improve UX & performance

---

## 📈 Final Goal

By the end of this track, this repository should contain:
- A **cleanly layered Django backend**
- A **working React frontend**
- **Well-tested APIs**


---

## 📝 Notes
- Advanced items are optional but strongly recommended
- Code quality, structure, and clarity matter more than feature count
- This README doubles as a **progress tracker**



# Interneers Lab

Welcome to the **Interneers Lab** repository! This serves as a minimal starter kit for learning and experimenting with:
- **Django** (Python)
- **Golang** (Go)
- **React**  (with TypeScript)
- **MongoDB** (via Docker Compose)
- Development environment in **VSCode** (recommended)

**Important:** Use the **same email** you shared during onboarding when configuring Git and related tools. That ensures consistency across all internal systems.

### Project structure

```
backend/
  go/          # Golang backend (see backend/go/README.md)
  python/      # Django (Python) backend (see backend/python/README.md)
frontend/      # React + TypeScript (see frontend/README.md)
```

---

## Table of Contents

1. [Getting Started with Git & Forking](#getting-started-with-git-and-forking)
2. [Prerequisites & where to find them](#prerequisites--where-to-find-them)
3. [Setting up & running](#setting-up--running)
4. [Development Workflow](#development-workflow)
   - [Pushing Your First Change](#pushing-your-first-change)
5. [Making your first change](#making-your-first-change)
6. [Running Tests](#running-tests)
7. [Frontend Setup](#frontend-setup)
8. [Further Reading](#further-reading)

---

## Getting Started with Git and Forking

### 1. Setting up Git and the Repo

1. **Install Git** (if not already):
   - **macOS**: [Homebrew](https://brew.sh/) users can run `brew install git`.
   - **Windows**: Use [Git for Windows](https://gitforwindows.org/).
   - **Linux**: Install via your distro's package manager, e.g., `sudo apt-get install git` (Ubuntu/Debian).

2. **Configure Git** with your name and email:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com" # Use the same email you shared during onboarding
   ```

3. **What is Forking?**

   Forking a repository on GitHub creates your own copy under your GitHub account, where you can make changes independently without affecting the original repo. Later, you can make pull requests to merge changes back if needed.

4. Fork the Rippling/interneers-lab repository (ensure you're in the correct org or your personal GitHub account, as directed).
5. **Clone** your forked repo:
   ```bash
   git clone git@github.com:<YourUsername>/interneers-lab.git
   cd interneers-lab
   ```

## Prerequisites & where to find them

Prerequisites (Python, Go, Node, Docker, etc.) and how to verify your setup are documented in each part of the repo:

- **[backend/python/README.md](backend/python/README.md)** — Python/Django, virtualenv, MongoDB
- **[backend/go/README.md](backend/go/README.md)** — Go, MongoDB
- **[frontend/README.md](frontend/README.md)** — Node, Yarn, React

Use the README for the part you're working on.

---

## Setting up & running

Setup and run instructions live in the domain READMEs:

- **Python backend:** [backend/python/README.md](backend/python/README.md) — venv, dependencies, `runserver`, Docker Compose for MongoDB
- **Go backend:** [backend/go/README.md](backend/go/README.md) — `make setup`, `make build-and-run`, Docker Compose
- **Frontend:** [frontend/README.md](frontend/README.md)

---

## Development Workflow

### Making your first change

Step-by-step tutorials live in the domain READMEs:

- **[backend/python/README.md](backend/python/README.md)** — Django starters (e.g. Hello World, Hello {name} API)
- **[backend/go/README.md](backend/go/README.md)** — Go hello-world and APIs
- **[frontend/README.md](frontend/README.md)** — React hello-world and APIs

### Pushing Your First Change

1. **Stage and commit**:
   ```bash
   git add .
   git commit -m "Your descriptive commit message"
   ```
2. **Push to your forked repo (main branch by default):**
   ```bash
   git push origin main
   ```

---

## Running Tests

See the domain READMEs for how to run tests in each stack:

- [backend/python/README.md](backend/python/README.md)
- [backend/go/README.md](backend/go/README.md)
- [frontend/README.md](frontend/README.md)

---

## Further Reading

Each domain has detailed README with links to relevant docs. In general:

- **Django:** [docs.djangoproject.com](https://docs.djangoproject.com/)
- **React:** [react.dev](https://react.dev/learn)
- **Go:** [go.dev/doc](https://go.dev/doc/)
- **MongoDB:** [docs.mongodb.com](https://docs.mongodb.com/)
- **Docker Compose:** [docs.docker.com/compose](https://docs.docker.com/compose/)
