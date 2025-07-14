# import os
# import shutil

# # Base directory where all folders will be created
# BASE_DIR = "MyDrive"

# def get_all_folders():
#     """List all folders in the base directory."""
#     print("\nFetching all folders...")
#     if not os.path.exists(BASE_DIR):
#         print("Base directory does not exist. No folders found.")
#         return
#     folders = [name for name in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, name))]
#     if not folders:
#         print("No folders found.")
#     else:
#         print("Folders:")
#         for folder in folders:
#             print(f" - {folder}")

# def create_folder(folder_name):
#     """Create a new folder in the base directory."""
#     print(f"\nCreating folder: {folder_name}")
#     if not os.path.exists(BASE_DIR):
#         os.makedirs(BASE_DIR)
#     folder_path = os.path.join(BASE_DIR, folder_name)
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#         print("Folder created successfully.")
#     else:
#         print("Folder already exists.")

# def update_folder_name(old_name, new_name):
#     """Rename an existing folder."""
#     print(f"\nRenaming folder from '{old_name}' to '{new_name}'")
#     old_path = os.path.join(BASE_DIR, old_name)
#     new_path = os.path.join(BASE_DIR, new_name)
#     if os.path.exists(old_path):
#         if not os.path.exists(new_path):
#             os.rename(old_path, new_path)
#             print("Folder renamed successfully.")
#         else:
#             print("A folder with the new name already exists.")
#     else:
#         print("Folder to rename does not exist.")

# def delete_folder(folder_name):
#     """Delete a folder from the base directory."""
#     print(f"\nDeleting folder: {folder_name}")
#     folder_path = os.path.join(BASE_DIR, folder_name)
#     if os.path.exists(folder_path):
#         shutil.rmtree(folder_path)
#         print("Folder deleted successfully.")
#     else:
#         print("Folder does not exist.")

# def main():
#     """Main console menu loop."""
#     while True:
#         print("\n=== Local Drive Console Application ===")
#         print("1. Get all folders")
#         print("2. Create a new folder")
#         print("3. Rename a folder")
#         print("4. Delete a folder")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")

#         if choice == "1":
#             get_all_folders()
#         elif choice == "2":
#             name = input("Enter folder name to create: ")
#             create_folder(name)
#         elif choice == "3":
#             old_name = input("Enter current folder name: ")
#             new_name = input("Enter new folder name: ")
#             update_folder_name(old_name, new_name)
#         elif choice == "4":
#             name = input("Enter folder name to delete: ")
#             delete_folder(name)
#         elif choice == "5":
#             print("Exiting... Bye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
