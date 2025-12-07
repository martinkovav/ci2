// Include alanine molecule
#include "ala.inc"

// create a regular point light source
light_source {
  <4.22505,3.33105,-7.67338>
  color rgb <1,1,1>    // light's color
}

// set a color of the background (sky)
background { color rgb <0.95 0.95 0.95> }

// perspective (default) camera
camera {
  location  <3, 3, -20>
  look_at   <1, 1, 0>
  right     x*image_width/image_height
}

// Include header for povray
#include "babel_povray3.inc"

// Draw pentagon outline
#declare pentagon_colour = color LightBlue

#declare vertex1 = <5, 0, 0>
#declare vertex2 = <1.545, 4.755, 0>
#declare vertex3 = <-4.045, 2.939, 0>
#declare vertex4 = <-4.045, -2.939, 0>
#declare vertex5 = <1.545, -4.755, 0>

cylinder { vertex1, vertex2, 0.1 pigment { pentagon_colour } }
cylinder { vertex2, vertex3, 0.1 pigment { pentagon_colour } }
cylinder { vertex3, vertex4, 0.1 pigment { pentagon_colour } }
cylinder { vertex4, vertex5, 0.1 pigment { pentagon_colour } }
cylinder { vertex5, vertex1, 0.1 pigment { pentagon_colour } }

// Pentagon with radius 5, centered at origin
// Vertices at angles: 0°, 72°, 144°, 216°, 288°

// Offset to center the Ala molecule
#declare offseted_mol = object {
	mol_0
  translate mol_0_center
}

// Vertex 1 (0°)
object {
	offseted_mol
	rotate <0, 0, 0>
  translate vertex1
}

// Vertex 2 (72°)
object {
	offseted_mol
  rotate <0, 0, 72>
	translate vertex2
}

// Vertex 3 (144°)
object {
	offseted_mol
  rotate <0, 0, 144>
	translate vertex3
}

// Vertex 4 (216°)
object {
	offseted_mol
  rotate <0, 0, 216>
	translate vertex4
}

// Vertex 5 (288°)
object {
	offseted_mol
  rotate <0, 0, 288>
	translate vertex5
}