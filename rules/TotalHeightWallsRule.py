import ifcopenshell
import ifcopenshell.geom

def checkRule(model):
    # Initialize a list to collect the results
    results = []
    
    # Find all elements of type IfcWall
    walls = model.by_type("IfcWall")
    
    # Loop through the found walls and read their dimensions
    for wall in walls:
        
        # Get the wall's geometry
        shape = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), wall)
        
        # Extract the vertices of the geometry
        vertices = shape.geometry.verts
        
        # Extract the Z coordinates (height)
        z_coords = [vertices[i+2] for i in range(0, len(vertices), 3)]  # Take only the Z coordinates
        
        # Calculate the wall height as the difference between the max and min Z
        min_z = min(z_coords)
        max_z = max(z_coords)
        height = max_z - min_z
        
        # Add the result to the list: the first element is the wall's ID, the second element is the height of that wall in meters
        results.append((wall.GlobalId, height))
    
    # Return the list of results
    return results
