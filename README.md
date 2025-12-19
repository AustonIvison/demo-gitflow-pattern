# Gitflow Pattern Demo (v1.3.0)

This repository demonstrates the **Gitflow** branching strategy.

## Philosophy & In-Depth Explanation
Gitflow is a strict branching model designed around the project release. It assigns very specific roles to different branches and defines how and when they should interact. It is excellent for projects that have a scheduled release cycle (e.g., "Version 1.0", "Version 2.0").

In Gitflow, the `main` branch only stores the official release history. The `develop` branch serves as an integration branch for features. When the `develop` branch reaches a stable point and is ready to be released, a `release` branch is created. This allows for final bug fixes and documentation generation before merging into `main` and tagging the release.

## Comparison with Other Patterns

| Pattern | Best For | Key Difference |
| :--- | :--- | :--- |
| **Gitflow** (This Repo) | Scheduled releases, legacy software, strict control. | Uses multiple long-lived branches (`develop`, `release`, `main`). |
| [**GitHub Flow**](https://github.com/AustonIvison/demo-github-flow-pattern) | Continuous deployment, web apps, small teams. | Much simpler. Only one long-lived branch (`main`). Everything else is a feature branch. |
| [**Trunk-Based**](https://github.com/AustonIvison/demo-trunk-based-pattern) | High-velocity teams, CI/CD, senior teams. | Developers commit directly to `main` (trunk) or use very short-lived branches. Uses feature flags to hide unfinished work. |

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
