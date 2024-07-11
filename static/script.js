const api_key = "Your api key";


function validateForm() {
  var x = document.getElementById("city-input").value;
  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${x}&appid=${api_key}`)
      .then(response => {
          if (!response.ok) {
              alert("Location not found");
              return false;
          } else {
              document.getElementsByClassName('find-location')[0].submit();
              return true;
          }
      })
      .catch(error => {
          console.error('Error:', error);
          return false;
      });
  return false;  // Prevent form submission until fetch completes
}
