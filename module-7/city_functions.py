# ----------------------------------------------
# Author: Amanda Brock
# Date: February 22, 2026
# Assignment: Module 7.2
# Purpose of Code: stores function then calls it 3 times
# ----------------------------------------------
# makes language optional
def city_country(city, country, population=None, language=None):
    """Return City, Country, optionally including population and language."""
    result = f"{city.title()}, {country.title()}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language.title()}"

    return result


# Call the function at least 3 times (for your screenshot)
if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("santiago", "chile", 5000000))
    print(city_country("santiago", "chile", 5000000, "spanish"))