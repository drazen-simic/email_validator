# email_validator
Python code for validation email adresses

User Input Validation for Email Address

Write a Python program that performs the following tasks:

User Email Input:

The program prompts the user to enter an email address using the input() function.

Using split and lower functions:

Converts the entered email to lowercase using lower().

Checks if the email contains exactly one '@' sign, then splits the email into two parts (username and domain) using split('@').

Regex Validation:

Validates the format of the username and domain using regex:

Username: Can contain only letters, numbers, dots (.), and underscores (_), and must start with a letter.

Domain: Must be in the format domain_name.extension where the extension is 2-6 letters.

Error Handling:

If the user enters an incorrectly formatted email address, the program uses raise to generate an error with a custom message.

Catch errors using a try-except block and display the error description to the user.

Using continue and break:

If the input is not valid, the program gives the user the option to re-enter the email (continue).

If the user enters "exit" instead of an email, the program terminates (break).

Verification and Output:

The program uses a boolean check to confirm if the email is valid.

Prints the valid email in the form: "You have entered a valid email: {email}" using f-string.

Raw String:

Use raw string to define regex patterns.
