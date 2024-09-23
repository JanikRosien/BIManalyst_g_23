import ifcopenshell
import ifcopenshell.geom

def checkRule(model):
# Insert the path to the IFC file (make sure it's correct)
file_path = 'import ifcopenshell
import ifcopenshell.geom

# Find all elements of type IfcWall
walls = ifc_file.by_type("IfcWall")

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
    
    # Print the wall's height
    result = f"Height of Wall {wall.GlobalId}: {height} meters"
    return result
