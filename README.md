# 🧹 JupyterClean

A lightweight Python tool to clean Jupyter notebooks before committing to version control. Removes execution counts, output cells, and metadata clutter — keeping your notebooks clean, professional, and git-friendly.

---

## 🎯 The Problem

Ever seen this when pushing notebooks to GitHub?

<!-- TODO: Add screenshot of the permission/metadata error here -->
![Notebook Metadata Issue](docs/error-screenshot.png)

Jupyter notebooks accumulate metadata, execution counts, and outputs that:
- ❌ Create massive, noisy git diffs
- ❌ Increase file size unnecessarily
- ❌ Make code reviews harder
- ❌ Cause merge conflicts
- ❌ Expose sensitive output data

**JupyterClean** solves this by stripping notebooks down to pure code and markdown — perfect for version control.

---

## ✨ Features

- 🧹 Removes all cell outputs
- 🔢 Clears execution counts
- 🗑️ Strips unnecessary metadata
- ⚡ Fast and simple to use
- 🔄 Works in-place (overwrites the original file)
- 🐍 Pure Python, minimal dependencies

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/JupyterClean.git
cd JupyterClean
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Or if you prefer using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic Usage
Clean a single notebook:
```bash
python clean_notebook.py path/to/your/notebook.ipynb
```

### Clean Multiple Notebooks
```bash
python clean_notebook.py notebook1.ipynb notebook2.ipynb notebook3.ipynb
```

### Before Committing to Git
```bash
# Clean your notebook
python clean_notebook.py analysis.ipynb

# Then commit as usual
git add analysis.ipynb
git commit -m "Add cleaned analysis notebook"
git push origin main
```

---

## 📋 Example

**Before cleaning:**
```json
{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 42,
      "metadata": {
        "collapsed": false,
        "scrolled": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Hello World\n"
        }
      ],
      "source": ["print('Hello World')"]
    }
  ]
}
```

**After cleaning:**
```json
{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": ["print('Hello World')"]
    }
  ]
}
```

Much cleaner! ✨

---

## 🛠️ How It Works

JupyterClean uses `nbconvert` under the hood with these preprocessors:
- `ClearOutputPreprocessor` — removes all cell outputs
- `ClearMetadataPreprocessor` — strips unnecessary metadata

The tool processes notebooks in-place, preserving your code and markdown while removing execution artifacts.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [nbconvert](https://nbconvert.readthedocs.io/)
- Inspired by the need for cleaner notebooks in version control

---

## 📬 Contact

Have questions or suggestions? Open an issue or reach out!

**Made with ❤️ for cleaner Jupyter notebooks**
