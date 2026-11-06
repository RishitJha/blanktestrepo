# Git Cheat Sheet

## Start a repository

```bash
git init                         # Start a repository in the current folder
git clone <url>                  # Copy an existing repository locally
git remote -v                    # Show configured remotes
git remote add origin <url>      # Connect this repository to a remote
```

## Check and save changes

```bash
git status                       # Show changed, staged, and untracked files
git diff                         # Review unstaged changes
git diff --staged                # Review staged changes
git add <file>                   # Stage one file
git add .                        # Stage all changes in the current directory
git commit -m "Describe change"  # Save staged changes in a commit
git log --oneline                # View recent commits
```

## Sync with a remote

```bash
git pull                         # Fetch and integrate remote changes
git push                         # Send commits to the configured remote
git push -u origin <branch>      # Push a new branch and set its upstream
```

## Branches

```bash
git branch                       # List local branches
git switch <branch>              # Switch branches
git switch -c <branch>           # Create and switch to a branch
git merge <branch>               # Merge a branch into the current branch
git branch -d <branch>           # Delete a merged local branch
```

## Undo and temporary changes

```bash
git restore <file>               # Discard unstaged changes to a file
git restore --staged <file>      # Unstage a file, keeping its changes
git stash                        # Temporarily save tracked working changes
git stash pop                    # Reapply the latest stash and remove it
```

`git restore <file>` discards edits in that file. Review `git status` and `git diff` before using it.
