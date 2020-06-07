Here is a rough implementation plan for Orkestra with backlog

## Release 1.0.0 (Active - Tracked in Github Issues)

**Milestones**

- Load AppState on Application Start-Up
- Load Folders on Application Start-Up
- Create Default Folder if it doesn't exist
- Add toolbar button to add a new Step
- Implement Dialog Box to select Step Type
- Add toolbar button to view environments
- Implement Modal Dialog to work with environment
- Add support for adding/removing/duplicating environment from the Dialog
- Persist environments when closing the Dialog
- Add a toolbar combobox widget to show currently selected environment
- Save current environment in AppState


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