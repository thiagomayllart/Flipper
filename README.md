# Flipper

Automated CBC Cipher Breaker

# What is this?

Flipper was developed with the intention of automating the process of cracking the CBC cipher by exploiting a vulnerability in the way the cipher works (using XOR operation). It simply byte flips every position in every block in a crypted string using a CBC cipher. You can also selected the specific position and the specific block you want to byte flip (in case you already know what that specific block/position really means when decrypted)

# How does it work?

The principle used in exploitation of the string is better described on this link: http://resources.infosecinstitute.com/cbc-byte-flipping-attack-101-approach/

# So, what is new?

Flipper allows you to not only selected a specific position/block and perform the XOR operation with the actual, previous and the string you want to insert in that space. It also allows you to test every single position in a string with something that you can guess.

In case the string (maybe a token in a cookie) has a parameter "anyparameter(let's just consider:admin)=false", you can simply use the tool to byte flip the "=false" substring and get a "=true" output in that position. Or, you can swap numbers that may be in the string to get access to other accounts. Example: id=1234. Choose '4' as a portion that you know about the string and choose, for example, '7' as a the final output. The id will be changed to id=1237, possibly providing you the access to the account with id 1237.

# Cool!! And how do I use it?

**First you need to setup the request file**

That's easy! 

This tool is integrated with the output produced using Burp Suite. You **MUST USE BURP SUITE**

1) Produce an output of the request containing the key/token/string/etc you want to test:
  In the **Site Map** interface in Burp Suite -> Right Click the request -> Save Item -> **UNCHECK Base64 encode requests and responses**
2) Change the extension: .xml to .txt.
3) Open the file and put the key/token/string/etc between the @@@. Example: key=@@@d2hhdGFzdXJwcmlzZQ==@@@

**Parameters**

 -f | The location of your .txt request
 
 -bs | The size of each block in your input (may be 8 or 16 depending on the type of AES encryption used)
 
 -bp | The position of inside the block of size 8 or 16 that the substring you want to change starts. If you want to test every block, simply type X.
 
 -pay | The payload you want to insert. You must select the starting position and then(separated by '-') the parameter you know it is in that position and then (separated by ',') the parameter you want to have in the end:
 
 2-false,true;
 
 If you want to test every position in that block, simply type X.
 
 -th | quantity of threads used
 
 -d | delay between each request
 
 Example:
 
flipper.py -f (file location) -bs 16 -bp 1 -pay 2-false,true;
flipper.py -f (file location) -bs 8 -bp 3 -pay 2-false,true;
flipper.py -f (file location) -bs 8 -bp X -pay X-0,1

