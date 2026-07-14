import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

auction_inventory = {
    101: {"name": "Vintage Mechanical Keyboard", "highest_bid": 1500, "bidder": "None","peak_price": 5000, "status": "Active","expires_at": time.time() + 3600},
    102: {"name": "4K Ultra-Wide Monitor", "highest_bid": 8000, "bidder": "None","peak_price": 15000, "status": "Active","expires_at": time.time() + 3600}
}



# ----------------- Authentication Module ----------------------


login_attempts = 0

def admin_login():
    global login_attempts
    while True:
        print("=========================================")
        print("   AUCTION MANAGEMENT SYSTEM - ADMIN PORTAL   ")
        print("=========================================")

        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
    
        if username == "GlobeMaster" and password == "api69":
            print("\nLoading...")
            time.sleep(0.8) 
            print("\nAccess Granted ✅. Initializing command interface...")
            print("Welcome back, Mr Admin.")
        
            admin_dashboard_menu()              #this calls the menu function
            break    
        else:
            print("\n Loading...")
            time.sleep(0.8) 
            print("\n {RED}{BOLD} Access Denied ❌ : Invalid credentials sequence.{RESET}")
        
            login_attempts += 1   
        
            # If hit 5 failures, system freezes
        
            if login_attempts >= 5:
                print("\n {MAGENTA}[SECURITY ALERT] 5 failed attempts reached.{RESET}")
                print("{YELLOW}System frozen for 15 seconds.....{RESET}")
                time.sleep(15) 
                print("Cooldown complete.")
                login_attempts = 0           # Resets the login attempts
            
                print("Terminating system process to maintain security boundaries.")
                sys.exit()   



# ------------------- Operational Module --------------------



#Function to view current catalog in table grid
def view_catalog():
   
    print("\n" + "=" * 70)
    print("               CURRENT AUCTION CATALOG                  ")
    print("=" * 70)
    print(f"{'ID':<8} {'Item Ledger Name':<32} {'Top Bid':<15} {'High Bidder':<16} {'Buyout Target':<15} {'Status':<10}")
    print("-" * 70)
    
    for item_id, details in auction_inventory.items():
        print(f"{item_id:<8} {details['name']:<32} Rs.{details['highest_bid']:<11} {details['bidder']:<16} Rs.{details['peak_price']:<11} {details['status']:<10}")
    print("=" * 100)


# Function to add new item :)
def add_new_item():

    print("\n----- [Inventory Generation Protocol] -----")
    try:
        new_id = int(input("Assign Unique Item ID (Integer): "))
        
        if new_id in auction_inventory:
            print("\n SYSTEM ERROR ⚠️ : Identity collision! This ID already exists in the warehouse.")
            return
            
        new_name = input("Enter Asset Name: ")
        starting_price = float(input("Set Base Reserve Price (Rs.): "))
        buyout_target = float(input("Set Peak Value Buyout Price (Rs.): ")) #this is the peak value
        
        #  DYNAMIC TIME INPUT FOR LIVE DEMONSTRATION
        lifespan_seconds = float(input("Set Auction Lifespan Window (in Seconds, e.g., 60): "))
        calculated_expiry = time.time() + lifespan_seconds 

        auction_inventory[new_id] = {
            "name": new_name,
            "highest_bid": starting_price,
            "bidder": "None",
            "peak_price": buyout_target,
            "status": "Active",
            "expires_at": calculated_expiry
        }
        print(f"\n Success 🎉 : '{new_name}' has been securely loaded into the catalog.")
        
    except ValueError:
        print("\n DATA ANOMALY ❌ : Invalid input metrics. ID must be an integer, Price must be a number.")


# ------------------  Transaction execution engine  ------------------------

