import ifcopenshell
import ifcopenshell.geom

# Specify the path to your updated IFC file
file_path = r'C:\Users\hughf\OneDrive\Documents\RMIT UNI\2024 Semester 2\Advanced BIM\CES_BLD_IFC_FILES\CES_BLD_24_06_STR.ifc'

# Specify the path to your updated IFC file
# file_path = r'C:\Users\hughf\OneDrive\Documents\RMIT UNI\2024 Semester 2\Advanced BIM\SKYLAB_IFC_FILES\LLYN - STRU.ifc'


# Open the IFC file
ifc_file = ifcopenshell.open(file_path)

# Function to calculate volume for an element
def calculate_volume(element):
    if hasattr(element, 'Volume'):
        return element.Volume
    else:
        # Use geometric data if volume attribute is not available
        try:
            shape = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), element)
            vertices = shape.geometry.verts
            if len(vertices) >= 24:  # Ensure sufficient vertices are available
                min_x = min(vertices[i] for i in range(0, len(vertices), 3))
                max_x = max(vertices[i] for i in range(0, len(vertices), 3))
                min_y = min(vertices[i + 1] for i in range(0, len(vertices), 3))
                max_y = max(vertices[i + 1] for i in range(0, len(vertices), 3))
                min_z = min(vertices[i + 2] for i in range(0, len(vertices), 3))
                max_z = max(vertices[i + 2] for i in range(0, len(vertices), 3))
                
                # Calculate the approximate bounding box volume
                return (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
        except:
            return 0  # Return 0 if the shape creation or calculation fails
    return 0

# Initialize dictionary to hold volume data
concrete_volumes = {"Floors": {}}

# Calculate volume for each floor (IfcBuildingStorey)
floors = ifc_file.by_type("IfcBuildingStorey")
for index, floor in enumerate(floors, start=1):
    floor_id = floor.GlobalId
    floor_name = floor.Name if floor.Name else f"Floor {index}"
    concrete_volumes["Floors"][floor_name] = 0  # Initialize volume for each floor
    
    # Find all columns associated with the floor
    columns = [w for w in ifc_file.by_type("IfcColumn") if w.ObjectPlacement.PlacementRelTo == floor.ObjectPlacement]
    
    # Calculate volume for columns
    for column in columns:
        concrete_volumes["Floors"][floor_name] += calculate_volume(column)

# Display the formatted volume
print("\nConcrete Volume Data (in cubic meters):")

# Display each floor's volume, filtering out zero-volume floors
for floor_name, volume in concrete_volumes["Floors"].items():
    if volume > 0:
        print(f"{floor_name} Volume: {volume:.2f} m³")
