# Costello

[![Build Status](https://travis-ci.org/johnbywater/costello.svg?branch=master)](https://travis-ci.org/johnbywater/costello)
[![Coverage Status](https://coveralls.io/repos/github/johnbywater/costello/badge.svg?branch=master#)](https://coveralls.io/github/johnbywater/costello)

System to support mass contact tracing for infectious disease.

This system is motivated by the occurrence of the Cononavirus (COVID-19) pandemic.


## Abstract

Costello is a reliable, scalable, event-sourced, open source software system designed to support
mass contact tracing for novel infectious diseases such as Coronavirus. It has been written
the none is expected for at least one year, perhaps two).

The virus causes no symptoms in some people. But of those people who
do develop symptoms, some will recover and some will die. The dispositions
to different outcomes are not very well understood, but age seems to be a
to support the need expressed many times by Anthony Costello.

## Analysis

- Detect suspected cases of infection
    - Open new suspected case of infection
        - Add personal information
            - Name
            - Telephone number
        - Record reason for opening case
            - Positive test result
                - Test reference number
                - Type of test
                - Date of test
            - Matching symptoms
                - Date of onset of symptoms
                - Notes
            - Contact with suspected case
                - Case ID
        - Notes
    - Select suspected case of infection
        - By case ID
        - By priority for investigation
        - By telephone number
        - By test request ID
    - Interview suspected case of infection
        - Record time of interview
        - Ask if recently tested
            - If not known
        - Record test result
        - Ask about and assess encounters with other people
            - From memory
            - Log in contract tracing app on mobile device
            - Details of each encounter
                - Place
                - Date and time
                - Type of encounter
                - Risk of transmission
                - Name of person
                - Telephone number of person
            - Open new suspected cases of infection...
        - Ask about use of shared spaces (work, public transport, shops, gyms, restaurants, etc)
            - From memory
            - Log in contract tracing app on mobile device
            - Details of each use
                - Place
                - Date and time
                - Type of use
                - Risk of transmission
        - Record use of shared spaces
            - Notes
            - Record public transport use
            - Record gyms, restaurants, bars, etc
        - Record symptoms
        - Give advice and instructions
            - Start recording encounters with other people
            - Avoid infecting other people
                - Quarantine requirements
                - Wear a mask during encounters with others
                - Avoid meeting vulnerable people
                - Avoid using shared spaces
            - Monitor symptoms and request medical assistance if required
                - Temperature, coughing, breathing, oxygen levels
        - Record advice and instructions given
        - Schedule follow up interview
    - Investigate other users of a shared space
        - Identify people who shared space at the same time or afterwards
        - Ask about and assess encounters with other people
            - From memory
            - Log in venue or transport vehicle
            - Details of each encounter
                - Place
                - Date and time
                - Type of encounter
                - Risk of transmission
                - Name of person
                - Telephone number of person
            - Open new suspected cases of infection...
    - Request test for suspected case of infection
    - Update suspected case with test result
    - Close suspected case of infection
        - Record reason for closing case


Need to register who went into a shared spaces so can contact trace?
Need to investigate use of shops (payment card information?)
Need model relating earliest time of infectiousness to:
   - first positive test result (14 days before?)
   - onset of matching symptoms (14 days before?)
   - contact with suspected case of infection (2/3 days later?)
