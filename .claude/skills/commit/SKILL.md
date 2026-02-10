---
name: commit
description: Create well-formatted git commits following project conventions
---

# Commit Skill

## When to Use

- After completing a feature or fix
- When changes are ready to be committed
- When user requests `/commit`

## Instructions

1. Check `git status` to see changed files
2. Review changes with `git diff`
3. Stage relevant files (be specific, avoid `git add .`)
4. Write commit message following conventions
5. Run pre-commit hooks
6. Create the commit

## Commit Message Format

```
<type>(<scope>): <short description>

<body - optional>

<footer - optional>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code change that neither fixes bug nor adds feature
- `test`: Adding or correcting tests
- `chore`: Maintenance tasks

### Examples

```
feat(auth): add OAuth2 login support

Implements OAuth2 authentication flow with Google and GitHub providers.
Includes token refresh mechanism and secure storage.

Closes #123
```

```
fix(api): handle null response from external service

The external API sometimes returns null for deleted resources.
Now we check for null before processing.
```

## Guidelines

- Keep first line under 72 characters
- Use imperative mood ("add" not "added")
- Reference issues when applicable
- Don't include sensitive information
- Ensure pre-commit hooks pass before committing
