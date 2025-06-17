
#the list of shows
SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family"
]

#the main function
def main():
    cleaned_show = []
    for show in SHOWS:
        cleaned_show.append(show.strip().title())
    print(', '.join(cleaned_show))
        
main()