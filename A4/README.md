# Assignment 4: Teach

## Tutorial - get the volume of an object in an IFC-File:

Problem: The IFC-File does not include the volume attribute for the object.

This tutoial teaches a way to calculate the volume of an object with a "simple" geometry, which doesn't have a volume attribute included in the IFC-File.

## Instructions:

## Step 1:

Include line "import ifcopenshell.geom" in your code

## Step 2:

Get geometric data for the objects from the IFC-File.

            shape = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), element)
            vertices = shape.geometry.verts
            if len(vertices) >= 24:  # Ensure sufficient vertices are available
                min_x = min(vertices[i] for i in range(0, len(vertices), 3))
                max_x = max(vertices[i] for i in range(0, len(vertices), 3))
                min_y = min(vertices[i + 1] for i in range(0, len(vertices), 3))
                max_y = max(vertices[i + 1] for i in range(0, len(vertices), 3))
                min_z = min(vertices[i + 2] for i in range(0, len(vertices), 3))
                max_z = max(vertices[i + 2] for i in range(0, len(vertices), 3))

![IMG 1](https://raw.githubusercontent.com/JanikRosien/BIManalyst_g_23/refs/heads/main/A4/pictures/IMG1.png)

## Step 3:

calculate the volume for the object with the geometric data.

Example for an parallelepiped:

return (max_x - min_x) * (max_y - min_y) * (max_z - min_z)

Example for an cylinder:

return (max_x - min_x) ** 2 * PI / 4 * (max_z - min_z)
