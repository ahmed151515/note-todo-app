# Note & Todo Application

## Overview
A desktop application built with Python and Tkinter that provides an efficient way to manage both notes and todos. The application features a modern tab-based interface allowing users to seamlessly switch between managing notes and todos.

## User Stories

### Note Management
1. As a user, I want to create new notes with titles and content so that I can save important information
2. As a user, I want to view all my saved notes in one place so I can easily find my information
3. As a user, I want to edit existing notes so I can update their content when needed


### Todo Management
1. As a user, I want to create todo items with descriptions so I can track my tasks
2. As a user, I want to view all my todos in a list so I can see what needs to be done
3. As a user, I want to edit my todos so I can update task details

## Requirements

### Functional Requirements

#### Note Features
- System shall allow users to create new notes with titles and descriptions
- System shall display all saved notes in an organized view
- System shall provide functionality to edit existing notes
- System shall load all saved notes when application starts

#### Todo Features
- System shall allow users to create new todo items
- System shall display all todos in a list format
- System shall provide functionality to edit existing todos
- System shall load all saved todos when application starts

### Non-Functional Requirements

#### Performance
- Application shall start up in less than 3 seconds
- All save operations shall complete in less than 1 second
- UI interactions shall respond within 0.5 seconds

#### Usability
- Interface shall be intuitive and easy to navigate
- Application shall provide clear feedback for user actions
- Tab-based navigation shall be clearly visible
- Text input areas shall be appropriately sized for content



## Features

### Notes Management
- Create and store notes with titles and descriptions
- View all saved notes in an organized interface
- Edit existing notes
- Persistent storage of notes using JSON

### Todo Management
- Create todo items with titles and descriptions
- View and manage your todo list
- Edit existing todos
- Data persistence using JSON storage

## Technical Details

### Technologies Used
- Python 3.x
- Tkinter (GUI Framework)
- JSON (Data Storage)

### Project Structure
```
note-todo-app/
├── classes/
│   ├── addNote.py      # Handles adding new notes
│   ├── addTodo.py      # Handles adding new todos
│   ├── main.py         # Application entry point
│   ├── note.py         # Note data model
│   ├── noteHomePage.py # Notes main interface
│   ├── todo.py         # Todo data model
│   ├── todoHomePage.py # Todos main interface
│   ├── note.json       # Notes storage
│   └── todo.json       # Todos storage
```

### Key Components
- `MainGui`: Main application window with tab control
- `Note`: Data model for notes management
- `Todo`: Data model for todos management
- `noteHomePage`: UI for notes display and management
- `todoHomePage`: UI for todos display and management

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- Tkinter (usually comes with Python)

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Run the application:
   ```bash
   python classes/main.py
   ```

### Usage
1. Launch the application
2. Use the tabs at the top to switch between Notes and Todos
3. Add new items using the appropriate interface
4. Edit or view existing items as needed
5. All data is automatically saved when closing the application

## Data Storage
- Notes and todos are stored in separate JSON files
- Data is automatically loaded when starting the application
- Changes are saved automatically when closing the application

## Contributing
Feel free to fork the project and submit pull requests for any improvements.
