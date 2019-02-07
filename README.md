# Summary

An API for checking name-email pairs. Intended for use in anti-phishing to verify that an email is from who the name claims.  
Data is kept in the file data.json. Each name can have multiple emails associated with it.

# Usage

Run with `python3 phishing.py`  
Access with `127.0.0.1:5001/[url]`

URLs:  
`api/check-pair`: Check if a name-email pair is in the database.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* "error" if not all arguments were given  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* "unknown" if the name is not in the database  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* "valid" if the email matches one associated with the name  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* "invalid" if the name is in the DB, but the email has no match  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Args:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* name: the name of the sender  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* email: the email address of the sender  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`127.0.0.1:5001/api/check-pair?name=Bill Wurst&email=billw@example.com`
    
# Requirements

Python 3  
Flask for Python
