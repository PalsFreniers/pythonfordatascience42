# 🧪 Example Test Package

This is a small Python utility package demonstrating basic list analysis and progress bar functionality for educational or testing purposes.

---

## 📦 Features

### 1. `count_in_list(lst, s)`

Counts how many times a specific value appears in a list.

```python
from yourpackage import count_in_list

print(count_in_list([1, 2, 3, 2, 2, 4], 2))
# Output: 3
```

---

### 2. `ft_tqdm(lst)`

A minimal reimplementation of a terminal progress bar, inspired by [`tqdm`](https://github.com/tqdm/tqdm).

It decorates an iterable (such as a `range`) and prints real-time progress updates as it iterates.

```python
from yourpackage import ft_tqdm
from time import sleep

for _ in ft_tqdm(range(100)):
    sleep(0.02)  # simulate work
```

> **Note:**
> `ft_tqdm` expects the iterable to have a `.stop` attribute (like a `range` object).
> It dynamically adjusts to your terminal width using `os.get_terminal_size()`.

---

### 3. `makeAssertError(s)`

Prints an assertion-style error message and exits the program.

```python
from yourpackage import makeAssertError

x = 5
if x != 10:
    makeAssertError("x should be equal to 10")
# Output:
# AssertionError: x should be equal to 10
```

---

## ⚙️ Requirements

* Python 3.8 or higher
* A Unicode-compatible terminal (for the progress bar)

---

## 🧭 Notes

* The progress bar automatically adapts to the terminal width.
* This package is for learning and testing purposes — not optimized for production.
* No external dependencies (pure standard library).

---

## 🧰 Example Output

```
 42%|███████████████████-----------------------| 42/100
```

---

## 🪪 License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.
You are free to use, modify, and distribute this software under the terms of the GPLv3.

See the [LICENSE](./LICENSE) file for details.
