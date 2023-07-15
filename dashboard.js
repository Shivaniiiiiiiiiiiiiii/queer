// Function to fetch and display posts
function loadPosts() {
  // Make a GET request to the Flask server to retrieve the posts data
  fetch('/posts')
    .then(response => response.json())
    .then(data => {
      // Get the posts container element
      const postsContainer = document.getElementById('posts-container');

      // Iterate over the posts data and create a post element for each post
      data.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('post');

        const titleElement = document.createElement('h3');
        titleElement.textContent = post.title;

        const contentElement = document.createElement('p');
        contentElement.textContent = post.content;

        postElement.appendChild(titleElement);
        postElement.appendChild(contentElement);

        postsContainer.appendChild(postElement);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

// Call the loadPosts function when the page is loaded
window.addEventListener('load', loadPosts);
