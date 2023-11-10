# Air Quality Information Web Application

## Team Name: IIT_codeGurus
### Team Members:
1. Rafid
2. Abir Ashab Niloy
3. Farhan Islam Shuvro

## Project Overview
The Air Quality Information Web Application is a web-based tool designed to provide real-time air quality data for cities around the world. The application is built using the Django web framework and utilizes the AirVisual API to fetch air quality information for different locations.

## Features

### 1. Get City List
- Users can input the state and country they are interested in.
- The application queries the AirVisual API to retrieve a list of cities in the specified state and country.
- Users can explore the list of cities with their names.

### 2. Interactive Map
- The "Go for Map" feature allows users to visualize air quality data on an interactive map.
- The map displays city markers, each with a color-coded representation of the Air Quality Index (AQI) value.
- Users can click on the markers to see detailed information about the city, including AQI, temperature, weather conditions, and more.

### 3. Detailed City Information
- Clicking on a city's name in the list or on the map redirects the user to a dedicated city information page.
- The city information page provides details such as:
  - Timestamp (ts)
  - Temperature (temp)
  - Weather conditions (weather)
  - Pollution levels (pollution)
  - Air Quality Index (AQI)
  - Air Quality Index Concentration (AQICN)

## System Requirements
- To run the Air Quality Information Web Application, you must have the following prerequisites installed:
  - Python
  - Django
  - Django Rest Framework

## How to Run the Application
To run the application on your local machine, follow these steps:

1. Open the project folder.
2. Navigate to the "apiproject" directory by `cd apiproject`.
3. Activate your virtual environment using the command specific to your virtual environment management.
   - Example: `...path...\draenv\Scripts\activate` for Windows.
4. Install Django and Django Rest Framework using the following commands:
    ```
    pip install django
    pip install djangorestframework
    ```
5. Start the Django development server with the following command:

## Usage Instructions
1. Launch a web browser and access the application at `http://localhost:8000/` (default URL for the Django development server).
2. Provide the state and country information.
3. Explore the list of cities in the specified region.
4. Click "Go for Map" to visualize the city data on the interactive map.
5. Click on city names in the list or on the map to access detailed information about each city.

## Conclusion
The Air Quality Information Web Application offers a user-friendly way to access real-time air quality data for different cities worldwide. It provides a visually appealing map and detailed information for each city, allowing users to make informed decisions based on air quality conditions. By following the provided instructions, users can run the application locally and explore air quality data for various locations. Please note that users are required to have Django and Django Rest Framework installed on their systems to run this application successfully. Feel free to customize this document to add any additional details or specific usage guidelines for your application.

## Targeted Prototype Link (Figma)
[Prototype](https://www.figma.com/proto/wC7zZfKiTu36lWqWHIme7x/IIT_codeGurus?type=design&node-id=57-1278&t=kaJ5xuVvXXYZ4dek-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=57%3A1278&mode=design)

## GitHub Repository Link
[GitHub Repository](https://github.com/Rafid13iit/IIT_Hackathon-ITverse23)
