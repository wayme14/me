from dotenv import load_dotenv

load_dotenv() 

import sys
from app.menus.util import clear_screen, pause
from app.client.engsel import *
from app.service.auth import AuthInstance
from app.menus.bookmark import show_bookmark_menu
from app.menus.account import show_account_menu
from app.menus.package import fetch_my_packages, get_packages_by_family

# Warna ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def show_main_menu(number, balance, balance_expired_at):
    clear_screen()
    phone_number = number
    remaining_balance = balance
    expired_at = balance_expired_at
    expired_at_dt = datetime.fromtimestamp(expired_at).strftime("%Y-%m-%d %H:%M:%S")
    
    # Info akun
    print(CYAN + "--------------------------" + RESET)
    print(YELLOW + "Informasi Akun" + RESET)
    print(f"{GREEN}Nomor      :{RESET} {phone_number}")
    print(f"{GREEN}Pulsa      :{RESET} Rp {remaining_balance}")
    print(f"{GREEN}Masa aktif :{RESET} {expired_at_dt}")
    print(CYAN + "--------------------------" + RESET)

    # Daftar menu
    menu_items = [
        "Login/Ganti akun",
        "Lihat Paket Saya",
        "Spesial For You",
        "Akrab 2Kb",
        "Bonus Flex Rp.0",
        "Kuota Bersama Rp 0",
        "Addon Hotrod/Xcs 8gb",
        "Xcs Flex Ori",
        "EduCoference Ori",
        "Mastif Bundling Setahun",
        "Paket XL Point",
        "Paket Bonus MyRewards",
        "Addon XCP 2GB",
        "Addon XCP 15GB",
        "Bebas Puas",
        "XCP OLD 10GB",
        "XCP VIP",
        "Akrab 2Kb New",
        "XCP GIFT",
        "Addon XCP 1GB",
        "Pilkada Damai Kuota",
        "Bonus Akrab Rp 0",
        "XC FLEX LENGKAP",
        "Unli Turbo Xcs/Hotrod",
        "Addon XCP 6GB",
        "Family Hide Addon Prepaid",
        "Add Slot Akrab",
        "Akrab Full Versi",
        "Akrab Big",
        "Booster Akrab",
        "Addon Akrab",
        "XCS 8GB & 14GB",
        "New Comer XCS 2GB & 4GB",
        "XC FLEX LENGKAP V2",
        "Paket Harian Rp 0",
        "Paket Youtube Bonus",
        "Xtra Combo Mini",
        "Biz Starter Unli",
        "EduCoference Rp 10",
        "Beli Paket XUT",
        "Family Code",
        "Family Code (Enterprise)"
    ]

    cols = 2
    width = 50  # lebar kolom

    print(YELLOW + "Menu:" + RESET)
    for i in range(0, len(menu_items), cols):
        row = ""
        for j in range(cols):
            idx = i + j
            if idx < len(menu_items):
                row += f"{idx+1:02}. {menu_items[idx]:{width}}"
        print(row)

    # Opsi penting
    print(RED + "00. Bookmark Paket".ljust(width * cols) + RESET)
    print(RED + "99. EXIT".ljust(width * cols) + RESET)
    print(CYAN + "--------------------------" + RESET)


