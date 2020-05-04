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
    - Open new suspected case
        - Add personal information
            - Name
            - Telephone number
        - Add reason for suspicion
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
        - Time of appointment
    - Interview suspected case of infection
        - Record time of interview
        - Ask if recently tested
            - If not known
        - Record test result
        - Ask about and assess encounters (since date of infection)
            - Name of person
            - Telephone number of person
            - Nature of encounter
            - Risk of transmission
        - Record encounters with potential cases of infection
            - Details of encounter
                - Name
                - Telephone number
                - Place
                - Date and time
                - Type of encounter
        - Ask about visits to shared spaces (work, public transport, shops, gyms, restaurants, etc)
            - Identify people who shared space at the same time or afterwards
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
        - Open new suspected cases of infection...
        - Schedule follow up interview
    - Request test for suspected case of infection
    - Update suspected case with test result


Need to register who went into a shared spaces so can contact trace?
Need to investigate use of shops (payment card information?)
