import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

def getAverageReviews(url):
    driver.get(url)
    info = driver.find_element("xpath", "/html/body/script[12]")
    front = info.get_attribute('innerHTML').find("\"{")
    end = info.get_attribute('innerHTML').find("}\"")+2
    js = info.get_attribute('innerHTML')[front:end]
    data = json.loads(js)
    data = json.loads(data)

    print(f"Average Rating: {data['average_rating']}")
    print(f"Average Instructor: {data['average_instructor']}")
    print(f"Average Fun: {data['average_fun']}")
    print(f"Average Recommendability: {data['average_recommendability']}")
    print(f"Average Difficulty: {data['average_difficulty']}")
    print(f"Average Hours of Work Per Week: {data['average_hours_per_week']}")
    print(f"Average Amount of Reading: {data['average_amount_reading']}")
    print(f"Average Amount of Writing: {data['average_amount_writing']}")
    print(f"Average Amount of Group Work: {data['average_amount_group']}")
    print(f"Average Amount of Homework: {data['average_amount_homework']}")
    return


def getTeachers(url):
    driver.get(url)

    name = (driver.find_elements("id", ("title")))
    rating = (driver.find_elements("id", ("rating")))
    difficulty = (driver.find_elements("id", ("difficulty")))
    gpa = (driver.find_elements("id", ("gpa")))
    link = (driver.find_elements("xpath", ('//*[@id="page-content-wrapper"]/div/div/div/div[3]/ul/li/div/div/a')))

    result = {}
    for l in link:
        if(l.text != ""):
            result[l.text] = l.get_attribute("href")
    for x in range(len(name)):
        if(name[x].text != ""):
            print(f"Instructor Name: {name[x].text}")
            print(f"Rating: {rating[x].text}")
            print(f"Difficulty: {difficulty[x].text}")
            print(f"Average GPA: {gpa[x].text}")
            print(result[name[x].text])
            print("_"*80)
    return result




if __name__ == "__main__":
    url = "https://thecourseforum.com/course/"

    course = input("Enter Course ID (i.e. MATH)")
    number = input("Enter Course Number(i.e. 3100)")

    url += course +'/'
    url += number
    request_response = requests.head(url)
    status_code = request_response.status_code
    if status_code == 200 or status_code == 301:
        print("valid course")
        data = getTeachers(url)
        name = input("Enter Instructor Name from the Course to view more information (i.e. Bob Smith): \n")
        if data.has_key(name):
            getAverageReviews(data[name])
        else:
            print("There does not exist a page for the instructor entered.")

    else:
        print("invalid course")

