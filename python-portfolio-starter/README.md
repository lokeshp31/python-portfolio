# Python Portfolio

A clean, professional portfolio of Python projects. Each project includes a clear README, instructions, and code organized for learning and interviews.

## 🧭 Structure
```
python-portfolio/
├─ projects/
│  ├─ 01-basics-calculator/
│  ├─ 02-todo-cli/
│  └─ 03-number-guessing-game/
├─ tests/            # optional unit tests
├─ scripts/          # helper scripts
├─ .gitignore
├─ LICENSE
├─ CONTRIBUTING.md
└─ README.md
```

## 📌 How to use
1. Create a virtual environment:
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux (bash/zsh):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2. Install project requirements when needed:
   ```bash
   pip install -r requirements.txt
   ```
3. Run a project (example):
   ```bash
   python projects/01-basics-calculator/calculator.py
   ```

## ✅ Project Quality Checklist (for every project)
- Clear **README** with: Problem, Features, How to Run, Example Usage, and Future Work
- **requirements.txt** with needed packages (or empty if none)
- **Screenshots/GIF** (optional but great for recruiters)
- **Simple tests** (optional for beginner projects)
- **Meaningful commits** with clear messages

## 🪪 License
MIT — feel free to use and modify.
