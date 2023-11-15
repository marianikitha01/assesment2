# Assessment with backend

This Flask application initializes Stanza for text processing and provides a simple web interface to input text for processing.

app.py: Contains the Flask routes for rendering the HTML template and processing the entered text.

assesment.html: HTML template for the user interface.

Routes

/process_text: Accepts a POST request with JSON containing the user text(address), processes it using Stanza, and returns the processed data.

Address field from the form is used for processing.

## Screenshots

![form_details](https://github.com/marianikitha01/assesment2/blob/main/images/form_details.png)
**This is a screenshot showcasing the form filled with details.**

![processed_text](https://github.com/marianikitha01/assesment2/blob/main/images/processed_text.png)
**This is a screenshot showcasing the form details in Network possted using POST menthod**

![processed_data](https://github.com/marianikitha01/assesment2/blob/main/images/processed_text.png)
**This is a screenshot showcasing the processed data in the console.**
