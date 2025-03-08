import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from datetime import datetime
from io import StringIO

# Get the races data
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Get the current year
    current_year = datetime.now().year
    
    # Create an empty DataFrame to store the data
    races_data = pd.DataFrame()
    
    # Loop from 1950 till the current year
    for year in range(1950, current_year + 1):
        url = f"https://www.formula1.com/en/results/{year}/races"
        page.goto(url)

        # Try to find the table and get the data
        try:
            table_element = page.query_selector("//table[@class='f1-table f1-table-with-data w-full']")
            if table_element:
                # Extract the html to transform into a DataFrame
                html_string = table_element.evaluate("element => element.outerHTML")
                df_races = pd.read_html(StringIO(html_string))[0]
                df_races['Year'] = year
                races_data = pd.concat([races_data, df_races], ignore_index=True)
        except Exception as e:
            print(f"Error processing the year {year}: {e}")
    
    # Close the navigator
    context.close()
    browser.close()

    # Save the DataFrame as a CSV file
    races_data.to_csv("formula1_race_results.csv", index=False)



with sync_playwright() as playwright:
    run(playwright)



# Get the drivers data
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Get the current year
    current_year = datetime.now().year
    
    # Create a empty DataFrame to store the data
    drivers_data = pd.DataFrame()
    
    # Loop from 1950 till the current year
    for year in range(1950, current_year + 1):
        url = f"https://www.formula1.com/en/results/{year}/drivers"
        page.goto(url)

        # Try to find the table and get the data
        try:
            table_element = page.query_selector("//table[@class='f1-table f1-table-with-data w-full']")
            if table_element:
                # Extract the html to transform into a DataFrame
                html_string = table_element.evaluate("element => element.outerHTML")
                df_drivers = pd.read_html(StringIO(html_string))[0]
                df_drivers['Year'] = year
                drivers_data = pd.concat([drivers_data, df_drivers], ignore_index=True)
        except Exception as e:
            print(f"Error processing the year {year}: {e}")
    
    # Close the navigator
    context.close()
    browser.close()

    # Save the DataFrame as a CSV file (choose the path to save)
    drivers_data.to_csv('formula1_drivers_results.csv', index=False)


with sync_playwright() as playwright:
    run(playwright)




# Get the teams data
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Get the current year
    current_year = datetime.now().year
    
    # Create a empty DataFrame to store the data
    teams_data = pd.DataFrame()
    
    # Loop from 1958 till the current year
    # Loop starts from 1958 because the Constructors Championship was not awarded until 1958
    for year in range(1958, current_year + 1):
        url = f"https://www.formula1.com/en/results/{year}/team"
        page.goto(url)

        # Try to find the table and get the data
        try:
            table_element = page.query_selector("//table[@class='f1-table f1-table-with-data w-full']")
            if table_element:
                # Extract the html to transform into a DataFrame
                html_string = table_element.evaluate("element => element.outerHTML")
                df_teams = pd.read_html(StringIO(html_string))[0]
                df_teams['Year'] = year
                teams_data = pd.concat([teams_data, df_teams], ignore_index=True)
        except Exception as e:
            print(f"Error processing the year {year}: {e}")
    
    # Close the navigator
    context.close()
    browser.close()

    # Save the DataFrame as a CSV file (choose the path to save)
    teams_data.to_csv('formula1_teams_results.csv', index=False)


with sync_playwright() as playwright:
    run(playwright)




# Get the fastest-laps data
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Get the current year
    current_year = datetime.now().year
    
    # Create a empty DataFrame to store the data
    fastest_laps_data = pd.DataFrame()
    
    # Loop from 1950 till the current year
    for year in range(1950, current_year + 1):
        url = f"https://www.formula1.com/en/results/{year}/fastest-laps"
        page.goto(url)

        # Try to find the table and get the data
        try:
            table_element = page.query_selector("//table[@class='f1-table f1-table-with-data w-full']")
            if table_element:
                # Extract the html to transform into a DataFrame
                html_string = table_element.evaluate("element => element.outerHTML")
                df_fastest_laps = pd.read_html(StringIO(html_string))[0]
                df_fastest_laps['Year'] = year
                fastest_laps_data = pd.concat([fastest_laps_data, df_fastest_laps], ignore_index=True)
        except Exception as e:
            print(f"Error processing the year {year}: {e}")
    
    # Close the navigator
    context.close()
    browser.close()

    # Save the DataFrame as a CSV file (choose the path to save)
    fastest_laps_data.to_csv('formula1_fastest_laps_results.csv', index=False)


with sync_playwright() as playwright:
    run(playwright)