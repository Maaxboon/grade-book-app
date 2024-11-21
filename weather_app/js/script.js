const apiKey = "62ca33fbf36e0cbcf1ef51a1e098b5a3";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather";

function WeatherApp() {
  const [location, setLocation] = React.useState("");
  const [weatherData, setWeatherData] = React.useState(null);
  const [unit, setUnit] = React.useState("metric");
  const [error, setError] = React.useState(null);
  const [localTime, setLocalTime] = React.useState("");

  const fetchWeather = async () => {
    if (!location.trim()) return;

    try {
      const response = await fetch(
        `${apiUrl}?q=${location}&appid=${apiKey}&units=${unit}`
      );
      const data = await response.json();

      if (response.ok) {
        setWeatherData(data);
        setError(null);
        calculateLocalTime(data.timezone); // Calculate local time for the city
      } else {
        setWeatherData(null);
        setError(data.message || "City not found.");
        setLocalTime("");
      }
    } catch (err) {
      setError("Failed to fetch weather data. Try again later.");
      setWeatherData(null);
      setLocalTime("");
    }
  };

  const toggleUnit = () => {
    setUnit((prev) => (prev === "metric" ? "imperial" : "metric"));
  };

  const calculateLocalTime = (timezoneOffset) => {
    const now = new Date();
    const utcTime = now.getTime() + now.getTimezoneOffset() * 60000; // Convert current time to UTC
    const localTime = new Date(utcTime + timezoneOffset * 1000); // Add city's timezone offset
    const gmtOffset = timezoneOffset / 3600; // Convert offset from seconds to hours

    // Format time and offset
    const timeString = localTime.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      hour12: true,
    });
    const offsetString =
      gmtOffset >= 0 ? `GMT +${gmtOffset}` : `GMT ${gmtOffset}`;

    setLocalTime(`${timeString} (${offsetString})`);
  };

  return (
    <div className="container">
      <h1>Weather App</h1>
      <input
        type="text"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        placeholder="Enter a city"
      />
      <button onClick={fetchWeather}>Search</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {weatherData && (
        <div className="weather-info">
          <h2>{weatherData.name}</h2>
          <p>Local Time: {localTime}</p>
          <p>
            Temperature: {Math.round(weatherData.main.temp)}
            {unit === "metric" ? "°C" : "°F"}
          </p>
          <p>Condition: {weatherData.weather[0].description}</p>
          <p>Humidity: {weatherData.main.humidity}%</p>
          <p>
            Wind Speed: {weatherData.wind.speed}{" "}
            {unit === "metric" ? "m/s" : "mph"}
          </p>
          <p className="unit-toggle" onClick={toggleUnit}>
            Switch to {unit === "metric" ? "Fahrenheit" : "Celsius"}
          </p>
        </div>
      )}
    </div>
  );
}

ReactDOM.render(<WeatherApp />, document.getElementById("root"));
