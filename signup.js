// Function to handle signup
function signup() {
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  // Make a POST request to the Flask server to create a new user
  fetch('/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email: email, password: password })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Signup successful!');
      // Redirect or perform any other action after successful signup
    } else {
      alert('Signup failed. Please try again.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred. Please try again.');
  });
}
