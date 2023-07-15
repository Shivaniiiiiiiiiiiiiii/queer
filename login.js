// Function to handle login
function login() {
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  // Make a POST request to the Flask server to authenticate the user
  fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email: email, password: password })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Login successful!');
      // Redirect or perform any other action after successful login
    } else {
      alert('Login failed. Please try again.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred. Please try again.');
  });
}
