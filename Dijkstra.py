

def find_lowest_cost_node(costs,processed):
    lowest_cost = float("inf")
    lowest_key = None
    for key in costs.keys():
        if costs[key] < lowest_cost and key not in processed:
            lowest_cost = costs[key]
            lowest_key = key
    return lowest_key

#Algorihtms of finding the fastest way in graph with weights
def main():

    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["fin"] = 5
    graph["b"]["a"] = 3

    graph["fin"] = {}
    infinity = float("inf")

    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["in"] = None

    processed = []

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        print(costs)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(costs)


if __name__ == "__main__":
    main()