from back import *

if __name__ == "__main__":
    f_input = open("путь_к_файлу_с_кодом.txt", "r", encoding="utf-8")
    s = f_input.read()
    f_input.close()
    p = Parser(s)
    f_out_txt = open("имя_выходного_txt_файла.txt", "w", encoding="utf-8")
    f_out_dox = open("keywords.txt", "r", encoding="utf-8")
    mas = f_out_dox.read().splitlines()
    f_out_dox.close()
    w = Writer(p.strings, f_out_txt, mas, "имя_выходного_docx_файла.docx")
    f_out_txt.close()
