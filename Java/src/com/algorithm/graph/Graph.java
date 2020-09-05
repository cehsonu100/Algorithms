/**
 * use adjacency list to represent the graph
 * e.g.
 * {a: [b, e]}
 * {b: [f, c]}
 * {e: [g, a, j, r]}
 * above: dictionary key represent the vertex and its values represent the vertices that are connected with dictionary's key vertex
 */
package com.algorithm.graph;

import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Graph {
    boolean isDirected = false;
    private Map<Integer, ArrayList<Integer>> allVertex;

    public Graph(boolean isDirected) {
        this.isDirected = isDirected;
        this.allVertex = new HashMap<Integer, ArrayList<Integer>>();
    }

    //add edge with 2 input vertices u & v
    public void addEdge(int u, int v) {
        if(!hasVertex(u)) addVertex(u);
        allVertex.get(u).add(v);

        //if graph is directed then map second vertex to first vertex also
        if(!this.isDirected) {
            if(!hasVertex(v)) addVertex(v);
            allVertex.get(v).add(u);
        }
    }

    //get all vertices connected with given source vertex u
    public ArrayList<Integer> getAddjacentVertices(int u) {
        if(hasVertex(u))
            return allVertex.get(u);
        else
            return null;
    }

    //check if vertex is already present in graph
    public boolean hasVertex(int v) {
        if(allVertex.containsKey(v)) return true;
        else
            return false;
    }

    //add new vertex if not present in graph
    private void addVertex(int v) {
        if(!hasVertex(v))
            allVertex.put(v, new ArrayList<>());
    }

}

class Vertex {
    int data;
    Vertex(int data) {
        this.data = data;
    }
}

