# SURJO LIVE TCP BOT

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful TCP bot for Free Fire with advanced features including spam, lag attacks, ghost join, and more. Developed by SURJO LIVE GAMING.

## 🚀 Features

- **Advanced Spam Commands**: Message spam, request spam, custom spam
- **Lag Attacks**: Squad and private chat lag with auto-stop
- **Ghost Join**: Join and leave squads automatically
- **YouTube Info**: Fetch YouTube channel statistics
- **TikTok Info**: Get TikTok user information
- **Player Info**: Detailed player and guild information
- **Emote Hijack**: Send emotes in squads
- **Multi-join**: Join multiple squads simultaneously
- **Title System**: Convert and use custom titles
- **Region Support**: IND, BD, and other regions

## 📋 Requirements

- Python 3.8 or higher
- Internet connection
- Valid Free Fire account credentials

## 🔧 Installation

### Quick Setup (Recommended)

#### Windows
```bash
# Double-click setup.bat or run:
setup.bat
```

#### Linux/Termux
```bash
chmod +x install.sh
./install.sh
```

The setup scripts will automatically:
- Create a virtual environment
- Install all dependencies
- Configure the project for you

### Manual Setup

#### Windows Setup

1. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Clone the Repository**
   ```bash
   git clone https://github.com/SURJO99exe/tcp.git
   cd tcp
   ```

3. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Credentials**
   - Copy `SURJO LIVE.txt.example` to `SURJO LIVE.txt`
   - Add your UID and password in this format:
     ```
     YOUR_UID
     YOUR_PASSWORD
     ```

6. **Run the Bot**
   ```bash
   python main.py
   ```

#### Linux Setup

1. **Install Python and pip**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv -y
   ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/SURJO99exe/tcp.git
   cd tcp
   ```

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Credentials**
   - Copy `SURJO LIVE.txt.example` to `SURJO LIVE.txt`
   - Add your UID and password:
     ```
     YOUR_UID
     YOUR_PASSWORD
     ```

6. **Run the Bot**
   ```bash
   python3 main.py
   ```

#### Termux Setup

1. **Install Termux**
   - Download Termux from F-Droid (recommended) or Google Play Store
   - Update Termux packages:
     ```bash
     pkg update && pkg upgrade -y
     ```

2. **Install Python and Git**
   ```bash
   pkg install python git -y
   ```

3. **Clone the Repository**
   ```bash
   git clone https://github.com/SURJO99exe/tcp.git
   cd tcp
   ```

4. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure Credentials**
   - Copy `SURJO LIVE.txt.example` to `SURJO LIVE.txt`
   - Add your UID and password:
     ```
     YOUR_UID
     YOUR_PASSWORD
     ```

7. **Run the Bot**
   ```bash
   python main.py
   ```

## 📝 Configuration

### SURJO LIVE.txt

Create a file named `SURJO LIVE.txt` in the project directory with your credentials:

```
YOUR_UID_HERE
YOUR_PASSWORD_HERE
```

**Note**: Replace `YOUR_UID_HERE` with your Free Fire UID and `YOUR_PASSWORD_HERE` with your account password.

## 🎮 Commands

### Basic Commands
- `/help` - Show all available commands
- `/info` - Display bot information
- `/bio <text>` - Set your bio
- `/guild` - Get guild information

### Spam Commands
- `/spam` - Start message spam
- `/stopspam` - Stop message spam
- `/reqspam` - Start request spam
- `/customspam <message>` - Custom message spam

### Attack Commands
- `/lag <team_code>` - Lag attack on squad (auto-stop after 10 seconds)
- `/attack <target>` - Attack command (auto-stop after 1 second)
- `/ghost <player_id> <secret_code>` - Ghost join

### Information Commands
- `/yt <channel>` - Get YouTube channel info
- `/tt <username>` - Get TikTok user info
- `/player <uid>` - Get player information

### Squad Commands
- `/join <squad_code>` - Join a squad
- `/leave` - Leave current squad
- `/me <emote_key>` - Send emote in squad
- `/multijoin <code1> <code2> ...` - Join multiple squads

### Title Commands
- `/title <title_id>` - Use custom title
- `/convert <title_id>` - Convert title to your system

## 🔒 Security Notes

- Never share your `SURJO LIVE.txt` file with anyone
- Use a secondary account for bot operations
- The bot is for educational purposes only
- Misuse may result in account bans

## 🐛 Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError
```
Solution: Install all dependencies using pip install -r requirements.txt
```

**Issue**: Invalid credentials
```
Solution: Check your SURJO LIVE.txt file and ensure UID and password are correct
```

**Issue**: Connection timeout
```
Solution: Check your internet connection and try again
```

**Issue**: Python not found
```
Solution: Ensure Python is installed and added to PATH (Windows) or use python3 (Linux/Termux)
```

## 📞 Support

- **Telegram**: @SURJO_LIVE
- **YouTube**: SURJO LIVE GAMING
- **GitHub**: https://github.com/SURJO99exe/tcp

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This bot is for educational purposes only. The developers are not responsible for any misuse of this software. Use at your own risk.

## 🙏 Credits

- **Developer**: SURJO LIVE GAMING
- **Modified by**: SURJO LIVE
- **Original Creator**: Black666FF

---

**Enjoy the bot! Contact us for any issues or suggestions.**
