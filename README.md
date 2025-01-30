
Step 1: 6/2024
download python(add py.exe to path)
pip install matplotlib

pip install alpaca-py
pip install alpaca-trade-api

pip install tensorflow

[complete]Choose a exchange application, i.e. Alpaca / Robhinhood
    > Using Alpaca paper, API library:
    > Github API link: https://github.com/alpacahq/alpaca-py/blob/master/examples/README.md

[complete]Initization of Account/SETUP: 6/2024
    >[DONE]open/access the account using the API Key, DONE
    >[DONE]focus crypto, DONE

[complete]Stream live crypto data on csv file: 7/2024
    >[DONE]stream the crypto of its latest bar,
    >[DONE]store the data into the csv file,

[complete]Display the plot as it stream: 8/3/2024
    >[DONE]read the csv file to be plot,
    >[DONE]fomate the plot,
    >[DONE]plot the data as stream updates/new-data is written,
    >[DONE]save plot into png,

Stream live stock+crypto data on csv file: 8/10/2024
    >[DONE]focus multiple ticket symbol,
    >[DONE]references account class focus array to be stream in market class
    >[DONE]references correct symbol name for naming consistency
    >[STALL]EXTRA: Stream multiple live data
        - API streaming/websocket limitation for one ticket type

[COMPLETE]Store histroical data into a csv file 8/19/2024
    >[DONE]Get historical raw data
    >[DONE]Convert histroical data into csv
    >[DONE]Plot histroical data into plot
    >[DONE]Combine histroical data + live data with live plot
    >[DONE]Organize the operation and steps taken

Write a simple interface to inpute keys, action, and display
    >[DONE]opening interface/profilio + input
    >[STALL]perform manual order action i.e. buy/sell
    >[STALL]display resulting profilio on action and update from stream

Step 2
Use histroical + live data to be anaylze  10/2024
    >[DONE]Immplement AI model to predict future price
    >[DONE]Histroical Data analayzed by the AI model is graphed 
    >[STALL]Optimized and simplified the inferface for scaling
    >[]Incorporate live data to be analayzed by the AI
    >[]design the complete inferface to stream crypto data

Step 3
Automated buy and sell request on historical + live data that are analzyed 


Step 4
Create multiple concurrent operating bot using different stragtry 
