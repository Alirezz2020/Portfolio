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

    document.addEventListener("DOMContentLoaded", function () {
    let links = document.querySelectorAll(".page-scroll");
    links.forEach(link => {
    link.addEventListener("click", function (event) {
    event.preventDefault();
    let url = this.href;
    window.scrollTo({top: 0, behavior: 'smooth'});
    setTimeout(() => {window.location.href = url;}, 300);
});
});
});

document.addEventListener("DOMContentLoaded", function () {
    let fadeElements = document.querySelectorAll(".fade-in");

    function fadeInOnScroll() {
        fadeElements.forEach(element => {
            let position = element.getBoundingClientRect().top;
            let windowHeight = window.innerHeight;
            if (position < windowHeight - 50) {
                element.style.opacity = "1";
                element.style.transform = "translateY(0)";
            }
        });
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll();  // Run initially in case elements are already in view
});
