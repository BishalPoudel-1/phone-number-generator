# 📞 Phone Number Generator

This Python script generates a list of phone numbers based on user input and saves them to a `.txt` file.

---

## 🚀 Features

* Generate phone numbers with a specified range of digits (min and max).
* Define the starting digit(s) of all phone numbers.
* Save the output to a custom file.
* Auto-generates all possible phone numbers starting with the specified digit(s) and within the digit range.

---

## 📂 How It Works

1. The user inputs:

   * Minimum number of digits (e.g., 7)
   * Maximum number of digits (e.g., 10)
   * Starting digit(s) for the phone number (e.g., 9)
   * Filename (without extension)

2. The script:

   * Starts generating numbers that begin with the specified digit.
   * Ensures that numbers don't exceed the maximum length.
   * Stops once the next generated number no longer begins with the given starting digit.
   * Saves all valid phone numbers in a `.txt` file named `{filename}phonenumber.txt`.

---

## 📝 Example Input

```bash
Enter the minimum Digits: 7  
Enter the maximum Digits: 10  
Enter the Starting Digit of Phone Number: 9  
Enter the filename: phone_list  
```

### 🧾 Output

* The script will generate numbers like:

  ```
  9000000
  9000001
  9000002
  ...
  ```
* These will be saved in `phone_listphonenumber.txt`.

---

## 💡 Notes

* The script generates sequential phone numbers starting from the smallest number that fits the starting digit and digit length.
* It stops automatically when the phone number no longer starts with the specified digit(s).

---

## 🛠 Requirements

* Python 3

---

## 🔄 Future Improvements

* Add an option to generate random numbers.
* Allow formatting (e.g., `(XXX) XXX-XXXX`).
* Add CLI options instead of input prompts.

---

## 📃 License

This script is provided as-is. You are free to use, modify, and distribute it.

---
