🎈 Alphabet Balloon Pop Game
Built with Gemini AI & Reflex (Python)
An interactive, educational web game designed for kids to learn the alphabet through real-time play. This project demonstrates a successful Human-AI Collaboration, using Google Gemini to architect the state logic and Reflex to deploy a full-stack application entirely in Python.

🤖 AI-Assisted Development
This application was developed in partnership with Gemini. The development process focused on:

Prompt Engineering: Iteratively refining game mechanics and UI requirements.

Problem Solving: Using AI to bridge the gap between Python backend logic and browser-level JavaScript audio triggers.

Rapid Prototyping: Moving from a basic script to a cloud-deployed game with custom assets in a single session.

🚀 Technical Features
Global Keyboard Listener: A "hidden input" strategy to capture keystrokes anywhere on the screen.

Synchronized Audio: Zero-latency sound effects (clapping and oops) managed via a custom JS-bridge.

Async Animations: Utilizing asyncio for smooth, timed "pop" transitions and state resets.

Focus Management: Automatic re-focusing of the input field after game resets for uninterrupted play.

🛠️ Tech Stack
Language: Python 3.13

Framework: Reflex (Full-stack Web)

AI Collaborator: Google Gemini

Deployment: Reflex Cloud

🎮 How to Play
Launch the game and click anywhere on the "sky" to activate the listener.

Type the letter shown inside the balloon.

Pop it! Watch the score go up and enjoy the clapping sound.

Hit "Restart" at any time to clear your score and start fresh.

📦 Installation
Bash
# Clone the repository
git clone https://github.com/dilmilsoach/balloon-pop-game.git

# Install dependencies
pip install -r requirements.txt

# Run the app
reflex run

📜 License
Distributed under the MIT License.

👤 Author
Dilmil Singh Soach
IRS Officer | Master's Student at Dalhousie University
