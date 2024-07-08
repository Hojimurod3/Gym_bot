Certainly! Here's a template for the README.md file in English:

---

# Telegram Gym Bot

Telegram Gym Bot is a simple bot that allows users to get information about different workouts categorized by weight. Users can select a weight category and receive details about the workout intensity, duration, and description.

## Features

- **Start Command**: Initiates the bot and presents a list of weight categories as clickable buttons.
- **Interactive Buttons**: Users can click on a weight category to receive detailed information about the workout associated with that category.
- **API Integration**: The bot integrates with an external API (`API_URL`) to fetch workout data dynamically.

## Technologies Used

- Python
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Python library for interacting with the Telegram Bot API.
- [requests](https://docs.python-requests.org/en/latest/): Python library for making HTTP requests.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/telegram-gym-bot.git
   cd telegram-gym-bot
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**

   - Replace `YOUR_TELEGRAM_BOT_TOKEN` in `main.py` with your actual Telegram bot token.
   - Ensure the `API_URL` in `main.py` points to the correct API endpoint providing workout data.

4. **Run the bot:**

   ```bash
   python main.py
   ```

## Usage

- Start the bot by sending the `/start` command to the bot in your Telegram chat.
- Click on the weight category buttons to receive detailed workout information.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the sections and details based on your specific implementation and preferences.
