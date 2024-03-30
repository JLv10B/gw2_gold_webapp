Guildwars 2 gold webapp

This project allows the user to decide how to best use their time to gain the most about of gold while playing Guildwars 2. The goal is to allow players to spend the most amount of time playing the game the way they want to while being able to have the gold they need to buy whatever items/skins/gems/etc. they need or want.

How to use the project:
-----------------------
After starting the app welcome message is displayed

User is given options to select from:
- User setup
- Calculate potential profit
- Calculate actual profit

User setup:
- Needs user API for inventory, materials, bank, etc. to calculate salvage rate, calculate optimal items to be crafted, etc.

Calculate potential profit:
-
- User must have an account with APIs setup
- App return how many unid gear is owned by the user, the current buy price, and current sell price
- User has 2 options 
    - Input how many of each quality of unid gear they wish to process, max is how many are currently owned
    - Input buy price (default is current buy price) and how many of each quality unid gear they wish to buy
- App returns estimation of raw materials gained and profit vs loss of buying Unid gear and salvaging into raw materials vs. buying the equivalent raw materials
- If there is a loss then program ends
- If there is a profit then returns profitable craftable items within an acceptable sales volume that is determined by the user
- User can adjust volume of each item crafted to take into account materials already owned and the app will calculate overall profit

Calculate Actual profit:
- User must have an account with APIs setup
- User initiates calculation of actual profit
    - App records time of initiation and records all items/materials owned by user
- User opens and salvages unid gear with following salvage kits
    - Blue unid gear: Copper-Fed Salvage-o-Matic 
    - Green unid gear: Runecrafter's Salvage-o-Matic
    - Yellow unid gear: Silver-Fed Salvage-o-Matic
- User completes processing unid gear and ends recording
    - 
5.) 



Salvage rates for potential profit:
1.) Salvage rates are updated per user
2.) 

Appendix:
---------
Unid gear - Unidentified gear