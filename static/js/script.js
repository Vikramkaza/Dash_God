/* script.js */

// Example of handling a button click event
document.getElementById('myButton').addEventListener('click', function() {
    alert('Button clicked!');
});

// Example of a function to show a success message
function showSuccessMessage(message) {
    var successDiv = document.createElement('div');
    successDiv.textContent = message;
    successDiv.classList.add('success-msg');

    document.body.appendChild(successDiv);

    // Automatically remove the message after 3 seconds
    setTimeout(function() {
        successDiv.remove();
    }, 3000);
}
