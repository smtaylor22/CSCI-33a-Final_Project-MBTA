document.addEventListener('DOMContentLoaded', function() {
    
    getPrediction();

});

function formatTime(time) {
    const arrival = new Date(time);
    // Learned how to subtract time of two dates in Javascript here: https://bearnithi.com/2019/11/10/how-to-calculate-the-time-difference-days-hours-minutes-between-two-dates-in-javascript/
    const prediction = Math.abs(arrival) - Math.abs(new Date());
    const minutes = Math.floor(prediction/60000);
    return minutes;
}

function getPrediction() {
    // Send a GET request to the URL
    fetch('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-qamnl', 
          {headers: {"x-api-key": "315e0282ead3407f8610cfca7c1595bb"}})
    // Put response into json form
    .then(response => response.json())
    .then(data => {
        // Log data to the console
        const predictions = data.data.map(item => item.attributes.arrival_time);
        console.log(predictions)
        const time = predictions[0];

        const minutes = formatTime(time);
 
        // need way to pick the correct stop 
        document.querySelector('#prediction').innerHTML = minutes
    });

}