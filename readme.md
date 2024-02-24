# LinkedIn Job Scraper

## Overview

This project aims to enhance job vacancy sourcing for a recruitment agency by automating the extraction of job posting data from LinkedIn. The solution utilizes web scraping tools, specifically Selenium and BeautifulSoup, to streamline the data collection process.

## Project Objectives

- Increase the efficiency of job vacancy sourcing
- Improve the quality of job vacancy sourcing
- Gain a competitive advantage for the recruitment agency

## Prerequisites

- Python 3
- Required libraries (install using `pip install -r requirements.txt`)

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies

## Usage

1. Run the script: `python Jobs_script.py`
2. Monitor the browser and console for progress updates
3. Once completed, find the scraped data in `Linkedin_Jobs.csv`

## Project Structure

- `Jobs_script.py`: Main script for web scraping
- `chromedriver.exe`: Chrome WebDriver executable
- `requirements.txt`: List of Python libraries required for the project
- `Linkedin_Jobs.csv`: Output file containing scraped job data

## Approach

The script follows these key steps:
1. Initializes a Chrome WebDriver using Selenium
2. Navigates to LinkedIn job search page
3. Dynamically loads job listings by clicking "See more jobs" button
4. Scrapes relevant job information using BeautifulSoup
5. Organizes data into a Pandas DataFrame and exports to CSV