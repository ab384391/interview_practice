import numpy as np

def embedding_lookup(indices, embedding_matrix):
    """
    Retrieves embeddings for a list of indices.
    
    Args:
        indices: List or array of indices of shape (batch_size, sequence_length) or (N,)
        embedding_matrix: Weights of shape (vocab_size, embedding_dim)
        
    Returns:
        out: Embeddings of shape (..., embedding_dim)
    """
    # Simple lookup
    # In NumPy, integer array indexing does exactly this.
    return embedding_matrix[indices]
