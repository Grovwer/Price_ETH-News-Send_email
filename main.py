import smtplib
import requests
STOCK_NAME = "ETH"
COMPANY_NAME = "Ethereum"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOK_API_KEY = "---EEI3CKKYSJV***"
NEW_API_KEY = "f4a4****0a9b42138c4a477b6b0daf***"
# получаем цену закрытия вчерашнего дня дня
stok_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOK_API_KEY,
    "market": "USD",

}

response = requests.get(STOCK_ENDPOINT, params=stok_params)
# print(response.json())
data = response.json()["Time Series (Digital Currency Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_prise = yesterday_data["4a. close (USD)"]
print(yesterday_closing_prise)

#Получаем цену закрытия позовчерашнего дня

day_before_yesterday_data = data_list[5]
day_before_yesterday_close_prise = day_before_yesterday_data["4a. close (USD)"]
print(day_before_yesterday_close_prise)

# узнаем разницу в цене
difference = abs(float(yesterday_closing_prise) - float(day_before_yesterday_close_prise))
print(difference)
# Переводим в проценты

dif_percent = (difference / float(yesterday_closing_prise)) * 100
print(dif_percent)
# оповещалка
if dif_percent > 5:
    # Получаем новости
    news_params = {
        "apiKey": NEW_API_KEY,
        "q": COMPANY_NAME,
        "language": 'en',
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    # print(news_response.json())
    articles = news_response.json()['articles']

# получаем первые статьи
    three_articles = articles[:3]


# создаем заголовки
    formatted_articles = [f"Headline: {articles['title']}, \nBrief: {articles['description']}" for articles in
                          three_articles]
    print(formatted_articles)
    my_email = "///***fire@yahoo.com"
    password = "***sopiehaxe***"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivatioon\n\n{formatted_articles}.".encode('utf-8')
                            )
