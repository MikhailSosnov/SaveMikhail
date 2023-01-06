class Enimals:
    def __init__(self, list_files_txt = [], enimals_dick = {}):
        self.list_files_txt = list_files_txt
        self.enimals_dick = enimals_dick

    def main(self):
        Enimals().read_dir_txt()
        Enimals().list_enimals()

    def read_dir_txt(self):
        import os, glob
        while True:
            try:
                patch_dir = input("Введите путь к папке с файлами описания животных: ")
                os.chdir(patch_dir)
            except:
                print("Путь к папке введен не корректно ...")
                continue
            file_number = 1
            for file in glob.glob("*.txt"):
                dic_in_dic = {}
                dic_dic = 0
                txt_f = open(file, 'r', encoding='utf-8-sig')
                while True:
                    line_1 = txt_f.readline()
                    line_1 = line_1.rstrip('\n')
                    if not line_1:
                        break
                    dic_dic += 1
                    dic_in_dic[dic_dic] = line_1
                self.list_files_txt.append(file)
                self.enimals_dick[file_number] = dic_in_dic
                file_number += 1
            break

    def list_enimals(self):
        for file_number in range(1, len(self.enimals_dick)+1):
            print(file_number, '. ', self.enimals_dick[file_number][1])
        while True:
            wait = input("For QUIT press Q / for continue press KEY with naber of ANIMAL (end press Enter)")
            if (wait == "Q") or (wait == "q") or (wait == "Й") or (wait == "й"):
                break
            elif (int(wait) >= 1) and (int(wait) <= len(self.enimals_dick)):
                for i in range(1, len(self.enimals_dick[int(wait)]) + 1):
                    print(i, '.', (self.enimals_dick[int(wait)][i]))
                while True:
                    wait_ref = input("For QUIT press Q / Ввведите номер корректируемого пункта (end press Enter) ")
                    if (wait_ref == "Q") or (wait_ref == "q") or (wait_ref == "Й") or (wait_ref == "й"):
                        break
                    elif (int(wait_ref) >= 1) and (int(wait_ref) <= len(self.enimals_dick[int(wait)])):
                        print('Старый текст пункта :', self.enimals_dick[int(wait)][int(wait_ref)])
                        new_text = input('Новый текст пункта :')
                        while True:
                            wait_write = input("Выйти без сохранения - Q / Выйти с сохранением - S (end press Enter) ")
                            if (wait_write == "Q") or (wait_write == "q") or (wait_write == "Й") or (wait_write == "й"):
                                break
                            elif (wait_write == "S") or (wait_write == "s") or (wait_write == "Ы") or (wait_write == "ы"):
                                self.enimals_dick[int(wait)][int(wait_ref)] = new_text
                                file_1 = open(self.list_files_txt[int(wait) - 1], 'w', encoding='utf-8-sig')
                                for i in range(1, len(self.enimals_dick[int(wait)]) + 1):
                                    file_1.writelines(self.enimals_dick[int(wait)][int(i)] + '\n')
                                file_1.close()
                                break
                            else:
                                print('Вееден неверный символ, повторите ввод')
                    else:
                        print('Вееден неверный символ, повторите ввод')
                        continue
                else:
                    print('Вееден неверный символ, повторите ввод')
                    continue
            else:
                print('Вееден неверный символ, повторите ввод')
                continue

if __name__ == '__main__':
    Enimals().main()