show_menu = True
def main():
    
    while True:
        active_user = AuthInstance.get_active_user()

        # Logged in
        if active_user is not None:
            balance = get_balance(AuthInstance.api_key, active_user["tokens"]["id_token"])
            balance_remaining = balance.get("remaining")
            balance_expired_at = balance.get("expired_at")

            show_main_menu(active_user["number"], balance_remaining, balance_expired_at)

            choice = input("Pilih menu: ")
            if choice == "1":
                selected_user_number = show_account_menu()
                if selected_user_number:
                    AuthInstance.set_active_user(selected_user_number)
                else:
                    print("No user selected or failed to load user.")
                continue
            elif choice == "2":
                fetch_my_packages()
                continue
            elif choice == "3":
                # Spesial For You  
                get_packages_by_family("6fda76ee-e789-4897-89fb-9114da47b805")
            elif choice == "4":
                # Akrab 2Kb  
                get_packages_by_family("340be7a9-9ab8-d23e5-3059-70b81ec984e")
            elif choice == "5":
                # Bonus Flex Rp.0  
                get_packages_by_family("1b42d4f6-a76e-4986-aa5c-e2979da952f4")
            elif choice == "6":
                # Kuota Bersama Rp 0  
                get_packages_by_family("434a1449-1d18-43f8-b059-10b3d5e3f5c3")
            elif choice == "7":
                # Addon Hotrod/Xcs 8gb  
                get_packages_by_family("74eb925a-4a05-4ede-b04b-edd90786419b")
            elif choice == "8":
                # Xcs Flex Ori  
                get_packages_by_family("4a1acab0-da54-462c-84b1-25fd0efa9318")
            elif choice == "9":
                # EduCoference Ori  
                get_packages_by_family("5d63dddd-4f90-4f4c-8438-2f005c20151f")
            elif choice == "10":
                # Mastif Bundling Setahun  
                get_packages_by_family("6bcc96f4-f196-4e8f-969f-e45a121d21bd")
            elif choice == "11":
                # Paket XL Point  
                get_packages_by_family("784be350-9364-4f03-8efa-e7cf31e8baa2")
            elif choice == "12":
                # Paket Bonus MyRewards   
                get_packages_by_family("07461ed8-8a81-4d89-a8f2-4dd0271efdde")
            elif choice == "13":
                # Addon XCP 2GB   
                get_packages_by_family("580c1f94-7dc4-416e-96f6-8faf26567516")
            elif choice == "14":
                # Addon XCP 15GB  
                get_packages_by_family("45c3a622-8c06-4bb1-8e56-bba1f3434600")
            elif choice == "15":
                # Bebas Puas  
                get_packages_by_family("d0a349a7-0b3a-4552-bc1d-3fd9ac0a17ee")
            elif choice == "16":
                # XCP OLD 10GB  
                get_packages_by_family("364d5764-77d3-41b8-9c22-575b555bf9df")
            elif choice == "17":
                # XCP VIP  
                get_packages_by_family("23b71540-8785-4abe-816d-e9b4efa48f95")
            elif choice == "18":
                # Akrab 2Kb New  
                get_packages_by_family("4889cc43-55c9-47dd-8f7e-d3ac9fae6022")
            elif choice == "19":
                # XCP GIFT  
                get_packages_by_family("0895946e-d277-4218-914c-b663c09debf7")
            elif choice == "20":
                # Addon XCP 1GB  
                get_packages_by_family("8080ddcf-18c5-4d6d-86a4-89eb8ca5f2d1")
            elif choice == "21":
                # Pilkada Damai Kuota  
                get_packages_by_family("e3b2c02e-0e2f-4275-a6de-84fb9efab992")
            elif choice == "22":
                # Bonus Akrab Rp 0  
                get_packages_by_family("a677d649-3c5a-46c2-a043-cb69ac841208")
            elif choice == "23":
                # XC FLEX LENGKAP  
                get_packages_by_family("3a6a256f-1524-4dc3-a989-35584f31c265")
            elif choice == "24":
                # Unli Turbo Xcs/Hotrod  
                get_packages_by_family("08a3b1e6-8e78-4e45-a540-b40f06871cfe")
            elif choice == "25":
                # Addon XCP 6GB  
                get_packages_by_family("5412b964-474e-42d3-9c86-f5692da627db")
            elif choice == "26":
                # Family Hide Addon Prepaid  
                get_packages_by_family("31c9605f-1a3a-4410-ae45-362650bb507d")
            elif choice == "27":
                # Add Slot Akrab  
                get_packages_by_family("86d86765-65a6-4ece-8056-ab2b220429e4")
            elif choice == "28":
                # Akrab Full Versi  
                get_packages_by_family("f4fd69c7-12a4-4047-a1f2-f4072a7c543e")
            elif choice == "29":
                # Akrab Big  
                get_packages_by_family("6e469cb2-443d-402f-ba77-681b032ead6a")
            elif choice == "30":
                # Booster Akrab  
                get_packages_by_family("5452eed8-91f3-4e9c-b7bb-0985759d5440")
            elif choice == "31":
                # Addon Akrab  
                get_packages_by_family("c5dbcb2d-31cc-462c-afe8-b3a767c6d404")
            elif choice == "32":
                # XCS 8GB & 14GB  
                get_packages_by_family("3e6d45f1-f314-4acd-a75b-be40c0726198")
            elif choice == "33":
                # New Comer XCS 2GB & 4GB  
                get_packages_by_family("6bc5a34d-7901-4bf9-8629-5bd7de28c89f")
            elif choice == "34":
                # XC FLEX LENGKAP V2  
                get_packages_by_family("3c71892a-852c-4a0f-8cb5-9cf731e26508")
            elif choice == "35":
                # Paket Harian Rp 0  
                get_packages_by_family("96d99f87-8963-40e4-a522-8bea86504fee")
            elif choice == "36":
                # Paket Youtube Bonus  
                get_packages_by_family("1fe292a5-5fef-430e-917b-e0eaeeb89f93")
            elif choice == "37":
                # Xtra Combo Mini  
                get_packages_by_family("ad176860-49d4-4bdd-9161-ab38dc6a631b")
            elif choice == "38":
                # Biz Starter Unli  
                get_packages_by_family("20342db0-e03e-4dfd-b2d0-cd315d7ddc36" ,is_enterprise=True)
            elif choice == "39":
                # EduCoference Rp0  
                get_packages_by_family("fcf982c8-523b-4748-9258-5fca2c0b703d" ,is_enterprise=True)

            elif choice == "40":
                # XUT 
                get_packages_by_family("08a3b1e6-8e78-4e45-a540-b40f06871cfe")
            
            elif choice == "41":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                    continue
                get_packages_by_family(family_code)
            elif choice == "42":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                    continue
                get_packages_by_family(family_code, is_enterprise=True)
            elif choice == "00":
                show_bookmark_menu()
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            elif choice == "9":
                # Playground
                pass
                # data = get_package(
                #     AuthInstance.api_key,
                #     active_user["tokens"],
                #     "U0NfX8A08oQLUQuLplGhfT_FXQokJ9GFF9kAKRiV5trm6BfbRoxrsizKkWIVNxM0az6lroT92FYXnWmTXRXZOl1Meg",
                #     ""
                #     ""
                #     )
                # print(json.dumps(data, indent=2))
                # pause()
            else:
                print("Invalid choice. Please try again.")
                pause()
        else:
            # Not logged in
            selected_user_number = show_account_menu()
            if selected_user_number:
                AuthInstance.set_active_user(selected_user_number)
            else:
                print("No user selected or failed to load user.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the application.")
    except Exception as e:
        print(f"An error occurred: {e}")
        