"""
This script processes an IFC (Industry Foundation Classes) file to calculate and display the element volumes
and element counts for each floor of a building. It is useful for analyzing structural components in 3D models
of buildings, typically created in BIM (Building Information Modeling) software.

Key Features:
1. Reads an IFC file to extract information about floors (IfcBuildingStorey) and elements (Ifcelement).
2. Calculates the total volume of the elements for each floor by summing up the volumes of its elements (in this example elements).
3. Handles cases where volume data is not directly available by estimating it using geometric data.

How to Use:
1. Replace `PATH_TO_YOUR_IFC_FILE.IFC` with the path to the IFC file on your device.
2. Run the script.
3. The script will output detailed information about the number of elements, their volumes, and the total volume
   of elements for each floor, as well as the total for the entire building.

Note: The script uses the `ifcopenshell` library, so ensure it is installed in your Python environment.
"""

import ifcopenshell
import ifcopenshell.geom


# Specify the path to IFC file (This requires user input for the tool to execute)
file_path = r'FILE_PATH_TO_YOUR_IFC_FILE.Ifc'

# Open the IFC file
ifc_file = ifcopenshell.open(file_path)

#Select Element type to calculate
Ifc_element_type = "IfcSlab" # Can be altered to target different IFC Elements e.g. IfcSlab, IfcWall, IfcBeam (This can be time consuming for large IFC Files with many elements.)

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
                return (max_x - min_x) * (max_y - min_y) * (max_z - min_z) # This formula can be altered for other shapes e.g. cylinders
               
        except Exception as e:
            print(f"Volume calculation failed for Element {element.GlobalId} with error: {e}")
            return 0  # Return 0 if the shape creation or calculation fails
    return 0

# Initialize dictionary to hold volume data
element_volumes = {"Floors": {}}
total_volume = 0  # Track total volume

# Calculate volume and element data for each floor (IfcBuildingStorey)
floors = ifc_file.by_type("IfcBuildingStorey")
for index, floor in enumerate(floors, start=1):
    floor_id = floor.GlobalId
    floor_name = floor.Name if floor.Name else f"Floor {index}"
    
    # Initialize data structure for each floor
    element_volumes["Floors"][floor_name] = {
        "Total Volume": 0, 
        "Total elements": 0, 
        "Elements": {}  # Store individual element data
    }
    
    # Find all elements associated with the floor
    elements = [w for w in ifc_file.by_type(Ifc_element_type) if w.ObjectPlacement.PlacementRelTo == floor.ObjectPlacement]
    element_volumes["Floors"][floor_name]["Total Elements"] = len(elements)  # Record number of elements on this floor
    
    # Calculate volume for each element and label them
    for element_index, element in enumerate(elements, start=1):
        element_name = element.Name if element.Name else f"Element {element_index}"
        element_volume = calculate_volume(element)
        
        # Add individual element data
        element_volumes["Floors"][floor_name]["Elements"][element_name] = element_volume
        element_volumes["Floors"][floor_name]["Total Volume"] += element_volume  # Add to floor total volume
        total_volume += element_volume  # Add to overall total volume

# Display formatted volume and element data
print("\nelement Volume and element Data (in cubic meters):")
print("=" * 50)

# Display each floor's data
for floor_name, floor_data in element_volumes["Floors"].items():
    if floor_data["Total Volume"] > 0:
        print(f"\n{floor_name}")
        print("-" * 50)
        print(f"  Total Elements: {floor_data['Total Elements']}")
        print(f"  Total Volume: {floor_data['Total Volume']:.2f} m³\n")

        # Display each element's data, with concise layout
        print("    Elements:")
        for element_name, element_volume in floor_data["Elements"].items():
            print(f"      - {element_name}: {element_volume:.2f} m³")
        print("-" * 50)

# Print total volume across all floors
print(f"\n{'=' * 50}")
print(f"Total Element Volume for All Floors: {total_volume:.2f} m³")
print(f"{'=' * 50}")
