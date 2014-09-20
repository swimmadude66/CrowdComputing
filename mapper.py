__author__ = 'adam'


num_nodes = 0
nodes = []
sourceid = ""


def setup():
    nodes = getNodes()      # get nodes
    num_nodes = len(nodes)  # get num nodes
    sourceid = getID()      # generate unique identifier


def map(data):
    node_data = []
    for i in range(0, num_nodes):
        node_data[i] = []
    for j in range(0, len(data)):
        node_data[j].append(data[j])
    for k in range(0, num_nodes):
        dest = nodes[k]
        send(node_data[k], dest, sourceid)


    