def place_bid():
    
    print("\n" + "=" * 45)
    print("         LIVE AUCTION BIDDING INTERFACE        ")
    print("=" * 45)
    
    try:
        target_id = int(input("Enter the Item ID you wish to bid on: "))
        
        if target_id not in auction_inventory:
            print("Loading....")
            time.sleep(0.6)
            print("\n TRANSACTION ERROR ⚠️ : The requested asset ID does not exist in our ledger.")
            return 
        
        item_card = auction_inventory[target_id]
        
        if item_card["status"] != "Active":
            print("Loading....")
            time.sleep(0.6)
            print(f"\n TRANSACTION DENIED ⚠️ : This item ('{item_card['name']}') is already SOLD!")
            return
        
        current_demo_time = time.time()
        if current_demo_time > item_card["expires_at"]:
            item_card["status"] = "Expired"  
            print("Processing timeline variable....")
            time.sleep(0.8)
            print(f"\n TIME LOCK BREACHED ❌ : The operational window for '{item_card['name']}' has closed!")
            print("No further economic inputs are accepted for this listing.")
            return


        bidder_name = input("Enter your name: ")
        new_bid = float(input(f"Current highest bid is Rs. {item_card['highest_bid']}. Enter your bid: "))
        
        if new_bid <= item_card["highest_bid"]:
            print("Loading....")
            time.sleep(1.2)
            print(f"\n {RED} TRANSACTION FAILED ❌ : Your bid of Rs. {new_bid} is too low!{RESET}")
            print(f"You must bid higher than the current standing price of Rs. {item_card['highest_bid']}.")
            return 
        
        # Overwriting the existing data fields

        item_card["highest_bid"] = new_bid
        item_card["bidder"] = bidder_name
        print("Loading....")
        time.sleep(1.2)
        print(f"\n {GREEN}{BOLD}AUTHORIZED 🎉 : {bidder_name} is now the leading bidder at Rs. {new_bid}!{RESET}")
        
        # Metdhod 2 of closing bid (Reaching Peak value)

        """
        item_card["highest_bid"] = new_bid
        item_card["bidder"] = bidder_name
        
        if new_bid >= item_card["peak_price"]:
            print("Loading....")
            time.sleep(1.2)
            item_card["status"] = "Sold"
            print(f"\n PEAK VALUE CEILING BREACHED! Rs. {new_bid} triggers instant buyout target.")
            print(f" TRANSACTION FINALIZED 🎉 : '{item_card['name']}' has been SOLD to {bidder_name}!")
        else:
            print("Loading....")
            time.sleep(1.2)
            print(f"\n AUTHORIZED 🎉 : {bidder_name} is leading at Rs. {new_bid}. (Buyout: Rs. {item_card['peak_price']})")
        """
        
        
        
    except ValueError:
        print("\n INPUT ANOMALY ❌ : Item ID must be an integer numeral.")


# Split Auction Settlement Architecture


def settle_auction():
    
    # ----- Method-1 (Manual Closing) -----
    print("\n" + "=" * 45)
    print("        ADMINISTRATIVE SETTLEMENT TERMINAL       ")
    print("=" * 45)
    
    try:
        
        target_id = int(input("Enter Item ID to finalize and close: "))
        
        if target_id not in auction_inventory:
            print("Loading...")
            time.sleep(0.8)
            print("\n SYSTEM ERROR ⚠️ : Target ID not found in inventory registry.")
            return
            
        item_card = auction_inventory[target_id]
        
        if item_card["status"] != "Active":
            print("Loading...")
            time.sleep(0.8)
            print(f"\n SETTLEMENT DENIED ❌ : '{item_card['name']}' is already closed.")
            return
            
        print(f"\n--- [Asset Settlement Summary] ---")
        print(f"Asset Name   : {item_card['name']}")
        print(f"Final Price  : Rs. {item_card['highest_bid']}")
        print(f"Winning Buyer: {item_card['bidder']}")
        
        confirm = input("\nAre you sure you want to finalize this sale? (yes/no): ").lower()
        
        if confirm == "yes" or confirm == "y":
            print("Loading...")
            time.sleep(0.8)
            item_card["status"] = "Sold"
            print(f"\n SUCCESS ✅ : Auction finalized! '{item_card['name']}' status updated to SOLD.")
        else:
            print("Loading...")
            time.sleep(0.8)
            print("\n SETTLEMENT ABORTED ⚠️ : Operational state remains active.")
            
    except ValueError:
        print("\n DATA ANOMALY ❌ : Invalid entry. Item ID must be an integer.")




# -------------------- CONTROL BLOCK -----------------------


#Dashboard menue function
def admin_dashboard_menu():
    
    while True:
        print("\n" + "•" * 40)
        print(f"        {BOLD}ADMIN CONTROL PANELS{RESET}         ")
        print("•" * 40)
        print(f"{CYAN}1.{RESET} View Active Asset Catalog")
        print(f"{CYAN}2.{RESET} Append New Asset Listing")
        print(f"{CYAN}3.{RESET} Execute Live Asset Bidding")
        print(f"{CYAN}4.{RESET} Finalize Asset Settlement (Close Auction)")
        print(f"{CYAN}5.{RESET} Sever Administrative Session (Exit)")
        
        choice = input("\nSelect an operational protocol (1-5): ")
        
        if choice == "1":
            view_catalog()
        elif choice == "2":
            add_new_item()
        elif choice == "3":
            place_bid()
        elif choice == "4":
            settle_auction()
        elif choice == "5":
            print("\nLogging out. Safely severing administrative terminal connection...")
            break
        else:
            print("\n ALERT ⚠️ : Unrecognized choice. Please re-input valid selection index (1-4).")


if __name__ == "__main__":
    admin_login()
   