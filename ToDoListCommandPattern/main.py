import os
from todo_list import TodoList
from commands import AddTaskCommand, RemoveTaskCommand, MarkAsDoneCommand
from command_manager import CommandManager

def clear_screen():
    # Membersihkan layar sesuai OS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo = TodoList()
    manager = CommandManager()

    while True:
        clear_screen()
        print("\n=== To-Do List (Command Pattern) ===")
        todo.show_tasks()
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tandai Selesai")
        print("4. Undo")
        print("5. Redo")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            task = input("Masukkan tugas: ")
            cmd = AddTaskCommand(todo, task)
            manager.execute_command(cmd)
        elif pilihan == "2":
            try:
                index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
                cmd = RemoveTaskCommand(todo, index)
                manager.execute_command(cmd)
            except:
                print("Indeks tidak valid.")
                input("Tekan Enter untuk lanjut...")
        elif pilihan == "3":
            try:
                index = int(input("Masukkan nomor tugas yang selesai: ")) - 1
                cmd = MarkAsDoneCommand(todo, index)
                manager.execute_command(cmd)
            except:
                print("Indeks tidak valid.")
                input("Tekan Enter untuk lanjut...")
        elif pilihan == "4":
            manager.undo()
            input("Undo selesai. Tekan Enter untuk lanjut...")
        elif pilihan == "5":
            manager.redo()
            input("Redo selesai. Tekan Enter untuk lanjut...")
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk coba lagi...")

if __name__ == "__main__":
    main()