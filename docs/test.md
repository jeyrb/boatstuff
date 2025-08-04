```python {marimo}
import marimo as mo

name = mo.ui.text(placeholder="Enter your name")
name
```

```python {marimo}
mo.md(f"Hello, **{name.value or '__'}**!")
```
