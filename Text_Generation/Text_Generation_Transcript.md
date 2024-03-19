# Assignment 4

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

can you help me write a program that takes an input has the parameters file_name:str, start_word:str, output_length:str and generates an output_text that is output_length long and starts at start_word and uses words from filename

ChatGPT

**ChatGPT**

Certainly! Below is a Python program that accomplishes what you described:

```python
pythonCopy code
Explain
import random

def generate_output(file_name, start_word, output_length):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        return "File not found."

    words = text.split()
    output_text = [start_word]

    while len(output_text) < int(output_length):
        next_word_options = []
        for i in range(len(words) - 1):
            if words[i] == output_text[-1]:
                next_word_options.append(words[i + 1])

        if next_word_options:
            next_word = random.choice(next_word_options)
            output_text.append(next_word)
        else:
            break

    return ' '.join(output_text)

# Example usage
file_name = input("Enter the file name: ")
start_word = input("Enter the start word: ")
output_length = input("Enter the desired output length: ")

output_text = generate_output(file_name, start_word, output_length)
print("Generated Text:")
print(output_text)

```

This program reads a text file specified by **`file_name`**, then starts generating a sequence of words from the **`start_word`**. It continues to append words from the file, choosing randomly from the possible next words until the length of the generated text reaches **`output_length`**. If there are no more possible next words, the generation stops. Finally, it prints the generated text.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

Since we're not reading from a file, create a sample text corpus and clean it

ChatGPT

**ChatGPT**

Sure, let's create a sample text corpus and clean it. For simplicity, I'll use a short paragraph as the sample text. Here's the modified code:

```python
pythonCopy code
Explain
import re
import random

# Sample text corpus
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

def clean_text(text):
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def generate_output(text, start_word, output_length):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    output_text = [start_word]

    while len(output_text) < int(output_length):
        next_word_options = []
        for i in range(len(words) - 1):
            if words[i] == output_text[-1]:
                next_word_options.append(words[i + 1])

        if next_word_options:
            next_word = random.choice(next_word_options)
            output_text.append(next_word)
        else:
            break

    return ' '.join(output_text)

# Example usage
start_word = input("Enter the start word: ")
output_length = input("Enter the desired output length: ")

output_text = generate_output(sample_text, start_word, output_length)
print("Generated Text:")
print(output_text)

```

In this version, the **`sample_text`** variable contains a short paragraph. The **`clean_text()`** function removes special characters and extra whitespaces from the text. The rest of the code remains the same. Now you can input a starting word and desired output length to generate text from the sample corpus.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

Create a dictionary to store word transitions

ChatGPT

**ChatGPT**

To create a dictionary to store word transitions, we'll modify the **`generate_output()`** function to build this dictionary while processing the text. Here's the updated code:

```python
pythonCopy code
Explain
import re
import random

# Sample text corpus
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

def clean_text(text):
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def generate_output(text, start_word, output_length):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    transitions = {}  # Dictionary to store word transitions

    # Build transitions dictionary
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in transitions:
            transitions[current_word].append(next_word)
        else:
            transitions[current_word] = [next_word]

    output_text = [start_word]
    while len(output_text) < int(output_length):
        current_word = output_text[-1]
        if current_word in transitions:
            next_word_options = transitions[current_word]
            next_word = random.choice(next_word_options)
            output_text.append(next_word)
        else:
            break

    return ' '.join(output_text)

# Example usage
start_word = input("Enter the start word: ")
output_length = input("Enter the desired output length: ")

output_text = generate_output(sample_text, start_word, output_length)
print("Generated Text:")
print(output_text)

```

In this version, the **`transitions`** dictionary stores each word as a key and its possible next words as values. This dictionary is built while processing the text. Then, during text generation, the program uses this dictionary to select the next word based on the current word.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

Generate the text

ChatGPT

**ChatGPT**

Sure! Here's the complete code to generate text based on word transitions:

