from bs4 import BeautifulSoup
from selenium import webdriver
import csv


def main():
    subReddit1= 'http://www.reddit.com/r/JuJutsuKaisen/'
    postInfo(subReddit1)

def parsecomments(u):
    print(u)
    driver2 = webdriver.Chrome()
    driver2.get(u)
    commentSoup = BeautifulSoup(driver2.page_source, 'html.parser')
    driver2.quit()
    comments = []
    for c in commentSoup.find_all('p'):
        comments.append(c.text)
    return(comments)


def postInfo(url):
    driver = webdriver.Chrome()
    #url = 'http://www.reddit.com/r/JuJutsuKaisen/'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    Information =[]
    for item in soup.select('.Post'):
        try:
            #Number of likes
            upvotes = item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()
            #Title
            title = item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()
            # of Comments
            number_comments = item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text().replace(" comments", "").replace(" comment", "")
            #Post Link
            link = 'http://www.reddit.com'+item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href']
            #Comments
            postComments = parsecomments( 'http://www.reddit.com'+item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])
        except Exception as e:
            # raise e
            print('')
        Info = [title, link, number_comments, upvotes, postComments]
        print(Info)
        Information.append(Info)

    filename ="post.csv"
    with open(filename, 'w', encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        csvwriter.writerow(['Title','Link','Number of comments','Upvotes','Comments'])
        csvwriter.writerows(Information)
    csvfile.close()


if __name__ =="__main__":
    main()