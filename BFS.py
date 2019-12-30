from collections import deque

def append_to_queue(deq , arr):
    for item in arr:
        deq.append(item)

def search_in_array(arr , target):
    for item in arr:
        if item == target:
            return True
    return False

#Broad first search (find path in non oriented graph)
def main():
    graph = {}
    graph["you"] = ["alice","bob","claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    

    
    search_queue = deque()
    append_to_queue(search_queue , graph["you"])
    searched = []

    while len(search_queue):
        person = search_queue.popleft()
        if not search_in_array(searched , person):
            if person == "anuj":
                print("person is seller")
            else:
                append_to_queue(search_queue, graph[person])
                searched.append(person)

if __name__ == "__main__":
    main()