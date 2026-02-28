import math

def estimate_indexing_cost(text_length_chars, model_price_per_1k_tokens=0.03):
    """
    Estimates the indexing cost for GraphRAG based on text length.
    
    Args:
        text_length_chars (int): The total number of characters in the input text.
        model_price_per_1k_tokens (float): Price per 1,000 tokens for the LLM.
        
    Returns:
        dict: A breakdown of estimated tokens and costs.
    """
    # Rough estimate: 1 token is about 4 characters
    estimated_tokens = text_length_chars / 4
    
    # GraphRAG indexing involves multiple passes (extraction, summarization, etc.)
    # Multiplier of 1.5x is a conservative estimate for overhead
    total_tokens_with_overhead = estimated_tokens * 1.5
    
    estimated_cost = (total_tokens_with_overhead / 1000) * model_price_per_1k_tokens
    
    return {
        "input_chars": text_length_chars,
        "estimated_tokens": round(estimated_tokens),
        "total_estimated_tokens_with_overhead": round(total_tokens_with_overhead),
        "estimated_cost_usd": round(estimated_cost, 4)
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        chars = int(sys.argv[1])
        result = estimate_indexing_cost(chars)
        print(f"Cost Analysis for {chars} characters:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print("Usage: python cost_analyzer.py <number_of_characters>")
