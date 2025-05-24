
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Neural Network of 3-Letter Words")
st.write("Select words to visualize how their characters connect!")

# Predefined list
default_words = ["cat", "dog", "bat", "sun", "man", "pen", "jar", "run", "box", "hat"]
selected_words = st.multiselect("Choose up to 5 words:", default_words, default=default_words[:5])

# Build graph
G = nx.DiGraph()
for word in selected_words:
    if len(word) == 3:
        a, b, c = word
        G.add_edge(a, b)
        G.add_edge(b, word)
        G.add_edge(word, c)

# Draw graph
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=2000, font_size=12, ax=ax)
st.pyplot(fig)
