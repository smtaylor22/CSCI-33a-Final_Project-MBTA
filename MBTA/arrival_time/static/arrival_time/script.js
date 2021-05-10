let stopID = null;
// Sample urls 
let urls = [('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-qamnl'),
 ('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-pktrm'),
  ('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-haecl')];

document.addEventListener('DOMContentLoaded', function() {
    
    const stops = document.querySelectorAll(".arrival-time");
    stops.forEach(stopID => getPrediction(stopID.dataset.stop));
    
    


    //console.log(stopID);
    //const element = document.querySelector(`.arrival-time[data-message="${stopID}"]`);
    //document.querySelectorAll('.arrival-time').forEach(element => getPrediction();
    

});





// Computes the time difference between now and the vehicle's predicted arrival time  
// Formats time values from milliseconds to minutes
function formatTime(time) {
    const arrival = new Date(time);
    // Learned how to subtract time of two dates in Javascript here: https://bearnithi.com/2019/11/10/how-to-calculate-the-time-difference-days-hours-minutes-between-two-dates-in-javascript/
    const prediction = Math.abs(arrival) - Math.abs(new Date());
    const minutes = Math.floor(prediction/60000);
    if (minutes <= 0) {
        addElement(0);
    }
    else {
        addElement(minutes);
    }
    
}

function getPrediction(stop) {
    stopID = stop;
    //console.log(stopID);
    //urls.push('https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-qamnl', {headers: {"x-api-key": "315e0282ead3407f8610cfca7c1595bb"}});
    // Send a GET request to the MBTA API route
    Promise.all(urls.map(url =>
        fetch(url)

                 
        .then(response => response.json())

        ))
        .then(data => {
            // Format the object data structure to select the predicted arrival_time attribute
            // Take only the first 4 
            const predictions = data.forEach(element => element.data.map(item => item.attributes.arrival_time).slice(0, 4));
        
            // Format the predicted time to minutes 
            predictions.forEach(item => formatTime(item));

    
        });

}

// Add the predicted time element to the HTML DOM 
function addElement(minutes) {
    //console.log(stopID);
    const element = document.createElement('div');
    element.innerHTML = `${minutes} minutes`;
    document.querySelector(`.arrival-time[data-stop="${stopID}"]`).appendChild(element);

    //document.querySelector('#prediction').appendChild(element)
}

