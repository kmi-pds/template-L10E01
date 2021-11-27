from logging import log
from os import name
import time
import random

from multiprocessing import current_process
from distsim import Network, Node, Link, Message


def node_code():
    node: Node = current_process()

    logger = node.init_logger()

    # fill your code here


if __name__ == "__main__":
    number_of_nodes = 8

    nodes = [Node(str(idx), node_code) for idx in range(number_of_nodes)]
    links = [
        Link("0", "1"), Link("0", "2"),
        Link("1", "4"), Link("1", "3"),
        Link("2", "3"), Link("2", "7"),
        Link("3", "6"),
        Link("4", "5"),
        Link("5", "6"),
        Link("6", "7")
    ]
    network = Network(nodes, links)

    network.start()
    time.sleep(5)
    network.kill()
