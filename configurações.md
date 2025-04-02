# Extensões para Python

- Autopep8
- Pylint

```json
"[python]": {
    "editor.defaultFormatter": "ms-python.autopep8",
    "editor.formatOnSave": true,
    "editor.formatOnPaste": false,
},
"autopep8.args": [
    "--max-line-length", "80",
    "--aggressive",
    "--aggressive",
    "--ignore", "E266",
    "--indent-size", "4"
],
"pylint.args": [
  "--disable=missing-module-docstring",
  "--max-line-length=120",
  "--disable=missing-function-docstring",
  "--disable=missing-class-docstring", 
], 
```
