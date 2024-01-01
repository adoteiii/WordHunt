# Word Hunt Solver with KivyMD

#### Video Demo: <https://youtu.be/I2sJlKjyYpQ>

#### Description:

Welcome to the Word Hunt Solver with KivyMD! This application is designed to assist users in solving Word Hunt puzzles by finding valid words within a grid of letters. Using the KivyMD framework, this solver provides a visually appealing and user-friendly interface. This README.md will guide you through the project.

### Kivy Imports

The project utilizes various modules from the Kivy and KivyMD libraries for creating the user interface and managing app behavior. Key imports include components for UI elements, layout, screen management, and clock scheduling.

### Other Module Imports

Custom modules such as iconbutton, tables, file_tree, and cardtextinput enhance the functionality and appearance of the application.

### Word Hunt Solver Components

The wordhuntanagram module provides core logic for solving Word Hunt puzzles, including classes for anagram generation (Anagram) and solving Word Hunt puzzles (WordHunt).

### KivyMD Layout Design

The layout is defined using the KivyMD language in the Builder.load_string section. It specifies the arrangement of widgets, their properties, and their interactions.

### SelectableRecycleBoxLayout and Row Classes

These classes define the behavior for selecting and interacting with rows in the application's recycle view.

### MainScreen Class

The MainScreen class is the main interface for the Word Hunt Solver, containing methods for adding tables, populating data, managing keyboard input, and controlling the flow of the application.

### Manager Class

The Manager class manages different screens within the application and currently includes only the MainScreen as the primary screen.

### WordGame Class (MDApp)

The WordGame class is the main application class, initializing the KivyMD theme, setting up the manager, and running the application.

## Design Choices

### KivyMD for UI Design

The use of KivyMD is a deliberate choice to create a modern and visually appealing user interface. It provides pre-built UI components and styles aligned with Material Design principles.

### Modular Code Structure

The project adopts a modular code structure using custom modules and organizing main functionality into distinct classes. This promotes code readability, maintainability, and ease of future enhancements.

### RecycleView for Word List Display

A RecycleView is employed to display the list of words, with the Row class defining the appearance and behavior of each row for user interaction.

### Dynamic Population of Word List

The populate method dynamically populates the word list based on the input grid, offering real-time feedback to the user.

### Keyboard Input Handling

The application efficiently handles keyboard inputs for left and right arrow keys, enabling users to navigate through the word list seamlessly.

## How to Run

To run the Word Hunt Solver with KivyMD, execute the WordGame class. Ensure that Kivy and KivyMD are installed in your Python environment.

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

Thank you for exploring the Word Hunt Solver with KivyMD. Feel free to reach out if you have any questions or feedback.

Happy word hunting!
