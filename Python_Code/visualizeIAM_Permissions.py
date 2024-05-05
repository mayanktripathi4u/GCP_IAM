import networkx as nx
import matplotlib.pyplot as plt

# Example IAM data (replace with actual IAM data)
iam_data = {
    "user1@example.com": ["roles/editor", "roles/viewer"],
    "user2@example.com": ["roles/owner"],
    "group1@example.com": ["roles/editor"],
    "group2@example.com": ["roles/viewer"],
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes for users and roles
for user, roles in iam_data.items():
    G.add_node(user, type='user')
    for role in roles:
        G.add_node(role, type='role')
        G.add_edge(user, role)

# Plot the graph
pos = nx.spring_layout(G, seed=42)  # Set seed for reproducibility
node_colors = ['#1f78b4' if G.nodes[node]['type'] == 'user' else '#33a02c' for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10)
plt.title('IAM Users and Roles')
plt.show()
