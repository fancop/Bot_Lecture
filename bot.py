import os

def load_courses():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    courses = {
        "Программирование на Python": {
            "файл": os.path.join(current_directory, "python_course.txt")
        },
        "Веб-разработка": {
            "файл": os.path.join(current_directory, "web_course.txt")
        },
        "Наука о данных": {
            "файл": os.path.join(current_directory, "data_science_course.txt")
        }
    }
    return courses


def greet():
    return ("Привет! Я чат-бот 'Лекторий'.\n"
            "Напишите слово 'старт', чтобы увидеть список команд, которые я могу выполнить.")


def list_courses(courses):
    return "\n".join([f"{index + 1}. {course}" for index, course in enumerate(courses.keys())])


def get_course_info(course_name, courses):
    if course_name in courses:
        course_info = courses[course_name]
        file_name = course_info['файл']
        with open(file_name, 'r', encoding='utf-8') as file:
            course_text = file.read()
        return f"{course_name}:\n{course_text}"
    else:
        return "Извините, такого курса нет в нашем списке."


def respond(user_input, courses):
    if "выход" in user_input.lower():
        return "До свидания!"
    elif "привет" in user_input.lower():
        return greet()
    elif "курсы" in user_input.lower():
        return ("Доступные курсы:\n" + list_courses(courses) + "\n"
                "Введите название курса для получения подробной информации.")
    elif user_input in courses:
        course_info = get_course_info(user_input, courses)
        print("Бот:", course_info)
        print("Доступные команды:\n"
              "- 'курсы' - для просмотра доступных курсов и выбора для изучения\n"
              "- 'выход' - для завершения работы с ботом")
        return None
    else:
        return "Извините, я не понимаю ваш запрос."


courses = load_courses()
print(greet())

while True:
    user_input = input("Вы: ")
    if user_input.strip().lower() == "старт":
        print("Доступные команды:\n"
              "- 'курсы' - для просмотра доступных курсов и выбора для изучения\n"
              "- 'выход' - для завершения работы с ботом")
        continue
    response = respond(user_input, courses)
    if response is not None:
        print("Бот:", response)
    if response == "До свидания!":
        break