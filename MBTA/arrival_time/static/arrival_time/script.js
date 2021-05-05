document.addEventListener('DOMContentLoaded', function() {
    
    // Send a GET request to the URL
    fetch('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-qamnl')
    // Put response into json form
    .then(response => response.json())
    .then(data => {
        // Log data to the console
        console.log(data);
        const test = data.data.attributes;
        console.log(test);
    });

});