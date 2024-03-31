Guildwars 2 gold webapp

This project allows the user to decide how to best use their time to gain the most gold while playing Guildwars 2. The goal is to allow players to spend the most amount of time playing the game the way they want to while being able to have the gold they need to buy whatever items/skins/gems/etc. they need or want.

python -m pip install Django
Pip install mysqlclient
pip install requests

***mongoDB***

How to use the project:
-------------------------------
After starting the app welcome message is displayed

User is given options to select from:
User setup
Calculate potential profit
Calculate actual profit
Update salvage data

User setup:
Needs user API for inventory, materials, bank, etc. to calculate salvage rate, calculate optimal items to be crafted, etc.

Calculate potential profit:
Calculates user potential profit for processing already owned unid gear or buying and processing unid gear.
User selects calculate potential profit
Check user API, if user does not have salvage rate data then app can’t calculate potential profit
App return how many unid gear is owned by the user, the current buy price, and current sell price
User has 2 options 
Input how many of each quality of unid gear they wish to process, max is how many are currently owned
Input buy price (default is current buy price) and how many of each quality unid gear they wish to buy
App returns estimation of raw materials gained and profit vs loss of buying Unid gear and salvaging into raw materials vs. buying the equivalent raw materials
Estimates are calculated by salvage rates associated with the user
If there is a loss then program ends
If there is a profit then returns profitable craftable items within an acceptable sales volume that is determined by the user
User can adjust volume of each item crafted to take into account materials already owned and the app will calculate overall profit

Calculate Actual profit:
Calculates user profit from buying and processing unid gear
User selects calculate actual profit
Check user API
User initiates calculation of actual profit
User can select/deselect what characters or bank that will be recorded, saves time for large datasets
App records time of initiation and records all items/materials owned by user
User opens and salvages unid gear with following salvage kits
Blue unid gear: Copper-Fed Salvage-o-Matic
Green unid gear: Runecrafter's Salvage-o-Matic
Yellow unid gear: Silver-Fed Salvage-o-Matic
User completes processing unid gear and ends recording
App records time of ending and records all items/materials owned by user
App calculates difference between initial recording and final recording
Returns raw materials gained
Returns profit vs loss of buying unid gear processing vs. buying the equivalent raw materials
Updates salvage data

Update salvage data: 
Salvage data can be updated manually or automatically when user calculates actual profit
User is prompted to input quantity of unid gear and raw materials salvaged
Separate prompts for blue, green, and yellow
App returns new salvage data
----------------------------------------------
Dataset vs Data Model vs Data Schema
Dataset: raw data
Data model: what I am storing

GW2 API wiki
----------------------------------------------
Datasets:
Gw2_items
Id = int
Name = string
Type = string
Rarity = string
Vender_value = int

CustomUser
Username = str
Password = str
Email = str
API = str

User default salvage rates
User = Foreignkey(customuser)
Id = int
Name = string
Salvage_rate = decimalfield
User default blue salvage rates (User default salvage rates)
User default green salvage rates (User default salvage rates)
User default yellow salvage rates (User default salvage rates)

Crafting recipes (MongoDB for more organic Schema)

User_Storage
user = Foreighkey(customuser)
Id = int
Name = ForeignKey(gw2_items, on_delete = models.cascade)
Count = int
User_bank
User_materials
User_shared_inventory
User_bag_inventory 

Trading_post_data
Id = int
Buys = JSONField()
Sells = JSONField()


Serializer
User_bag_inventorySerializer (example)
Count = serializermethodfield()
Get_count = 

Appendix:
--------------
Unid gear - Unidentified gear

