# A2a: About your group

Q: How much do you agree wiht the following statement: I am confident coding in Python

A: Between 0 and 1 - It's the first time the three of us code in Python

# A2b: Identify Claim

Q: Select which building(s) to focus on for you focus area

A: Building #2406

Q: Identify a ‘claim’ / issue / fact to check from one of those reports.

A: Volume of concrete used in columns for every floor

Q: Write a short description of the claim you wish to check. It could be the same as the previous assignment,
   or if this is too simple you could identify a new claim from the report to check in this assignment

A: The report is giving dimensions for the concrete columns, we want to chack these dimensions by calculating the volume of the columns on each floor.

Q: Justify your selection of your claim

A: By checking this claim, we want to prevent the existence of wrong information in the report. This way unnecessary costs can be reduces.
It is also usefull to know how much concrete is needed for the columns on each floor, because you can use these informatino improve the workflow and safe time.

# A2c: Use Case

Q: How you would check this claim?

A: 1 - Repeat for every floor: 
         1.1 - To check this claim we have to repeat this action for every column in every floor:
         1.1.1 - check the height of the column 
         1.1.2 - check the Area of a cross section of a column
         1.1.3 - check the number of rebars and their area (maybe it's not in the IFCModel, in that case we take the data from the report)
         1.1.4 - calculate the effective area of concrete in a column
         1.1.5 - Calculate the volume of the column
         1.2 - Sum the volumes of the columns
         2 - Create a table that fit the results

Q: When would this claim need to be checked?

A: At the beginning of and before the construction of each floor, to take any changes into account.

Q: What information does this claim rely on?

A: Dimension of the columns and number and type of reebars

Q: What phase? planning, design, build or operation

A: Design and build

Q: What BIM purpose is required? Gather, generate, analyse, communicate or realise?

A: Analyse

Q: Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one

A: -**02: Cost estimation**
   - 11: Sustainability Analysis
   - 13: Design Coordination
   - 14: Site Utilization Planning

Q: Produce a BPMN drawing for your chosen use case. link to this so we can see it in your markdown file. To do this you will have to save it as an SVG,
   please also save the BPMN with it.You can use this online tool to create a BPMN file

A: 

# A2d: Scope the use case

Q: From the ‘whole use case’ identify where a new script / function / tool is needed. Highlight this in your BPMN diagram. Show this clearly in a new SVG diagram.

A:
    
# A2e: Tool Idea

Q: Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.

A: Our idea is it to create a tool, which helps the owner, by reducing unnecessary costs due to waste of material and reducing the construction.
But also the executing company, because the gained information can be used to structure the workflow, use the constructino area in a more efficient way and therefore safe time in the long run.
The tool gatheres the dimensions of the columns used in the model and compares these to the given information from the report. The information are documentated in a table.

Q: What is the business and societal value of your tool?

A: business value:
   -   reduce material costs
   -   structure the workflow
   -   reduce total emissions
   -   reduce construction time
     
   societal value:
   -   shorten the time of noise pollution
   -   reduce total emissions
   -   construction finished earlier -> earlier accessible for society

Q: Produce a BPMN diagram to summarise your idea. Save this in a folder in your repository along with an SVG of the disagram and embed the SVG in the Markdown as an            image.

A:
![SVG tool](https://raw.githubusercontent.com/JanikRosien/BIManalyst_g_23/refs/heads/main/A2/IMG/241007%20totalcolumns.svg)

# A2f: Information Requirements
Identify what information you need to extract from the model

Q: Where is this in IFC?

A:

Q: Is it in the model?

A:

Q: Do you know how to get it in ifcOpenShell?

A:

Q: What will you need to learn to do this? [Enrolled students only]: add to this excel in teams

A:

# A2g: Identify appropriate software licence

Q: What software licence will you choose for your project?

A: 

