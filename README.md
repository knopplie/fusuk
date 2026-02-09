# fusuk

A simple proof-of-concept package to generate UK/US Based realistic names.

## Usage

```python
from fusuk import getname

# Basic: random US name
print(getname())  # "James Wilson"

# With options
print(getname(country="uk", gender="female"))  # "Emily Clark"
```

**Function:** `getname(country="us", gender=None)`

playground is included for tests