import re
import os 
import logging




def get_image_paths_for_latex(images_dir, deck_list):
    cards_paths_latex = []
    image_paths = os.listdir(images_dir)

    for card in deck_list:
        path = card[1].replace(" ","-").lower()
        r = re.compile(f".*{path}.*")
        path = list(filter(r.match, image_paths)) 

        if path:
            for i in range(card[0]):
                cards_paths_latex.append(path)
        else:
            logging.warn(f"Unable to find {card[1]}")
            
    return cards_paths_latex

def make_latex_card_table(cards_paths_latex):
    table_text = []
    begin_table = "\\begin{tabular}{ccc}"
    end_table = "\\end{tabular}"

    for i, path in enumerate(cards_paths_latex):
        if i == 0:
            table_text.append(begin_table)
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}&"
            table_text.append(text)

        elif i == len(cards_paths_latex)-1:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}"
            table_text.append(text)
            table_text.append(end_table)

        elif (i+1) % 9 == 0:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}"
            table_text.append(text)
            table_text.append(end_table)
            table_text.append("")
            table_text.append("\\newpage")
            table_text.append("")
            table_text.append(begin_table)   

        elif (i+1) % 3 == 0:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}} \\\\"
            table_text.append(text)
            table_text.append("")


        else:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}&"
            table_text.append(text)
    
    return table_text

def make_latex_tex_file(image_folder, deck_list, pdf_folder):
    
    file_name = "cards_for_print.tex"
    
    cards_paths = get_image_paths_for_latex(image_folder, deck_list)
    
    card_table = make_latex_card_table(cards_paths)
    
    preamble = '''
    \\documentclass{article}
    \\usepackage{graphicx}
    \\usepackage[ paperwidth=210mm, paperheight=297mm, margin=10mm]{geometry}
    \\usepackage[table]{xcolor}

    \\begin{document}

    \\setlength{\\tabcolsep}{0.5pt}   
    \\addtolength{\\tabcolsep}{0.5pt} 
    \\def\\arraystretch{0.5} 



        '''
    graphics = f"\\graphicspath{{{{{image_folder}/}}}}\n"

    ending = "\\end{document}"
    


    if os.path.exists(os.path.join(pdf_folder, file_name)):
      os.remove(os.path.join(pdf_folder, file_name))

    f = open(os.path.join(pdf_folder, file_name), "x")
    f.write(preamble)
    f.write(graphics)

    for listitem in card_table:
        f.write('%s\n' % listitem)

    f.write(ending)
    f.close()

    return os.path.join(pdf_folder, file_name)

def compile_tex(latex_file, target_dir):
    '''Compiles a latex_file document and places resulting .pdf file into the target directory'''

    file_dir = latex_file.rsplit("/", 1)[0]

    file_name = latex_file.rsplit("/", 1)[1][:-4]

    #compile
    if os.path.exists(latex_file):
        os.system(f"pdflatex -interaction=nonstop -output-directory={file_dir} {latex_file}")

    #move
    pdf_file = f"{file_dir}/{file_name}.pdf"
    if os.path.exists(pdf_file):
        os.system(f"mv {pdf_file} {target_dir}/{file_name}.pdf")






#pdflatex -interaction=nonstop -output-directory=/Users/ARyder/Desktop/tt/latex pdf /Users/ARyder/Desktop/tt/latex/cards_for_print.tex



#file = "/Users/ARyder/Desktop/tt/latex/cards_for_print.tex"
#compile_tex(file, "/Users/ARyder/Desktop/tt")


