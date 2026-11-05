This script uses LangChain and Google Gemini to extract **structured data** (a Python dictionary) from a raw, unstructured text review.

---

### 1. What is `TypedDict` and Why Do We Use It?

A **`TypedDict`** is a feature from Python's typing system (`from typing import TypedDict`). It lets you define a blueprint for a standard Python dictionary by specifying what keys are allowed and what data type each key should hold.

* **Why use it?** Normally, when you ask an LLM to extract information, it returns a raw string (like a markdown block or paragraph). If you want to use that data in code, parsing it is painful. `TypedDict` acts as a contract: it tells Gemini, *"Fill out a dictionary that strictly has these exact keys and data types."*
* **What you get back:** When you run `structured_model.invoke()`, the result is a clean Python dictionary where you can access values using keys, like `result['name']` or `result['summary']`.

---

### 2. Pros and Cons of `TypedDict`

**Pros:**

* **Lightweight:** Built directly into Python; you don't need to install external libraries like Pydantic.
* **Familiarity:** It returns a plain Python dictionary (`dict`), making it easy to pass into JSON APIs, databases, or existing functions.
* **IDE Support:** Gives your code editor autocomplete suggestions for dictionary keys.

**Cons:**

* **No Runtime Validation:** Unlike Pydantic, `TypedDict` is purely for type hints. If the LLM mistakenly returns a string inside a list field, Python won't block it or throw a runtime error.
* **No Constraints:** You cannot enforce strict numeric boundaries (e.g., rating must be between 1 and 5) with basic `TypedDict`.

---

### 3. Why Use `Annotated`, `Optional`, and `Literal`?

Your script uses three powerful modifier tools to guide Gemini:

* **`Annotated`**: Allows you to attach metadata or instructions to a specific field. For example, `Annotated[list[str], "Write down all the key themes..."]` tells the LLM *what* to look for. Without descriptions, the LLM has to guess what a key means.
* **`Literal`**: Restricts the model's output options to a strict, hardcoded set of choices.
> *Note on your code:* Your `sentiment` field specifies `Literal["pos", "neg"]`, but your description says `"either negative, positive or neutral"`. Because of `Literal`, Gemini will *only* be allowed to output `"pos"` or `"neg"`. If you want "neutral" included, you should update it to `Literal["positive", "negative", "neutral"]`.


* **`Optional`**: Means the field is allowed to be `None` (or missing) if the review doesn't mention it. For example, if a review doesn't state the reviewer's name, `Optional[str]` prevents the model from crashing or hallucinating a random name; it will just return `None`.

---

### 4. Step-by-Step Breakdown of Your Code

1. **Imports & Setup:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

```



```
   * Loads your environment variables (like your Google API key) and initializes the Gemini model.

2. **Defining the Schema (`Review`):**
   ```python
   class Review(TypedDict):
     key_themes: Annotated[
         list[str], "Write down all the key themes discussed..."
     ]
     summary: Annotated[str, "A brief summary of the review"]
     sentiment: Annotated[Literal["pos", "neg"], "Return sentiment..."]
     pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
     cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
     name: Annotated[Optional[str], "Write the name of the reviewer"]

```

* This blueprint maps out every piece of information you want extracted from the text block.

3. **Binding to the Model:**
```python
structured_model = model.with_structured_output(Review)

```



```
   * This is the magic line. It instructs LangChain to take your `Review` TypedDict, convert it into a schema format Gemini understands, and force the model to output data matching that structure.

4. **Invoking and Printing:**
   ```python
   result = structured_model.invoke("...Samsung Galaxy S24 Ultra review...")
   print(result['name'])

```

* Passes the messy, unstructured text review into Gemini. Gemini reads it, extracts the fields according to your descriptions, and returns a Python dictionary.
* `print(result['name'])` digs into that dictionary and prints out just the reviewer's name (**Nitish Singh**).