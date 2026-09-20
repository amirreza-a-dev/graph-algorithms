# Graph Algorithms

A simple terminal-based app for implementing and using graph algorithms.

## Description

This is a simple implementation of graph traversal algorithms. It helps users find the shortest path between two vertices, as well as find all vertices connected to a given vertex.

## Features

* [x] Breadth First Search
* [x] Depth First Search
* [x] Support for undirected and unweighted graphs

## Built With

* Python
* C++

## Requirements

* Python 3.10 or newer
* C++ compiler (g++)

## Usage

```bash
python main.py
```
## Input Format

Each edge should be entered as a pair of vertex numbers in the following format:

```bash
0 1
```

where 0 and 1 represent the two vertices of the edge.

Vertices are represented by non-negative integers starting from 0. The set of vertices must be consecutive, meaning that if the input contains a vertex n, then all vertices from 0 through n-1 must also be present somewhere in the input.

For example, the following input is valid:

```bash
0 1
1 7 
2 3 
3 4 
4 5 
5 6 
6 2
```

The order of the edges does not matter. Although vertex 7 appears before some of the other vertices, all vertices from 0 through 7 are present in the input.

The following input is invalid:

```bash
0 1
1 7
```

because vertices 2, 3, 4, 5, and 6 are missing.

## Status

🚧 **Work in Progress**

## Learning Goals

* Improve my knowledge of graph algorithms.
* Learn the basics of C++.
* Improve my Python skills.