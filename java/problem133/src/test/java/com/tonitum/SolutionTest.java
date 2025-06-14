package com.tonitum;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class SolutionTest {

    @Test
    public void testCaseOne() {
        Solution handle = new Solution();
        // adjList = [[2,4],[1,3],[2,4],[1,3];
        Node nodeOne = new Node(1);
        Node nodeTwo = new Node(2);
        Node nodeThree = new Node(3);
        Node nodeFour = new Node(4);
        nodeOne.neighbors.add(nodeTwo);
        nodeOne.neighbors.add(nodeFour);

        nodeTwo.neighbors.add(nodeOne);
        nodeTwo.neighbors.add(nodeThree);

        nodeThree.neighbors.add(nodeTwo);
        nodeThree.neighbors.add(nodeFour);

        nodeFour.neighbors.add(nodeThree);
        nodeFour.neighbors.add(nodeOne);

        Node cloned = handle.cloneGraph(nodeOne);
        assertEquals(1, cloned.val);
        assertEquals(2, cloned.neighbors.size());

    }
}

