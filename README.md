Here’s the **revised README** with **only English and Chinese** support mentioned and unnecessary references to Hindi removed:

---

# 🌐 Text Summarizer Web App (English & Chinese)

Welcome to the Text Summarizer web app! This project contains the code for a **Flask-based** application that performs **text summarization** using the **T5 Transformer model**, with optional output in **English** or **Chinese** via Google Translate.

---

### 📥 Input (English)


### 📤 Output (English)

### 📥 Input (Chinese)



### 📤 Output (Chinese)


---

## 🧠 Overview

The core of the app (`app.py`) integrates:

* ✅ **Flask** for the web backend
* ✅ **T5 transformer** for abstractive summarization
* ✅ **Google Translate API** for output in Chinese (if selected)

Users can enter text, select between English or Chinese, and receive a condensed version of the content in the selected language.

---

## ⚙️ Installation

Install the required packages using:

```bash
pip install Flask transformers googletrans==4.0.0-rc1
```

> ⚠️ Be sure to use `googletrans==4.0.0-rc1` for stable translation support.

---

## 🚀 Usage

1. Navigate to the project directory:

```bash
cd Desktop/Text-Summarizer-main
```

2. Start the Flask app:

```bash
python app.py
```

3. Open your browser and visit:

```
http://localhost:5000
```

4. Enter text, select language (English/Chinese), and click **Summarize**.

---

## 🙏 Acknowledgments

This project uses:

* 🤖 [T5 Transformer](https://huggingface.co/t5-small) from HuggingFace
* 🌐 Google Translate API
* 🧪 Flask for web hosting

> ⚠️ This app runs in **debug mode**. Disable it before deploying to production.

---

Would you like me to also rewrite the HTML to remove Hindi references or clean up the `app.py` logic to support just English/Chinese?
