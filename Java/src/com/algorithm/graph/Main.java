package com.algorithm.graph;

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph(false);
        graph.addEdge(2, 5);
        graph.addEdge(3, 5);
        graph.addEdge(2, 9);
        graph.addEdge(2, 10);
        if(graph.getAddjacentVertices(2) != null)
            System.out.println(graph.getAddjacentVertices(2));
        else
            System.out.println("null");
    }
}
