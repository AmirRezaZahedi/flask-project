const lamp = document.querySelector('.lamp');
        let isOn = false;
    
        lamp.addEventListener('click', function() {
          if (isOn) {
            document.body.style.transition = 'background-color 2s';
            document.body.style.backgroundColor = '#fff';
            isOn = false;
          } else {
            document.body.style.transition = 'background-color 2s';
            document.body.style.backgroundColor = '#ff00ff';
            isOn = true;
          }
        });
function rotateClockHands() {
    var now = new Date();
    var hour = now.getHours() % 12;
    var minute = now.getMinutes();
    var second = now.getSeconds();

    var hourRotation = (hour + minute / 60) * 30;
    var minuteRotation = (minute + second / 60) * 6;
    var secondRotation = second * 6;

    document.getElementById('hour-hand').style.transform = 'translate(-50%, -100%) rotate(' + hourRotation + 'deg)';
    document.getElementById('minute-hand').style.transform = 'translate(-50%, -100%) rotate(' + minuteRotation + 'deg)';
    document.getElementById('second-hand').style.transform = 'translate(-50%, -100%) rotate(' + secondRotation + 'deg)';
}
setInterval(rotateClockHands, 1000);

document.addEventListener('DOMContentLoaded', function() {
    fetch('/user_count') // Send a request to '/user_count' endpoint
        .then(response => response.json()) // Convert response to JSON format
        .then(data => {
            const userCountElement = document.getElementById('userCountNumber');
            userCountElement.textContent = data.userCount; // Set the element's content to the received user count
        })
        .catch(error => console.error(error));
});


