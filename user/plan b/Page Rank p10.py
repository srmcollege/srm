#page rank
import numpy as np

def page_rank(graph, d=0.85, max_iter=100, tol=1e-6):
  
    # Initialize PageRank values
    num_nodes = len(graph)
    pagerank = {node: 1 / num_nodes for node in graph}
    
    # Create a list of nodes
    nodes = list(graph.keys())
    
    for _ in range(max_iter):
        new_pagerank = {node: (1 - d) / num_nodes for node in graph}
        
        for node in nodes:
            # Iterate through the outgoing links
            for neighbor in graph[node]:
                new_pagerank[neighbor] += d * pagerank[node] / len(graph[node])
        
        # Check for convergence
        if sum(abs(new_pagerank[node] - pagerank[node]) for node in nodes) < tol:
            break
            
        pagerank = new_pagerank
    
    return pagerank

# Example usage
if __name__ == "__main__":
    # Define a sample directed graph
    graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C'],
        'E': ['A', 'B', 'C']
    }
    
    # Calculate PageRank
    pagerank_values = page_rank(graph)
    
    # Print the results
    for node, rank in pagerank_values.items():
        print(f"Node {node}: PageRank = {rank:.4f}")


==========================================================

