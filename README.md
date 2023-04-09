# Spotify Analyser

## Contents

1. [Overview](#overview)
1. [Setup](#setup)
1. [Implementation of Statistics](#implementation-of-statistics)
1. [To Do](#to-do)

## Overview

This program will produce statistics and infographics about a user's Spotify listening behaviour

Statistics Implemented:

- Time Listened

## Setup

The folder structure should look like this:

Parent Folder
    Spotify-Analyser
    Results (created automatically by the program)
    Spotify API Keys.txt
    Data

The contents of "Spotify API Keys.txt" should look like this:

SPOTIPY_CLIENT_ID=AppClientID
SPOTIPY_CLIENT_SECRET=AppClientSecret

"SPOTIPY_CLIENT_ID" and "SPOTIPY_CLIENT_SECRET" are the key words that the spotipy authenticator uses. You find these inside the settings of an app you have created on the "Spotify for Developers" website.

## Implementation of Statistics

Each statistic gets it's own class that is saved in the "Children" folder inside "Statistics". This needs to be imported into the "Spotify" class and added to a list of statistic classes. Each statistic object is a subclass of a statistic type, and each statistic type is a subclass of a general statistic class.

TimeListened is a simple example. It records the number of times you have listened to tracks for a time period within a certain range, for example someone might have listened to tracks for 30-60 seconds 200 times. The Statistic class should handle all the high level processing, such as the folder the results are going to be saved into, reading the data from the files, etc. In this case the statistic type class is StatisticRange, and this handles how data is sorted into the ranges, and how to output range data, etc. The only job of the lowest level class (TimeListened in this case) is how to extract the right values from the songs. It also contains data such as any units if relevant, or data about the ranges such as in the TimeListened example.

Outputting the data to a text file is handled by a function in the Strings script in Utils. It takes in a dictionary and outputs the data in aligned columns.

## To Do

