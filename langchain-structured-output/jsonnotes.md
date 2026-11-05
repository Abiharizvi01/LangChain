# Structured Output — JSON Schema

## 1. What is Structured Output?

Normally, an LLM returns free-form text.

**Structured output** means telling the LLM the exact structure/format in which we want the response.

Example:

```json
{
  "summary": "...",
  "sentiment": "pos",
  "pros": ["...", "..."]
}
```

This is useful when we want to use the LLM's response programmatically.

---

# 2. Three Common Ways to Define the Structure

In LangChain, structured output can be defined using:

1. **TypedDict**
2. **Pydantic**
3. **JSON Schema**

### TypedDict
Defines the expected structure using Python type hints.

```python
class Review(TypedDict):
    summary: str
    sentiment: str
```

### Pydantic
Defines the structure using a Pydantic model and provides validation.

```python
class Review(BaseModel):
    summary: str
    sentiment: str
```

### JSON Schema
Defines the structure using a JSON object.

```python
json_schema = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string"
        },
        "sentiment": {
            "type": "string"
        }
    },
    "required": ["summary", "sentiment"]
}
```

So the main difference is **how we describe the expected structure**.

---

# 3. JSON Schema

JSON Schema is a standard way of describing the **structure and rules of JSON data**.

It tells us:

- What fields exist
- What type each field should have
- Which fields are required
- What values are allowed
- Whether a field can be `null`
- What type of elements an array contains

Think of it as a **blueprint/rulebook for JSON data**.

---

# 4. Basic JSON Schema Structure

```python
json_schema = {
    "title": "Review",

    "type": "object",

    "properties": {
        ...
    },

    "required": [...]
}
```

### `title`

Gives the schema a name.

```python
"title": "Review"
```

### `type`

Defines the type of the overall data.

```python
"type": "object"
```

means the output should be a JSON object.

### `properties`

Defines the fields inside the object.

### `required`

Defines which fields must be present.

---

# 5. Common JSON Schema Types

```text
string   → "hello"
number   → 10.5
integer  → 10
boolean  → true / false
array    → ["Python", "SQL"]
object   → {"name": "Ali"}
null     → null
```

---

# 6. Arrays

To define an array:

```python
{
    "type": "array",
    "items": {
        "type": "string"
    }
}
```

This means:

> The field must be an array, and every element inside the array must be a string.

Valid:

```json
["camera", "battery", "performance"]
```

---

# 7. Enum

`enum` restricts a field to specific allowed values.

```python
{
    "type": "string",
    "enum": ["pos", "neg"]
}
```

The value can only be:

```text
"pos"
"neg"
```

It cannot be:

```text
"neutral"
"positive"
"negative"
```

unless those values are added to the enum.

---

# 8. Nullable Fields

```python
"type": ["array", "null"]
```

means the field can contain either:

- an array
- or `null`

For example:

```json
"pros": ["Great camera", "Good battery"]
```

or:

```json
"pros": null
```

Similarly:

```python
"type": ["string", "null"]
```

means the value can be either a string or `null`.

---

# 9. Description

Example:

```python
"description": "A brief summary of the review"
```

The description explains what the field represents and can provide guidance to the model about what to generate.

---

# 10. Required Fields

```python
"required": [
    "key_themes",
    "summary",
    "sentiment"
]
```

These fields must be present in the output.

Therefore:

### Required

```text
key_themes
summary
sentiment
```

### Optional

```text
pros
cons
name
```

Important:

**Optional does not necessarily mean nullable.**

For example, `name` has:

```python
"type": ["string", "null"]
```

So if `name` is present, it can be a string or `null`.

But because `name` is not in `required`, the field can also be completely absent.

---

# 11. Connecting JSON Schema to LangChain

```python
structured_model = model.with_structured_output(json_schema)
```

This tells LangChain:

> Use this JSON Schema to define the structure of the model's output.

Then:

```python
result = structured_model.invoke(...)
```

returns the review information according to the defined structure rather than ordinary free-form text.

---

# 12. Structure of This Particular Review Schema

```text
Review
│
└── object
    │
    ├── key_themes
    │      └── array of strings
    │
    ├── summary
    │      └── string
    │
    ├── sentiment
    │      └── "pos" or "neg"
    │
    ├── pros
    │      └── array of strings OR null
    │
    ├── cons
    │      └── array of strings OR null
    │
    └── name
           └── string OR null
```

---

# 13. Expected Output

For the given Samsung review, the model could produce something like:

```json
{
    "key_themes": [
        "Performance",
        "Camera",
        "Battery",
        "S-Pen",
        "Design",
        "Bloatware",
        "Price"
    ],
    "summary": "The reviewer is highly impressed with the performance, camera and battery life, but dislikes the phone's size, bloatware and high price.",
    "sentiment": "pos",
    "pros": [
        "Powerful processor",
        "Excellent camera",
        "Long battery life",
        "S-Pen support"
    ],
    "cons": [
        "Heavy and large",
        "Bloatware",
        "Expensive"
    ],
    "name": "Nitish Singh"
}
```

---

## Key takeaway

**TypedDict, Pydantic and JSON Schema all describe the structure of the output, but they express that structure differently.**

```text
TypedDict
    ↓
Python type hints

Pydantic
    ↓
Python class + validation

JSON Schema
    ↓
JSON-based description of data structure + rules
```

And:

```python
model.with_structured_output(schema)
```

means:

**"LLM, return your answer according to this defined structure."**