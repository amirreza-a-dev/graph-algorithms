![License](https://img.shields.io/badge/license-MIT-red)
![Python](https://img.shields.io/badge/python-3.14-blue)
![C++](https://img.shields.io/badge/C%2B%2B-yellow)

# Graph Algorithms

A simple terminal-based app for implementing and using graph algorithms.

## Description

This is a simple implementation of graph traversal algorithms. It helps users find the shortest path between two vertices, as well as find all vertices connected to a given vertex.

## Features

* [x] Breadth First Search
* [x] Depth First Search
* [x] Support for directed, undirected and mixed unweighted graphs

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

The graph is read from a text file where each line represents an edge using three values:

<source> <destination> <type>
* source — the starting vertex.
* destination — the ending vertex.
* type — specifies whether the edge is directed or undirected:
    * d — directed edge
    * u — undirected edge

For example, the following input is valid:

```bash
0 1 u
2 1 d
end
```
And for example the following lines invalidate the input.:

```bash
1 0 2
0 1 x
1 u 0
d 1 0
1 2
```

Vertices are represented by non-negative integers starting from 0. The set of vertices must be consecutive, meaning that if the input contains a vertex n, then all vertices from 0 through n-1 must also be present somewhere in the input.

For example, the following input is valid:

```bash
0 1 d
1 7 d
2 3 u
3 4 d
4 5 u
5 6 u
6 2 u
end
```

The order of the edges does not matter. Although vertex 7 appears before some of the other vertices, all vertices from 0 through 7 are present in the input.

The following input is invalid:

```bash
0 1 u
1 7 e
end
```

because vertices 2, 3, 4, 5, and 6 are missing.

## Status

🚧 The project is currently under active development.

Version 1.1.0
* Added support for directed and undirected edges.
* Added validation and error handling for invalid graph file data.
* Improved the user interface and input prompts.

## Learning Goals

* Improve my knowledge of graph algorithms.
* Learn the basics of C++.
* Improve my Python skills.