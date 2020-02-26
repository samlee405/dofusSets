import requests
from bs4 import BeautifulSoup


def get_soup(url):
    url_response = requests.get(url)
    soup = BeautifulSoup(url_response.text, "html.parser")
    return soup


def get_alternate_names(soup, url):
    alt_links = {}
    raw_links = soup.find("head").find_all("link", {"rel": "alternate"})
    for link in raw_links:
        link = link["href"]
        if "dofus" in link:
            alt_links[link.split("/")[3]] = link
    alt_links["en"] = url

    names = {}
    for key, value in alt_links.items():
        alt_soup = get_soup(value)
        name = alt_soup.find("h1", attrs={"class": "ak-return-link"}).text.strip()
        names[key] = name

    return names


def get_stats(soup):
    raw_stats = soup.find(
        "div", {"class": "ak-container ak-content-list ak-displaymode-col"}
    )
    stats = []
    custom_stats = []

    for stat in raw_stats:
        description = stat.find_next("div", {"class": "ak-title"}).text.strip()

        # The dofus site does not distinguish special descriptive or custom
        # stats from normal combat stats. As such, discerning them from
        # normal stats is a bit difficult. For now, I'm simply using a
        # char count analysis to separate the 2. This will need testing
        # or refactoring at a later time
        if len(description) > 40:
            custom_stats.append(description)
            continue

        type = None
        min_stat = None
        max_stat = None

        # check and adjust for the description typo that substitutes "HP" for "Initiative"
        description = description.replace("HP", "Initiative")

        # check and adjust for values that have ranges and negative values
        if "to" in description and "-" not in description:
            arr = description.split(" ")
            min_stat = int(arr[0].replace("%", ""))
            max_stat = int(arr[2].replace("%", ""))
            del arr[0]
            del arr[0]
            del arr[0]
            type = " ".join(arr)
        elif "to" in description and "-" in description:
            arr = description.split(" ")
            min_stat = int(arr[2].replace("%", ""))
            max_stat = int(arr[0].replace("%", ""))
            del arr[0]
            del arr[0]
            del arr[0]
            type = " ".join(arr)
        else:
            arr = description.split(" ")
            max_stat = int(arr[0].replace("%", ""))
            del arr[0]
            type = " ".join(arr)

        if "%" in description and "Critical" not in description:
            type = "% " + type

        stats.append({"stat": type, "minStat": min_stat, "maxStat": max_stat})

    return (stats, custom_stats)


def get_bonuses(soup):
    all_bonuses = {}
    raw_bonuses = soup.find_all("div", attrs={"class": "set-bonus-list"})
    for i in range(len(raw_bonuses)):
        stats = []
        bonuses = raw_bonuses[i].find_all("div", attrs={"class": "ak-title"})
        for bonus in bonuses:
            description = bonus.text.strip()
            type = None
            value = None

            # check and adjust for the description typo that substitutes "HP" for "Initiative"
            description = description.replace("HP", "Initiative")

            # check and adjust for values that have ranges and negative values
            if "to" in description and "-" not in description:
                arr = description.split(" ")
                max_stat = arr[2].replace("%", "")
                del arr[0]
                del arr[0]
                del arr[0]
                type = " ".join(arr)
            elif "to" in description and "-" in description:
                arr = description.split(" ")
                max_stat = arr[0].replace("%", "")
                del arr[0]
                del arr[0]
                del arr[0]
                type = " ".join(arr)
            else:
                arr = description.split(" ")
                max_stat = arr[0].replace("%", "")
                del arr[0]
                type = " ".join(arr)

            if "%" in description and "Critical" not in description:
                type = "% " + type

            stats.append({"stat": type, "value": max_stat})

        item_count = 2 + i
        all_bonuses[item_count] = stats

    return all_bonuses


def get_conditions(soup):
    raw_conditions = soup.find(
        "div", attrs={"class": "ak-container ak-panel no-padding"}
    )
    conditions = []

    if raw_conditions:
        raw_conditions = (
            raw_conditions.text.strip().strip("Conditions").strip().split(" ")
        )
        stat_type = raw_conditions[0]
        condition_type = raw_conditions[1]
        limit = int(raw_conditions[2])

        conditions.append(
            {"statType": stat_type, "condition": condition_type, "limit": limit,}
        )

    return conditions
