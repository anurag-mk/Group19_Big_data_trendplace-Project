﻿{
  "metadata": {
    "name": "Group 19 Demo",
    "kernelspec": {
      "language": "scala",
      "name": "spark2-scala"
    },
    "language_info": {
      "codemirror_mode": "text/x-scala",
      "file_extension": ".scala",
      "mimetype": "text/x-scala",
      "name": "scala",
      "pygments_lexer": "scala"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2,
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": "## Welcome to Zeppelin.\n#### This is a demo from MSBA6330 Group 19 trends marketplace \n\n"
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\npip install s3fs"
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\npip install -U pandasql"
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\nimport pandas as pd\nimport s3fs\n"
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": "## Data Ingestion by Python"
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\ndf \u003d pd.read_csv(\"s3://li002180-msba6330/trendmarketplace/players_21.csv\")"
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\ndf"
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": "## Data Preparation by Python "
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\n# Filter useful columns\nuseless_column \u003d [\u0027dob\u0027,\u0027sofifa_id\u0027,\u0027player_url\u0027,\u0027long_name\u0027,\u0027body_type\u0027,\u0027real_face\u0027,\u0027nation_position\u0027,\u0027loaned_from\u0027,\u0027nation_jersey_number\u0027]\nfifa_21 \u003d df.drop(useless_column, axis \u003d 1)"
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\n# Create a new columns to calculate BMI\nfifa_21[\u0027BMI\u0027] \u003d fifa_21 [\u0027weight_kg\u0027] / (fifa_21[\u0027height_cm\u0027] / 100) ** 2"
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\n# checking missing values \nfifa_21.isnull().any().any()"
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\n# Fill the missing value to 0 \nfifa_21 \u003d fifa_21.fillna(0)"
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\n# checking missing values again\nfifa_21.isnull().any().any()"
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python\nfifa_21.head(5)"
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": "## Data Discovery with SQL"
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python.sql\nselect preferred_foot, count(short_name) as player_count from fifa_21 group by preferred_foot"
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python.sql\nselect age, avg(potential) as avg_potential from fifa_21 where age \u003c\u003d40 group by age order by age asc "
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python.sql\nselect age, preferred_foot, round(avg(overall),1) as avg_rating from fifa_21 where (age \u003e\u003d 20 and age \u003c\u003d30) group by age,preferred_foot"
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "autoscroll": "auto"
      },
      "outputs": [],
      "source": "%python.sql\nselect nationality, count(short_name) as players_num from (select short_name, nationality, overall from fifa_21 order by overall desc limit 50) group by nationality order by players_num desc \n"
    },
    {
      "cell_type": "raw",
      "metadata": {
        "format": "text/plain"
      },
      "source": "%python\n"
    }
  ]
}