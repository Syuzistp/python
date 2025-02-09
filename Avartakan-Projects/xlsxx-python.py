import xlsxwriter
import random

def read_people_from_txt(file_name):
    people = []
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            if len(parts) == 5:
                people.append({
                    "Name": parts[0],
                    "Surname": parts[1],
                    "Age": int(parts[2]),
                    "Gender": parts[3],
                    "Profession": parts[4]
                })
    return people

def generate_random_color():
    #random guyni yntrutyun
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def add_people_to_excel(file_name, people_data):
    #excel fayli stexcum
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet("Peoples")

    # glxavor toxi guyni yntrutyun
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': 'yellow',
        'border': 1
    })

    # masnagitutyunneri guyneri hamar dict
    profession_colors = {}

    # glxavor tox
    headers = ["Name", "Surname", "Age", "Gender", "Profession"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header, header_format)

    # informacianer
    for row_num, person in enumerate(people_data, start=1):
        # masnagitutyunneri hamar guyni yntrutyun
        profession = person.get("Profession", "")
        if profession not in profession_colors:
            # ete masnagitutyan hamar guyn yntrvac che stexcum enq nory
            profession_colors[profession] = workbook.add_format({
                'bold': True,
                'bg_color': generate_random_color(),
                'border': 1
            })

        row_format = profession_colors[profession]

        # amboxj toxy grum enq yntrvac guynov
        worksheet.write(row_num, 0, person.get("Name", ""), row_format)
        worksheet.write(row_num, 1, person.get("Surname", ""), row_format)
        worksheet.write(row_num, 2, person.get("Age", 0), row_format)
        worksheet.write(row_num, 3, person.get("Gender", ""), row_format)
        worksheet.write(row_num, 4, profession, row_format)


    workbook.close()


people_file = "people.txt"
output_excel = "peoples.xlsx"

# faylic kardum enq informacia
people = read_people_from_txt(people_file)

# informacian avelacnum enq excel fayl
add_people_to_excel(output_excel, people)
