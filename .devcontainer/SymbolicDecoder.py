import os
import requests
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from collections import Counter
from multiprocessing import Pool
from scipy.stats import entropy, chi2_contingency

# === SYMBOLIC MAPPING SYSTEM (Triadic-Based) ===
char_map = {
    **dict.fromkeys(['A', 'E', 'I'], 1),
    **dict.fromkeys(['B', 'F', 'J', 'O', 'U'], 2),
    **dict.fromkeys(['C', 'G', 'K', 'P', 'V'], 3),
    **dict.fromkeys(['D', 'H', 'L', 'Q', 'W'], 4),
    **dict.fromkeys(['M', 'R', 'X'], 5),
    **dict.fromkeys(['N', 'S', 'Y'], 6),
    **dict.fromkeys(['T', 'Z'], 7)
}

# === WORD TRANSFORMATION ===
def transform_word(word):
    return tuple(char_map.get(c.upper(), 0) for c in word if c.upper() in char_map)

# === WORD DATASET DOWNLOADER ===
def download_word_dataset():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    local_path = "words.txt"

    if not os.path.exists(local_path):
        print("Downloading word dataset...")
        response = requests.get(url)
        with open(local_path, "wb") as f:
            f.write(response.content)

    with open(local_path, "r") as f:
        word_list = [line.strip() for line in f if line.strip()]
    return word_list

# === PARALLEL WORD PROCESSING ===
def process_words_parallel(word_list):
    with Pool() as pool:
        return pool.map(transform_word, word_list)

# === SYMBOLIC GRAPH BUILDER ===
def build_graph(transformed_words, original_words):
    G = nx.DiGraph()

    for original, transformed in zip(original_words, transformed_words):
        if not transformed:
            continue
        str_transformed = "-".join(map(str, transformed))

        # Add nodes with role-based tagging
        G.add_node(original, type="word", role="raw")
        G.add_node(str_transformed, type="symbolic", role="code")

        # Add directional edges
        G.add_edge(original, str_transformed, flip_type="forward", weight=1.0)
        G.add_edge(str_transformed, original, flip_type="reverse", weight=0.5)

    return G

# === GRAPH ANALYSIS ===
def analyze_graph(G):
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    clustering = nx.clustering(G.to_undirected())

    top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_degree, top_betweenness, clustering

# === GRAPH VISUALIZER ===
def visualize_graph(G, sample_size=100):
    sample_nodes = list(G.nodes)[:sample_size]
    subgraph = G.subgraph(sample_nodes)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(subgraph, seed=42)
    nx.draw(subgraph, pos, with_labels=True, node_size=500, font_size=7)
    plt.title("Symbolic Transformation Subgraph")
    plt.show()

# === SYMBOLIC PATTERN ANALYZER ===
def analyze_patterns(transformed_data):
    pattern_counts = Counter(transformed_data)
    observed = np.array(list(pattern_counts.values()))

    ent = entropy(observed, base=2)
    expected = np.full_like(observed, np.mean(observed))

    chi2, p_value = chi2_contingency([observed, expected])[:2]
    return ent, chi2, p_value

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("Loading dataset...")
    words = download_word_dataset()
    print(f"{len(words):,} words loaded.")

    print("Processing word transformations...")
    transformed = process_words_parallel(words)

    print("Building symbolic graph...")
    graph = build_graph(transformed, words)

    print("Analyzing graph...")
    top_deg, top_bet, cluster_vals = analyze_graph(graph)

    print("\nTop 10 by Degree Centrality:")
    for node, score in top_deg:
        print(f"{node}: {score:.4f}")

    print("\nTop 10 by Betweenness Centrality:")
    for node, score in top_bet:
        print(f"{node}: {score:.4f}")

    print("\nVisualizing symbolic structure...")
    visualize_graph(graph)

    print("Performing symbolic statistical analysis...")
    entropy_val, chi2_stat, p_val = analyze_patterns(transformed)

    print("\nSymbolic Pattern Analysis:")
    print(f"Entropy: {entropy_val:.4f}")
    print(f"Chi-Square: {chi2_stat:.4f}")
    print(f"P-Value: {p_val:.4f}")
    if p_val < 0.05:
        print("→ STRUCTURED PATTERN DETECTED")
    else:
        print("→ Appears random or evenly distributed.")
