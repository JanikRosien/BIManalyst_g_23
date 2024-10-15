## A2a: About your group

**Q: How much do you agree with the following statement: I am confident coding in Python**

A: 0 - It's the first time the three of us are coding in Python.

---

## A2b: Identify Claim

**Q: Select which building(s) to focus on for your focus area**

A: Building #2406

**Q: Identify a ‘claim’ / issue / fact to check from one of those reports.**

A: Volume of concrete used in columns for every floor.

**Q: Write a short description of the claim you wish to check. It could be the same as the previous assignment, or if this is too simple you could identify a new claim from the report to check in this assignment.**

A: The report is providing dimensions for the concrete columns, and we want to check these dimensions by calculating the volume of the columns on each floor.

**Q: Justify your selection of your claim**

A: By checking this claim, we want to prevent incorrect information in the report. This way, unnecessary costs can be reduced. It is also useful to know how much concrete is needed for the columns on each floor because this information can be used to improve the workflow and save time.

---

## A2c: Use Case

**Q: How would you check this claim?**

A: 

1. Repeat for every floor:
   - 1.1 To check this claim, we have to repeat this action for every column on every floor:
     - 1.1.1 Check the height of the column.
     - 1.1.2 Check the area of a cross-section of the column.
     - 1.1.3 Check the number of rebars and their area (if it's not in the IFCModel, we will take the data from the report).
     - 1.1.4 Calculate the effective area of concrete in the column.
     - 1.1.5 Calculate the volume of the column.
   - 1.2 Sum the volumes of the columns.
2. Create a table that fits the results.

**Q: When would this claim need to be checked?**

A: At the beginning of and before the construction of each floor, to take any changes into account.

**Q: What information does this claim rely on?**

A: Dimension of the columns and number and type of rebars.

**Q: What phase? planning, design, build, or operation**

A: Design and build.

**Q: What BIM purpose is required? Gather, generate, analyze, communicate, or realize?**

A: Analyze.

**Q: Review use case examples - do any of these help? What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one.**

A: 
- **02: Cost estimation**
- **11: Sustainability Analysis**
- **13: Design Coordination**
- **14: Site Utilization Planning**

**Q: Produce a BPMN drawing for your chosen use case. Link to this so we can see it in your markdown file. To do this, you will have to save it as an SVG. Please also save the BPMN with it.**

A: 
![Use Case - Cost Estimation](https://raw.githubusercontent.com/JanikRosien/BIManalyst_g_23/refs/heads/main/A2/IMG/USE_CASE_OVERALL.svg)

---

## A2d: Scope the use case

**Q: From the ‘whole use case’ identify where a new script / function / tool is needed. Highlight this in your BPMN diagram. Show this clearly in a new SVG diagram.**

A:
![Use Case - Tool Integration](https://raw.githubusercontent.com/JanikRosien/BIManalyst_g_23/refs/heads/main/A2/IMG/USE_CASE_HIGHLIGHTED.svg)

---

## A2e: Tool Idea

**Q: Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.**

A: Our idea is to create a tool that helps the owner by reducing unnecessary costs due to material waste and construction delays. It will also benefit the executing company, as the information can be used to structure the workflow and use the construction area more efficiently, thus saving time in the long run. The tool gathers the dimensions of the columns used in the model and compares them to the information from the report. The results are documented in a table.

**Q: What is the business and societal value of your tool?**

A: 

- **Business Value:**
   - Reduce material quantity and costs.
   - Structure the workflow.
   - Reduce total emissions.
   - Reduce construction time.
     
- **Societal Value:**
   - Shorten the duration of noise pollution.
   - Reduce total emissions.
   - Construction finished earlier, making it accessible to society sooner.

**Q: Produce a BPMN diagram to summarize your idea. Save this in a folder in your repository along with an SVG of the diagram and embed the SVG in the Markdown as an image.**

A:
![SVG Tool](https://raw.githubusercontent.com/JanikRosien/BIManalyst_g_23/refs/heads/main/A2/IMG/241007%20totalcolumns.svg)

---

## A2f: Information Requirements

**Q: Identify what information you need to extract from the model.**

A: 

- Identify the floor.
- Identify concrete structures (columns).
- Location of columns (assignment to floor).
- Dimensions of columns (height, cross-section).
- Volume of columns (gross volume).
- Information about the reinforcement in the columns.
- Concrete volume of columns (net volume).

**Q: Where is this in IFC?**

A: In the IFC model, this data is typically located in `IfcBuildingElement` or `IfcColumn` entities. The dimensions are in properties like `IfcPropertySingleValue`, and volume calculations are derived from geometric data.

**Q: Is it in the model?**

A: Yes, all the data, except information about the reinforcement, should be available in the IFC file.

**Q: Do you know how to get it in ifcOpenShell?**

A: We would need to use the `ifcopenshell` library to access and query the IFC entities, extracting dimensions and performing volume calculations.

**Q: What will you need to learn to do this?**

A: We will need to learn how to query the IFC model using `ifcopenshell` and perform calculations based on the data extracted.

---

## A2g: Identify appropriate software license

**Q: What software license will you choose for your project?**

A: An appropriate license would be the MIT License or GNU GPL, as these are common for open-source projects and provide flexibility in usage and distribution while maintaining authorship and contribution integrity. We will likely choose GPL-3.0 as it is what the course is based in.
