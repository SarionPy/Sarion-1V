import random
import os
import shutil
from os import path

from obshenie import *
from frazi import *

os.chdir("..")

print(startTxt)
command = input()

# Показывает рабочию деректорию
if command == NowDIR:
	print("Текущая деректория:", os.getcwd())

# Создаёт папку
if command == dir_command:
	print(dir_command_name)
	DirName = input()

	print("Деректория в которой я создам папку:", os.getcwd())
	os.mkdir(DirName)
	print("\nПапка " + DirName + " успешно создана!")

# Создаёт папку и другие папки в ней
if command == dirs_command:
	print("Текущая деректория:", os.getcwd())

	print(dirs_command_numberTxt)
	numbers = input()

	if numbers == "2":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		os.makedirs(Dir1+"/"+Dir2+"/")

	elif numbers == "3":		
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/")

	elif numbers == "4":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/")

	elif numbers == "5":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/")

	elif numbers == "6":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		print(dir6Name)
		Dir6 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/"+Dir6+"/")

	elif numbers == "7":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		print(dir6Name)
		Dir6 = input()
		print(dir7Name)
		Dir7 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/"+Dir6+"/"+Dir7+"/")

	elif numbers == "8":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		print(dir6Name)
		Dir6 = input()
		print(dir7Name)
		Dir7 = input()
		print(dir8Name)
		Dir8 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/"+Dir6+"/"+Dir7+"/"+Dir8+"/")

	elif numbers == "9":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		print(dir6Name)
		Dir6 = input()
		print(dir7Name)
		Dir7 = input()
		print(dir8Name)
		Dir8 = input()
		print(dir9Name)
		Dir9 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/"+Dir6+"/"+Dir7+"/"+Dir8+"/"+Dir9+"/")

	elif numbers == "10":
		print(dir1Name)
		Dir1 = input()
		print(dir2Name)
		Dir2 = input()
		print(dir3Name)
		Dir3 = input()
		print(dir4Name)
		Dir4 = input()
		print(dir5Name)
		Dir5 = input()
		print(dir6Name)
		Dir6 = input()
		print(dir7Name)
		Dir7 = input()
		print(dir8Name)
		Dir8 = input()
		print(dir9Name)
		Dir9 = input()
		print(dir10Name)
		Dir10 = input()
		os.makedirs(Dir1+"/"+Dir2+"/"+Dir3+"/"+Dir4+"/"+Dir5+"/"+Dir6+"/"+Dir7+"/"+Dir8+"/"+Dir9+"/"+Dir10+"/")

# Создаёт файл
if command == file_command:
	print(fileName_txt)
	FileName = input()
	print(fileFormat_txt)
	FileFormat = input()
	text_file = open(FileName+"."+FileFormat, "w")
	print("Файл - "+FileName+"."+FileFormat, "создан в ", os.getcwd())

# Переименует файл
if command == renameFILE_command:
	print(renameFILE_command_Say)
	NameFile = input()
	print("\nКакой формат у файла:")
	FormatFile = input()
	print(renameFILE_command_Say2)
	NewNameFile = input()
	print("\nКакой формат будет у файла:")
	NewFormatFile = input()
	os.rename(NameFile+"."+FormatFile, NewNameFile+"."+NewFormatFile)


# Переименует папку
if command == renameDIR_command:
	print(renameDIR_command_Say)
	NameDIR = input()
	print(renameDIR_command_Say2)
	NewNameDIR = input()
	os.rename(NameDIR, NewNameDIR)


# Перемещает файл
if command == moveFILE_command:
	print(moveFILE_command_Say)
	source_path = input()
	if path.exists(source_path):
		print(moveFILE_command_Say2)
		destination_path = input()
		new_location = shutil.move(source_path, destination_path)
		print("\n% s перемещен в указаное место, % s" % (source_path , new_location))
	else :
		print(moveFILE_command_Say3)


# Перемещает папку
if command == moveDIR_command:
	print(moveDIR_command_Say)
	source_path = input()
	if path.exists(source_path):
		print(moveDIR_command_Say2)
		destination_path = input()
		new_location = shutil.move(source_path, destination_path)
		print("\n% s перемещен в указаное место, % s" % (source_path , new_location))
	else :
		print(moveDIR_command_Say3)


# Удаляет файл
if command == FileDelet_command:
	print(FileDelet_command_Say)
	FileName = input()
	print(FileDelet_command_Say2)
	FileFormat = input()
	os.remove(FileName+"."+FileFormat)
	print("Файл"+FileName+"."+FileFormat+"успешно удалён!")


# Удаляет папку
if command == DirDelet_command:
	print(DirDelet_command_Say)
	DirName = input()
	shutil.rmtree(DirName)
	print("Папка "+DirName+" успешно удалена!")


if command == MineCraft_command:
	os.popen("C:\\Users\\Вячеслав\\AppData\\Roaming\\.tlauncher\\legacy\\Minecraft\\TL.exe")


if command == blender_command:
	os.popen("C:\\Program Files\\Blender Foundation\\Blender 2.92\\blender.exe")



if command == Help_command:
	print(Help_command_Say)


if command == Commands_command:
	print(Commands_command_Say)


else:
	print("\nДанной команды не существует!\nЕсли команды тебе не известны напиши мне **Помощь** или **Команды**\n")
