# Gitflow Pattern Demo (v1.2.0)

This repository demonstrates the **Gitflow** branching strategy.

## Philosophy
Gitflow is a strict branching model designed around the project release. It provides a robust framework for managing larger projects.

## Key Branches
- **main**: Stores the official release history.
- **develop**: Serves as an integration branch for features.
- **feature/**: New features are developed in these branches off of `develop`.
- **release/**: Prepares a new production release.
- **hotfix/**: Quickly patches production releases.

## How to Interact
1. **Start a Feature**: Create a branch off `develop`.
   `git checkout -b feature/my-feature develop`
2. **Finish a Feature**: Merge `feature/my-feature` back into `develop`.
3. **Release**: Create a `release/v1.0` branch off `develop`, then merge into `main` and `develop`.