```python
pythonCopy code
Explain
import re
import random

# Sample text corpus
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

def clean_text(text):
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def generate_output(text, start_word, output_length):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    transitions = {}  # Dictionary to store word transitions

    # Build transitions dictionary
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in transitions:
            transitions[current_word].append(next_word)
        else:
            transitions[current_word] = [next_word]

    output_text = [start_word]
    while len(output_text) < int(output_length):
        current_word = output_text[-1]
        if current_word in transitions:
            next_word_options = transitions[current_word]
            next_word = random.choice(next_word_options)
            output_text.append(next_word)
        else:
            break

    return ' '.join(output_text)

# Example usage
start_word = input("Enter the start word: ")
output_length = input("Enter the desired output length: ")

output_text = generate_output(sample_text, start_word, output_length)
print("Generated Text:")
print(output_text)

```

You can run this code, input a starting word and desired output length, and it will generate text based on the provided sample text corpus and word transitions.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

give an example usage instead of getting input

ChatGPT

**ChatGPT**

Certainly! Here's an example usage with predefined values instead of getting input:

```python
pythonCopy code
Explain
start_word = "Lorem"
output_length = "20"

output_text = generate_output(sample_text, start_word, output_length)
print("Generated Text:")
print(output_text)

```

In this example, the text generation starts with the word "Lorem" and generates a sequence of 20 words based on the provided sample text corpus and word transitions. You can adjust the **`start_word`** and **`output_length`** variables to generate text with different starting points and lengths.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

now give whole code

ChatGPT

**ChatGPT**

Certainly! Here's the whole code including the example usage:

```python
pythonCopy code
Explain
import re
import random

# Sample text corpus
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

def clean_text(text):
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def generate_output(text, start_word, output_length):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    transitions = {}  # Dictionary to store word transitions

    # Build transitions dictionary
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in transitions:
            transitions[current_word].append(next_word)
        else:
            transitions[current_word] = [next_word]

    output_text = [start_word]
    while len(output_text) < int(output_length):
        current_word = output_text[-1]
        if current_word in transitions:
            next_word_options = transitions[current_word]
            next_word = random.choice(next_word_options)
            output_text.append(next_word)
        else:
            break

    return ' '.join(output_text)

# Example usage
start_word = "Lorem"
output_length = "20"

output_text = generate_output(sample_text, start_word, output_length)
print("Generated Text:")
print(output_text)

```

This code includes the function for text generation, the sample text corpus, a function to clean the text, and the example usage demonstrating how to generate text with predefined values.

[https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c](https://lh3.googleusercontent.com/a/AGNmyxZEmC_MGXM87EHTlZdfsghColMim67WjIBR9349=s96-c)

**You**

prove some test cases to verify

ChatGPT

**ChatGPT**

Certainly! Here are some test cases to verify the functionality of the text generation:

```python
pythonCopy code
Explain
# Test case 1: Starting word not in sample text
start_word = "Nonexistent"
output_length = "10"
output_text = generate_output(sample_text, start_word, output_length)
print("Test Case 1 Output:")
print(output_text)

# Test case 2: Short output length
start_word = "Lorem"
output_length = "5"
output_text = generate_output(sample_text, start_word, output_length)
print("\nTest Case 2 Output:")
print(output_text)

# Test case 3: Long output length
start_word = "Lorem"
output_length = "100"
output_text = generate_output(sample_text, start_word, output_length)
print("\nTest Case 3 Output:")
print(output_text)

# Test case 4: Random starting word and output length
start_word = random.choice(sample_text.split())
output_length = str(random.randint(5, 30))
output_text = generate_output(sample_text, start_word, output_length)
print("\nTest Case 4 Output:")
print(output_text)

```

These test cases cover various scenarios such as starting with a word not in the sample text, generating text with short and long output lengths, and using random starting words and output lengths. You can run these test cases to verify the correctness and robustness of the text generation function.