import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch data from API
API_KEY = "acffc0454e0096c2c401605fd8951bc4"  # Replace this with your real API key
CITY = "indore"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Step 2: Extract temperature data
dates = []
temperatures = []

for item in data['list']:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])

# Step 3: Plot the data
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='blue')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
