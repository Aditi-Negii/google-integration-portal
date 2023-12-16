# Your Project Name

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd your_project_directory
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate      # For Linux/Mac
    # OR
    .\venv\Scripts\activate       # For Windows
    ```

3. **Install dependencies:**
    ```bash
    # Install Flask dependencies
    pip install -r requirements.txt

    # Install React dependencies
    cd react_app
    npm install
    ```

4. **Set up Google OAuth 2.0 credentials:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - Confugure the OAuth screen
    - Navigate to the "Credentials" page.
    - Create a new OAuth client ID.
    - Insert "https://google-reviews-portal-02b7446f7592.herokuapp.com/" url.
    - Copy the client ID.

5. **Configure OAuth client ID in the project:**
    - Open `react_app/src/index.js` in your code editor.
    - Locate the section where you set the client ID.
    - Replace the existing client ID with the one you obtained from the Google Cloud Console.
      
6. **Add your client ID to project:**
    - Navigate to project-root/client/src/index.js.
    - Replace the client ID with your client ID.

8. **Run the project:**
    ```bash
    # Start Flask app
    python your_flask_app.py

    # Start React app (in a separate terminal)
    cd react_app
    npm start
    ```

7. **Open your browser and navigate to [http://localhost:3000](http://localhost:3000).**

8. **Heroku Deployment:**
    - The website is deployed on Heroku. You can access it [https://google-reviews-portal-02b7446f7592.herokuapp.com/](https://google-reviews-portal-02b7446f7592.herokuapp.com/).



