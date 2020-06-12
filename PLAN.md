Here is a rough implementation plan for Orkestra with backlog

## Release 1.0.0 (Active - Tracked in Github Issues)

**Milestones**

- 0.1.0 - Load AppState on Application Start-Up
- 0.2.0 - Load Folders on Application Start-Up
- 0.2.0 - Create Default Folder if it doesn't exist
- 0.3.0 - Add toolbar button to add a new Step
- 0.3.0 - Implement Dialog Box to select Step Type
- 0.3.5 - Create Widget for HTTP Client
- 0.3.5 - Create Widget for SQL Client
- 0.3.5 - Implement functionality to show client based on the Step Type
- 0.3.5 - Bonus: Implement automated swapping between Step Type to detect any memory leaks
- 0.4.0 - Add toolbar button to view environments
- 0.4.0 - Implement Modal Dialog to work with environment
- 0.4.0 - Add support for adding/removing/duplicating environment from the Dialog
- 0.4.0 - Persist environments when closing the Dialog
- 0.4.0 - Add a toolbar combobox widget to show currently selected environment
- 0.4.0 - Save current environment in AppState

**Release 0.8.0**
- Implement functionality behind HTTP Client

**Release 0.9.0** 
- Implement functionality behind SQL Client

**Outstanding Tasks**
- Variables in Environment
- Using Variables in Steps
- Custom List Item Widget to Display Step 
- Load all steps from database on application start-up

## Release 2.0.0

- User should be able to format HTTP Request data (XML or JSON)
- User should be able to search for Steps
- User should be able to add Folders
- User should be able to Copy/Move Steps between Folders
- User should be able to see the last active folder on re-start (requires persistence)
- User should be able to see last active step on re-start (requires persistence)

## Release 3.0.0

- User should be able to define pre and post scripts using Python (default language selected in the combo box)
- User should be able to set context variables
- User should be able to use context variables in subsequent steps
- User should be able to write assertions

## Release 4.0.0

- User should be able to generate code using default templates
- User should be able to add a new template for a step
- User should be able to generate code for all the steps in the selected folder
- User should be able to generate code for all the steps filtered by the search query