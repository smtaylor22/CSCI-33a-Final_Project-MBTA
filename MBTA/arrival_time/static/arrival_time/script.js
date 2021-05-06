document.addEventListener('DOMContentLoaded', function() {
    
    // Send a GET request to the URL
    fetch('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-qamnl')
    // Put response into json form
    .then(response => response.json())
    .then(data => {
        // Log data to the console
        console.log(data.data.map(item => item.attributes.arrival_time));
        const train = data.data[3];
        const time = train.attributes.arrival_time;
        const t = new Date(time);

        // Learned how to subtract time of two dates in Javascript here: https://bearnithi.com/2019/11/10/how-to-calculate-the-time-difference-days-hours-minutes-between-two-dates-in-javascript/
        const prediction = Math.abs(t) - Math.abs(new Date());
        console.log(t);
        console.log(prediction/60000);
        console.log(Math.floor(prediction/60000));
        console.log(data);

        
        document.querySelector('#arrival-time').innerHTML = time
    });

});