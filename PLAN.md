Here is a rough implementation plan for Orkestra with backlog

## Release 1.0.0 (Active - Tracked in Github Issues)

**Milestones**

- 0.1.0 - Load AppState on Application Start-Up
- 0.2.0 - Load Folders on Application Start-Up
- 0.2.0 - Create Default Folder if it doesn't exist
- 0.3.0 - Create a new step - https://github.com/namuan/orkestra/issues/10
- 0.3.5 - Swap between steps - https://github.com/namuan/orkestra/issues/4
- 0.4.0 - Environments - https://github.com/namuan/orkestra/issues/5
- 0.5.0 - Variables in Environment - https://github.com/namuan/orkestra/issues/6
- 0.6.0 - Try Layout switching with QStackedWidget
- 0.6.0 - _Welcome Screen_ Setup Default Actions if no steps are currently added
- 0.6.0 - Load all steps from database on application start-up
- 0.6.0 - Custom List Item Widget to Display Step
- 0.7.0 - Implement functionality behind HTTP Client
- 0.8.0 - Implement functionality behind SQL Client
- 0.9.0 - Using Variables in Steps
- 0.9.0 - Hide/Disable "Add New" button if no environments present 
- 1.0.0 - Release Prep

**Outstanding Tasks**

- Prepare setup for Mac Release
 -- Icon
 -- WebPage on DeskRiders
 -- Mac Release
 -- Windows Release

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