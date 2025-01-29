// Smooth Scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Example of a simple form validation
document.querySelector('form').addEventListener('submit', function (event) {
    let isValid = true;
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    if (!name || !email || !message) {
        isValid = false;
        alert('Please fill out all fields.');
    }

    if (!isValid) {
        event.preventDefault();
    }
});
