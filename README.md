## Flask Application Design for File Compare Web Application

### HTML Files
- **index.html**: The main HTML file that serves as the user interface. It should include a form for uploading two files and a button to initiate the comparison.
- **compare.html**: The HTML file that displays the results of the file comparison. It should include a tabular representation of the differences between the two files.

### Routes
- **index**: The route associated with the index.html file. It handles the GET request for the main page and renders the index.html template.
- **compare**: The route associated with the compare.html file. It handles the POST request from the index.html file, reads the uploaded files, compares them, and renders the compare.html template with the comparison results.