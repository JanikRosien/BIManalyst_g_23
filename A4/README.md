# Assignment 4: Teach

## Summary
# Volume Calculation for Objects in an IFC-File

When looking for the volume of an object, we stumbled uppon the issue, that some objects don't have a volume attribute in the IFC-File. So we decided to calculate the volume with a simple code. In the first step, the code is getting the dimensions of the objects in the x, y and z direction, out of the model. After that, the volume is calculated, this is done, by using the correct volume-fomula, depending on the shape of the object. 

## Tutorial - get the volume of an object in an IFC-File:

Problem: The IFC-File does not include the volume attribute for the object.

This tutoial teaches a way to calculate the volume of an object with a "simple" geometry, which doesn't have a volume attribute included in the IFC-File.

## Instructions:

## Step 1:

Include line "import ifcopenshell.geom" in your code

## Step 2:

Get geometric data for the objects from the IFC-File.

            def calculate_volume(element):

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

## Example for calculating column volumes:
            
            import ifcopenshell
            import ifcopenshell.geom

            # Load the IFC file
            ifc_file = ifcopenshell.open("path_to_your_ifc_file.ifc")

            # Get all IfcColumn elements from the IFC file
            columns = ifc_file.by_type("IfcColumn")

            # Function to calculate volume for an element
            def calculate_volume(element):
                shape = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), element)
                vertices = shape.geometry.verts
                        if len(vertices) >= 24:  # Ensure sufficient vertices
                    min_x = min(vertices[i] for i in range(0, len(vertices), 3))
                    max_x = max(vertices[i] for i in range(0, len(vertices), 3))
                    min_y = min(vertices[i + 1] for i in range(0, len(vertices), 3))
                    max_y = max(vertices[i + 1] for i in range(0, len(vertices), 3))
                    min_z = min(vertices[i + 2] for i in range(0, len(vertices), 3))
                    max_z = max(vertices[i + 2] for i in range(0, len(vertices), 3))
                    return (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
                return 0

            # Calculate and print volume for each IfcColumn
            for column in columns:
                volume = calculate_volume(column)
                print(f"Column ID: {column.GlobalId}, Volume: {volume}")
