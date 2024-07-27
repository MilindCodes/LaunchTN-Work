import nltk
from collections import Counter
import re

# Sample text
text = "A harness for domestic dogs, brace and mobility support dogs, or service/companion animals. The harness provides multiple handles for balance and stability and for controlling the movement of the dog. D-rings and additional connection points are provided for attaching a leash as well as securing the harness to a wheelchair. The harness provides a chest protector for protection from abrasion and for load distribution at the dog's center of mass. The harness straps are constructed with nylon or polyester webbing material with a mesh padded covering. At the harness connections, plastic buckles are utilized with Velcro straps. The harness geometry is designed to eliminate the leash pulling forces on the dog's hip, neck, and trachea, by focusing the leash pulling forces at the dog's center of mass middle chest area and by more evenly distributing forces and loads across the body, torso, and chest."

# Remove punctuation and convert to lowercase
text = re.sub(r'[^\w\s]', '', text.lower())

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stop words (optional)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

# Count word frequencies
word_counts = Counter(words)

# Find the top 10 most common words
top_10_words = word_counts.most_common(10)

# Print the results
for word, count in top_10_words:
    print(f"{word}: {count}")
