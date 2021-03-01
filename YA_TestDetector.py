def fileopen(data):
    with open(data, 'r', encoding='UTF8') as file:
        text = file.read()

    return text

target_text = fileopen(".\data_file\예시자료2.txt")
