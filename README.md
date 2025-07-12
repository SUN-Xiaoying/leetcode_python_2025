# Set up
```bash
python3 -m venv venv
source venv/bin/activate
```

# Upgrade

```bash
python -m pip install --upgrade pip
```


## Python naming
|Concept| Naming                                  ||
|---|-----------------------------------------|---|
|Function and Variable Names| Lowercase with underscores (snake_case) |`string_utils.py`,`math_helpers.py`|
|Class Names| Camel                                   |`class DataLoader:`|
Global Variable (Private)|Prefix with an underscore _|`_internal_var = 42`|


# Jackpot

> No, you do not need to add a semicolon (;) at the end of every statement in Python. **Python uses line breaks to determine the end of a statement, making ; optional in most cases**.

|Concept|Code|
|---|---|
|HashMap|`dict()`|

## Mid

```python
    mid = left + (right - left) // 2
```

## Sum

```python
    expected_sum = n * (n + 1) // 2
```