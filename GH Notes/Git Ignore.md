# gitignore File
Tells Git what to ignore for tracking. Useful for logs and .envs

```bash
.env # Ignore .env file
*.log # Ignore all log files
log/ # Ignore entire directory
file*.txt # Wildcards work-- file123.txt, file456.txt all will be ignored
```

# File Permissions
Git saves file permissions, you can ignore them with fileMode

`git config core.fileMode false`