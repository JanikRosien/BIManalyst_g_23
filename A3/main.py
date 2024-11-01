import ifcopenshell
import ifcopenshell.geom

# Specify the path to IFC file
file_path = r'C:\Users\hughf\OneDrive\Documents\RMIT UNI\2024 Semester 2\Advanced BIM\CES_BLD_IFC_FILES\CES_BLD_24_06_STR.ifc'

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
        except Exception as e:
            print(f"Volume calculation failed for element {element.GlobalId} with error: {e}")
            return 0  # Return 0 if the shape creation or calculation fails
    return 0

# Initialize dictionary to hold volume data
concrete_volumes = {"Floors": {}}
total_volume = 0  # Track total volume

# Calculate volume and column data for each floor (IfcBuildingStorey)
floors = ifc_file.by_type("IfcBuildingStorey")
for index, floor in enumerate(floors, start=1):
    floor_id = floor.GlobalId
    floor_name = floor.Name if floor.Name else f"Floor {index}"
    
    # Initialize data structure for each floor
    concrete_volumes["Floors"][floor_name] = {
        "Total Volume": 0, 
        "Total Columns": 0, 
        "Columns": {}  # Store individual column data
    }
    
    # Find all columns associated with the floor
    columns = [w for w in ifc_file.by_type("IfcColumn") if w.ObjectPlacement.PlacementRelTo == floor.ObjectPlacement]
    concrete_volumes["Floors"][floor_name]["Total Columns"] = len(columns)  # Record number of columns on this floor
    
    # Calculate volume for each column and label them
    for column_index, column in enumerate(columns, start=1):
        column_name = column.Name if column.Name else f"Column {column_index}"
        column_volume = calculate_volume(column)
        
        # Add individual column data
        concrete_volumes["Floors"][floor_name]["Columns"][column_name] = column_volume
        concrete_volumes["Floors"][floor_name]["Total Volume"] += column_volume  # Add to floor total volume
        total_volume += column_volume  # Add to overall total volume

# Display formatted volume and column data
print("\nConcrete Volume and Column Data (in cubic meters):")
print("=" * 50)

# Display each floor's data
for floor_name, floor_data in concrete_volumes["Floors"].items():
    if floor_data["Total Volume"] > 0:
        print(f"\n{floor_name}")
        print("-" * 50)
        print(f"  Total Columns: {floor_data['Total Columns']}")
        print(f"  Total Volume: {floor_data['Total Volume']:.2f} m³\n")

        # Display each column's data, with concise layout
        print("    Columns:")
        for column_name, column_volume in floor_data["Columns"].items():
            print(f"      - {column_name}: {column_volume:.2f} m³")
        print("-" * 50)

# Print total volume across all floors
print(f"\n{'=' * 50}")
print(f"Total Concrete Volume for All Floors: {total_volume:.2f} m³")
print(f"{'=' * 50}")
