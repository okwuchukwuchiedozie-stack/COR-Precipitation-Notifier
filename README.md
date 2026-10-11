# ⛈️ COR-Precipitation-Notifier (Automated Status Engine)

An optimized, production-ready backend script built in Python that dynamically monitors precipitation trajectories using the **OpenWeatherMap 5-Day Forecast API**. 

If automated precipitation identifiers are logged within the upcoming 12-hour horizon, the script securely triggers the **Twilio API for WhatsApp** to deploy an immediate alert notification directly to your verified mobile device. It features integrated, timezone-aware console telemetry and a defensive request firewall.

---

## 🛠️ Key Architectural Layout & Enhancements

- **Defensive Request Firewall:** Protects the main runtime process by trapping structural network failures (`requests.RequestException`) inside localized `try-except` containment shells to keep the script from hard crashing if connection signals fail.
- **Active Real-Time Telemetry Tracking:** Introduces an isolated telemetry tracking variable (`worst_condition_code = 900`) that processes the entire payload matrix array to find and expose the highest-risk weather code configuration.
- **Bi-Directional Status Logs:** Adds a responsive console logging interface. When conditions are clear, it outputs a clean, real-time timestamp confirmation message rather than running completely silent, confirming the system is actively monitoring.
- **Explicit Horizon Optimization:** Sets tight API query thresholds (`"cnt": 4`) to parse precisely the upcoming 12-hour forecast sequence (four discrete 3-hour chunks) for resource conservation.

---

## 📦 System Dependencies

- **requests:** Manages structural HTTP packet routing data pipelines to meteorology servers.
- **twilio:** Provides connectivity configurations directly to Twilio's WhatsApp delivery matrix nodes.
- **python-dotenv:** Processes hidden keys and coordinates straight from the environment scope layer.

Initialize these baseline dependencies using your terminal workspace prompt tool:
```bash
pip install -r requirements.txt
```

---

## 🚀 Rapid Initial Configuration Setup

### 1. Build Local Hidden Variables (`.env`)
Create a file named precisely `.env` in the root folder of your project and drop your unique parameter settings inside:
```text
# OpenWeatherMap Security Access Tokens
API_KEY=your_openweathermap_api_key_string

# Twilio Security Authentication Identifiers
ACCOUNT_SID=your_twilio_account_sid_string
AUTH_TOKEN=your_twilio_auth_token_string

# Phone Destination Mapping Configuration Profile
TWILIO_WHATSAPP_NUMBER=+14155238886
MY_TWILIO_VERIFIED_NUMBER=+234XXXXXXXXXX
```

### 2. Lock Public Version Tracks (`.gitignore`)
Ensure your private data sets never leak onto public platforms by appending these files into a `.gitignore` container tracking block:
```text
.env
__pycache__/
*.pyc
.idea/
.venv/
```

### 3. Launch the Telemetry Monitors
Fire up the updated tracking loop directly inside your computer shell environment:
```bash
python main.py
```

---

## ⚖️ License
Distributed under the custom **COR_CARES** Development Framework. Copyright &copy; 2026. All rights reserved.
