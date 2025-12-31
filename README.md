# Caesar Cipher 🔐

My take on Caesar cipher - works on ALL characters (letters + symbols) using custom math I figured out.

## Demo

Do you want to Encrypt(e) or Decrypt(d) the message (q to quit) ? : e
Message to be Encrypted: Anirud Here
Enter key (Intiger only) : 31
Encrypted message: ***`.)25$?g%2%***
Do you want to Encrypt(e) or Decrypt(d) the message (q to quit) ? : d
Message to be Dencrypted: `.)25$?g%2%
Enter key (Intiger only) : 31
Decrypted message: ***Anirud Here***
Do you want to Encrypt(e) or Decrypt(d) the message (q to quit) ? : q
Bye!


## How It Works

- ((ord(char) - 32 + key) % 95) + 32
- 32 = start of printable chars (space)
- %95 = wraps z→space→A (no weird symbols!)
- Handles spaces, punctuation, everything


## Features

- User picks any integer key (positive/negative)
- `try/except` for invalid key inputs
- Separate encrypt/decrypt modes
- Modular functions + clean main loop
- Quit anytime with 'q'


## Tech I Used

- Custom ASCII math (no string.ascii_lowercase)
- List comprehensions: `[ord(char) for char in msg]`
- `chr()` + `ord()` conversion
- Multiple return values from functions
