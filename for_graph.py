import pygraphviz as pgv

def create_dependency_graph(project_structure):
    graph = pgv.AGraph(directed=True)

    # Add nodes for each module/package
    for module in project_structure:
        graph.add_node(module)

    # Add edges for dependencies
    for module, dependencies in project_structure.items():
        for dependency in dependencies:
            graph.add_edge(module, dependency)

    return graph

def save_graph(graph, output_file):
    graph.draw(output_file, prog="dot", format="png")

if __name__ == "__main__":
    # Define your project structure (module -> dependencies)
    project_structure = {
        "module1": ["module2", "module3"],
        "module2": ["module3"],
        "module3": [],
    }

    # Create the dependency graph
    dependency_graph = create_dependency_graph(project_structure)

    # Save the graph to a file
    save_graph(dependency_graph, "dependency_graph.png")