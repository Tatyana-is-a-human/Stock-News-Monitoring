# Stock-News-Monitoring
Checks daily price fluctuations in a stock of your choice. If it changes by more than 5%, this programs gathers the top 3 headlines about it and texts them to you.

Currently the program is set up to moniter the TLSA stock using the aphlavantage.co API. This is easily changable in the code. newsapi.org searchs for the top 3 headlines relating to Telsa or whatever company you opt for.

You will have to make free (or paid if you prefer) accounts with alphavantage.co, newsapi.org, and twilio.com.
Lines 6-11 of code are for you to enter your API keys, account SID, authentification token, personal phone number, and automated phone number. Directly below that is where you can change the target stock.

This project is day 36 of udemy.com's 100 days to python mastery challenge. Enjoy!
