let closed_form = false;

document.getElementById("openFormBtn").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "block";
});

document.getElementById("closeFormBtn").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "none";
    closed_form = true;
});

document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Serialize form data into JSON format
    const formData = new FormData(this);
    const formDataJson = {};
    formData.forEach((value, key) => {
        formDataJson[key] = value;
    });
    console.log(formDataJson);

    // Extract the dynamic part of the URL
    const dynamicPart = window.location.pathname.match(/\/(\d+)\/$/)[1]; // Extracts '20' from '/detalles/20/'

    // Construct the API URL with the dynamic part
    const apiUrl = '/detalles/' + dynamicPart + '/';

    // Send form data to server using Fetch API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Add any additional headers if needed (e.g., CSRF token)
        },
        body: JSON.stringify(formDataJson),
    })
    .then(response => {
        if (response.ok) {
            // Handle successful form submission
            closed_form = false;
            document.getElementById("popupForm").style.display = "none"; // Hide the form after successful submission
        } else {
            // Handle error response from server
            closed_form = false;
            alert("Error submitting form. Please try again.");
        }
    })
    .catch(error => {
        // Handle fetch error
        console.error('Error:', error);
        alert("An error occurred while submitting the form. Please try again later.");
    });
});