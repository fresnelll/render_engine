# Ray Tracing Optimization: BVH vs. Monte Carlo Path Tracing

This project explores the optimization of ray tracing algorithms in computer graphics, focusing on Bounding Volume Hierarchy (BVH) and Monte Carlo path tracing. The research investigates how these methods affect rendering efficiency, using Python to implement and analyze the algorithms.

---

## Overview

### Research Question
How does optimization of acceleration structures, such as BVH, affect the efficiency and performance of the Ray Tracing algorithm in comparison to the Monte Carlo path tracing algorithm?

### Goal
To evaluate and compare the performance of BVH and Monte Carlo path tracing algorithms in rendering 3D scenes, with a focus on time complexity and rendering speed.

---

## Implementation Details

### Algorithms
1. **Monte Carlo Path Tracing**  
   - Simulates light transport by tracing paths using random sampling.
   - Produces highly realistic images but is computationally expensive.

2. **Bounding Volume Hierarchy (BVH)**  
   - Optimizes ray tracing by organizing 3D objects into a hierarchical structure.
   - Reduces the number of intersection tests, improving rendering speed.

### Experiment Setup
- **Hardware**: MacBook Pro (Apple M1 Pro, 16GB RAM)  
- **Software**: Python 3.12 with NumPy and Matplotlib libraries.  
- **Rendering Resolution**: 3000x2000 pixels.  

### Methodology
- Rendered the same scene using both algorithms.
- Measured rendering time for each algorithm over multiple trials.
- Compared performance based on rendering speed and time complexity.

---

## Results

- **Monte Carlo Path Tracing**: Average render time ~429 seconds.
- **BVH Optimization**: Average render time ~94.7 seconds.
- **Conclusion**: BVH is approximately 4.5 times faster than Monte Carlo path tracing while maintaining comparable image quality.

---

## Key Files
- `montecarlo.py`: Implements Monte Carlo path tracing.  
- `bvh.py`: Implements BVH optimization for ray tracing.  

---

## Limitations and Future Work
- **Limitations**: The BVH implementation was simplified for computational feasibility. A full BVH implementation would further enhance performance.  
- **Future Work**: Explore hybrid approaches combining BVH with other optimization techniques for more efficient rendering.

---

This research demonstrates the importance of acceleration structures in improving rendering efficiency, offering valuable insights for computer graphics applications.
