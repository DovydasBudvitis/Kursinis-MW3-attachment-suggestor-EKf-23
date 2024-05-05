# Kursinis MW3 attachment suggestor EKf-23
MW3 Attachment Suggestor is a Python application designed to suggest weapon attachments for players of the game Call of Duty: Modern Warfare 3 (MW3). This application provides a user-friendly interface for selecting playstyles and weapons, then generates attachment suggestions based on the user's choices.

INTRODUCTION

Features
   Allows users to select from various playstyles, including close-range, long-range, sniper-support, sniper, and all-rounder.
   Provides a wide selection of primary weapons from MW3 for users to choose from.
   Suggests attachments based on the selected playstyle and weapon.
   Offers the option to save attachment suggestions to a file for future reference.

How to Run the Program
  To run the MW3 Attachment Suggestor, follow these steps:

    1. Ensure you have Python installed on your system.
    2. Clone or download the repository to your local machine.
    3. Navigate to the directory containing the MW3_Attachment_Suggestor.py file.
    4. Open a terminal or command prompt in that directory.
    5. Run the following command:
    ![image](https://github.com/DovydasBudvitis/Kursinis-MW3-attachment-suggestor-EKf-23/assets/168678893/8d57eaae-52a3-46fc-ae46-49f79f959c31)
    6. The application window will open, allowing you to interact with the MW3 Attachment Suggestor.

How to Use the Program
   1. Upon launching the application, you will see options to select your preferred playstyle and weapon.
   2. Choose your desired playstyle and weapon from the available lists.
   3. Click the "Select" button next to each selection to confirm your choices.
   4. Once both a playstyle and weapon are selected, click the "Submit" button to view attachment suggestions.
   5. A new window will display the selected playstyle, weapon, and suggested attachments.
   6. You can click the "Resuggest" button to generate new attachment suggestions or click "Save to File" to save the suggestions to a text file.

BODY/ANALYSIS

Object-Oriented Programming Pillars:
1. Polymorphism:
     Definition: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the same method name to be used for different classes, providing flexibility and extensibility.
     Usage in Code: In the provided code, polymorphism is utilized through method overriding. Subclasses of `AttachmentSuggestorBase` such as `MW3AttachmentSuggestor` override the `create_widgets()` and `open_new_window()` methods to provide specific implementations while still adhering to the base class interface.
   ![image](https://github.com/DovydasBudvitis/Kursinis-MW3-attachment-suggestor-EKf-23/assets/168678893/a16b3a20-d9ed-4c75-a2b6-4f56bdd92f73)
3. Abstraction:
     Definition: Abstraction refers to hiding the complex implementation details and showing only the necessary features of an object. It allows developers to focus on the essential aspects of an object without worrying about its internal workings.
     Usage in Code: The `AttachmentSuggestorBase` class serves as an abstraction by defining methods like `create_widgets()` and `open_new_window()` without specifying their implementations. Subclasses are responsible for providing concrete implementations, allowing the base class to be used as a template for different attachment suggestor applications.
   ![image](https://github.com/DovydasBudvitis/Kursinis-MW3-attachment-suggestor-EKf-23/assets/168678893/3a29f0d7-a22d-4202-a44c-5a506701ab35)
3. Inheritance:
     Definition: Inheritance is a mechanism where a new class inherits properties and behaviours from an existing class. It promotes code reusability and establishes a hierarchical relationship between classes.
     Usage in Code: The `MW3AttachmentSuggestor` class inherits from the `AttachmentSuggestorBase` class, acquiring its attributes and methods. This inheritance allows `MW3AttachmentSuggestor` to leverage the common functionality defined in `AttachmentSuggestorBase` while providing specific features tailored to MW3 attachment suggestion.
   ![image](https://github.com/DovydasBudvitis/Kursinis-MW3-attachment-suggestor-EKf-23/assets/168678893/4d448080-efe3-4fca-8aad-d8f8db3e6d1a)
5. Encapsulation:
     Definition: Encapsulation is the bundling of data and methods that operate on the data into a single unit, known as a class. It restricts direct access to the internal state of an object and only allows interaction through well-defined interfaces.
     Usage in Code: Encapsulation is demonstrated in the code by encapsulating data such as selected playstyle, selected weapon, and attachments within the `AttachmentSuggestorBase` class. These attributes are accessed and modified through getter methods (`selected_playstyle`, `selected_weapon`, `attachments`), enforcing encapsulation principles and maintaining data integrity.
   ![image](https://github.com/DovydasBudvitis/Kursinis-MW3-attachment-suggestor-EKf-23/assets/168678893/bfd95b3b-516d-477f-aee3-76a41c4a778e)

Design Patterns:
1. Factory Method Pattern:
    Explanation: The Factory Method Pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It promotes loose coupling by decoupling the object creation logic from the client code.
    Usage in Code: The `GUIElementFactory` class serves as a factory for creating GUI elements such as labels, buttons, and listboxes. It encapsulates the creation logic within factory methods (`create_label`, `create_button`, `create_listbox`), allowing subclasses to provide customized implementations if necessary.
2. Singleton Pattern:
    Explanation: The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance. It is useful in scenarios where a single, shared resource needs to be accessed from multiple parts of the program.
    Usage in Code: While the Singleton Pattern is not explicitly implemented in the provided code, it could be applied to manage global resources such as the `AttachmentSuggestion` class instance. By restricting instantiation to a single object and providing a static method to access it, the Singleton Pattern could ensure consistent attachment suggestion functionality across the application.

File Input/Output:
1. Reading from File: The program can incorporate file reading functionality to import data such as weapon configurations or user preferences. This data could be used to customize the attachment suggestion process or pre-populate GUI elements.
2. Writing to File: After generating attachment suggestions, the program can save the results to a file for future reference. This file could contain details about the selected playstyle, weapon, and suggested attachments, facilitating data persistence and analysis.

Results:
  1. The implementation of the MW3 Attachment Suggestor program provides a user-friendly interface for players to receive attachment suggestions based on their selected playstyle and weapon.
  2. Challenges were encountered during the integration of the GUI elements with the backend attachment suggestion logic, particularly in ensuring seamless communication between different components of the application.
Conclusions:
  1. This coursework has successfully achieved the objective of creating a functional attachment suggestion tool for MW3 players, enhancing their gaming experience.
  2. The program's result is a robust application that facilitates the selection of optimal attachments, thereby aiding players in improving their in-game performance.
  3. Future prospects of the program include potential enhancements such as incorporating more advanced attachment suggestion algorithms, expanding the range of supported playstyles and weapons and improving the user interface for better usability and aesthetics.



