# STREAM.ElasticPrincipalGraph

Elastic principal graph learning. 

ElPiGraph is a completely redesigned algorithm for the previously introduced elastic principal graph optimization based on the use of elastic matrix Laplacian, trimmed mean square error, explicit control of topological complexity and scalability to millions of points on an ordinary laptop. 

Elastic principal graphs are structured data approximators, consisting of vertices connected by edges. The vertices are embedded into the space of the data, minimizing the mean squared distance (MSD) to the data points, similarly to k-means. Unlike unstructured k-means, the edges connecting the vertices are used to define an elastic energy term. The elastic energy term and MSD are used to create penalties for edge stretching and bending of branches. To find the optimal graph structure, ElPiGraph uses a topological grammar (or, graph grammar) approach.

* epg_n_nodes: `int`, optional (default: 50)
    Number of nodes for elastic principal graph.
* incr_n_nodes: `int`, optional (default: 30)
    Incremental number of nodes for elastic principal graph when epg_n_nodes is not big enough.
* epg_lambda: `float`, optional (default: 0.02)
    lambda parameter used to compute the elastic energy.
* epg_mu: `float`, optional (default: 0.1)
    mu parameter used to compute the elastic energy.
* epg_trimmingradius: `float`, optional (default: 'Inf')  
    maximal distance from a node to the points it controls in the embedding.
* epg_finalenergy: `str`, optional (default: 'Penalized')
    indicate the final elastic energy associated with the configuration.
* epg_alpha: `float`, optional (default: 0.02)
    alpha parameter of the penalized elastic energy.
* epg_beta: `float`, optional (default: 0.0)
    beta parameter of the penalized elastic energy.
* epg_n_processes: `int`, optional (default: 1)
    the number of processes to use.

