# 🐱🐭 Finding Cats and Mouse

## 📖 Overview
This is a Python program that determines which cat will reach the mouse first, based on their positions on a number line.  
- 🐱 If **Cat A** is closer → output `"Cat A"`  
- 🐱 If **Cat B** is closer → output `"Cat B"`  
- 🐭 If both cats are equally far → output `"Mouse C"` (since the mouse escapes).  

This is a classic **problem-solving exercise** often seen in coding challenges.

---

## 🛠️ Features
- 🔢 Takes positions of **Cat A**, **Cat B**, and **Mouse C** as input.  
- ⚡ Calculates which cat will catch the mouse first.  
- 🟰 Handles the tie case when both cats are at the same distance.  
- ✅ Input validation and error handling included.  
- 🔄 Runs multiple test cases until the user chooses to exit.

---

## 📂 Project Structure
cats-and-mouse/
│── cats_and_mouse.py # Main source code
│── README.md # Documentation
│── LICENSE # License file (MIT recommended)
│── .gitignore # Ignore unnecessary files


---

## 🚀 Getting Started
### ✅ Prerequisites
- Python 3.x installed on your system.

### ▶️ Running the Program
```bash
python cats_and_mouse.py

💻 Example Run
Enter the place of Cat A: 2
Enter the place of Cat B: 5
Enter the place of Mouse C: 4
Expecting Animal is: Cat B 

Do you want to try again? (y/n): y
Enter the place of Cat A: 3
Enter the place of Cat B: 6
Enter the place of Mouse C: 4
Expecting Animal is: Cat A 

Do you want to try again? (y/n): n
Exiting program. Goodbye!

📊 Explanation
--🐱 Cat A at position 2
--🐱 Cat B at position 5
--🐭 Mouse at position 4

📏 Distance from Cat A → |4 - 2| = 2
📏 Distance from Cat B → |5 - 4| = 1
✅ Cat B is closer → "Cat B"

🚧 Future Improvements
--🧪 Add unit tests for automated verification.
--🌍 Extend to 2D positions instead of just a number line.
--🖥️ Create a GUI version for visualization.

🤝 Author
--👨‍💻 A.G. Hasan Zarook
