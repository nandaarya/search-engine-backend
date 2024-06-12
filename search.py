from collections import defaultdict
import math

def log_hello_world():
  """Logs "Hello, World!" to the console."""
  print("Hello, World!")


def perform_search(keyword, algorithm, documents):
  """
  Performs search based on the chosen algorithm and documents.

  Args:
      keyword: String representing the search query.
      algorithm: String representing the search algorithm to use.
      documents: List of strings representing the documents to search.

  Returns:
      List of dictionaries containing document and score.
  """
  keyword_terms = keyword.split()
  results = []

  for doc in documents:
    doc_terms = doc.lower().split()
    score = 0

    if algorithm == 'vector-space':
      score = vector_space_model(keyword_terms, doc_terms)
    elif algorithm == 'cosine-similarity':
      score = cosine_similarity(keyword_terms, doc_terms)
    elif algorithm == 'naive-bayes':
      score = naive_bayes(keyword_terms, doc_terms)
    elif algorithm == 'extended-boolean':
      score = extended_boolean(keyword_terms, doc_terms)
    elif algorithm == 'knn':
      # Replace with KNN implementation (for simplicity using cosine similarity)
      score = cosine_similarity(keyword_terms, doc_terms)

    if score > 0:
      results.append({"doc": doc, "score": score})

  results.sort(key=lambda x: x["score"], reverse=True)
  return results

def vector_space_model(query_terms, doc_terms):
  """
  Calculates a simple vector space score based on term presence.

  Args:
      query_terms: List of strings representing the query terms.
      doc_terms: List of strings representing the document terms.

  Returns:
      Integer representing the vector space score for the document.
  """
  score = 0
  for term in query_terms:
    if term in doc_terms:
      score += 1
  return score

def cosine_similarity(query_terms, doc_terms):
  """
  Calculates cosine similarity between two text documents.

  Args:
      query_terms: List of strings representing the query terms.
      doc_terms: List of strings representing the document terms.

  Returns:
      Float representing the cosine similarity score between the query and document.
  """
  query_vector = create_term_frequency_vector(query_terms)
  doc_vector = create_term_frequency_vector(doc_terms)
  dot_product = dot_product_vectors(query_vector, doc_vector)
  magnitude_query = vector_magnitude(query_vector)
  magnitude_doc = vector_magnitude(doc_vector)

  # Handle cases where either magnitude is 0 to avoid division by zero
  if magnitude_query == 0 or magnitude_doc == 0:
    return 0

  return dot_product / (magnitude_query * magnitude_doc)

def naive_bayes(query_terms, doc_terms):
  """
  Calculates a simple Naive Bayes score for document relevance.

  Args:
      query_terms: List of strings representing the query terms.
      doc_terms: List of strings representing the document terms.

  Returns:
      Float representing the Naive Bayes score for the document.
  """
  score = 1.0
  for term in query_terms:
    term_frequency = doc_terms.count(term)  # Count occurrences of term in document
    score *= term_frequency / len(doc_terms)  # Probability of term in document
  return score

def extended_boolean(query_terms, doc_terms):
  """
  Calculates a score based on the presence of all query terms in the document.

  Args:
      query_terms: List of strings representing the query terms.
      doc_terms: List of strings representing the document terms.

  Returns:
      Integer representing the score based on the presence of query terms.
  """
  score = 0
  for term in query_terms:
    if term in doc_terms:
      score += 1
  return score**2  # Square to emphasize matching all terms

def knn(query_terms, doc_terms):
  """
  Placeholder function for KNN search. 
  (Replace with actual KNN implementation)

  Args:
      query_terms: List of strings representing the query terms.
      doc_terms: List of strings representing the document terms.

  Returns:
      Float (placeholder, can be similarity score from another algorithm)
  """
  # For simplicity, use cosine similarity as a placeholder for KNN
  return cosine_similarity(query_terms, doc_terms)

def create_term_frequency_vector(terms):
  """
  Creates a dictionary representing term frequency for a list of terms.

  Args:
      terms: List of strings representing the terms.

  Returns:
      Dictionary mapping terms to their frequency in the list.
  """
  term_frequency = defaultdict(int)
  for term in terms:
    term_frequency[term] += 1
  return term_frequency

def dot_product_vectors(vector1, vector2):
  """
  Calculates the dot product of two dictionaries representing vectors.

  Args:
      vector1: Dictionary representing the first vector.
      vector2: Dictionary representing the second vector.

  Returns:
      Integer representing the dot product of the two vectors.
  """
  dot_product = 0
  for term, weight in vector1.items():
    if term in vector2:
      dot_product += weight * vector2[term]
  return dot_product

def vector_magnitude(vector):
  """
  Calculates the magnitude (length) of a dictionary representing a vector.

  Args:
      vector: Dictionary representing the vector.

  Returns:
      Float representing the magnitude of the vector.
  """
  magnitude = 0
  for weight in vector.values():
    magnitude += weight**2
  return math.sqrt(magnitude)
