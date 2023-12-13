

The provided Flask-based code creates a dynamic web application showcasing earthquake data via various interactive visualizations and informational sections. It employs Flask, Pandas, Chart.js, and HTML/CSS to produce a comprehensive webpage.

#Imports and Setup: 
Essential libraries such as Flask, render_template_string, and pandas are imported to establish the Flask application instance.

#Earthquake Data: 
Sample earthquake data comprising date, time, magnitude, depth, and epicenter is structured within a list of dictionaries named earthquake_data.

#Locations Affected by the Earthquake:
Lists including jaipur_locations, surrounding_locations, and near_jaipur_locations contain affected location names.

#Pandas DataFrame Creation:
The earthquake_data is transformed into a Pandas DataFrame (df) for better manipulation and utilization within the Flask app.

#Flask Routes:
The application defines a route ('/') managed by the index() function, rendering an HTML template via render_template_string.

#HTML Template:
The template comprises:

#Header Section:
Displays basic information and social media links.


Chart Sections: Utilizes Chart.js to create Bar, Line, and Pie charts, visualizing earthquake magnitude, depth, and distribution across different locations.
Affected Areas Section: Lists impacted areas based on predefined locations.
Earthquake Impact Information Section: Presents a table and details about the earthquake impact.
Footer Section: Contains contact details and social media links.
Chart.js Script: Embedded JavaScript initializes Chart.js, configuring chart data (magnitude, depth, distribution) within the HTML template.

Header Visibility Toggle: Additional JavaScript is included to manage header visibility on scroll, toggling based on scrolling direction.

Flask App Execution: The script verifies if the current file is being run directly and initiates the Flask app in debug mode if true.

In summary, this code amalgamates various technologies to deliver an engaging web interface that effectively communicates earthquake data through graphical representations and informative sections.
