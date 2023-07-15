from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_HOST = 'YOUR_RAPIDAPI_HOST'
RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'
RAPIDAPI_ENDPOINT = 'YOUR_RAPIDAPI_ENDPOINT_URL'

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id='YOUR_AUTH0_CLIENT_ID',
    client_secret='YOUR_AUTH0_CLIENT_SECRET',
    api_base_url='https://YOUR_AUTH0_DOMAIN',
    access_token_url='https://YOUR_AUTH0_DOMAIN/oauth/token',
    authorize_url='https://YOUR_AUTH0_DOMAIN/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

def create_user(email, password):
    # Auth0 Management API endpoint
    management_api_url = 'https://YOUR_AUTH0_DOMAIN/api/v2/users'

    # Auth0 Management API access token
    management_api_token = 'YOUR_AUTH0_MANAGEMENT_API_TOKEN'

    # Headers with the access token and content type
    headers = {
        'Authorization': 'Bearer ' + management_api_token,
        'Content-Type': 'application/json'
    }

    # User data to be sent in the request body
    user_data = {
        'email': email,
        'password': password,
        'connection': 'Username-Password-Authentication'
    }

    try:
        # Send a POST request to the Auth0 Management API to create a user
        response = requests.post(management_api_url, headers=headers, data=json.dumps(user_data))
        response.raise_for_status()
        
        # Return the created user information
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Error creating user: {e}')
        return None


# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve the user data from the request
    email = request.json.get('email')
    password = request.json.get('password')

    # Logic to create the user, e.g., store it in a database or perform any other action
    create_user(email, password)
    # Return a response indicating success or failure
    return jsonify({'success': True})  # Modify as needed

# Login route
@app.route('/login', methods=['POST'])
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:5000/callback')

@app.route('/callback')
def callback():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    # Process the user information and authenticate the user
    authenticated = True  # Placeholder logic, replace with actual authentication
    
    # Return a response indicating success or failure
    return jsonify({'success': authenticated})  # Modify as needed
      
@app.route('/posts')
def get_posts():
    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': RAPIDAPI_HOST
    }

    try:
        response = requests.get(RAPIDAPI_ENDPOINT, headers=headers)
        data = response.json()

        # Extract the relevant post information from the response data
        posts = []
        for item in data:
            title = item.get('title')
            content = item.get('content')
            post = {'title': title, 'content': content}
            posts.append(post)

        return jsonify(posts)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return jsonify([])

if __name__ == '__main__':
    app.run()
