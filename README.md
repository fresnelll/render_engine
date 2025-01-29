# render_engine
Rendering engine based on python 
optimization of acceleration structures, such as BVH (Bounding Volume Hierarchy), affect the efficiency and performance of the Ray Tracing algorithm in comparison to Monte Carlo path tracing algorithm. 

Conceptually light rays can be divided into 6 parts. Light rays are divided in the following order:
primary, shadow, reflection, refraction, pixel and eye rays. Further in the paragraph I will be discussing the characteristics of each of the light rays.
Shadow rays are the ones which deliver the light from a light source directly to an object surface. Pixel and eye rays are responsible for delivering rays to the screen coming from the camera. Primary rays are directly forwarded rays of light. Reflection and refraction rays are rays that hold the light rays after reflecting and refracting from the surface. To conclude, even though rays can be different they are treated similarly while tracing them. Differentiating these rays will help us in some cases to know more about colours inside of the image.

When it comes to rendering images, various ray tracing algorithms kick in. However, Monte Carlo
path tracing algorithm is unique. MC path tracing algorithm offers an elegant solution to the rendering equation. Rendering equation is a function that has to be completed while rendering. This equation has been designed to showcase the steps and goals rendering should achieve.
<img width="534" alt="Screenshot 2025-01-29 at 12 40 37 PM" src="https://github.com/user-attachments/assets/355f9d3c-bf54-4ea6-ada9-3853450efc77" />

The equation provided upfront is a fundamental equation of rendering. L in the equation is radiance leaving the initial point 𝜔"⃗ to the set direction 𝑥⃗. Radiance is a term often used in optics to represent radiance exerted from the source emitting area and propagated in the Solid angle. or in simple words, the amount of light arriving at particular point from a certain direction. Integral is
r e s p o n s i b l e f o r s u m m i n g a l l t h e l i g h t r a y ’ s i n c o m i n g f r o m t h e 𝜔" " ⃗ t o 𝑥⃗ . I n t h e a l g o r i t h m t h i s e q u a t i o n i s responsible for finding the radiance of the light ray shined from the certain point to the surface of the object.
However, it is also important to mention why I chose a Monte Carlo path tracing algorithm besides having an elegant solution to this equation. Monte Carlo algorithm works on integration of the rendering equation by tracing paths of lights whenever they interact with surface. Estimation of the ray hitting the surface is majorly based on the random sampling. In addition, as a program receives big amount of data (has traced lots of rays), solution of the equation becomes highly accurate. Therefore, the image rendered becomes realistic.

Bounding Volume Hierarchy is an algorithm responsible for accelerating the process of tracing the
ray. BVH is an optimization algorithm and it’s is not the same as a ray tracing algorithm. Bounding Volume Hierarchy is responsible for optimizing the speed of the render however it has no effect on movement of rays or tracing them. The basic concept of ray tracing is to analyze whether the object that takes the hit from ray should be rendered. Thus, eliminating the unnecessary parts of the virtual scene to be rendered. However, getting into details of a BVH will require a bit more than once one statement.

For this experiment I will taking one of my previously made renders and will demonstrate the Bounding Volume Hierarchy in it.
<img width="588" alt="Screenshot 2025-01-29 at 12 41 59 PM" src="https://github.com/user-attachments/assets/d8294d64-52a7-4326-856b-82b1a8a24263" />
This image showcases the visualization of a room with a daylight lightning. To move to the next stage of explaining Bounding Volume Hierarchy we should interpret BVH as a tree. In another words hierarchy in the bounding volumes should be interpreted as a tree structure. A tree where leaves store objects or geometrical figures. These trees are called primitives
Trees often form the following structure:
<img width="640" alt="Screenshot 2025-01-29 at 12 42 20 PM" src="https://github.com/user-attachments/assets/c7558728-826e-4189-a277-fc5db486f753" />
This tree represents distribution of primitives on the tree. The tree has nodes. The root node is called the top-level node and it covers the entire screen. Interior nodes divide nodes into smaller disjoint regions. Interior nodes are characterized in the following way:
Every single one of them has two child nodes, they’re called left child and the right child. Parent node divides primitives into two child node subsets. The least level nodes are called leaf nodes. These nodes do not have child nodes however they contain the reference to primitives. One of the main characteristics of the leaf node is following: whenever ray traversal (a ray responsible for following from the root node to the leaf node) reaches a lead node, all of the intersection tests will be made on the primitives that are stored inside of that lead node. What all of these nodes do is that they bound a box around the object that encompasses the primitive beneath it, thus ray that won’t intersect a node’s bound will skip the subtree itself.
Division in nodes on the rendered image would look in the following way:
<img width="439" alt="Screenshot 2025-01-29 at 12 43 10 PM" src="https://github.com/user-attachments/assets/7a1c3599-cb74-4d51-830c-df5bbf442084" />

