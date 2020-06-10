from PyQt5.QtCore import Qt

# Step List roles reserved between 100 - 200
STEP_LIST_TYPE_ROLE = Qt.UserRole + 100
STEP_LIST_OBJECT_ROLE = STEP_LIST_TYPE_ROLE + 1
STEP_LIST_ID_ROLE = STEP_LIST_TYPE_ROLE + 2

# Add additional different roles from + 200

AVAILABLE_STEPS = ["HTTP", "SQL"]
