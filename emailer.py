import weather
import mailer

def get_emails():
    # create an empty list to read emails from a file
    emails = {}
    # check if emails_file.txt exists and program doesn't crash
    try:
        emails_file = open('emails_file.txt', 'r')
        for line in emails_file:
            (email, name)=line.split(',')
            # send key equal to the value & remove new line character
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print (err)

    return emails

def get_shows():
    # reading shows from a file
    try:
        shows_file = open('shows.txt', 'r')
        shows = shows_file.read()
    except FileNotFoundError as err:
        print (err)

    return shows


def main():
    emails = get_emails()

    shows = get_shows()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails,shows,forecast)

main()
