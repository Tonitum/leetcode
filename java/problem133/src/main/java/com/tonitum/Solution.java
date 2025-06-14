package com.tonitum;

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        Map<Integer, Node> graph = new HashMap<Integer, Node>();
        Queue<Node> next = new ArrayDeque<Node>();
        Node root = new Node(node.val);
        graph.put(root.val, root);
        next.add(node);
        while (!next.isEmpty()) {
            Node curr = next.remove();
            Node newCurr = graph.containsKey(curr.val) ? graph.get(curr.val) : new Node(curr.val);
            if (!newCurr.neighbors.isEmpty()) {
                continue;
            }
            // add nodes for the neighbors
            for (Node neighbor : curr.neighbors) {
                Node newNeighbor = graph.containsKey(neighbor.val) ? graph.get(neighbor.val) : new Node(neighbor.val);
                newCurr.neighbors.add(newNeighbor);
                if (!graph.containsKey(newNeighbor.val)) {
                    graph.put(neighbor.val, newNeighbor);
                    next.add(neighbor);
                    continue;
                }
                if (graph.get(neighbor.val).neighbors.isEmpty() && !next.contains(neighbor)) {
                    next.add(neighbor);
                }
            }
        }
        return graph.get(node.val);
    }
}
